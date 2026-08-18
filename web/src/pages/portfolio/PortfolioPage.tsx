import { useEffect, useState, useCallback, useMemo } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { Skeleton } from "@/components/ui/skeleton";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import SkillPortfolioCard from "@/components/portfolio/SkillPortfolioCard";
import { sessionsApi } from "@/services/sessions";
import { vacanciesApi } from "@/services/vacancies";
import { portfoliosApi } from "@/services/portfolios";
import { usePolling } from "@/hooks/usePolling";
import { ArrowLeft, Download, Loader2, RefreshCw, Zap, FileText, Award, BarChart3, CheckCircle2 } from "lucide-react";
import type { Portfolio, AssessorOverride, Vacancy } from "@/types";

export default function PortfolioPage() {
  const { id, sessionId } = useParams<{ id: string; sessionId: string }>();
  const navigate = useNavigate();
  const [portfolio, setPortfolio] = useState<Portfolio | null>(null);
  const [generating, setGenerating] = useState(false);
  const [loading, setLoading] = useState(true);
  const [overrides, setOverrides] = useState<Record<number, AssessorOverride>>({});
  const [vacancies, setVacancies] = useState<Vacancy[]>([]);
  const [selectedVacancy, setSelectedVacancy] = useState<string>("");
  const [exporting, setExporting] = useState<"pdf" | "json" | null>(null);
  const [candidateName, setCandidateName] = useState<string | null>(null);

  const fetchPortfolio = useCallback(async () => {
    const res = await sessionsApi.getPortfolio(Number(sessionId));
    const data = res.data as any;
    if (data.status === "generating" || data.portfolio?.generation_status === "generating" || data.portfolio?.generation_status === "pending") {
      setGenerating(true);
    } else if (data.portfolio) {
      setPortfolio(data.portfolio);
      setGenerating(false);
      // Build overrides map
      const overrideMap: Record<number, AssessorOverride> = {};
      data.portfolio.overrides.forEach((o: AssessorOverride) => {
        overrideMap[o.portfolio_skill_id] = o;
      });
      setOverrides(overrideMap);
    }
  }, [sessionId]);

  useEffect(() => {
    Promise.all([fetchPortfolio(), vacanciesApi.list(), sessionsApi.get(Number(sessionId))])
      .then(([, vRes, sRes]) => {
        setVacancies(vRes.data.vacancies);
        setCandidateName(sRes.data.session.candidate_name ?? null);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [fetchPortfolio, sessionId]);

  // Poll while generating
  usePolling(fetchPortfolio, 5000, generating);

  const handleOverrideSaved = (skillId: number, override: AssessorOverride) => {
    setOverrides((prev) => ({ ...prev, [skillId]: override }));
  };

  const handleRunFitGap = () => {
    if (!selectedVacancy || !portfolio) return;
    navigate(`/assessments/${id}/sessions/${sessionId}/fitgap/${selectedVacancy}`);
  };

  const handleExport = async (format: "pdf" | "json") => {
    if (!portfolio) return;
    setExporting(format);
    try {
      const res = await portfoliosApi.exportPortfolio(
        portfolio.id,
        format,
        selectedVacancy ? Number(selectedVacancy) : undefined
      );
      if (format === "json") {
        const blob = new Blob([JSON.stringify(res.data, null, 2)], { type: "application/json" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `portfolio-${sessionId}.json`;
        a.click();
        URL.revokeObjectURL(url);
      } else {
        const blob = new Blob([res.data as BlobPart], { type: "application/pdf" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `portfolio-${sessionId}.pdf`;
        a.click();
        URL.revokeObjectURL(url);
      }
    } finally {
      setExporting(null);
    }
  };

  // Metrics summary
  const summaryStats = useMemo(() => {
    if (!portfolio?.skills) return null;
    const assessed = portfolio.skills.filter((s) => s.ai_level !== null && s.ai_level !== undefined);
    const highConfidence = portfolio.skills.filter((s) => s.ai_confidence?.toLowerCase() === "high");
    const avgScore = assessed.length > 0
      ? (assessed.reduce((acc, s) => acc + (Number(s.ai_level) || 0), 0) / assessed.length).toFixed(1)
      : "—";

    return {
      total: portfolio.skills.length,
      assessedCount: assessed.length,
      highConfidenceCount: highConfidence.length,
      avgScore,
    };
  }, [portfolio]);

  if (loading) {
    return (
      <div className="max-w-3xl mx-auto space-y-6 py-8">
        <Skeleton className="h-10 w-64 bg-slate-800" />
        <Skeleton className="h-32 w-full bg-slate-800 rounded-2xl" />
        <Skeleton className="h-48 w-full bg-slate-800 rounded-2xl" />
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto space-y-8 py-6">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-5 bg-slate-900/70 backdrop-blur-xl border border-slate-800 rounded-2xl shadow-xl">
        <div className="flex items-center gap-3">
          <Link
            to={`/assessments/${id}/invite`}
            className="p-2 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-700 transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
          </Link>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl font-bold tracking-tight text-white">Portofolio Kompetensi Kandidat</h1>
              <span className="px-2 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold">
                Verified
              </span>
            </div>
            {candidateName && (
              <p className="text-xs text-slate-400 mt-0.5">Kandidat: <strong className="text-slate-200 font-medium">{candidateName}</strong></p>
            )}
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Link
            to={`/assessments/${id}/sessions/${sessionId}/transcript`}
            className="inline-flex items-center gap-1.5 text-xs font-medium border border-slate-700 bg-slate-800/60 rounded-xl px-3.5 py-2 hover:bg-slate-700 text-slate-200 transition-colors shadow-sm"
          >
            <FileText className="h-3.5 w-3.5 text-blue-400" />
            Transkrip Sesi
          </Link>
          {!generating && portfolio && (
            <>
              <Button
                variant="outline"
                size="sm"
                onClick={() => handleExport("pdf")}
                disabled={!!exporting}
                className="border-slate-700 bg-slate-800/60 rounded-xl text-xs text-slate-200 hover:bg-slate-700"
              >
                {exporting === "pdf" ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <Download className="h-3.5 w-3.5 mr-1" />}
                PDF
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => handleExport("json")}
                disabled={!!exporting}
                className="border-slate-700 bg-slate-800/60 rounded-xl text-xs text-slate-200 hover:bg-slate-700"
              >
                {exporting === "json" ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <Download className="h-3.5 w-3.5 mr-1" />}
                JSON
              </Button>
            </>
          )}
        </div>
      </div>

      {/* Generating state */}
      {generating && (
        <div className="border border-slate-800 bg-slate-900/60 backdrop-blur-xl rounded-3xl p-12 text-center space-y-4 shadow-2xl">
          <div className="w-12 h-12 rounded-2xl bg-blue-500/10 border border-blue-500/20 text-blue-400 flex items-center justify-center mx-auto">
            <Loader2 className="h-6 w-6 animate-spin" />
          </div>
          <div>
            <p className="text-base font-semibold text-white">Memproses Evaluasi Portofolio AI...</p>
            <p className="text-xs text-slate-400 mt-1 max-w-sm mx-auto leading-relaxed">
              Model AI sedang menganalisis transkrip wawancara dan mengekstrak bukti keahlian.
            </p>
          </div>
        </div>
      )}

      {/* Failed state */}
      {!generating && portfolio?.generation_status === "failed" && (
        <div className="border border-red-500/30 bg-red-950/30 rounded-3xl p-8 text-center space-y-3 shadow-xl">
          <p className="text-sm font-semibold text-red-300">Generasi Portofolio Gagal</p>
          <p className="text-xs text-slate-400 max-w-md mx-auto">{portfolio.generation_error || "Terjadi kesalahan saat memproses evaluasi LLM."}</p>
          <Button
            variant="outline"
            size="sm"
            onClick={async () => {
              await sessionsApi.regeneratePortfolio(Number(sessionId));
              setGenerating(true);
            }}
            className="mt-2 border-red-500/30 text-red-300 hover:bg-red-500/10 rounded-xl"
          >
            <RefreshCw className="h-3.5 w-3.5 mr-1.5" /> Coba Lagi
          </Button>
        </div>
      )}

      {/* Ready state */}
      {!generating && portfolio?.generation_status === "complete" && (
        <>
          {/* Metrics summary cards */}
          {summaryStats && (
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3.5">
              <div className="p-4 bg-slate-900/60 border border-slate-800 rounded-2xl">
                <span className="text-[11px] font-medium text-slate-400">Total Keahlian</span>
                <p className="text-2xl font-bold text-white mt-1">{summaryStats.total}</p>
              </div>
              <div className="p-4 bg-slate-900/60 border border-slate-800 rounded-2xl">
                <span className="text-[11px] font-medium text-slate-400">Tervalidasi (Assessed)</span>
                <p className="text-2xl font-bold text-emerald-400 mt-1">{summaryStats.assessedCount}</p>
              </div>
              <div className="p-4 bg-slate-900/60 border border-slate-800 rounded-2xl">
                <span className="text-[11px] font-medium text-slate-400">High Confidence</span>
                <p className="text-2xl font-bold text-blue-400 mt-1">{summaryStats.highConfidenceCount}</p>
              </div>
              <div className="p-4 bg-slate-900/60 border border-slate-800 rounded-2xl">
                <span className="text-[11px] font-medium text-slate-400">Rata-Rata Level</span>
                <p className="text-2xl font-bold text-cyan-400 mt-1">L{summaryStats.avgScore}</p>
              </div>
            </div>
          )}

          {/* Configured skills */}
          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <Award className="h-4 w-4 text-blue-400" />
              <h2 className="text-sm font-bold text-white tracking-wide uppercase">Keahlian Utama (Configured Skills)</h2>
            </div>
            <div className="space-y-3.5">
              {portfolio.skills
                .filter((s) => !s.is_discovered)
                .map((skill) => (
                  <SkillPortfolioCard
                    key={skill.id}
                    skill={skill}
                    override={overrides[skill.id]}
                    onOverrideSaved={(o) => handleOverrideSaved(skill.id, o)}
                  />
                ))}
            </div>
          </div>

          {/* Discovered skills */}
          {portfolio.skills.some((s) => s.is_discovered) && (
            <>
              <Separator className="bg-slate-800" />
              <div className="space-y-4">
                <div className="flex items-center gap-2">
                  <Zap className="h-4 w-4 text-amber-400" />
                  <h2 className="text-sm font-bold text-white tracking-wide uppercase">Keahlian Tambahan (Discovered Skills)</h2>
                </div>
                <div className="space-y-3.5">
                  {portfolio.skills
                    .filter((s) => s.is_discovered)
                    .map((skill) => (
                      <SkillPortfolioCard
                        key={skill.id}
                        skill={skill}
                        override={overrides[skill.id]}
                        onOverrideSaved={(o) => handleOverrideSaved(skill.id, o)}
                      />
                    ))}
                </div>
              </div>
            </>
          )}

          <Separator className="bg-slate-800" />

          {/* Fit/Gap analysis trigger */}
          <div className="p-6 bg-gradient-to-r from-blue-950/40 to-slate-900/60 border border-slate-800 rounded-3xl flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-xl">
            <div className="space-y-1">
              <div className="flex items-center gap-2 text-white font-semibold text-sm">
                <BarChart3 className="h-4 w-4 text-cyan-400" />
                <span>Analisis Kesesuaian Lowongan (Fit/Gap Report)</span>
              </div>
              <p className="text-xs text-slate-400">
                Bandingkan profil portofolio ini terhadap kualifikasi lowongan pekerjaan yang dituju.
              </p>
            </div>
            <div className="flex items-center gap-3 w-full sm:w-auto">
              <Select value={selectedVacancy} onValueChange={setSelectedVacancy}>
                <SelectTrigger className="w-full sm:w-60 bg-slate-800/80 border-slate-700 rounded-xl text-xs text-white">
                  <SelectValue placeholder="Pilih lowongan..." />
                </SelectTrigger>
                <SelectContent className="bg-slate-900 border-slate-800 text-white">
                  {vacancies.map((v) => (
                    <SelectItem key={v.id} value={String(v.id)} className="text-xs focus:bg-slate-800">
                      {v.role_title}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <Button
                onClick={handleRunFitGap}
                disabled={!selectedVacancy}
                className="bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs whitespace-nowrap shadow-lg shadow-blue-600/20"
              >
                Jalankan Analisis →
              </Button>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

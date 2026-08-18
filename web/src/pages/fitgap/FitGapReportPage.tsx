import { useEffect, useState, useCallback } from "react";
import { useParams, Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Skeleton } from "@/components/ui/skeleton";
import ComparisonTable from "@/components/fitgap/ComparisonTable";
import { portfoliosApi } from "@/services/portfolios";
import { sessionsApi } from "@/services/sessions";
import { usePolling } from "@/hooks/usePolling";
import { ArrowLeft, Download, Loader2, RefreshCw, Zap, Sparkles, Building2, UserCheck2 } from "lucide-react";
import type { FitGapReport, Portfolio } from "@/types";

export default function FitGapReportPage() {
  const { id, sessionId, vacancyId } = useParams<{
    id: string;
    sessionId: string;
    vacancyId: string;
  }>();

  const [report, setReport] = useState<FitGapReport | null>(null);
  const [portfolio, setPortfolio] = useState<Portfolio | null>(null);
  const [generating, setGenerating] = useState(false);
  const [loading, setLoading] = useState(true);
  const [exporting, setExporting] = useState<"pdf" | "json" | null>(null);
  const [regenerating, setRegenerating] = useState(false);

  const fetchReport = useCallback(async () => {
    if (!portfolio) return;
    try {
      const res = await portfoliosApi.getFitGap(portfolio.id, Number(vacancyId));
      setReport(res.data.report);
      setGenerating(false);
    } catch (e: any) {
      if (e?.response?.status === 404) {
        try {
          await portfoliosApi.triggerFitGap(portfolio.id, Number(vacancyId));
          setGenerating(true);
        } catch {
          setGenerating(false);
        }
      }
    }
  }, [portfolio, vacancyId]);

  useEffect(() => {
    sessionsApi
      .getPortfolio(Number(sessionId))
      .then(async (res) => {
        const data = res.data as any;
        if (data.portfolio) {
          setPortfolio(data.portfolio);
        }
      })
      .finally(() => setLoading(false));
  }, [sessionId]);

  useEffect(() => {
    if (portfolio) fetchReport();
  }, [portfolio, fetchReport]);

  usePolling(fetchReport, 5000, generating && !!portfolio);

  const handleRegenerate = async () => {
    if (!portfolio) return;
    setRegenerating(true);
    try {
      await portfoliosApi.regenerateFitGap(portfolio.id, Number(vacancyId));
      setReport(null);
      setGenerating(true);
    } finally {
      setRegenerating(false);
    }
  };

  const handleExport = async (format: "pdf" | "json") => {
    if (!portfolio) return;
    setExporting(format);
    try {
      const res = await portfoliosApi.exportPortfolio(portfolio.id, format, Number(vacancyId));
      const ext = format;
      const blob = format === "pdf"
        ? new Blob([res.data as BlobPart], { type: "application/pdf" })
        : new Blob([JSON.stringify(res.data, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `fitgap-${sessionId}-${vacancyId}.${ext}`;
      a.click();
      URL.revokeObjectURL(url);
    } finally {
      setExporting(null);
    }
  };

  if (loading) {
    return (
      <div className="max-w-3xl mx-auto space-y-6 py-8">
        <Skeleton className="h-10 w-64 bg-slate-800" />
        <Skeleton className="h-48 w-full bg-slate-800 rounded-2xl" />
        <Skeleton className="h-48 w-full bg-slate-800 rounded-2xl" />
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto space-y-8 py-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-5 bg-slate-900/70 backdrop-blur-xl border border-slate-800 rounded-2xl shadow-xl">
        <div className="flex items-center gap-3">
          <Link
            to={`/assessments/${id}/sessions/${sessionId}/portfolio`}
            className="p-2 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-700 transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
          </Link>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl font-bold tracking-tight text-white">Laporan Kesesuaian Lowongan</h1>
              <span className="px-2 py-0.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold">
                Fit/Gap Report
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">Membandingkan portofolio kandidat terhadap kualifikasi posisi lowongan.</p>
          </div>
        </div>

        {portfolio && (
          <div className="flex items-center gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={handleRegenerate}
              disabled={regenerating || generating}
              className="border-slate-700 bg-slate-800/60 rounded-xl text-xs text-slate-200 hover:bg-slate-700"
            >
              {regenerating ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <RefreshCw className="h-3.5 w-3.5 mr-1" />}
              Analisis Ulang
            </Button>
            {report && (
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
        )}
      </div>

      {/* Generating state */}
      {generating && (
        <div className="border border-slate-800 bg-slate-900/60 backdrop-blur-xl rounded-3xl p-12 text-center space-y-4 shadow-2xl">
          <div className="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 flex items-center justify-center mx-auto">
            <Loader2 className="h-6 w-6 animate-spin" />
          </div>
          <div>
            <p className="text-base font-semibold text-white">Menghasilkan Laporan Fit/Gap...</p>
            <p className="text-xs text-slate-400 mt-1 max-w-sm mx-auto leading-relaxed">
              Mesin analisis sedang mencocokkan level kompetensi dan mensintesis narasi budaya kerja.
            </p>
          </div>
        </div>
      )}

      {/* Report ready */}
      {report && (
        <>
          {/* Skill comparison matrix */}
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <Building2 className="h-4 w-4 text-cyan-400" />
              <h2 className="text-sm font-bold text-white tracking-wide uppercase">Matriks Perbandingan Kompetensi</h2>
            </div>
            <ComparisonTable comparisons={report.skill_comparisons} />
          </div>

          <Separator className="bg-slate-800" />

          {/* Culture & competency narrative */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <Card className="border-slate-800 bg-slate-900/60 backdrop-blur-md rounded-2xl shadow-lg">
              <CardHeader className="pb-2.5">
                <CardTitle className="text-sm font-bold text-white flex items-center gap-2">
                  <Sparkles className="h-4 w-4 text-amber-400" />
                  Kesesuaian Budaya &amp; Cara Kerja
                </CardTitle>
              </CardHeader>
              <CardContent className="px-5 pb-5">
                <p className="text-xs text-slate-300 leading-relaxed whitespace-pre-wrap bg-slate-950/40 p-3.5 rounded-xl border border-slate-800">
                  {report.culture_narrative || "Narasi kesesuaian budaya belum tersedia."}
                </p>
              </CardContent>
            </Card>

            <Card className="border-slate-800 bg-slate-900/60 backdrop-blur-md rounded-2xl shadow-lg">
              <CardHeader className="pb-2.5">
                <CardTitle className="text-sm font-bold text-white flex items-center gap-2">
                  <UserCheck2 className="h-4 w-4 text-emerald-400" />
                  Rekomendasi Eksekutif
                </CardTitle>
              </CardHeader>
              <CardContent className="px-5 pb-5">
                <p className="text-xs text-slate-300 leading-relaxed whitespace-pre-wrap bg-slate-950/40 p-3.5 rounded-xl border border-slate-800">
                  {report.overall_narrative || "Rekomendasi keseluruhan belum tersedia."}
                </p>
              </CardContent>
            </Card>
          </div>

          {/* Discovered skills */}
          {portfolio && portfolio.skills.some((s) => s.is_discovered) && (
            <>
              <Separator className="bg-slate-800" />
              <Card className="border-slate-800 bg-slate-900/40 rounded-2xl">
                <CardHeader className="pb-3">
                  <CardTitle className="text-sm font-bold text-white flex items-center gap-1.5">
                    <Zap className="h-4 w-4 text-amber-400" />
                    Keahlian Tambahan yang Terdeteksi
                  </CardTitle>
                </CardHeader>
                <CardContent className="px-5 pb-5 space-y-2.5">
                  {portfolio.skills
                    .filter((s) => s.is_discovered)
                    .map((s) => (
                      <div key={s.id} className="text-xs flex items-center justify-between p-3 rounded-xl bg-slate-800/40 border border-slate-800">
                        <div className="flex items-center gap-2">
                          <span className="font-semibold text-white">{s.skill_label}</span>
                          <span className="px-2 py-0.5 rounded-full bg-slate-700 text-slate-300 text-[10px]">
                            {s.ai_level || "Unassessed"}
                          </span>
                        </div>
                        <span className="text-[11px] text-slate-400">Nilai tambah di luar kualifikasi posisi</span>
                      </div>
                    ))}
                </CardContent>
              </Card>
            </>
          )}
        </>
      )}
    </div>
  );
}

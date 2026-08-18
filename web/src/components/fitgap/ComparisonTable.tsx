import { LEVEL_LABELS, FIT_GAP_RESULT_LABELS, FIT_GAP_RESULT_CLASSES } from "@/utils/constants";
import { cn } from "@/lib/utils";
import { CheckCircle2, Star, AlertTriangle, HelpCircle, UserCheck } from "lucide-react";
import type { SkillComparison } from "@/types";

interface ComparisonTableProps {
  comparisons: SkillComparison[];
}

function ResultBadge({ comparison }: { comparison: SkillComparison }) {
  const label = FIT_GAP_RESULT_LABELS[comparison.result] || comparison.result;
  const classes = FIT_GAP_RESULT_CLASSES[comparison.result] || "bg-slate-800 text-slate-300";

  let Icon = HelpCircle;
  let suffix = "";
  if (comparison.result === "match") {
    Icon = CheckCircle2;
  } else if (comparison.result === "exceed") {
    Icon = Star;
    suffix = comparison.delta ? ` (+${comparison.delta})` : "";
  } else if (comparison.result === "gap") {
    Icon = AlertTriangle;
    suffix = comparison.delta ? ` (${comparison.delta})` : "";
  }

  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 text-xs font-semibold px-2.5 py-1 rounded-lg shadow-sm border",
        classes
      )}
    >
      <Icon className="h-3.5 w-3.5" />
      <span>{label}{suffix}</span>
    </span>
  );
}

export default function ComparisonTable({ comparisons }: ComparisonTableProps) {
  const matchCount = comparisons.filter((c) => c.result === "match").length;
  const gapCount = comparisons.filter((c) => c.result === "gap").length;
  const exceedCount = comparisons.filter((c) => c.result === "exceed").length;
  const notAssessedCount = comparisons.filter((c) => c.result === "not_assessed").length;

  return (
    <div className="space-y-4">
      {/* Metric pills header */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
        <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-emerald-950/30 border border-emerald-500/20 text-emerald-300 text-xs">
          <CheckCircle2 className="h-4 w-4 text-emerald-400" />
          <span><strong>{matchCount}</strong> Sesuai (Match)</span>
        </div>
        <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-blue-950/30 border border-blue-500/20 text-blue-300 text-xs">
          <Star className="h-4 w-4 text-blue-400" />
          <span><strong>{exceedCount}</strong> Melebihi (Exceed)</span>
        </div>
        <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-amber-950/30 border border-amber-500/20 text-amber-300 text-xs">
          <AlertTriangle className="h-4 w-4 text-amber-400" />
          <span><strong>{gapCount}</strong> Kesenjangan (Gap)</span>
        </div>
        <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-slate-800/40 border border-slate-700/40 text-slate-400 text-xs">
          <HelpCircle className="h-4 w-4 text-slate-400" />
          <span><strong>{notAssessedCount}</strong> Belum Diuji</span>
        </div>
      </div>

      {/* Table container */}
      <div className="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900/40 backdrop-blur-md">
        <table className="w-full text-xs">
          <thead>
            <tr className="border-b border-slate-800 bg-slate-900/80 text-slate-400 uppercase tracking-wider text-[11px]">
              <th className="text-left px-4 py-3 font-semibold">Kompetensi</th>
              <th className="text-center px-4 py-3 font-semibold">Standar Lowongan</th>
              <th className="text-center px-4 py-3 font-semibold">Hasil Kandidat</th>
              <th className="text-center px-4 py-3 font-semibold">Status Evaluasi</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {comparisons.map((c, i) => {
              const reqLevel = (c as any).expected_level ?? c.required_level;
              return (
                <tr key={i} className="hover:bg-slate-800/30 transition-colors">
                  <td className="px-4 py-3 font-medium text-slate-200">{c.skill_label}</td>
                  <td className="px-4 py-3 text-center text-slate-400 font-medium">
                    {reqLevel ? LEVEL_LABELS[reqLevel] || `L${reqLevel}` : "—"}
                  </td>
                  <td className="px-4 py-3 text-center">
                    {c.candidate_level != null ? (
                      <div className="inline-flex items-center gap-1 font-semibold text-white">
                        <span>{LEVEL_LABELS[c.candidate_level] || `L${c.candidate_level}`}</span>
                        {c.is_override && (
                          <span title="Disesuaikan oleh Asesor" className="inline-flex items-center text-purple-400">
                            <UserCheck className="h-3 w-3" />
                          </span>
                        )}
                      </div>
                    ) : (
                      <span className="text-slate-500 italic">Unassessed</span>
                    )}
                  </td>
                  <td className="px-4 py-3 text-center">
                    <ResultBadge comparison={c} />
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

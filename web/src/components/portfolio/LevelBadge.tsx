import { LEVEL_LABELS, LEVEL_BADGE_CLASSES, LEVEL_DESCRIPTIONS } from "@/utils/constants";
import { cn } from "@/lib/utils";

interface LevelBadgeProps {
  level?: number | null;
  size?: "sm" | "md";
  className?: string;
}

export default function LevelBadge({ level, size = "md", className }: LevelBadgeProps) {
  if (!level || !LEVEL_LABELS[level]) {
    return (
      <div
        className={cn(
          "inline-flex flex-col items-center justify-center rounded-lg font-medium bg-slate-800 border border-slate-700 text-slate-400",
          size === "md" ? "px-3 py-2 min-w-16 text-xs" : "px-2 py-1 min-w-12 text-[11px]",
          className
        )}
      >
        <span>Unassessed</span>
        {size === "md" && (
          <span className="text-[9px] font-normal opacity-70">Belum Dievaluasi</span>
        )}
      </div>
    );
  }

  return (
    <div
      className={cn(
        "inline-flex flex-col items-center justify-center rounded-lg font-semibold shadow-sm",
        size === "md" ? "px-3 py-2 min-w-14 text-base" : "px-2 py-1 min-w-10 text-sm",
        LEVEL_BADGE_CLASSES[level] || "bg-slate-700 text-slate-200",
        className
      )}
    >
      <span>{LEVEL_LABELS[level]}</span>
      {size === "md" && (
        <span className="text-[10px] font-normal opacity-80">{LEVEL_DESCRIPTIONS[level]}</span>
      )}
    </div>
  );
}

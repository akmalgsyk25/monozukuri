import React from "react";
import { Sparkles, Mic, Volume2, Radio } from "lucide-react";
import { cn } from "@/lib/utils";

export type AIInteractionStatus = "listening" | "thinking" | "speaking" | "idle";

interface AIThoughtIndicatorProps {
  status: AIInteractionStatus;
  className?: string;
}

export const AIThoughtIndicator: React.FC<AIThoughtIndicatorProps> = ({ status, className }) => {
  const config = {
    listening: {
      label: "Mendengarkan Jawaban Anda...",
      containerClass: "border-emerald-500/30 bg-emerald-950/30 text-emerald-300 shadow-[0_0_15px_rgba(16,185,129,0.15)]",
      dotClass: "bg-emerald-400 animate-ping",
      icon: <Mic className="w-4 h-4 animate-pulse text-emerald-400" />,
    },
    thinking: {
      label: "AI Sedang Menganalisis Konteks...",
      containerClass: "border-amber-500/30 bg-amber-950/30 text-amber-300 shadow-[0_0_15px_rgba(245,158,11,0.15)]",
      dotClass: "bg-amber-400 animate-pulse",
      icon: <Sparkles className="w-4 h-4 animate-spin text-amber-400" />,
    },
    speaking: {
      label: "AI Sedang Menyampaikan Pertanyaan...",
      containerClass: "border-cyan-500/30 bg-cyan-950/30 text-cyan-300 shadow-[0_0_15px_rgba(6,182,212,0.15)]",
      dotClass: "bg-cyan-400 animate-bounce",
      icon: <Volume2 className="w-4 h-4 animate-pulse text-cyan-400" />,
    },
    idle: {
      label: "Sesi Wawancara Siap",
      containerClass: "border-slate-700 bg-slate-800/40 text-slate-400",
      dotClass: "bg-slate-500",
      icon: <Radio className="w-4 h-4 text-slate-500" />,
    },
  }[status];

  return (
    <div
      className={cn(
        "inline-flex items-center gap-2.5 px-4 py-2 rounded-full border text-xs font-medium backdrop-blur-md transition-all duration-300",
        config.containerClass,
        className
      )}
    >
      <span className="relative flex h-2 w-2">
        <span className={cn("absolute inline-flex h-full w-full rounded-full opacity-75", config.dotClass)} />
        <span className={cn("relative inline-flex rounded-full h-2 w-2", config.dotClass.split(" ")[0])} />
      </span>
      {config.icon}
      <span className="tracking-wide font-medium">{config.label}</span>
    </div>
  );
};

export default AIThoughtIndicator;

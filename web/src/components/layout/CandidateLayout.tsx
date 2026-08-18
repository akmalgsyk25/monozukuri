import { Outlet } from "react-router-dom";
import { RakaminLogo } from "@/components/ui/RakaminLogo";
import { ThemeToggle } from "@/components/ui/ThemeToggle";
import { ShieldCheck } from "lucide-react";

export default function CandidateLayout() {
  return (
    <div className="min-h-screen flex flex-col bg-background text-foreground transition-colors duration-200">
      {/* Candidate Focused Header */}
      <header className="border-b border-border/80 bg-card/85 backdrop-blur-md sticky top-0 z-40">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <RakaminLogo size="sm" subtitle="Candidate Assessment Room" />
          </div>

          <div className="flex items-center gap-3">
            <div className="hidden sm:flex items-center gap-1.5 text-xs text-muted-foreground bg-muted/50 px-2.5 py-1 rounded-full border border-border/50">
              <ShieldCheck className="h-3.5 w-3.5 text-emerald-500" />
              <span>Privasi Terlindungi (UU PDP)</span>
            </div>
            <ThemeToggle variant="segmented" />
          </div>
        </div>
      </header>

      {/* Main Candidate Interaction View */}
      <main className="flex-1 flex flex-col">
        <Outlet />
      </main>
    </div>
  );
}

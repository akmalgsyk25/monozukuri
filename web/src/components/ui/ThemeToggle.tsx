import React from "react";
import { useAtom } from "jotai";
import { themeAtom, type Theme } from "@/stores/themeAtom";
import { Sun, Moon, Laptop } from "lucide-react";
import { cn } from "@/lib/utils";

interface ThemeToggleProps {
  className?: string;
  variant?: "segmented" | "button";
}

export const ThemeToggle: React.FC<ThemeToggleProps> = ({ className, variant = "segmented" }) => {
  const [theme, setTheme] = useAtom(themeAtom);

  const options: { value: Theme; label: string; icon: React.ComponentType<{ className?: string }> }[] = [
    { value: "light", label: "Light", icon: Sun },
    { value: "dark", label: "Dark", icon: Moon },
    { value: "system", label: "System", icon: Laptop },
  ];

  if (variant === "button") {
    const current = options.find((o) => o.value === theme) || options[0];
    const CurrentIcon = current.icon;
    const nextTheme: Theme = theme === "light" ? "dark" : theme === "dark" ? "system" : "light";

    return (
      <button
        onClick={() => setTheme(nextTheme)}
        className={cn(
          "p-2 rounded-xl border border-border bg-card hover:bg-muted text-muted-foreground hover:text-foreground transition-all shadow-sm active:scale-95",
          className
        )}
        title={`Current: ${current.label}. Click to toggle.`}
        aria-label="Toggle theme"
      >
        <CurrentIcon className="h-4 w-4" />
      </button>
    );
  }

  return (
    <div
      className={cn(
        "inline-flex items-center p-1 rounded-xl bg-muted/60 border border-border/80 shadow-inner",
        className
      )}
      role="group"
      aria-label="Theme selector"
    >
      {options.map(({ value, label, icon: Icon }) => {
        const isActive = theme === value;
        return (
          <button
            key={value}
            onClick={() => setTheme(value)}
            className={cn(
              "relative flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-medium transition-all duration-200 cursor-pointer select-none",
              isActive
                ? "bg-card text-foreground shadow-sm font-semibold border border-border/50"
                : "text-muted-foreground hover:text-foreground hover:bg-muted/40"
            )}
            aria-pressed={isActive}
          >
            <Icon className={cn("h-3.5 w-3.5", isActive ? "text-primary" : "text-muted-foreground")} />
            <span className="hidden sm:inline">{label}</span>
          </button>
        );
      })}
    </div>
  );
};

export default ThemeToggle;

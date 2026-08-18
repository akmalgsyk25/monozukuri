import React from "react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { AlertCircle, ShieldCheck } from "lucide-react";

interface EndSessionModalProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onConfirm: () => void;
  isSubmitting?: boolean;
}

export const EndSessionModal: React.FC<EndSessionModalProps> = ({
  open,
  onOpenChange,
  onConfirm,
  isSubmitting = false,
}) => {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-md bg-slate-900/95 backdrop-blur-xl border-slate-800 text-white shadow-2xl">
        <DialogHeader>
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400">
              <AlertCircle className="w-6 h-6" />
            </div>
            <div>
              <DialogTitle className="text-lg font-semibold text-white">Akhiri Sesi Wawancara?</DialogTitle>
              <p className="text-xs text-slate-400 mt-0.5">Konfirmasi penyelesaian wawancara kompetensi</p>
            </div>
          </div>
          <DialogDescription className="text-slate-300 mt-3 text-sm leading-relaxed">
            Apakah Anda yakin ingin mengakhiri sesi ini? Seluruh rekaman suara, transkrip percakapan, dan bukti kompetensi Anda akan disimpan secara aman. Sistem AI akan langsung memproses kalkulasi portofolio dan evaluasi asesmen Anda.
          </DialogDescription>
        </DialogHeader>

        <div className="my-2 p-3 bg-slate-800/50 rounded-lg border border-slate-700/50 flex items-start gap-2.5 text-xs text-slate-300">
          <ShieldCheck className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
          <span>
            Data Anda dilindungi sesuai standar privasi UU PDP dan hanya dapat diakses oleh tim rekrutmen yang berwenang.
          </span>
        </div>

        <DialogFooter className="gap-2 sm:gap-0 mt-4">
          <Button
            variant="ghost"
            onClick={() => onOpenChange(false)}
            disabled={isSubmitting}
            className="text-slate-300 hover:bg-slate-800 hover:text-white border border-slate-700/50"
          >
            Lanjutkan Wawancara
          </Button>
          <Button
            variant="destructive"
            onClick={onConfirm}
            disabled={isSubmitting}
            className="bg-red-600 hover:bg-red-700 text-white shadow-lg shadow-red-600/30"
          >
            {isSubmitting ? "Mengakhiri..." : "Ya, Selesaikan Wawancara"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};

export default EndSessionModal;

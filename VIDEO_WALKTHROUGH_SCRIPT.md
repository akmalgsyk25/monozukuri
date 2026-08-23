# 🎬 PANDUAN & NASKAH LENGKAP REKAMAN VIDEO DEMONSTRASI (3–5 MENIT)
## AI Talent Intelligence Platform — Monozukuri Engineering Revamp
**Kandidat / Author**: Akmal Muzakki Bakir  
**Posisi**: Fullstack Product Engineer (Take-Home Case Study)  
**Link Folder Google Drive**: [Folder Pengumpulan Video & PDF](https://drive.google.com/drive/folders/19_2FUWJDyjjmZsbTGJc2g_Y_EGfWrNqD?usp=sharing)  
**Target Durasi**: 3 menit 30 detik s/d 4 menit 30 detik  

---

## 📋 CHECKLIST PERSIAPAN SEBELUM RECORDING (Pre-Recording Setup)

Buka 5 Tab di Browser Anda agar transisi rekaman mulus tanpa jeda:

1. **Tab 1 — Portal Penilai & Daftar Asesmen**:
   * URL: `http://localhost:5173/assessments`
   * Siapkan dalam tema terang (Light Mode) untuk menunjukkan warna khas Rakamin Teal (`#01959F`) dan logo monogram resmi.
2. **Tab 2 — Pre-Flight Hardware Check (Sisi Kandidat)**:
   * Buka tautan sesi baru (contoh: `http://localhost:5173/sessions/<invite_token>/hardware-check` atau buat sesi baru).
   * Pastikan izin mikrofon browser aktif agar VU Meter bergerak dinamis.
3. **Tab 3 — Ruang Wawancara Suara Live AI**:
   * URL: `http://localhost:5173/sessions/<invite_token>/interview`
   * Siapkan visualizer waveform audio yang aktif dan siap merespons suara.
4. **Tab 4 — Portofolio Kompetensi Kandidat**:
   * URL: `http://localhost:5173/assessments/3/sessions/8/portfolio` (Kandidat: Haikal)
   * Tunjukkan kartu kompetensi, anchor level L1–L5, dan kutipan verbatim AI.
5. **Tab 5 — Fit/Gap Role Matching & Ekspor PDF**:
   * URL: `http://localhost:5173/assessments/3/sessions/8/fitgap/1`
   * Tunjukkan perbandingan delta role, narasi kecocokan budaya, dan tombol download PDF.
6. **Aplikasi Terminal / VS Code di Background**:
   * Tampilkan hasil RSpec: `18 examples, 0 failures`.

---

## ⏱️ RANGKUMAN ALUR WAKTU (TIMELINE OVERVIEW)

| Menit | Adegan (Scene) | Fokus Demonstrasi |
| :--- | :--- | :--- |
| **00:00 – 00:45** | **Scene 1: Problem Statement & Monozukuri Vision** | Pengenalan diri, masalah baseline prototype, dan visi solusi menyeluruh. |
| **00:45 – 01:45** | **Scene 2: Live Candidate Experience & Audio Stream** | Pre-flight check, VU meter, dan live wawancara suara dengan Google Gemini. |
| **01:45 – 02:45** | **Scene 3: Evidence-Grounded Portfolio & Assessor Override** | Ekstraksi kutipan verbatim AI, anchor L1–L5, dan kontrol penilai (override). |
| **02:45 – 03:45** | **Scene 4: Fit/Gap Matching Intelligence & PDF Export** | Analisis delta skill lowongan, rekomendasi budaya kerja, dan download PDF. |
| **03:45 – 04:30** | **Scene 5: Engineering Rigor, UU PDP, & Closing** | Bukti RSpec 100% lulus, perlindungan data UU PDP, dan penutup. |

---

# 🎙️ NASKAH LENGKAP WORD-FOR-WORD (PROMPTER SCRIPT)

---

### 🟢 SCENE 1 (00:00 – 00:45) │ PROBLEM STATEMENT & MONOZUKURI VISION
**Tampilan Layar**: Buka **Tab 1** (`http://localhost:5173/assessments`).  
**Aksi Kursor**: Arahkan kursor ke logo Rakamin, navigasi SaaS modern, dan klik tombol tema (Light/Dark/System toggle).

> **Naskah Suara (Ucapkan dengan tenang & percaya diri):**
> 
> *"Halo tim rekrutmen dan technical assessor Rakamin. Nama saya **Akmal Muzakki Bakir**, dan pada kesempatan ini saya mempresentasikan hasil perombakan menyeluruh pada platform **AI Talent Assessment & Skill Intelligence**.*
> 
> *Saat pertama kali menganalisis codebase awal, kami menemukan beberapa titik kerapuhan kritis: protokol streaming audio yang sering terputus, kalkulasi skor yang mengalami crash jika ada skill yang belum terasesmen, serta ketiadaan bukti kutipan nyata dari kandidat yang membuat rekruter sulit memvalidasi hasil AI.*
> 
> *Dengan memegang prinsip **Monozukuri**—yaitu kebanggaan dalam ketelitian rekayasa piranti lunak—kami mentransformasikan platform ini menjadi sistem asesmen berbasis bukti yang andal, aman secara regulasi data pribadi, dan memiliki pengalaman pengguna bertaraf enterprise."*

---

### 🟢 SCENE 2 (00:45 – 01:45) │ LIVE CANDIDATE EXPERIENCE & AUDIO STREAM
**Tampilan Layar**: Pindah ke **Tab 2** (Hardware Check), lalu masuk ke **Tab 3** (Live Interview Room).  
**Aksi Kursor**: 
1. Tunjukkan bar VU Meter mikrofon bergerak saat Anda berbicara.
2. Klik tombol "Mulai Tes Kecepatan" (local speed test tanpa CORS issue).
3. Masuk ke ruang wawancara, tunjukkan **Waveform Audio Visualizer** dan **AI Thought Indicator** ("Mendengarkan...", "AI Menganalisis...").
4. Klik tombol "Selesaikan Wawancara" dan tunjukkan modal konfirmasi dengan perlindungan UU PDP.

> **Naskah Suara:**
> 
> *"Mari kita lihat alur pengalaman kandidat. Sebelum wawancara dimulai, kandidat disambut dengan **Pre-Flight Hardware Check**. Di sini terdapat **VU Meter mikrofon real-time** berbasis Web Audio API dan tes kecepatan koneksi lokal untuk memastikan kelancaran teknis tanpa hambatan.*
> 
> *Saat wawancara berlangsung, platform terhubung langsung ke **Gemini Multimodal Live API (`v1alpha`)** menggunakan model native audio `gemini-2.5-flash`. Komunikasi suara berjalan dua arah secara real-time dengan visualisasi gelombang audio dinamis dan indikator status AI.*
> 
> *Kami juga mengimplementasikan **silence pump 30 milidetik** di backend Rails ActionCable untuk memastikan deteksi jeda suara VAD berjalan akurat tanpa ada koneksi yang menggantung.*
> 
> *Saat kandidat mengakhiri sesi, data langsung dikunci secara aman dan dialihkan ke tahap evaluasi portofolio."*

---

### 🟢 SCENE 3 (01:45 – 02:45) │ EVIDENCE PORTFOLIO & ASSESSOR OVERRIDE
**Tampilan Layar**: Pindah ke **Tab 4** (`http://localhost:5173/assessments/3/sessions/8/portfolio`).  
**Aksi Kursor**:
1. Scroll ke kartu kompetensi (misal: *Node.js / Backend Development*).
2. Tunjukkan badge **Anchor Perilaku L1–L5** dan skor kepercayaan AI (*Confidence Score*).
3. Sorot bagian **"Kutipan Verbatim Ucapan Kandidat"** (kutipan asli tanpa halusinasi AI).
4. Klik tombol **"Override Rating ▼"**, ubah level rekomendasi, ketik catatan singkat, lalu klik **"Simpan Penilaian"**.

> **Naskah Suara:**
> 
> *"Setelah sesi berakhir, worker background secara otomatis memproses transkrip percakapan menggunakan **Gemini 3.1 Pro**.*
> 
> *Hasil evaluasi tidak berupa skor mentah, melainkan **Portofolio Kompetensi Terstruktur**. Model AI memetakan jawaban kandidat ke standar anchor perilaku L1 hingga L5 dan mengekstrak **kutipan verbatim asli** yang diucapkan kandidat. Hal ini memberikan transparansi penuh sehingga rekruter dapat mengaudit dasar penilaian AI secara objektif.*
> 
> *Selain itu, kami tetap menempatkan manusia sebagai pengambil keputusan tertinggi melalui fitur **Assessor Override**. Rekruter dapat menyesuaikan tingkat level penilaian dengan catatan justifikasi yang langsung tersimpan rapi dalam audit trail sistem."*

---

### 🟢 SCENE 4 (02:45 – 03:45) │ FIT/GAP MATCHING & EXECUTIVE PDF DOSSIER
**Tampilan Layar**: Pindah ke **Tab 5** (Halaman Fit/Gap).  
**Aksi Kursor**:
1. Tunjukkan matrix komparasi skill (status: *Exceed, Match, Gap, Unassessed*).
2. Tunjukkan narasi rekomendasi kecocokan budaya kerja (*Culture Fit Narrative*).
3. Klik tombol **"Ekspor PDF Dossier"** di pojok kanan atas.
4. Buka file PDF yang baru terunduh untuk memperlihatkan dokumen dossier resmi yang rapi.

> **Naskah Suara:**
> 
> *"Langkah selanjutnya adalah pencocokan kandidat ke kebutuhan posisi melalui **Fit/Gap Intelligence Engine**.*
> 
> *Engine ini menghitung delta kesesuaian secara akurat dengan penanganan null-safe yang tangguh untuk skill yang belum terasesmen. Sistem mengklasifikasikan status ke dalam empat kategori: Exceed, Match, Gap, dan Not Assessed, dilengkapi narasi kecocokan budaya organisasi.*
> 
> *Dengan satu klik pada tombol **Ekspor PDF**, sistem backend menggunakan pustaka Prawn untuk menghasilkan berkas dossier kandidat siap cetak berstandar eksekutif, lengkap dengan ringkasan metrik, grafik komparasi, dan jejak override asesor."*

---

### 🟢 SCENE 5 (03:45 – 04:30) │ ENGINEERING RIGOR, UU PDP, & CLOSING
**Tampilan Layar**: Pindah ke **Terminal / VS Code** (menampilkan test RSpec dan Rails code), lalu kembali ke layar utama portal.  
**Aksi Kursor**: 
1. Sorot tulisan `18 examples, 0 failures`.
2. Tunjukkan sekilas file `config/initializers/filter_parameter_logging.rb`.
3. Tampilkan kembali dashboard web Rakamin.

> **Naskah Suara:**
> 
> *"Seluruh fitur ini didukung oleh fondasi rekayasa piranti lunak yang sangat kokoh:*
> 
> 1. *Kami membangun test suite RSpec komprehensif dengan **18 skenario pengujian yang lulus 100% tanpa kegagalan**, mencakup pengujian regresi dan **Seeded Fault Test**.*
> 2. *Data pribadi kandidat dilindungi secara ketat sesuai amanat **UU Pelindungan Data Pribadi (UU PDP No. 27 Tahun 2022)** dengan parameter masking pada seluruh log transaksi audio dan transkrip.*
> 3. *Antarmuka frontend React Vite dibangun dengan sistem tema adaptif resmi Rakamin yang bebas AI-slop dan ramah aksesibilitas.*
> 
> *Platform ini kini siap release ke production dan siap kami pertanggungjawabkan pada sesi Live Technical Defense.*
> 
> *Terima kasih atas perhatian tim Rakamin. Saya Akmal Muzakki Bakir, salam Monozukuri!"*

---

## 💡 TIPS REKAMAN AGAR MAKSIMAL & ONE-TAKE:
* **Resolusi Layar**: Gunakan resolusi 1080p (1920x1080) pada browser (zoom 100% atau 90%).
* **Audio**: Gunakan headset / mic yang jernih dengan artikulasi santai dan tempo teratur.
* **Durasi Target**: Idealnya selesai di kisaran **3 menit 45 detik hingga 4 menit 15 detik**.
* **Upload**: Setelah selesai merekam, simpan file video (MP4) ke folder Google Drive:  
  👉 `https://drive.google.com/drive/folders/19_2FUWJDyjjmZsbTGJc2g_Y_EGfWrNqD?usp=sharing`

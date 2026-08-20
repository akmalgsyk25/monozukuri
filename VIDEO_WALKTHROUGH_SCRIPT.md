# PANDUAN REKAMAN VIDEO DEMONSTRASI (3–5 MENIT)
## AI Talent Intelligence Platform — Monozukuri Engineering Revamp
**Target**: Video Walkthrough untuk submission take-home case study Rakamin (Steps 1–6).  
**Platform Rekomendasi**: [Loom](https://www.loom.com), YouTube (Unlisted), atau Google Drive.  
**Durasi**: 3 menit 30 detik s/d 4 menit 30 detik.

---

## 🎬 Persiapan Sebelum Merekam (Pre-Recording Setup)

1. Buka browser di tab terpisah:
   - **Tab 1 (Portal Penilai)**: `http://localhost:5173/login` (Login dengan `admin@rakamin.com` / `password123`).
   - **Tab 2 (Daftar Asesmen)**: `http://localhost:5173/assessments`.
   - **Tab 3 (Portofolio Kandidat)**: Buka salah satu portofolio kandidat yang sudah terasesmen (contoh: `http://localhost:5173/assessments/1/sessions/1/portfolio`).
   - **Tab 4 (Fit/Gap Report)**: `http://localhost:5173/assessments/1/sessions/1/fitgap/1`.
   - **Tab 5 (Ruang Wawancara Kandidat)**: Buka link invite sesi baru di tab incognito untuk menunjukkan hardware check & waveform audio.
2. Siapkan terminal di background yang menampilkan:
   - Hasil RSpec: `18 examples, 0 failures`.

---

## 🎙️ Naskah & Alur Adegan Video (Scene-by-Scene Script)

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ MENIT 00:00 – 00:45 │ SCENE 1: PROBLEM STATEMENT & MONOZUKURI VISION          │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Tampilan Layar**: Dashboard Login & Navbar Portal Penilai (`http://localhost:5173`).
- **Poin Narasi**:
  > *"Halo tim penilai Rakamin, perkenalkan saya [Nama Anda]. Hari ini saya mempresentasikan hasil fullstack revamp platform AI Interview dengan pendekatan Monozukuri — menghadirkan pride in craftsmanship, arsitektur yang tangguh, dan kepatuhan hukum UU PDP No. 27/2022.*  
  > *Pada baseline awal, sistem mengalami beberapa critical gap: koneksi WebSocket audio yang rapuh, speed test yang terblokir CORS, potensi error matematika pada unassessed skills, dan ketiadaan bukti transkrip otentik. Kami telah merombak arsitektur ini secara menyeluruh dari backend Rails hingga frontend React."*

---

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ MENIT 00:45 – 01:45 │ SCENE 2: LIVE VOICE INTERVIEW & CANDIDATE EXPERIENCE    │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Tampilan Layar**: Halaman Pre-flight Hardware Check & Ruang Wawancara Kandidat.
- **Aksi di Layar**:
  1. Tunjukkan **Hardware Check**: Speed test lokal (tanpa CORS), uji mikrofon dengan VU meter animasi real-time, dan audio test.
  2. Klik **Mulai Wawancara**: Tunjukkan koneksi WebSocket Gemini Multimodal Live (`gemini-2.5-flash-native-audio-latest` pada `v1alpha`).
  3. Tunjukkan **Waveform Visualizer**, status *AI Sedang Mendengarkan / Menyampaikan Pertanyaan*, dan transkrip percakapan yang masuk secara live.
- **Poin Narasi**:
  > *"Untuk kandidat, kami membangun pengalaman wawancara suara real-time yang stabil dan minim latensi menggunakan Gemini Live API v1alpha. Sebelum masuk, hardware check memastikan mikrofon dan koneksi internet stabil. Selama wawancara, VAD silence-pump memastikan tidak ada audio yang terputus, dan transkrip direkam dengan enkripsi sesuai prinsip minimisasi data UU PDP."*

---

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ MENIT 01:45 – 02:45 │ SCENE 3: EVIDENCE-BASED PORTFOLIO & AUDIT KUTIPAN       │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Tampilan Layar**: Halaman Portofolio Kandidat (`/portfolio`).
- **Aksi di Layar**:
  1. Tunjukkan kartu ringkasan metrik (Total Keahlian, Dievaluasi, High Confidence, Rata-Rata Level).
  2. Buka salah satu kartu keahlian (contoh: *React / Frontend Core*).
  3. Sorot **Anchor Perilaku L1–L5** dan **Kutipan Verbatim Transkrip** (Candidate Evidence Quote).
  4. Tunjukkan penanganan keahlian yang belum diuji (*Unassessed badge* yang aman tanpa merusak perhitungan).
- **Poin Narasi**:
  > *"Setelah sesi selesai, model reasoning Gemini 3.1 Pro mengevaluasi transkrip secara mendalam. Yang membedakan sistem ini dari AI generik adalah evidence-grounding: setiap level keahlian (L1 sampai L5) wajib menyertakan kutipan langsung ucapan kandidat. Rekruter tidak perlu menebak, karena semua penilaian memiliki bukti konkret yang dapat diaudit."*

---

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ MENIT 02:45 – 03:45 │ SCENE 4: FIT/GAP LOWONGAN & EXPORT PDF DOSSIER          │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Tampilan Layar**: Halaman Fit/Gap Report (`/fitgap/1`).
- **Aksi di Layar**:
  1. Tunjukkan matriks komparasi status: **Sesuai (Match)**, **Melebihi (Exceed)**, dan **Kesenjangan (Gap)** dengan perhitungan delta yang null-safe.
  2. Tunjukkan narasi **Kesesuaian Budaya & Rekomendasi Eksekutif**.
  3. Tunjukkan fitur **Assessor Override** (penilai dapat menyesuaikan skor dengan catatan klinis).
  4. Klik tombol **PDF Download**: Tunjukkan file PDF Prawn yang terunduh rapi dengan kop resmi, skor, dan kutipan bukti.
- **Poin Narasi**:
  > *"Pada modul Fit/Gap, profil kompetensi kandidat dicocokkan otomatis dengan standar posisi lowongan. Asesor juga memiliki wewenang penuh untuk melakukan override jika diperlukan. Hanya dengan 1 klik, rekruter dapat mengunduh dokumen eksekutif PDF dossier siap cetak untuk diserahkan ke Hiring Manager."*

---

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ MENIT 03:45 – 04:30 │ SCENE 5: ENGINEERING RIGOR & TEST HARNESS               │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Tampilan Layar**: Terminal dengan hasil test suite RSpec dan branch git.
- **Aksi di Layar**:
  1. Tunjukkan terminal: `bundle exec rspec` → **18 examples, 0 failures**.
  2. Jelaskan singkat **Seeded Fault Test** (membuktikan test gagal saat guard null dihilangkan).
  3. Tunjukkan **Theme Toggle** (Light/Dark/System) yang mendukung UI/UX modern tanpa AI slop.
- **Poin Narasi**:
  > *"Dari sisi reliabilitas software, kami membangun test harness RSpec lengkap dengan 18 unit & integration tests yang 100% passing, memvalidasi failure paths, dan membuktikan ketahanan logika melalui Seeded Fault Test. Seluruh UI juga mematuhi prinsip anti-slop dengan desain Rakamin modern dan dukungan dual-mode theme.*  
  > *Demikian transformasi Monozukuri AI Interview Platform. Terima kasih atas perhatiannya!"*

---

## 💡 Tips Rekaman:
- Gunakan headset agar suara Anda terdengar jernih.
- Pastikan resolusi rekaman minimal 1080p (Full HD).
- Setelah video selesai diupload (misal di Loom atau YouTube Unlisted), salin link videonya untuk disematkan ke dalam laporan PDF.

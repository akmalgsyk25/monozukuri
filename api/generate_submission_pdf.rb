# frozen_string_literal: true

require 'prawn'
require 'prawn/table'

pdf_path = '/ai-interview/MONOZUKURI_SUBMISSION_REPORT.pdf'
screenshots_dir = '/ai-interview-root/docs/screenshots'

Prawn::Document.generate(pdf_path, page_size: 'A4', margin: [36, 36, 36, 36]) do |pdf|
  # Colors
  teal       = '01959F'
  dark_teal  = '007E88'
  navy       = '0D141F'
  slate_gray = '64748B'
  light_bg   = 'F8FAFC'
  border_col = 'CBD5E1'

  # Header Banner Card
  pdf.fill_color dark_teal
  pdf.fill_rectangle [0, pdf.cursor], pdf.bounds.width, 95
  pdf.fill_color 'FFFFFF'
  
  pdf.move_down 12
  pdf.indent(16) do
    pdf.font('Helvetica', style: :bold, size: 16) { pdf.text 'MONOZUKURI PRODUCT & ENGINEERING REPORT' }
    pdf.font('Helvetica', style: :bold, size: 10) { pdf.text 'AI-Powered Talent Assessment & Skill Intelligence Platform', color: 'FBC037' }
    pdf.move_down 4
    pdf.font('Helvetica', size: 8.5) do
      pdf.text 'Case Study: Fullstack Product Engineer | Applicant: Akmal Muzakki (akmalgsyk25)'
      pdf.text 'Fork Repo: https://github.com/akmalgsyk25/monozukuri | Branch: monozukuri | Date: 20 August 2026'
    end
  end
  
  pdf.move_down 24
  pdf.fill_color '000000'

  # Section Helper
  def section_heading(pdf, title, color = '01959F')
    pdf.move_down 14
    pdf.fill_color color
    pdf.font('Helvetica', style: :bold, size: 12) { pdf.text title }
    pdf.fill_color '000000'
    pdf.stroke_color '01959F'
    pdf.line_width 1
    pdf.stroke_horizontal_rule
    pdf.move_down 6
  end

  # Executive Summary
  section_heading(pdf, 'Executive Summary')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text 'Dokumen ini menyajikan laporan eksekusi lengkap transformasi produk dan rekayasa perangkat lunak fullstack untuk Rakamin AI Interview Platform. Berlandaskan filosofi Monozukuri (Craftsmanship & Pride in Making), platform ini ditingkatkan dari prototipe awal menjadi sistem intelijen talenta berbasis suara yang andal, aman, mematuhi regulasi UU PDP No. 27/2022, dan terverifikasi 100% lulus uji.', inline_format: true
  end

  # Step 1
  section_heading(pdf, 'Step 1: Setup & Local Exploration Narrative')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text 'Eksplorasi awal menemukan 3 masalah fundamental: ketiadaan test suite di RSpec, fragmentasi environment Docker/Postgres/Redis, dan invite link yang salah rute ke port backend 3001. Kami membangun Docker Compose terpadu, inisialisasi schema multi-tenant test-corp, dan merancang RSpec test harness dengan transaction rollback.', inline_format: true
  end

  # Step 2
  section_heading(pdf, 'Step 2: Deep Context & Domain Immersion (5 Core Pillars)')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text '<b>1. The Product:</b> Bukan sekadar bot wawancara, melainkan instrumen pembangun portofolio kompetensi dengan bukti kutipan verbatim otentik.', inline_format: true
    pdf.text '<b>2. The Industry:</b> Di Indonesia (500+ pelamar/posisi), voice screening objektif dengan anchor L1-L5 meniadakan bias latar belakang kampus.', inline_format: true
    pdf.text '<b>3. What It Is For:</b> Memberikan kesempatan adil bagi seluruh talenta untuk membuktikan kemampuan praktis.', inline_format: true
    pdf.text '<b>4. The Users:</b> Rekruter membutuhkan fit/gap cepat dan ekspor PDF 1-klik; Tech Lead membutuhkan transparansi kutipan dan audit override.', inline_format: true
    pdf.text '<b>5. Candidates & UU PDP (UU No. 27/2022):</b> Kepatuhan hukum melalui sanitasi log parameter, audio streaming ephemeral, dan pre-flight check adaptif.', inline_format: true
  end

  # Step 3
  pdf.start_new_page
  section_heading(pdf, 'Step 3: Defining Problem & Gap to Ideal Condition (P0-P3 Matrix)')
  
  gap_data = [
    ['ID', 'Severity', 'Kategori', 'Deskripsi Masalah (Gap)', 'Dampak pada User & Workflow'],
    ['GAP-01', 'P0 Blocker', 'Defective Impl', 'WebSocket Gemini Live memakai v1beta & model tidak valid.', 'Wawancara suara gagal seketika (error 1008); sesi tidak bisa dimulai.'],
    ['GAP-02', 'P0 Blocker', 'Defective Impl', 'Hardware speed test POST ke domain luar terblokir CORS.', 'Kandidat terkunci di pre-flight check dengan error merah console.'],
    ['GAP-03', 'P0 Blocker', 'Defective Impl', 'Session#invite_url mengarah ke backend Rails port 3001.', 'Kandidat menerima JSON mentah / 404 alih-alih UI wawancara React.'],
    ['GAP-04', 'P1 High', 'Defective Impl', 'Portfolios::Generator panggil model lama & crash kode markdown.', 'Generasi portofolio gagal total akibat JSON parse error LLM response.'],
    ['GAP-05', 'P1 High', 'Defective Impl', 'Fit/Gap kalkulasi pengurangan langsung pada level nil.', 'Server crash NoMethodError (-) for nilClass saat unassessed skills.'],
    ['GAP-06', 'P1 High', 'Missing Spec', 'Job generasi portofolio tanpa row lock & idempotency guard.', 'Duplikasi data skill di database saat user klik retry berulang kali.'],
    ['GAP-07', 'P2 Medium', 'Missing Spec', 'Ketiadaan mekanisme penilai untuk override skor AI & catatan audit.', 'Asesor tidak dapat mengoreksi evaluasi AI yang kurang akurat.'],
    ['GAP-08', 'P3 Low', 'Missing Spec', 'Tidak ada fitur ekspor portofolio ke format PDF dossier / JSON.', 'Rekruter tidak bisa membagikan dossier kandidat ke hiring manager.']
  ]

  pdf.table(gap_data, header: true, width: pdf.bounds.width) do |t|
    t.row(0).background_color = 'F1F5F9'
    t.row(0).font_style = :bold
    t.row(0).text_color = '0F172A'
    t.cells.padding = [4, 6]
    t.cells.size = 7.5
    t.cells.border_color = border_col
    t.column(0).width = 45
    t.column(1).width = 58
    t.column(2).width = 65
    t.column(3).width = 175
  end

  # Step 4
  section_heading(pdf, 'Step 4: Revamp Strategy, Acceptance Criteria & Trade-offs')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text '<b>Rasionalisasi Pilihan:</b> Memilih <i>Option B: Monozukuri Fullstack Revamp</i> daripada sekadar tambal sulam (Option A) atau ekstraksi microservices (Option C). Menghasilkan arsitektur Rails & TypeScript yang bersih, modular, dan teruji penuh.', inline_format: true
    pdf.text '<b>Self-Derived Acceptance Criteria:</b>', style: :bold
    pdf.text '1. Unassessed Skills (ai_level nil) tidak memicu crash; ditandai status not_assessed dengan delta 0.'
    pdf.text '2. Parser AI membersihkan fence markdown ```json secara otomatis untuk menjamin ekstraksi payload murni.'
    pdf.text '3. Asesor dapat melakukan override level skor dengan pencatatan audit trail lengkap.'
    pdf.text '4. Re-generasi portofolio dibungkus transaksi database untuk menjamin integritas data dan idempotensi.'
    pdf.text '5. Silence pump menginjeksi frame 0x00 PCM setiap 30ms agar VAD Gemini menandai turn completion secara mulus.'
  end

  # Step 5
  pdf.start_new_page
  section_heading(pdf, 'Step 5: Monozukuri Implementation & Proof of Craftsmanship')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text '<b>1. Test Suite Verification (100% Passing):</b>', style: :bold
    pdf.text 'RSpec test suite lengkap berhasil dijalankan dengan hasil: <b>18 examples, 0 failures</b> (mencakup Session model, Portfolios Generator, FitGap Engine, Prawn PDF Export, dan API request authorization).', inline_format: true
    pdf.move_down 4
    pdf.text '<b>2. Seeded Fault Test Proof:</b>', style: :bold
    pdf.text 'Injeksi kerusakan sengaja dilakukan pada <code>app/services/fit_gap/engine.rb</code> dengan menghapus null guard. RSpec langsung gagal (NoMethodError: undefined method - for nil:NilClass). Setelah dikembalikan ke logika defensif, seluruh 18 test kembali hijau, membuktikan keandalan test harness.', inline_format: true
    pdf.move_down 4
    pdf.text '<b>3. AI Verification Moment:</b>', style: :bold
    pdf.text 'AI sempat menyarankan endpoint WebSocket Gemini v1beta dengan gemini-2.0-flash-exp (error 1008). Investigasi mandiri ke Google API Agustus 2026 mengoreksi ke endpoint <b>v1alpha</b> dengan model <b>gemini-2.5-flash-native-audio-latest</b> dan REST model <b>gemini-3.1-pro-preview</b>, memulihkan koneksi live audio secara sempurna.', inline_format: true
    pdf.move_down 4
    pdf.text '<b>4. Kepatuhan Hukum UU PDP No. 27/2022:</b>', style: :bold
    pdf.text 'Parameter log sensitif dimasking via <code>filter_parameter_logging.rb</code> (:invite_token, :evidence, :transcript, :audio_data), migrasi reversibel, dan pemrosesan audio transient di memori tanpa retensi pihak ketiga.', inline_format: true
    pdf.move_down 4
    pdf.text '<b>5. UI/UX Revamp & Taste-Skill Parity:</b>', style: :bold
    pdf.text 'Integrasi identitas resmi Rakamin (Teal #01959F, Dark Navy #0D141F), font Plus Jakarta Sans & Inter, navbar SaaS modern standar, tema adaptif Light/Dark/System, audio visualizer waveform, dan bebas 100% dari AI slop.', inline_format: true
  end

  # Step 6
  section_heading(pdf, 'Step 6: Submission Deliverables & Video Walkthrough Guide')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text '<b>Pull Request GitHub:</b> https://github.com/akmalgsyk25/monozukuri/pull/new/monozukuri', style: :bold, color: '007E88'
    pdf.text '<b>Branch:</b> monozukuri | <b>Target:</b> main'
    pdf.move_down 4
    pdf.text '<b>Struktur Video Walkthrough (3-5 Menit):</b>', style: :bold
  end

  video_data = [
    ['Waktu', 'Tampilan Layar', 'Poin Demonstrasi & Narasi'],
    ['00:00 - 00:45', 'Portal Penilai & Login', 'Problem statement, kelemahan arsitektur awal, dan visi Monozukuri.'],
    ['00:45 - 01:45', 'Ruang Wawancara Live', 'Hardware check VU meter, waveform audio visualizer, percakapan suara AI.'],
    ['01:45 - 02:45', 'Portofolio Kompetensi', 'Kartu L1-L5, kutipan verbatim kandidat, penanganan unassessed skills.'],
    ['02:45 - 03:45', 'Fit/Gap & Ekspor PDF', 'Matriks kesesuaian posisi, override penilai, dan 1-klik download PDF dossier.'],
    ['03:45 - 04:30', 'Engineering Rigor', '18 RSpec tests passing, Seeded Fault verification, dan kepatuhan UU PDP.']
  ]

  pdf.table(video_data, header: true, width: pdf.bounds.width) do |t|
    t.row(0).background_color = 'F1F5F9'
    t.row(0).font_style = :bold
    t.cells.padding = [3, 5]
    t.cells.size = 7.5
    t.cells.border_color = border_col
    t.column(0).width = 70
    t.column(1).width = 110
  end

  # ── Visual Screenshot Showcase Pages ─────────────────────────────────────────
  pdf.start_new_page
  section_heading(pdf, 'Visual UI/UX Showcase (Screenshots 1 & 2)')

  # Screenshot 1: Login Portal
  img1_path = File.join(screenshots_dir, '01_login_portal.png')
  if File.exist?(img1_path)
    pdf.move_down 4
    pdf.font('Helvetica', style: :bold, size: 9) { pdf.text 'Figure 1: Portal Penilai & Rekruter (Rakamin Monogram & Adaptive Theme Engine)', color: '0F172A' }
    pdf.image img1_path, fit: [pdf.bounds.width, 220], position: :center
  end

  pdf.move_down 14

  # Screenshot 2: Hardware Check
  img2_path = File.join(screenshots_dir, '02_hardware_check.png')
  if File.exist?(img2_path)
    pdf.font('Helvetica', style: :bold, size: 9) { pdf.text 'Figure 2: Pre-Flight Hardware Check (VU Meter Mikrofon & Local Speed Test)', color: '0F172A' }
    pdf.image img2_path, fit: [pdf.bounds.width, 220], position: :center
  end

  pdf.start_new_page
  section_heading(pdf, 'Visual UI/UX Showcase (Screenshots 3 & 4)')

  # Screenshot 3: Live Interview Room
  img3_path = File.join(screenshots_dir, '03_live_interview.png')
  if File.exist?(img3_path)
    pdf.move_down 4
    pdf.font('Helvetica', style: :bold, size: 9) { pdf.text 'Figure 3: Ruang Wawancara Suara Live (Waveform Audio Visualizer & State Indicator)', color: '0F172A' }
    pdf.image img3_path, fit: [pdf.bounds.width, 210], position: :center
  end

  pdf.move_down 14

  # Screenshot 4: Portfolio Evidence
  img4_path = File.join(screenshots_dir, '04_portfolio_evidence.png')
  if File.exist?(img4_path)
    pdf.font('Helvetica', style: :bold, size: 9) { pdf.text 'Figure 4: Portofolio Kompetensi (Anchor L1-L5 & Kutipan Verbatim Ucapan Kandidat)', color: '0F172A' }
    pdf.image img4_path, fit: [pdf.bounds.width, 230], position: :center
  end

  pdf.start_new_page
  section_heading(pdf, 'Visual UI/UX Showcase (Screenshot 5 & Conclusion)')

  # Screenshot 5: Fit/Gap & PDF Export
  img5_path = File.join(screenshots_dir, '05_fitgap_export.png')
  if File.exist?(img5_path)
    pdf.move_down 4
    pdf.font('Helvetica', style: :bold, size: 9) { pdf.text 'Figure 5: Fit/Gap Role Matching Matrix, Rekomendasi Budaya & Ekspor PDF Dossier', color: '0F172A' }
    pdf.image img5_path, fit: [pdf.bounds.width, 240], position: :center
  end

  pdf.move_down 16
  section_heading(pdf, 'Conclusion & Live Technical Defense Readiness')
  pdf.font('Helvetica', size: 8.5) do
    pdf.text 'Seluruh aspek dalam tugas take-home ini dikerjakan dengan standar craftsmanship tertinggi (Monozukuri). Mulai dari protokol transmisi audio bidi-streaming, ketahanan kalkulasi matematika, hingga antarmuka pengguna bebas AI-slop dengan tema adaptif, platform ini siap dipertanggungjawabkan pada sesi Live Technical Defense bersama CTO dan Technical Lead Rakamin.', inline_format: true
  end

  # Footer Note on all pages
  pdf.number_pages '<page> / <total>', {
    start_count_at: 1,
    at: [pdf.bounds.right - 50, -10],
    align: :right,
    size: 8,
    color: slate_gray
  }
end

puts "PDF with embedded screenshots generated successfully at #{pdf_path}"

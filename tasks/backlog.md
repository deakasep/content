# Backlog

Task yang sudah didefinisikan tapi belum dikerjakan. Urut berdasarkan priority. Format: [task-template](./templates/task-template.md).

## TASK-011: Verifikasi spec platform (ASSUMPTION → DATA FINAL)

- ID: TASK-011
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Nilai teknis di file platform (batas caption IG, jumlah hashtag, rasio, batas teks GBP, durasi/caption TikTok) masih berstatus ASSUMPTION/CLIENT CONFIRMATION. Cek ke help center resmi tiap platform. **Blocker 2026-10-04:** help.instagram.com, facebook.com, support.tiktok.com, dan support.google.com diblokir egress proxy sesi Claude Code; perlu verifikasi manual oleh owner atau allowlist domain di environment.
- Acceptance Criteria: Setiap baris spec punya sumber + tanggal akses dan status DATA FINAL, atau dicatat kenapa tidak bisa diverifikasi; validator lulus.
- Related: [instagram.md](../knowledge/platforms/instagram.md), [tiktok.md](../knowledge/platforms/tiktok.md), [google-business.md](../knowledge/platforms/google-business.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/1>

## TASK-028: Review independen (manusia) atas pilot 2 v3

- ID: TASK-028
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Rule 08: konten L2 butuh claim review independen. Semua QA pilot 2 (v1, v2, v3) masih self-review agent. Sejak split, pilot ada di repo clau-ai-marketing.
- Acceptance Criteria: Owner/content lead menghitung ulang tabel ekstraksi kalimat, kecocokan brief, dan publication checklist v3 dengan rubrik skor; mengisi status Independent score; mencatat selisih dengan self-score 92 (selisih > 5 poin = temuan).
- Related: [v3](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/examples/pilot-2/v3.md), [scoring-rubric](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/qa/scoring-rubric.md), [claim-verification](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/qa/claim-verification.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/28>
- Note 2026-10-04: owner meng-approve semua item pending, tapi hitung ulang independen belum dilakukan. Self-score v3 (92) belum berstatus Independent score; task tetap terbuka sampai ada recount.

## TASK-032: Dynamic approval level di platform (clau-ai-agents)

- ID: TASK-032
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-06
- Due: —
- Description: (Dikerjakan saat backend mulai menyimpan draft & approval.) `registry.json` hanya menyimpan approval **minimum** per intent (mis. `localize` L1, `review-reply` L1). Level sebenarnya harus naik otomatis dari isi konten: ada harga/promo → min L2; review negatif / isu agama-adat / konten berbayar → L3; `localize` mengikuti level konten asal (rule 08, router.md, decision-tree.md).
- Acceptance Criteria: Fungsi server `effective_level(draft)` = max(level intent, level dari klaim/kategori konten, level konten asal); approval & "Kirim ke klien" memakai level ini; UI menampilkan level + alasannya; test untuk kasus harga/promo, review negatif, localize dari konten L2.
- Related: <https://github.com/d34faiza-commits/clau-ai-agents/blob/main/agents/registry.json>, <https://github.com/d34faiza-commits/clau-ai-core/blob/main/orchestrator/router.md>, <https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/rules/08-APPROVAL-PUBLICATION-STANDARD.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/29>

## TASK-035: Aktivasi Pilar 2 — AI Sales

- ID: TASK-035
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Setelah TASK-034 memutuskan scope, jalankan 6 langkah "Menambah Pilar" di core: repo pilar (struktur seperti clau-ai-marketing + submodule `core/`), workflow & rules pilar, skill untuk intent `inquiry-reply` (agent Galih), lalu aktifkan di router + `registry.json` (`agents` dan `pillars`) + README core. UI: antrean Inquiry di Studio + konfirmasi harga & paket di Portal. Sampai selesai, permintaan intent `inquiry-reply` dieskalasi ke owner (`POST /route` → `escalate_to_owner`). Konsep v2: menjadi **AI Sales** (gabung dengan TASK-036); cetak biru `clau-ai-core/docs/blueprints/sales.md`.
- Acceptance Criteria: Harga, tanggal, ketersediaan di draft hanya dari fakta DATA FINAL; server menolak draft dengan fakta CLIENT CONFIRMATION untuk ditandai siap. Status pilar **Aktif** di core README = `active` di `registry.json` (test registry lulus); eval agent Galih lulus (deterministik PASS + rubrik ≥ 4, dinilai manusia); pilot SIMULASI end-to-end tercatat; layar pilar di `design/pillars.md` masuk wireframe & mockup.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-ai-agents/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/36>

## TASK-036: Pilar 2 AI Sales — pesan tamu & eskalasi keluhan (bagian dari TASK-035)

- ID: TASK-036
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Setelah TASK-034 memutuskan scope, jalankan 6 langkah "Menambah Pilar" di core: repo pilar (struktur seperti clau-ai-marketing + submodule `core/`), workflow & rules pilar, skill untuk intent `guest-message` (agent Sari), lalu aktifkan di router + `registry.json` (`agents` dan `pillars`) + README core. UI: antrean pesan tamu + eskalasi keluhan di Studio. Sampai selesai, permintaan intent `guest-message` dieskalasi ke owner (`POST /route` → `escalate_to_owner`). Konsep v2: digabung ke **AI Sales** (TASK-035); cetak biru `clau-ai-core/docs/blueprints/sales.md`.
- Acceptance Criteria: Keluhan serius otomatis RISK + L3; tidak ada identitas tamu lengkap yang disimpan di platform. Status pilar **Aktif** di core README = `active` di `registry.json` (test registry lulus); eval agent Sari lulus (deterministik PASS + rubrik ≥ 4, dinilai manusia); pilot SIMULASI end-to-end tercatat; layar pilar di `design/pillars.md` masuk wireframe & mockup.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-ai-agents/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/37>

## TASK-037: Aktivasi Pilar 3 — AI Admin

- ID: TASK-037
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Setelah TASK-034 memutuskan scope, jalankan 6 langkah "Menambah Pilar" di core: repo pilar (struktur seperti clau-ai-marketing + submodule `core/`), workflow & rules pilar, skill untuk intent `sop` (agent Teguh), lalu aktifkan di router + `registry.json` (`agents` dan `pillars`) + README core. UI: Library SOP (versi, pemilik, tanggal review). Sampai selesai, permintaan intent `sop` dieskalasi ke owner (`POST /route` → `escalate_to_owner`). Konsep v2: diperluas menjadi **AI Admin** (invoice, quotation, data entry, laporan, inventory, SOP); cetak biru `clau-ai-core/docs/blueprints/admin.md`.
- Acceptance Criteria: Langkah keselamatan di SOP wajib FIELD VERIFICATION sebelum Approved. Status pilar **Aktif** di core README = `active` di `registry.json` (test registry lulus); eval agent Teguh lulus (deterministik PASS + rubrik ≥ 4, dinilai manusia); pilot SIMULASI end-to-end tercatat; layar pilar di `design/pillars.md` masuk wireframe & mockup.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-ai-agents/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/38>

## TASK-038: Pilar 4 AI Business Intelligence — template laporan sendiri & data lintas pilar

- ID: TASK-038
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Intent `report` (agent Intan, Pilar 4 AI BI sejak v3.0.0) masih memakai template `monthly-report` Pilar 1 dan hanya metrik konten. Buat template laporan Pilar 5 dengan bagian per pilar aktif dan aturan "angka apa adanya, tanpa atribusi palsu", sesuai tab *Per pilar* di wireframe Laporan Studio. Data lintas pilar mengikuti `shared/data-flow.md` (P1→P5, P2→P5 tanpa data pribadi, P3→P5). Konsep v2: menjadi **AI Business Intelligence**; cetak biru `clau-ai-core/docs/blueprints/business-intelligence.md`.
- Acceptance Criteria: Template Pilar 4 ada di repo pilarnya (atau di clau-ai-marketing sementara, dengan catatan); `registry.json` agent `report-builder` menunjuk ke template itu; pilar belum aktif tampil "Belum ada data", bukan 0; setiap angka contoh menyebut sumber + waktu tarik data; test registry lulus.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/orchestrator/router.md>, <https://github.com/d34faiza-commits/clau-ai-core/blob/main/shared/data-flow.md>, [design/wireframes/dashboard-wireframe.md](../design/wireframes/dashboard-wireframe.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/39>

## TASK-039: Pilar 5 AI Automation — keputusan engine alur & konektor pertama

- ID: TASK-039
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Pilar baru konsep v2. Automation = lapisan penghubung antar pilar (WA/IG → AI → CRM → Sheets → invoice → email → follow-up), dijual sebagai langganan. Putuskan engine (bangun sendiri di clau-ai-agents atau n8n self-hosted di VPS) dan konektor pertama (usulan: WhatsApp Business Platform + Google Sheets). Cetak biru: `clau-ai-core/docs/blueprints/automation.md`. Bergantung pada TASK-040 dan Fase 0 platform.
- Acceptance Criteria: Keputusan engine tercatat; alur pertama berjalan di SIMULASI dengan audit log, dry run, dan tombol berhenti; setiap langkah punya level otonomi; tidak ada credential di repo.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/blueprints/automation.md>, <https://github.com/d34faiza-commits/clau-ai-agents/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/41>

## TASK-042: AI Marketing v2 — landing page, iklan, visual brief, brand voice

- ID: TASK-042
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Perluasan Pilar 1 yang sudah aktif: copy website/landing page, konsep & copy iklan berbayar, brief foto/video produk, voice guide & tagline. Intent usulan `landing-page`, `ad-brief`, `visual-brief`, `brand-voice` (belum di router). Cetak biru: `clau-ai-core/docs/blueprints/marketing.md`.
- Acceptance Criteria: Skill + template + QA tiap layanan di clau-ai-marketing; standar iklan berbayar di rules; intent di `router.md` + agent di `registry.json` (nama disetujui owner, avatar, persona, eval); test registry & validator lulus; pilot SIMULASI per layanan.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/blueprints/marketing.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/44>

## TASK-014: Quarterly review AI-CONSTITUTION

- ID: TASK-014
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: 2027-01-04
- Description: Review berkala sesuai `review_cycle: Quarterly` di AI-CONSTITUTION v2.0.0 (Approved & efektif 2026-10-04; menggantikan Content Constitution v1.0.0). Cek perubahan regulasi, kebijakan platform, dan pelajaran dari pilot/project. Perubahan hanya atas perintah Pak Indra atau Dea Karisna (d34faiza).
- Acceptance Criteria: Revision History AI-CONSTITUTION punya entry review (berubah atau "no change"), versi & README Versi Dokumen konsisten; validator core lulus.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/AI-CONSTITUTION.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/14>

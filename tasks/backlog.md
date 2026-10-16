# Backlog

Task yang sudah didefinisikan tapi belum dikerjakan. Urut berdasarkan priority. Format: [task-template](./templates/task-template.md).

## TASK-063: AI Content Agent — "Paket Konten Bulanan" (produk pertama)

- ID: TASK-063
- Status: Backlog
- Priority: High
- Assignee: AI → Dea Karisna (review & approve)
- Created: 2026-10-15
- Due: —
- Description: Arahan owner 2026-10-15: mulai dari satu agent yang menghasilkan uang. Alur berantai di atas Tahap 2 (TASK-052): strategi 30 hari (model sulit) → ✋ checkpoint owner → 30 ide → 30 caption + hashtag → 12 konsep visual → 8 naskah video pendek → CTA → AI fact-check ke fakta klien → ✋ review & approve owner → persetujuan tertulis klien (Rule 08) → publish oleh manusia. Butuh agent baru: strategi & riset, hashtag/keyword & repurposing, konsep visual (nama dipilih owner). Aset gambar/video menyusul (Rule 07).
- Acceptance Criteria: Satu paket lengkap untuk klien SIMULASI dihasilkan dari satu permintaan; setiap klaim faktual punya fact_key yang dikonfirmasi (klaim tanpa dasar ditandai dan memblok approval); dua checkpoint owner tercatat di audit log; biaya paket tercatat; tidak ada jalur publish otomatis.
- Related: TASK-052, TASK-042, [usulan Tahap 2 § 1a](https://github.com/d34faiza-commits/clau-core/blob/main/docs/proposals/tahap-2-ai-drafting.md)

## TASK-049: Backup VPS 2 tiap 6 jam + Backblaze B2 + pemulihan manual (pasang di server)

- ID: TASK-049
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna + AI
- Created: 2026-10-15
- Due: —
- Description: Kode siap di agents#54 (backup tiap 6 jam, salinan B2 dengan Object Lock, `clau-vps2-restore`, mode server pengganti). Menunggu CI (kuota GitHub Actions habis s.d. awal bulan) lalu merge. Owner: simpan `CLAU_SECRET_KEY` di password manager (bisa sekarang), buat akun B2 (langkah I nomor 1–5).
- Acceptance Criteria: agents#54 merged dengan CI hijau; langkah E diulang di VPS 2; `clau-vps2-offsite setup` menampilkan `OK Object Lock aktif`; `clau-vps2-check` menunjukkan salinan B2 ≤ 13 jam; `CLAU_SECRET_KEY` tersimpan di password manager.
- Related: https://github.com/d34faiza-commits/clau-agent/pull/54, [vps-2-setup § 3 H–I, § 5](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/deploy/vps-2-setup.md)

## TASK-050: CI hemat menit (GitHub Free 2.000 menit/bulan)

- ID: TASK-050
- Status: Backlog
- Priority: High
- Assignee: AI
- Created: 2026-10-15
- Due: —
- Description: Kuota Actions habis pertengahan Oktober 2026 → PR tidak bisa di-merge dan VPS tidak menerima versi baru. Usulan: CI sekali per commit (bukan push + pull_request), batalkan run lama saat ada commit baru, job `docker` hanya bila file Docker/backend/frontend berubah, cek lintas repo harian → mingguan + saat berubah. Aturan `main` wajib CI hijau tetap.
- Acceptance Criteria: Jumlah run per commit PR turun (1 run CI per commit); check wajib tetap melapor di setiap PR (tidak ada PR yang terkunci karena check tidak jalan); estimasi menit/bulan dicatat di PR.
- Related: https://github.com/d34faiza-commits/clau-agent/blob/main/.github/workflows/ci.yml

## TASK-051: Uji coba "VPS 2 hilang total" di VPS sementara

- ID: TASK-051
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna + AI
- Created: 2026-10-15
- Due: —
- Description: Membuktikan panduan server pengganti benar-benar jalan sebelum ada data klien nyata: VPS kecil sementara → langkah A–E → `clau-vps2-offsite setup` → `clau-vps2-restore --server-pengganti` dari B2 → login akun lama dengan 2FA → hapus VPS uji.
- Acceptance Criteria: Data tampil sama dengan VPS 2, login + 2FA akun lama berhasil di server uji, waktu pemulihan dicatat, temuan dimasukkan ke panduan; VPS uji dihapus.
- Related: [vps-2-setup § 5](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/deploy/vps-2-setup.md), TASK-049

## TASK-053: Legal & data pribadi (UU PDP) sebelum klien nyata

- ID: TASK-053
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna (+ konsultan hukum)
- Created: 2026-10-15
- Due: —
- Description: Kebijakan privasi, perjanjian pengolahan data dengan klien (termasuk pengolah AI), masa simpan data, penanggung jawab data, plus review hukum L1–L6 yang masih terbuka. AI menyiapkan draft; keputusan & tanda tangan oleh manusia.
- Acceptance Criteria: Kebijakan privasi + template perjanjian pengolahan data disetujui owner (dan dicek konsultan hukum); masa simpan per jenis data tercatat di core `shared/`; L1–L6 berstatus jelas.
- Related: [review-packet § 2](../docs/review-packet-task-041.md), [data-flow](https://github.com/d34faiza-commits/clau-core/blob/main/shared/data-flow.md)

## TASK-054: Keamanan tambahan sebelum klien login

- ID: TASK-054
- Status: Backlog
- Priority: Normal
- Assignee: AI
- Created: 2026-10-15
- Due: —
- Description: Di luar TASK-047 (domain/HTTPS/CSP/rate limit IP): 2FA wajib juga untuk `content_lead`, `purge-sessions` terjadwal di VPS 2, rotasi secret terdokumentasi, cek ulang `security.md` § 6.
- Acceptance Criteria: Test backend untuk 2FA `content_lead`; timer purge-sessions dicek `clau-vps2-check`; prosedur rotasi secret di panduan.
- Related: https://github.com/d34faiza-commits/clau-agent/blob/main/docs/security.md

## TASK-055: Onboarding klien nyata pertama (1 klien, 1 vertical, 1 kanal)

- ID: TASK-055
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna + AI
- Created: 2026-10-15
- Due: —
- Description: Setelah TASK-047, TASK-052, TASK-053: fact sheet nyata lewat Konfirmasi Fakta, brief, draft AI, review independen, approval tertulis klien, publish manual. Data klien hanya di platform/Client Workspace, tidak di repo.
- Acceptance Criteria: Satu konten klien nyata Approved lewat alur lengkap di platform; semua fakta DATA FINAL dari Konfirmasi Fakta; catatan pembelajaran masuk status.
- Related: [client-onboarding](https://github.com/d34faiza-commits/clau-market/blob/main/templates/client-onboarding.md)

## TASK-056: Monitoring & alarm (server, backup, biaya AI)

- ID: TASK-056
- Status: Backlog
- Priority: Normal
- Assignee: AI
- Created: 2026-10-15
- Due: —
- Description: Notifikasi ke owner (mis. email/Telegram) bila server/aplikasi mati, backup/salinan B2 gagal, disk penuh, atau biaya AI mendekati batas.
- Acceptance Criteria: Alarm uji (matikan backend, gagalkan backup) sampai ke owner < 10 menit; tanpa data klien di isi notifikasi.
- Related: https://github.com/d34faiza-commits/clau-agent/blob/main/scripts/deploy/vps2-check.sh

## TASK-057: Server staging (uji versi baru sebelum dipakai klien)

- ID: TASK-057
- Status: Backlog
- Priority: Low
- Assignee: AI
- Created: 2026-10-15
- Due: —
- Description: Lingkungan terpisah dengan data SIMULASI untuk mencoba rilis & migrasi sebelum VPS 2. Diaktifkan menjelang ±30 klien atau saat Tahap 2 mulai dipakai klien.
- Acceptance Criteria: Rilis melewati staging dulu (dicatat di panduan deploy); staging tidak pernah berisi data klien nyata.
- Related: https://github.com/d34faiza-commits/clau-agent/blob/main/docs/deploy/vps-2-setup.md

## TASK-058: Dashboard biaya & kualitas AI

- ID: TASK-058
- Status: Backlog
- Priority: Normal
- Assignee: AI
- Created: 2026-10-15
- Due: —
- Description: Biaya AI per klien/intent/bulan, persentase draft lolos QA, jumlah revisi, waktu sampai approval. Sumber: tabel log panggilan AI Tahap 2.
- Acceptance Criteria: Halaman owner menampilkan biaya bulan berjalan vs batas dan kualitas per agent; angka cocok dengan log.
- Related: TASK-052

## TASK-059: SOP tim: reviewer, eskalasi, insiden

- ID: TASK-059
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna + AI
- Created: 2026-10-15
- Due: —
- Description: Kapasitas review manusia = batas jumlah klien. SOP review independen (Rule 08), eskalasi Level C, dan respons insiden (server mati, data salah tayang, kebocoran).
- Acceptance Criteria: SOP tertulis disetujui owner; satu simulasi insiden dijalankan dan dicatat.
- Related: [rules/08](https://github.com/d34faiza-commits/clau-market/tree/main/rules)

## TASK-060: Paket langganan & penagihan

- ID: TASK-060
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna + AI
- Created: 2026-10-15
- Due: —
- Description: Paket harga, invoice, dan pencatatan langganan klien; menyambung ke Pilar 3 AI Admin (TASK-037).
- Acceptance Criteria: Paket & template invoice disetujui owner; data komersial klien tidak di repo.
- Related: TASK-037

## TASK-061: Rancangan skala 200+ klien

- ID: TASK-061
- Status: Backlog
- Priority: Low
- Assignee: AI
- Created: 2026-10-15
- Due: —
- Description: Worker AI di server terpisah (diskalakan sesuai antrean), database terkelola dengan replika + point-in-time recovery, 2+ server aplikasi di belakang load balancer, penyimpanan media terpisah, pentest pihak luar. Dipicu metrik beban, bukan jadwal.
- Acceptance Criteria: Rancangan + ambang pemicu (antrean, CPU, jumlah klien) tertulis di core `docs/`; tidak ada perubahan infrastruktur sebelum ambang tercapai.
- Related: TASK-052

## TASK-062: Bukti hasil untuk penjualan (case study pilot)

- ID: TASK-062
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-15
- Due: —
- Description: Kumpulkan data hasil klien pertama (engagement, inquiry, booking) dengan izin klien untuk bahan jualan.
- Acceptance Criteria: Satu case study dengan angka bersumber dan izin tertulis klien.
- Related: TASK-055

## TASK-047: Domain + HTTPS + CSP nonce (blocker deploy login)

- ID: TASK-047
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna (domain) → AI
- Created: 2026-10-13
- Due: —
- Description: Owner memilih/membeli domain. Lalu: Cloudflare + sertifikat, HSTS di Nginx, CSP berbasis nonce, rate limit login per IP, `vps-1-setup.md` Bagian 10–11. Kode login sudah siap (backend 0.6.0) tapi tidak boleh dipakai di server tanpa HTTPS.
- Acceptance Criteria: Dashboard hanya via HTTPS (HTTP → redirect), header HSTS, CSP tanpa `'unsafe-inline'` untuk script; `clau-vps1-check` diperluas dengan cek sertifikat.
- Related: <https://github.com/d34faiza-commits/clau-agent/blob/main/docs/security.md>

## TASK-011: Verifikasi spec platform (ASSUMPTION → DATA FINAL)

- ID: TASK-011
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Nilai teknis di file platform (batas caption IG, jumlah hashtag, rasio, batas teks GBP, durasi/caption TikTok) masih berstatus ASSUMPTION/CLIENT CONFIRMATION. Cek ke help center resmi tiap platform. **Blocker 2026-10-04:** help.instagram.com, facebook.com, support.tiktok.com, dan support.google.com diblokir egress proxy sesi Claude Code; perlu verifikasi manual oleh owner atau allowlist domain di environment.
- Acceptance Criteria: Setiap baris spec punya sumber + tanggal akses dan status DATA FINAL, atau dicatat kenapa tidak bisa diverifikasi; validator lulus.
- Related: [instagram.md](../knowledge/platforms/instagram.md), [tiktok.md](../knowledge/platforms/tiktok.md), [google-business.md](../knowledge/platforms/google-business.md), issue <https://github.com/d34faiza-commits/clau-content/issues/1>

## TASK-028: Review independen (manusia) atas pilot 2 v3

- ID: TASK-028
- Status: Backlog
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Rule 08: konten L2 butuh claim review independen. Semua QA pilot 2 (v1, v2, v3) masih self-review agent. Sejak split, pilot ada di repo clau-market.
- Acceptance Criteria: Owner/content lead menghitung ulang tabel ekstraksi kalimat, kecocokan brief, dan publication checklist v3 dengan rubrik skor; mengisi status Independent score; mencatat selisih dengan self-score 92 (selisih > 5 poin = temuan).
- Related: [v3](https://github.com/d34faiza-commits/clau-market/blob/main/examples/pilot-2/v3.md), [scoring-rubric](https://github.com/d34faiza-commits/clau-market/blob/main/qa/scoring-rubric.md), [claim-verification](https://github.com/d34faiza-commits/clau-market/blob/main/qa/claim-verification.md), issue <https://github.com/d34faiza-commits/clau-content/issues/28>
- Note 2026-10-04: owner meng-approve semua item pending, tapi hitung ulang independen belum dilakukan. Self-score v3 (92) belum berstatus Independent score; task tetap terbuka sampai ada recount.

## TASK-032: Dynamic approval level di platform (clau-agent)

- ID: TASK-032
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-06
- Due: —
- Description: (Dikerjakan saat backend mulai menyimpan draft & approval.) `registry.json` hanya menyimpan approval **minimum** per intent (mis. `localize` L1, `review-reply` L1). Level sebenarnya harus naik otomatis dari isi konten: ada harga/promo → min L2; review negatif / isu agama-adat / konten berbayar → L3; `localize` mengikuti level konten asal (rule 08, router.md, decision-tree.md).
- Acceptance Criteria: Fungsi server `effective_level(draft)` = max(level intent, level dari klaim/kategori konten, level konten asal); approval & "Kirim ke klien" memakai level ini; UI menampilkan level + alasannya; test untuk kasus harga/promo, review negatif, localize dari konten L2.
- Related: <https://github.com/d34faiza-commits/clau-agent/blob/main/agents/registry.json>, <https://github.com/d34faiza-commits/clau-core/blob/main/orchestrator/router.md>, <https://github.com/d34faiza-commits/clau-market/blob/main/rules/08-APPROVAL-PUBLICATION-STANDARD.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/29>

## TASK-035: Aktivasi Pilar 2 — AI Sales

- ID: TASK-035
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Setelah TASK-034 memutuskan scope, jalankan 6 langkah "Menambah Pilar" di core: repo pilar (struktur seperti clau-market + submodule `core/`), workflow & rules pilar, skill untuk intent `inquiry-reply` (agent Galih), lalu aktifkan di router + `registry.json` (`agents` dan `pillars`) + README core. UI: antrean Inquiry di Studio + konfirmasi harga & paket di Portal. Sampai selesai, permintaan intent `inquiry-reply` dieskalasi ke owner (`POST /route` → `escalate_to_owner`). Konsep v2: menjadi **AI Sales** (gabung dengan TASK-036); cetak biru `clau-core/docs/blueprints/sales.md`.
- Acceptance Criteria: Harga, tanggal, ketersediaan di draft hanya dari fakta DATA FINAL; server menolak draft dengan fakta CLIENT CONFIRMATION untuk ditandai siap. Status pilar **Aktif** di core README = `active` di `registry.json` (test registry lulus); eval agent Galih lulus (deterministik PASS + rubrik ≥ 4, dinilai manusia); pilot SIMULASI end-to-end tercatat; layar pilar di `design/pillars.md` masuk wireframe & mockup.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-agent/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/36>

## TASK-036: Pilar 2 AI Sales — pesan tamu & eskalasi keluhan (bagian dari TASK-035)

- ID: TASK-036
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Setelah TASK-034 memutuskan scope, jalankan 6 langkah "Menambah Pilar" di core: repo pilar (struktur seperti clau-market + submodule `core/`), workflow & rules pilar, skill untuk intent `guest-message` (agent Sari), lalu aktifkan di router + `registry.json` (`agents` dan `pillars`) + README core. UI: antrean pesan tamu + eskalasi keluhan di Studio. Sampai selesai, permintaan intent `guest-message` dieskalasi ke owner (`POST /route` → `escalate_to_owner`). Konsep v2: digabung ke **AI Sales** (TASK-035); cetak biru `clau-core/docs/blueprints/sales.md`.
- Acceptance Criteria: Keluhan serius otomatis RISK + L3; tidak ada identitas tamu lengkap yang disimpan di platform. Status pilar **Aktif** di core README = `active` di `registry.json` (test registry lulus); eval agent Sari lulus (deterministik PASS + rubrik ≥ 4, dinilai manusia); pilot SIMULASI end-to-end tercatat; layar pilar di `design/pillars.md` masuk wireframe & mockup.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-agent/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/37>

## TASK-037: Aktivasi Pilar 3 — AI Admin

- ID: TASK-037
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Setelah TASK-034 memutuskan scope, jalankan 6 langkah "Menambah Pilar" di core: repo pilar (struktur seperti clau-market + submodule `core/`), workflow & rules pilar, skill untuk intent `sop` (agent Teguh), lalu aktifkan di router + `registry.json` (`agents` dan `pillars`) + README core. UI: Library SOP (versi, pemilik, tanggal review). Sampai selesai, permintaan intent `sop` dieskalasi ke owner (`POST /route` → `escalate_to_owner`). Konsep v2: diperluas menjadi **AI Admin** (invoice, quotation, data entry, laporan, inventory, SOP); cetak biru `clau-core/docs/blueprints/admin.md`.
- Acceptance Criteria: Langkah keselamatan di SOP wajib FIELD VERIFICATION sebelum Approved. Status pilar **Aktif** di core README = `active` di `registry.json` (test registry lulus); eval agent Teguh lulus (deterministik PASS + rubrik ≥ 4, dinilai manusia); pilot SIMULASI end-to-end tercatat; layar pilar di `design/pillars.md` masuk wireframe & mockup.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-agent/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/38>

## TASK-038: Pilar 4 AI Business Intelligence — template laporan sendiri & data lintas pilar

- ID: TASK-038
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Intent `report` (agent Intan, Pilar 4 AI BI sejak v3.0.0) masih memakai template `monthly-report` Pilar 1 dan hanya metrik konten. Buat template laporan Pilar 5 dengan bagian per pilar aktif dan aturan "angka apa adanya, tanpa atribusi palsu", sesuai tab *Per pilar* di wireframe Laporan Studio. Data lintas pilar mengikuti `shared/data-flow.md` (P1→P5, P2→P5 tanpa data pribadi, P3→P5). Konsep v2: menjadi **AI Business Intelligence**; cetak biru `clau-core/docs/blueprints/business-intelligence.md`.
- Acceptance Criteria: Template Pilar 4 ada di repo pilarnya (atau di clau-market sementara, dengan catatan); `registry.json` agent `report-builder` menunjuk ke template itu; pilar belum aktif tampil "Belum ada data", bukan 0; setiap angka contoh menyebut sumber + waktu tarik data; test registry lulus.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/orchestrator/router.md>, <https://github.com/d34faiza-commits/clau-core/blob/main/shared/data-flow.md>, [design/wireframes/dashboard-wireframe.md](../design/wireframes/dashboard-wireframe.md), issue <https://github.com/d34faiza-commits/clau-content/issues/39>

## TASK-039: Pilar 5 AI Automation — keputusan engine alur & konektor pertama

- ID: TASK-039
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Pilar baru konsep v2. Automation = lapisan penghubung antar pilar (WA/IG → AI → CRM → Sheets → invoice → email → follow-up), dijual sebagai langganan. Putuskan engine (bangun sendiri di clau-agent atau n8n self-hosted di VPS) dan konektor pertama (usulan: WhatsApp Business Platform + Google Sheets). Cetak biru: `clau-core/docs/blueprints/automation.md`. Bergantung pada TASK-040 dan Fase 0 platform.
- Acceptance Criteria: Keputusan engine tercatat; alur pertama berjalan di SIMULASI dengan audit log, dry run, dan tombol berhenti; setiap langkah punya level otonomi; tidak ada credential di repo.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/blueprints/automation.md>, <https://github.com/d34faiza-commits/clau-agent/blob/main/docs/post-vps-checklist.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/41>

## TASK-042: AI Marketing v2 — landing page, iklan, visual brief, brand voice

- ID: TASK-042
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Perluasan Pilar 1 yang sudah aktif: copy website/landing page, konsep & copy iklan berbayar, brief foto/video produk, voice guide & tagline. Intent usulan `landing-page`, `ad-brief`, `visual-brief`, `brand-voice` (belum di router). Cetak biru: `clau-core/docs/blueprints/marketing.md`.
- Acceptance Criteria: Skill + template + QA tiap layanan di clau-market; standar iklan berbayar di rules; intent di `router.md` + agent di `registry.json` (nama disetujui owner, avatar, persona, eval); test registry & validator lulus; pilot SIMULASI per layanan.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/blueprints/marketing.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/44>

## TASK-014: Quarterly review AI-CONSTITUTION

- ID: TASK-014
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: 2027-01-04
- Description: Review berkala sesuai `review_cycle: Quarterly` di AI-CONSTITUTION (sekarang v3.1.0 Approved; v2.0.0 efektif 2026-10-04 menggantikan Content Constitution v1.0.0). Cek perubahan regulasi, kebijakan platform, dan pelajaran dari pilot/project. Perubahan hanya atas perintah Pak Indra atau Dea Karisna (d34faiza).
- Acceptance Criteria: Revision History AI-CONSTITUTION punya entry review (berubah atau "no change"), versi & README Versi Dokumen konsisten; validator core lulus.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/AI-CONSTITUTION.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/14>

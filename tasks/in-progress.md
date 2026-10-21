# In Progress

Task yang sedang dikerjakan. Batasi **maksimal 3 task** sekaligus supaya fokus dan cepat selesai. Format: [task-template](./templates/task-template.md).

## TASK-052: Tahap 2 — AI menulis draft (antrean kerja, model per tugas, batas biaya)

- ID: TASK-052
- Status: In Progress
- Priority: High
- Assignee: AI (rancangan) → Dea Karisna (keputusan)
- Created: 2026-10-15
- Due: —
- Description: Rancangan di clau-core `docs/proposals/tahap-2-ai-drafting.md`: worker + antrean kerja di PostgreSQL, panggilan Claude API dengan output terstruktur (draft + klaim), aturan data ke provider (usulan AI-BOUNDARY, butuh persetujuan owner), batas biaya per klien & global, eval 33 kasus sebagai gerbang, tombol mati. Implementasi bertahap PR 4a–4d setelah keputusan owner.
- Acceptance Criteria: Rancangan disetujui owner (termasuk teks AI-BOUNDARY); PR 4a–4d merged dengan CI hijau; 33 kasus eval lulus untuk agent yang diaktifkan; tidak ada data tamu mentah terkirim ke provider (dites).
- Related: [post-vps-checklist](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/post-vps-checklist.md), [integrations](https://github.com/d34faiza-commits/clau-core/blob/main/shared/integrations.md)
- Progress 2026-10-15: rancangan di core#16; arahan owner: model per tingkat kesulitan (Fable 5.1 sulit, Opus 5.5 utama, Haiku 5.5 ringan setelah eval), tidak ada AI → langsung publish, AI Content Agent dulu (TASK-063).
- Progress 2026-10-16: owner "setuju gas" → **AI-BOUNDARY v1.4.0** (§ Data ke Provider AI). PR 4a (kontrak core API 0.9.0, 3 tabel AI) di core#16; PR 4b (migrasi 0006, endpoint job, worker container terpisah, AI fact-check, batas biaya, provider tiruan, 28 test + smoke compose) di agents#54. Sisa: audit, PR 4c (provider Claude, menunggu akun & biaya owner), PR 4d (UI).
- Progress 2026-10-16 (lanjutan): audit adversarial 10 temuan, semua diperbaiki (draft AI klien nyata min L2, peminta draft AI = pembuat, DATA FINAL wajib cocok nilai, lease worker, reservasi biaya, tombol mati, penyamaran); 389 test lulus. **PR 4d (UI) selesai** di agents#54: tombol *Buat draft dengan AI* di `/requests/[id]`, halaman owner `/ai-usage`; E2E browser 12 cek lulus. Sisa: PR 4c (provider Claude: akun API, batas biaya, retensi data dari owner), CI ulang setelah kuota Actions reset (±1 Nov), merge core#16 lalu agents#54.
- Progress 2026-10-19: core#16 dan agents#54 merged; backend v0.9.0 live di VPS 2 (antrean AI + worker, provider tiruan, AI mati). Sisa hanya PR 4c (provider Claude), menunggu akun API, batas biaya, dan keputusan retensi data dari owner.

## TASK-041: Vertical fokus siap enterprise — villa, restoran/cafe, wedding, travel (lalu non-hospitality)

- ID: TASK-041
- Status: In Progress
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Fokus sekarang hospitality. Knowledge segment awal untuk 7 vertical sudah disiapkan sebagai **ASSUMPTION** (Planned, belum untuk client) di `clau-market/knowledge/segments/`; urutan gelombang di `clau-core/docs/verticals.md`. Vertical di luar hospitality menunggu amandemen scope (TASK-040).
- Acceptance Criteria: Per vertical yang diaktifkan: checklist aktivasi di `verticals.md` selesai (baris ASSUMPTION diverifikasi atau jadi CLIENT CONFIRMATION, rule tambahan bila ada regulasi sektor, voice guide, ≥ 2 kasus eval, pilot SIMULASI), status di `verticals.md` → Aktif, validator marketing lulus.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/verticals.md>, <https://github.com/d34faiza-commits/clau-market/tree/main/knowledge/segments>, issue <https://github.com/d34faiza-commits/clau-content/issues/43>, [paket review manusia](../docs/review-packet-task-041.md)
- Progress 2026-10-09: v3.0.0 §2 menetapkan 4 vertical fokus. Dibuat: fact sheet F&B/wedding/travel, schema brief v1.4, `GUARANTEE_TERMS` di check_caption, voice guide per vertical, pilot SIMULASI kafe/wedding/travel (clau-market#15), +5 kasus eval vertical (clau-agent#16). Sisa: verifikasi baris ASSUMPTION di segment wedding & travel (sumber resmi + tanggal akses), review independen manusia atas 3 pilot, legal review baris pernikahan WNA & izin operator. Non-hospitality tetap menunggu amandemen scope.
- Progress 2026-10-09 (2): riset sumber sekunder TN Komodo & pernikahan WNA masuk segment (clau-market#18). Semua langkah manusia yang tersisa (review independen 3 pilot, 6 pertanyaan legal, 7 verifikasi sumber primer, 2 keputusan owner) disiapkan di [docs/review-packet-task-041.md](../docs/review-packet-task-041.md).
- Progress 2026-10-09 (3): review independen 3 pilot oleh Dea Karisna (owner; metode: pre-review kritis AI + "setuju"). Hasil: Kafe 83, Wedding 84, Travel 83, Kesiapan 0, **belum lulus**. v2 ketiganya menunggu cek ulang reviewer. Dicatat lewat clau-market#22 dan [paket review § 1](../docs/review-packet-task-041.md). Sisa: cek ulang v2, legal L1–L6, sumber primer S2–S7.
- Progress 2026-10-09 (4): cek ulang v2 → reviewer **"lulus semua"** (kafe, wedding, travel; travel tetap tertahan gate izin sebelum tayang). Sisa TASK-041: legal L1–L6, sumber primer S2–S7, lalu status wedding & travel di `verticals.md` → Aktif. Handoff lintas sesi: [docs/status.md](../docs/status.md).

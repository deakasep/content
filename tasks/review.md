# Review

Output/draft sudah ada di repo, menunggu review owner dan verifikasi sumber sebelum dipindah ke [Done](./done.md).

## TASK-048: Tahap 1 PR 3b — fact sheet, konfirmasi fakta, dan UI workflow

- ID: TASK-048
- Status: Review
- Priority: High
- Assignee: AI (Claude Code), review owner
- Created: 2026-10-14
- Due: —
- Description: Endpoint kelola klien, fact sheet (versi, approve oleh approver klien), dan konfirmasi fakta (`fact_confirmations`, append-only) sesuai kontrak core; lalu halaman workflow di frontend (daftar request, editor draft + klaim, QA, tombol keputusan dengan bukti tertulis). Sampai ini selesai, approval draft yang memuat klaim fakta tetap ditolak (`facts_unconfirmed`, fail closed).
- Acceptance Criteria: Kontrak core diperbarui & di-merge dulu; konfirmasi fakta hanya oleh approver klien/owner dengan jejak; UI tidak menampilkan tombol publish; test PostgreSQL + E2E lewat frontend; CI hijau.
- Related: TASK-046, <https://github.com/d34faiza-commits/clau-ai-core/blob/main/shared/api-contracts.md>
- Note 2026-10-14: PR [core#15](https://github.com/d34faiza-commits/clau-ai-core/pull/15) (kontrak 0.8.0) dan [agents#48](https://github.com/d34faiza-commits/clau-ai-agents/pull/48) (backend 0.8.0 + UI). 295 test, uji mutasi 34/35, E2E Docker + uji browser lulus; 10 temuan audit adversarial diperbaiki. Pindah ke Done setelah kedua PR merge dengan CI hijau.

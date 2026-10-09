# Review

Output/draft sudah ada di repo, menunggu review owner dan verifikasi sumber sebelum dipindah ke [Done](./done.md).

## TASK-043: Keputusan nama produk untuk 5 pilar

- ID: TASK-043
- Status: Review
- Priority: Low
- Assignee: Pak Indra / Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Dipisah dari TASK-034. AI-CONSTITUTION v3.0.0 menetapkan 5 pilar v2 tetapi tidak memutuskan nama produk. Opsi A: tetap "CLAU AI Content Studio" untuk semua pilar. Opsi B: merek payung "CLAU AI", "Content Studio" = modul AI Marketing. Detail: [design/pillars.md § Nama Produk](../design/pillars.md#nama-produk).
- Acceptance Criteria: Keputusan tercatat; bila B: string i18n `app.name` + brand guideline diperbarui; validator lulus.
- Related: [design/pillars.md](../design/pillars.md), [design/brand/brand-guideline.md](../design/brand/brand-guideline.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/46>
- Note 2026-10-09: **Diputuskan opsi B** oleh owner Dea Karisna (d34faiza) atas rekomendasi agent ("gas kak.. kasih aku yg terbaik. aku percaya kaka"): merek payung **CLAU AI**, "Content Studio" = modul AI Marketing. Diterapkan di design/ (brand guideline, README, pillars.md, Figma/prototype guide, wireframe, tokens) dan frontend clau-ai-agents (logo, judul, Pengaturan); menunggu merge PR.

## TASK-044: Selaraskan WORKFLOW.md core dengan 5 pilar v2

- ID: TASK-044
- Status: Review
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: `clau-ai-core/WORKFLOW.md` (Approved v1.0.0) masih menyebut "1 Marketing & Content" di tabel workflow pilar. Persetujuan v3.0.0 hanya mencakup AI-CONSTITUTION, jadi WORKFLOW.md tidak diubah tanpa perintah owner.
- Acceptance Criteria: Owner memerintahkan perubahan; WORKFLOW.md naik versi PATCH dengan Revision History; README core Versi Dokumen sama; validator core lulus.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/WORKFLOW.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/47>
- Note 2026-10-09: Diperintahkan owner Dea Karisna (d34faiza) atas rekomendasi agent. WORKFLOW.md v1.0.1 (PATCH) di clau-ai-core#6; menunggu merge.

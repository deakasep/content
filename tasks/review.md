# Review

Output/draft sudah ada di repo, menunggu review owner dan verifikasi sumber sebelum dipindah ke [Done](./done.md).

## TASK-034: Keputusan owner — scope, nama, urutan pilar 2–5 & nama produk

- ID: TASK-034
- Status: Review
- Priority: High
- Assignee: Pak Indra / Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: `5-pillar-architecture.md` di core masih Draft: pilar 2–5 berstatus ASSUMPTION menunggu CLIENT CONFIRMATION soal nama, urutan, scope, dan nama repo (`clau-ai-sales`, `clau-ai-guest`, `clau-ai-operations`, `clau-ai-analytics` = usulan). Sekalian putuskan nama produk: tetap "CLAU AI Content Studio" untuk semua pilar (opsi A) atau merek payung "CLAU AI" dengan "Content Studio" sebagai modul Pilar 1 (opsi B). Sertakan keputusan **konsep v2** (AI Marketing, AI Sales, AI Admin, AI Business Intelligence, AI Automation; cetak biru di `clau-ai-core/docs/blueprints/`): dipakai sebagai nama 5 pilar atau tidak. Langkah ini membuka TASK-035–042.
- Acceptance Criteria: Keputusan tercatat di Revision History AI-CONSTITUTION; `5-pillar-architecture.md` tidak lagi bertanda ASSUMPTION untuk item yang diputuskan; tabel pilar di core README, `registry.json` → `pillars`, dan `design/pillars.md` § Nama Produk sudah sama; test registry clau-ai-agents dan validator core lulus.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-ai-agents/blob/main/agents/registry.json>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/35>
- Note 2026-10-09: **Diputuskan owner** (Dea Karisna / d34faiza): AI-CONSTITUTION v3.0.0 Approved — 5 pilar v2, otonomi A/B/C default B, vertical fokus villa, restoran/cafe, wedding, travel. Diterapkan di core (tabel pilar, router, 5-pillar-architecture) dan registry agents; menunggu merge core#5 + agents#16 + marketing#15 (d34faiza-commits). Nama produk belum diputuskan → dipisah ke TASK-043.

## TASK-040: Keputusan amandemen otonomi bertingkat & perluasan scope vertical

- ID: TASK-040
- Status: Review
- Priority: Normal
- Assignee: Pak Indra / Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: AI Sales (WhatsApp assistant) dan AI Automation butuh AI mengirim ke customer, sedangkan AI-CONSTITUTION §4.7 (Approved) melarangnya; §2 juga membatasi scope ke hospitality. Draf amandemen (Level A otomatis / B draft / C eskalasi + perluasan vertical) sudah disiapkan di `clau-ai-core/docs/proposals/autonomy-levels.md` dan **belum berlaku**.
- Acceptance Criteria: Owner memutuskan terima/ubah/tolak; bila diterima: AI-CONSTITUTION naik versi dengan Revision History, kolom Otonomi di `router.md`, `autonomy_max` di `registry.json` + test, validator core & test agents lulus.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/proposals/autonomy-levels.md>, <https://github.com/d34faiza-commits/clau-ai-core/blob/main/AI-CONSTITUTION.md>, issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/42>
- Note 2026-10-09: Usulan 1 (otonomi bertingkat) **Approved** di AI-CONSTITUTION v3.0.0 §4.7 + §4a; kolom Otonomi router + `autonomy_max` registry + test sudah dibuat, menunggu merge core#5 + agents#16 + marketing#15 (d34faiza-commits). Usulan 2 (scope di luar hospitality) **tidak** diputuskan; tetap usulan, dilacak di TASK-041.

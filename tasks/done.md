# Done

Arsip task yang sudah lolos acceptance criteria. Jangan dihapus — ini jejak traceability. Tambahkan `- Completed: YYYY-MM-DD` dan `- Commit: <hash>` saat memindahkan task ke sini. Format: [task-template](./templates/task-template.md).

## TASK-012: Pilot workflow dengan brief fiktif end-to-end

- ID: TASK-012
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Uji WORKFLOW.md (9 langkah) memakai properti fiktif ("Villa Contoh Ubud") dari brief sampai approval record, untuk menemukan celah di rules/skills/QA sebelum dipakai untuk client nyata.
- Acceptance Criteria: Satu brief valid terhadap schema, draft dari minimal 2 skill, semua QA gate terisi, daftar temuan/perbaikan dibuat sebagai task baru.
- Related: [pilot](../examples/pilot-villa-contoh-ubud/README.md), [WORKFLOW.md](../WORKFLOW.md), [content-brief schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/12>
- Completed: 2026-10-04
- Commit: 12c1eaa

## TASK-015: Tambah Voice Card ke schema & template brief

- ID: TASK-015
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-01 pilot TASK-012: brief tidak membawa Voice Card, sehingga brand voice tidak bisa diverifikasi dan skill jatuh ke voice default.
- Acceptance Criteria: Schema brief punya field voice (arketipe, 3 kata sifat, 3 "bukan", sapaan, emoji, kata wajib/terlarang) atau referensi Voice Card; `templates/content-brief.md` selaras; brief pilot diperbarui; validator lulus.
- Related: [pilot F-01](../examples/pilot-villa-contoh-ubud/README.md), [rule 03](../rules/03-CLIENT-BRAND-VOICE-STANDARD.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/15>
- Completed: 2026-10-04
- Commit: d05bda3

## TASK-016: Bikin template fact sheet properti

- ID: TASK-016
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-02 pilot TASK-012: tidak ada template fact sheet properti (bed type, ukuran kamar, kamar mandi, kebijakan, check-in/out, aksesibilitas), sehingga listing OTA tertahan placeholder.
- Acceptance Criteria: `templates/property-fact-sheet.md` ada (minimal vertical accommodation), setiap field punya kolom label evidence; skill `write-ota-listing` merujuk template ini; validator lulus.
- Related: [pilot F-02](../examples/pilot-villa-contoh-ubud/README.md), [write-ota-listing](../skills/write-ota-listing/SKILL.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/16>
- Completed: 2026-10-04
- Commit: ccb0145

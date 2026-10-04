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

## TASK-017: Mode simulasi/pilot di WORKFLOW & approval record

- ID: TASK-017
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-05 pilot TASK-012: WORKFLOW dan approval record tidak punya mode simulasi, sehingga record pilot berisiko terbaca sebagai approval nyata.
- Acceptance Criteria: `WORKFLOW.md` dan `templates/approval-record.md` punya aturan eksplisit mode SIMULASI (penanda wajib, langkah yang boleh dilewati, larangan publish); versi & Revision History naik; validator lulus.
- Related: [pilot F-05](../examples/pilot-villa-contoh-ubud/README.md), [WORKFLOW.md](../WORKFLOW.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/17>
- Completed: 2026-10-04
- Commit: 3dd6aee

## TASK-018: Self-check klaim tersirat di skill draft-caption

- ID: TASK-018
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-06 pilot TASK-012: klaim tersirat di Varian C lolos self-check skill dan baru tertangkap di claim gate.
- Acceptance Criteria: Self-check `draft-caption` (dan skill drafting lain yang relevan) menambah langkah ekstrak klaim tersirat (view, jarak, suasana, kapasitas) lalu cocokkan ke tabel klaim; validator lulus.
- Related: [pilot QA klaim #7](../examples/pilot-villa-contoh-ubud/qa-and-approval.md), [draft-caption](../skills/draft-caption/SKILL.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/18>
- Completed: 2026-10-04
- Commit: 32a6b47

## TASK-019: Wajibkan source_date untuk klaim DATA FINAL di schema

- ID: TASK-019
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-07 pilot TASK-012: schema hanya mewajibkan `source` untuk klaim DATA FINAL, padahal rule 01 dan Constitution meminta versi/tanggal sumber.
- Acceptance Criteria: Schema brief mewajibkan `source` + `source_date` untuk klaim DATA FINAL; brief contoh tetap valid; validator lulus.
- Related: [pilot F-07](../examples/pilot-villa-contoh-ubud/README.md), [schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/19>
- Completed: 2026-10-04
- Commit: 139718e

## TASK-010: Bikin automations/level-1-manual/README.md

- ID: TASK-010
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Dokumentasikan automation level 1 (manual/semi-manual) untuk workflow konten: checklist harian, copy-paste skill/prompt ke AI tool, scheduling manual oleh manusia. Folder `automations/` belum ada.
- Acceptance Criteria: Folder `automations/level-1-manual/` ada dengan README berisi scope, langkah, tools yang dipakai, dan batas (AI tidak publish/approve sendiri sesuai CONTENT-CONSTITUTION); validator lulus; README root mencantumkan folder baru.
- Related: [automations level 1](../automations/level-1-manual/README.md), [WORKFLOW.md](../WORKFLOW.md), [rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/11>
- Completed: 2026-10-04
- Commit: 99ed168

# Backlog

Task yang sudah didefinisikan tapi belum dikerjakan. Urut berdasarkan priority. Format: [task-template](./templates/task-template.md).

## TASK-010: Bikin automations/level-1-manual/README.md

- ID: TASK-010
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Dokumentasikan automation level 1 (manual/semi-manual) untuk workflow konten: checklist harian, copy-paste skill/prompt ke AI tool, scheduling manual oleh manusia. Folder `automations/` belum ada.
- Acceptance Criteria: Folder `automations/level-1-manual/` ada dengan README berisi scope, langkah, tools yang dipakai, dan batas (AI tidak publish/approve sendiri sesuai CONTENT-CONSTITUTION); validator lulus; README root mencantumkan folder baru.
- Related: [WORKFLOW.md](../WORKFLOW.md), [rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/11>

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

## TASK-013: Review knowledge/platforms/google-business.md & destinations

- ID: TASK-013
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Dua file knowledge yang belum masuk daftar review TASK-002–009. Cek akurasi, relevansi untuk 3 vertical awal, dan selaraskan dengan research pack 2026.
- Acceptance Criteria: Tidak ada klaim tanpa label; fakta volatile punya sumber + tanggal akses atau ditandai cek ulang; validator lulus.
- Related: [google-business.md](../knowledge/platforms/google-business.md), [indonesia-overview.md](../knowledge/destinations/indonesia-overview.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/13>

## TASK-014: Quarterly review CONTENT-CONSTITUTION

- ID: TASK-014
- Status: Backlog
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: 2027-01-03
- Description: Review berkala sesuai `review_cycle: Quarterly` di Constitution v1.0.0 (efektif 2026-10-03). Cek perubahan regulasi, kebijakan platform, dan pelajaran dari pilot/project.
- Acceptance Criteria: Revision History Constitution punya entry review (berubah atau "no change"), versi & README Versi Dokumen konsisten; validator lulus.
- Related: [CONTENT-CONSTITUTION.md](../CONTENT-CONSTITUTION.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/14>

## TASK-017: Mode simulasi/pilot di WORKFLOW & approval record

- ID: TASK-017
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-05 pilot TASK-012: WORKFLOW dan approval record tidak punya mode simulasi, sehingga record pilot berisiko terbaca sebagai approval nyata.
- Acceptance Criteria: `WORKFLOW.md` dan `templates/approval-record.md` punya aturan eksplisit mode SIMULASI (penanda wajib, langkah yang boleh dilewati, larangan publish); versi & Revision History naik; validator lulus.
- Related: [pilot F-05](../examples/pilot-villa-contoh-ubud/README.md), [WORKFLOW.md](../WORKFLOW.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/17>

## TASK-018: Self-check klaim tersirat di skill draft-caption

- ID: TASK-018
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-06 pilot TASK-012: klaim tersirat di Varian C lolos self-check skill dan baru tertangkap di claim gate.
- Acceptance Criteria: Self-check `draft-caption` (dan skill drafting lain yang relevan) menambah langkah ekstrak klaim tersirat (view, jarak, suasana, kapasitas) lalu cocokkan ke tabel klaim; validator lulus.
- Related: [pilot QA klaim #7](../examples/pilot-villa-contoh-ubud/qa-and-approval.md), [draft-caption](../skills/draft-caption/SKILL.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/18>

## TASK-019: Wajibkan source_date untuk klaim DATA FINAL di schema

- ID: TASK-019
- Status: Backlog
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-07 pilot TASK-012: schema hanya mewajibkan `source` untuk klaim DATA FINAL, padahal rule 01 dan Constitution meminta versi/tanggal sumber.
- Acceptance Criteria: Schema brief mewajibkan `source` + `source_date` untuk klaim DATA FINAL; brief contoh tetap valid; validator lulus.
- Related: [pilot F-07](../examples/pilot-villa-contoh-ubud/README.md), [schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/19>

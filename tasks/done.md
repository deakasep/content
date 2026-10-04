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

## TASK-020: Atur kata positioning (luxury/mewah) & nama brand yang menyiratkan klaim

- ID: TASK-020
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-05 pilot 2: "mewah/luxury" dan nama brand seperti "Sunset" tidak diatur di rules, hanya di file riset regulasi.
- Acceptance Criteria: Rule 02 punya bagian kata positioning & nama brand (checklist, risk, eskalasi); voice guide punya daftar kata positioning + pengganti; validator lulus.
- Related: [rule 02](../rules/02-HOSPITALITY-CLAIM-STANDARD.md), [pilot-2 G-05](../examples/pilot-2/REPORT.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/20>
- Completed: 2026-10-04
- Commit: ae3d6c4

## TASK-021: Prompt & skill reel/video script

- ID: TASK-021
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-02 pilot 2: tidak ada prompt/skill reel script; script dibuat improvisasi.
- Acceptance Criteria: `prompts/video/reel-script.md` + skill `draft-reel-script` (SKILL.md + agents/openai.yaml) dengan shot list, klaim & consent per shot; README index; validator lulus.
- Related: [reel-script](../prompts/video/reel-script.md), [skill](../skills/draft-reel-script/SKILL.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/21>
- Completed: 2026-10-04
- Commit: 03cf564

## TASK-022: Prompt Stories + aturan Reels/Stories/alt text di rule 05

- ID: TASK-022
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-03 & G-07 pilot 2: tidak ada prompt Stories; aturan emoji/hook/sticker/link dan alt text per slide belum ada.
- Acceptance Criteria: `prompts/stories/stories-sequence.md`; rule 05 punya aturan Reels, Stories, alt text per gambar + checklist; validator lulus.
- Related: [stories-sequence](../prompts/stories/stories-sequence.md), [rule 05](../rules/05-PLATFORM-STANDARD.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/22>
- Completed: 2026-10-04
- Commit: 090d678

## TASK-023: Brief sanity check di WORKFLOW Step 1

- ID: TASK-023
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-01 pilot 2: ketidakcocokan strategi (villa 5 kamar vs target pasangan) tidak dicek sistem.
- Acceptance Criteria: WORKFLOW Step 1 punya tabel sanity check (kapasitas, harga, objective, positioning, nama brand, consent); template brief §9b; versi WORKFLOW naik; validator lulus.
- Related: [WORKFLOW](../WORKFLOW.md), [content-brief](../templates/content-brief.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/23>
- Completed: 2026-10-04
- Commit: 8a6c1f9

## TASK-024: check_caption tool + pengetatan self-check skill drafting

- ID: TASK-024
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-04, G-06, G-07 pilot 2: hook >125 lolos, klaim tersirat hanya ditandai, alt text 1 per post.
- Acceptance Criteria: `scripts/check_caption.py` (hook, panjang, hashtag, emoji, kata terlarang); exit criteria skill: klaim tersirat non-DATA FINAL = Fail; alt text per slide; validator lulus.
- Related: [check_caption.py](../scripts/check_caption.py), [draft-caption](../skills/draft-caption/SKILL.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/24>
- Completed: 2026-10-04
- Commit: 80098d3

## TASK-025: Schema v1.3: jam publish & CTA per channel

- ID: TASK-025
- Status: Done
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-08 pilot 2: schema tidak punya jam publish dan target CTA.
- Acceptance Criteria: Schema v1.3 punya `deadlines.publish_time` dan `channels[].cta` (target wajib untuk link/nomor); brief contoh valid; template & publication checklist selaras; validator lulus.
- Related: [schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/25>
- Completed: 2026-10-04
- Commit: 34ce0c4, 43ef8c2

## TASK-026: Aturan review independen & self-review agent

- ID: TASK-026
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-10 pilot 2: QA dijalankan oleh pembuat output yang sama.
- Acceptance Criteria: Rule 08 mewajibkan claim review independen untuk L2/L3; record QA punya kolom Independen?; AGENTS.md mengatur QA agent = self-review; validator lulus.
- Related: [rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md), [AGENTS.md](../AGENTS.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/26>
- Completed: 2026-10-04
- Commit: 2110c66

## TASK-027: Re-run pilot 2 setelah perbaikan

- ID: TASK-027
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Membuktikan perbaikan TASK-020–026 dengan menjalankan ulang pilot 2.
- Acceptance Criteria: `examples/pilot-2/v2.md` dengan sanity check, drafts v2, check_caption PASS, QA v2, approval SIMULASI; REPORT diperbarui dengan status temuan & skor v2.
- Related: [v2](../examples/pilot-2/v2.md), [REPORT](../examples/pilot-2/REPORT.md), issue <https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/27>
- Completed: 2026-10-04
- Commit: 1c377b9

## TASK-029: Split repo jadi clau-ai-core, clau-ai-marketing, clau-ai-agents

- ID: TASK-029
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Memisahkan fondasi, Pilar 1, dan platform ke tiga repo private; repo ini jadi arsip.
- Acceptance Criteria: Tiga repo ter-push dan CI hijau; core sebagai submodule di marketing & agents; `scripts/split_repo.py` reproducible; README arsip menunjuk ke repo baru.
- Related: [split_repo.py](../scripts/split_repo.py), <https://github.com/d34faiza-commits/clau-ai-core>, <https://github.com/d34faiza-commits/clau-ai-marketing>, <https://github.com/d34faiza-commits/clau-ai-agents>
- Completed: 2026-10-04
- Commit: c46c0b9, 4d1ae12 (arsip); core c23ec00, marketing f347e0a, agents e66a17a

## TASK-030: Rekomendasi review adversarial 2–6: proses QA

- ID: TASK-030
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Ekstraksi klaim per kalimat, re-check penuh per versi, cek field brief di QA, CTA check di check_caption.py, rubrik skor.
- Acceptance Criteria: check_caption menangkap R-01 (2 CTA) dan R-06 (CTA beda dari brief) pada draft lama; QA docs dan rubrik ada; CI hijau.
- Related: [scoring-rubric](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/qa/scoring-rubric.md), [claim-verification](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/qa/claim-verification.md), [check_caption.py](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/scripts/check_caption.py)
- Completed: 2026-10-04
- Commit: clau-ai-marketing f4bcdfd

## TASK-031: Pilot 2 v3 dengan proses QA baru (rekomendasi 7)

- ID: TASK-031
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Perbaiki R-01–R-08, jalankan QA baru penuh, skor dengan rubrik.
- Acceptance Criteria: v3.md berisi tabel ekstraksi kalimat semua konten, kecocokan brief, output check_caption aktual, self-score berbasis rubrik; temuan baru dicatat.
- Related: [v3](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/examples/pilot-2/v3.md), [v3 brief](https://github.com/d34faiza-commits/clau-ai-marketing/blob/main/examples/pilot-2/v3/brief.json)
- Completed: 2026-10-04
- Commit: clau-ai-marketing e7e06e7

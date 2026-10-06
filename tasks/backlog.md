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

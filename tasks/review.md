# Review

Output/draft sudah ada di repo, menunggu review owner dan verifikasi sumber sebelum dipindah ke [Done](./done.md).

## TASK-046: Tahap 1 PR 3 — workflow request → draft → QA → approval di API

- ID: TASK-046
- Status: Review
- Priority: High
- Assignee: AI (Claude Code), review owner
- Created: 2026-10-13
- Due: —
- Description: Endpoint requests/drafts/qa-records/approvals sesuai kontrak core; aturan Rule 08 dicek di server (kode di `api-contracts.md` § Kode Aturan Approval, termasuk `facts_unconfirmed` lewat `claims.fact_key` + `drafts.fact_sheet_id`); isolasi data per klien di setiap query. Tidak butuh VPS 2.
- Acceptance Criteria: Kontrak core di-merge dulu; test ke PostgreSQL sungguhan untuk setiap kode aturan; tidak ada endpoint publish; CI hijau.
- Related: <https://github.com/d34faiza-commits/clau-ai-core/blob/main/shared/api-contracts.md>, TASK-032
- Note 2026-10-14: PR [core#14](https://github.com/d34faiza-commits/clau-ai-core/pull/14) (kontrak 0.7.0) dan [agents#46](https://github.com/d34faiza-commits/clau-ai-agents/pull/46) (backend 0.7.0). 242 test lulus, mutation test 28/28, E2E Docker lulus; 14 temuan audit adversarial diperbaiki. Pindah ke Done setelah kedua PR merge dengan CI hijau.

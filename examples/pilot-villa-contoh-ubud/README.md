# Pilot TASK-012 — Villa Contoh Ubud (FIKTIF)

> **Properti fiktif.** Semua nama, harga, aset, dan approver di folder ini dibuat untuk menguji workflow. Tidak ada data client nyata ([CONTENT-BOUNDARY.md](../../CONTENT-BOUNDARY.md)).

## Tujuan

Menjalankan [WORKFLOW.md](../../WORKFLOW.md) end-to-end dengan brief fiktif untuk menemukan celah di rules, skills, schema, dan QA sebelum dipakai untuk client nyata.

## Isi

| File | Langkah WORKFLOW |
|---|---|
| [brief.json](./brief.json) | 1. Brief — valid terhadap [content-brief.schema.json](../../schemas/content-brief.schema.json) (dicek validator) |
| [drafts.md](./drafts.md) | 2. Classify, 3. Draft — skill `draft-caption` (3 varian IG) + `write-ota-listing` (Booking.com EN) |
| [fact-sheet.md](./fact-sheet.md) | Input fakta properti (ditambahkan saat TASK-016) |
| [qa-and-approval.md](./qa-and-approval.md) | 4–8. Claim check, content review, visual (N/A), privacy, approval **SIMULASI**, publication pre-check |

## Hasil Ringkas

| Langkah | Hasil |
|---|---|
| 1 Brief | ✅ Valid schema |
| 2 Classify | ✅ 9 klaim berlabel; 3 klaim non-DATA FINAL ditahan dari konten |
| 3 Draft | ✅ 3 caption + listing OTA |
| 4 Claim check | ⚠️ Conditional — QA gate menangkap klaim tersirat di Varian C yang lolos self-check skill |
| 5 Content review | ⚠️ Conditional — Voice Card tidak tersedia di brief |
| 6 Privacy & rights | ✅ Pass |
| 7 Approval | SIMULASI — Varian A siap diajukan; listing OTA tertahan placeholder |
| 8–9 Publish/monitor | Tidak dijalankan |

**Kesimpulan:** alur 9 langkah bisa dijalankan dan QA gate bekerja, karena berhasil menangkap klaim yang lolos dari self-check skill. Celah utamanya ada di **input**, bukan di gate: brief belum membawa Voice Card dan fact sheet properti yang lengkap.

## Temuan

| ID | Temuan | Dampak | Tindak lanjut |
|---|---|---|---|
| F-01 | Schema/template brief tidak punya field Voice Card | Brand voice tidak bisa diverifikasi dari brief; skill jatuh ke default | TASK-015 — **selesai**: schema v1.1 punya field `voice`; brief pilot diperbarui |
| F-02 | Tidak ada template/schema **fact sheet properti** (bed type, ukuran kamar, kebijakan, check-in) | Listing OTA tertahan `<KONFIRMASI>` | TASK-016 — **selesai**: [template fact sheet](../../templates/property-fact-sheet.md); listing pilot di-run ulang tanpa placeholder ([fact-sheet.md](./fact-sheet.md), drafts Step 3c) |
| F-03 | Belum ada lokasi resmi untuk contoh fiktif/pilot | Contoh bisa tercecer atau tercampur dengan data client | **Selesai di pilot ini** — folder `examples/` |
| F-04 | Validator tidak memvalidasi contoh brief terhadap schema | Contoh bisa tidak valid tanpa ketahuan | **Selesai di pilot ini** — validator cek `examples/**/brief.json` |
| F-05 | WORKFLOW & approval record tidak punya mode simulasi/pilot | Risiko record simulasi terbaca sebagai approval nyata | TASK-017 — **selesai**: WORKFLOW §Mode SIMULASI + field `Mode` di approval record |
| F-06 | Self-check skill `draft-caption` tidak memeriksa **klaim tersirat** (mis. "view X dan Y terlihat") | Klaim lolos sampai claim gate | TASK-018 — **selesai**: self-check klaim tersirat di `draft-caption`, `write-ota-listing`, `plan-seasonal-campaign` |
| F-07 | Schema tidak mewajibkan `source_date` untuk klaim **DATA FINAL**, padahal rule 01 meminta versi/tanggal sumber | Traceability lemah | TASK-019 — **selesai**: schema v1.2 mewajibkan `source` + `source_date` untuk klaim DATA FINAL |
| F-08 | Spec platform (batas caption, dll.) masih **ASSUMPTION** | Cek panjang konten belum bisa jadi gate | TASK-011 (blocked: akses help center) |

## Tanggal

Dijalankan 2026-10-04 oleh AI agent (Claude Code) sebagai pilot. Review owner tetap diperlukan untuk menerima temuan.

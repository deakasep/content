# Approval Record

> Satu record per konten (atau per batch L1). Simpan di workspace client. Rule: [08 Approval & Publication](../rules/08-APPROVAL-PUBLICATION-STANDARD.md).

## Identitas Konten

| Field | Isi |
|---|---|
| Record ID | `<CLIENTCODE>-APR-<YYYYMMDD>-<NN>` |
| Brief ID | |
| Channel & format | |
| Versi konten | v1 / v2 / ... |
| Jadwal publish | (tanggal, jam, zona waktu WIB/WITA/WIT) |
| Level approval | L1 / L2 / L3 |

## Paket yang Direview

| Item | Lokasi file / link (workspace client) |
|---|---|
| Teks final | |
| Visual final | |
| Tabel klaim | |
| Hasil QA (content, claim, visual, privacy) | |

## Hasil QA

| Gate | Hasil | Reviewer | Tanggal |
|---|---|---|---|
| [Content review](../qa/content-review.md) | Pass / Conditional / Fail | | |
| [Claim verification](../qa/claim-verification.md) | | | |
| [Visual AI review](../qa/visual-ai-review.md) | / N/A | | |
| [Privacy & rights](../qa/privacy-rights-review.md) | | | |

## Keputusan Approver

| Field | Isi |
|---|---|
| Keputusan | Approved / Approved with changes / Rejected |
| Nama & peran approver | |
| Tanggal & jam | |
| Kanal approval (email/tool/chat yang diarsipkan) | |
| Catatan / perubahan yang diminta | |

## Perubahan Setelah Approval

| Tanggal | Perubahan | Perlu approval ulang? | Approver ulang |
|---|---|---|---|
| | | Ya / Tidak | |

## Publikasi

| Field | Isi |
|---|---|
| Dipublish oleh | |
| Waktu publish aktual | |
| URL | |
| Versi yang dipublish | |

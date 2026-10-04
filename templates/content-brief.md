# Content Brief

> Salin template ini ke workspace client (bukan ke repo). Versi machine-readable: [schemas/content-brief.schema.json](../schemas/content-brief.schema.json).

## 1. Identitas

| Field | Isi |
|---|---|
| Brief ID | `<CLIENTCODE>-<YYYYMM>-<NN>` |
| Client (kode internal) | |
| Vertical | accommodation / food-beverage / spa-wellness / experience |
| Lokasi umum | (kabupaten/kota) |
| Requester | |
| Approver (level L1/L2/L3) | |
| Tanggal brief | |
| Deadline draft | |
| Tanggal publish target | |
| Jam publish + zona waktu | HH:MM WIB / WITA / WIT (wajib sebelum publication checklist) |

## 2. Objective

| Field | Isi |
|---|---|
| Objective | awareness / engagement / direct booking / reservation / walk-in / review |
| Ukuran keberhasilan | (metrik + sumber data) |
| Pesan utama (1 kalimat) | |

## 3. Audience

| Field | Isi |
|---|---|
| Segmen utama | |
| Asal (domestik/negara) | |
| Bahasa konten | ID / EN / bilingual |

## 3b. Voice (ringkasan Voice Card — [rule 03](../rules/03-CLIENT-BRAND-VOICE-STANDARD.md))

| Field | Isi | Field schema |
|---|---|---|
| Status Voice Card | **DATA FINAL** (disetujui client) / **CLIENT CONFIRMATION** (pakai default sementara) | `voice.evidence_label` |
| Referensi Voice Card (workspace client) | | `voice.voice_card_ref` |
| Arketipe | tenang-membumi / hangat-kekeluargaan / elegan-tertata / santai-playful / informatif-praktis ([voice guide](../knowledge/voice-guides/hospitality-voice.md)) | `voice.archetype` |
| 3 kata sifat brand | | `voice.adjectives` |
| 3 "kami bukan…" | | `voice.not_like` |
| Sapaan | kamu / Anda / Kak / you | `voice.address` |
| Aturan emoji | | `voice.emoji_rule` |

Bila status **DATA FINAL**, semua field wajib diisi. Kata wajib/terlarang diisi di bagian 9.

## 4. Channel & Format

| Channel | Format | Jumlah | CTA (1 per konten) + target | Catatan |
|---|---|---|---|---|
| Instagram | feed / carousel / Reels / Stories | | | |
| TikTok | video | | | |
| Google Business Profile | update / offer / event | | | |
| OTA | listing update | | | |
| WhatsApp | broadcast (opt-in saja) | | | |

CTA: save / comment / share / link-in-bio / link-sticker / whatsapp / dm / book-button / call. Untuk CTA berupa link atau nomor, target diisi referensi ke URL/nomor resmi di workspace client (`channels[].cta.target_ref`).

## 5. Offer (bila ada)

| Field | Isi | Label |
|---|---|---|
| Nama paket/promo | | |
| Harga + mata uang + unit | | |
| Net / ++ | | |
| Periode berlaku | | |
| Syarat utama | | |
| Kapasitas | | |

## 6. Fakta & Klaim yang Akan Dipakai

Klaim **DATA FINAL** wajib punya sumber **dan** tanggal sumber (`claims[].source` + `claims[].source_date` di schema).

| Klaim | Label | Sumber (dokumen/versi/tanggal) | Catatan |
|---|---|---|---|
| | **DATA FINAL** | | |
| | **CLIENT CONFIRMATION** | | |
| | **FIELD VERIFICATION** | | |

## 7. Asset

| Asset | Sumber (media library client) | Kategori visual (A/B/C/D) | Consent orang di dalamnya? |
|---|---|---|---|
| | | | Ya / Tidak / Tidak ada orang |

## 8. Klasifikasi Data (4 axis)

| Axis | Nilai |
|---|---|
| Sensitivity | Public / Internal / Confidential |
| Lifecycle | Draft / For Review / Approved |
| Scope | Client Specific / Campaign Specific |
| Evidence | (lihat tabel klaim) |

## 9. Batasan & Do/Don't

- Kata/klaim wajib:
- Kata/klaim terlarang:
- Topik sensitif yang dihindari:

## 9b. Brief Sanity Check ([WORKFLOW Step 1](../WORKFLOW.md#step-1--brief))

| Cek | Hasil (OK / RISK) | Catatan |
|---|---|---|
| Kapasitas ↔ segmen | | |
| Harga ↔ segmen | | |
| Objective ↔ channel & format | | |
| Positioning ↔ bukti | | |
| Nama brand ↔ fakta | | |
| Aset ↔ consent | | |

Setiap RISK → isi di bagian 10.

## 10. Risk & Next Action

| Item | Label | Owner | Target |
|---|---|---|---|
| | **RISK** | | |
| | **NEXT ACTION** | | |

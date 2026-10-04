# Pilot QA & Approval — Villa Contoh Ubud (FIKTIF)

> **Contoh fiktif untuk pilot TASK-012.** Approval di bawah adalah **SIMULASI** — tidak ada approver nyata. Draft: [drafts.md](./drafts.md).

## Step 4 — [Claim Verification](../../qa/claim-verification.md)

| # | Klaim (di konten) | Kategori | Label | Sumber | Hasil |
|---|---|---|---|---|---|
| 1 | 2 kamar tidur, maks 4 dewasa | facility | **DATA FINAL** | Fact sheet fiktif v1 | OK |
| 2 | Kolam privat 3 × 6 m | facility | **DATA FINAL** | Fact sheet + foto A | OK |
| 3 | Teras timur menghadap sawah | location | **DATA FINAL** | Foto A bertanggal | OK |
| 4 | Sarapan Indonesia diantar ke teras (2 orang) | F&B | **DATA FINAL** | Fact sheet + offer terms | OK |
| 5 | Parkir di ujung gang, jalan kaki ±80 m | location | **DATA FINAL** | Fact sheet | OK |
| 6 | Rp1.500.000/villa/malam, min 3 malam, 1 Nov–15 Des 2026, ++, tidak bisa digabung | price | **DATA FINAL** | Brief `offer` | OK — net/++ ditulis; persentase pajak tidak disebut (**CLIENT CONFIRMATION**) |
| 7 | "view sawah atau view kolam … dua-duanya kelihatan" (Varian C) | location | **FIELD VERIFICATION** | Foto belum menunjukkan sawah & kolam dalam satu pandangan | **Ubah** — Varian C perlu foto bukti atau kalimat dihapus |
| 8 | Jarak ke pusat Ubud | location | **FIELD VERIFICATION** | — | Tidak dipakai di konten ✔ |
| 9 | Wi-Fi cepat | facility | **ASSUMPTION** | — | Tidak dipakai di konten ✔ |

Superlatif / klise / halal / bintang / medis: **tidak ada** (dicek otomatis terhadap `restrictions.forbidden_terms` dan daftar klise).

**Hasil:** **Conditional** — Varian A & B lolos; Varian C butuh bukti klaim #7.

## Step 5 — [Content Review](../../qa/content-review.md)

| Area | Hasil | Catatan |
|---|---|---|
| Objective & struktur | Pass | 1 CTA (WhatsApp via link bio), hook ≤125 karakter di semua varian |
| Brand voice | Conditional | Voice Card client tidak ada di brief → pakai default "Tenang & Membumi" (temuan F-01) |
| Bahasa & budaya | Pass | Bilingual paritas klaim A cocok (harga, periode, ++, sarapan); topik subak/upacara tidak disentuh |
| Platform | Conditional | Panjang caption ≤745 karakter; batas IG 2.200 masih **ASSUMPTION** (TASK-011) |
| Kelengkapan | Pass | Tabel klaim & open items ada |

## Step 5b — [Visual & AI Review](../../qa/visual-ai-review.md)

**N/A untuk pilot** — aset VCU-MEDIA-001…003 fiktif (kategori A/B, tanpa orang). Pada client nyata gate ini wajib dijalankan pada file asli.

## Step 6 — [Privacy & Rights Review](../../qa/privacy-rights-review.md)

| Item | Hasil |
|---|---|
| Orang yang dapat dikenali | Tidak ada (brief: `people: none`) |
| Data pribadi tamu | Tidak ada |
| UGC / repost | Tidak ada |
| Lisensi aset | Fiktif — milik client (asumsi pilot) |
| Konten berbayar | Tidak (`paid: false`) → disclosure tidak diperlukan |

**Hasil:** Pass.

## Step 7 — Approval Record (SIMULASI)

| Field | Isi |
|---|---|
| Mode | **SIMULASI** |
| Record ID | `VCU-APR-20261004-01` |
| Brief ID | `VCU-202610-01` |
| Channel & format | Instagram carousel (Varian A) + Booking.com description (EN) |
| Versi konten | v1 |
| Jadwal publish | 2026-10-20, WITA |
| Level approval | L2 (ada promo & harga) |
| Keputusan | **SIMULASI — tidak ada approval nyata** |
| Catatan | Varian A siap diajukan. Varian C ditahan (klaim #7). OTA listing **belum bisa** diajukan: 3 placeholder `<KONFIRMASI>` (temuan F-02) |

## Step 8 — [Publication Checklist](../../qa/publication-checklist.md)

**Tidak dijalankan** — pilot berhenti sebelum publish (tidak ada akun, approver, atau tanggal nyata). Pre-check yang bisa dicek: Varian A tidak mengandung placeholder; OTA listing masih mengandung `<KONFIRMASI>` → akan gagal item "Teks final tanpa placeholder".

## Step 9 — Monitor & Report

**Tidak dijalankan** (tidak ada publikasi).

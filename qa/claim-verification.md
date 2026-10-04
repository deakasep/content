# QA — Claim Verification

## Purpose

Gate wajib untuk memastikan setiap klaim di konten (teks, visual, voice-over, on-screen text) terbukti dan berstatus **DATA FINAL** sebelum approval.

## Required Inputs

- Draft final (semua varian & bahasa).
- Tabel klaim dari creator.
- Dokumen sumber client (fact sheet, menu, rate card, sertifikat).

## Langkah

1. Ekstrak **semua** klaim dari teks, visual, dan on-screen text — termasuk klaim implisit (foto kolam = klaim "ada kolam").
2. Cocokkan dengan tabel klaim; tambahkan klaim yang terlewat.
3. Verifikasi setiap klaim ke sumber; catat versi/tanggal sumber.
4. Klaim tanpa sumber → hapus/ubah, atau tandai **CLIENT CONFIRMATION** / **FIELD VERIFICATION** dan blok publish.

## Tabel Verifikasi

| # | Klaim (persis seperti di konten) | Kategori | Label | Sumber + versi/tanggal | Verifier | Hasil |
|---|---|---|---|---|---|---|
| 1 | | fasilitas / lokasi / harga / rating / sertifikasi / F&B / treatment / experience | | | | OK / Ubah / Hapus |

## Checklist per Kategori ([rule 02](../rules/02-HOSPITALITY-CLAIM-STANDARD.md))

### Umum

- [ ] Tidak ada superlatif tanpa bukti ("terbaik", "nomor 1", "best", "termurah").
- [ ] Tidak ada testimoni/review karangan.
- [ ] Klaim musiman/bersyarat menyebut kondisinya.
- [ ] Tidak ada penyebutan kompetitor.

### Rating, sertifikasi, award

- [ ] Bintang = sertifikat klasifikasi berlaku (bukan rating OTA).
- [ ] Rating platform menyebut platform + tanggal.
- [ ] Sertifikasi/award: nama, penyelenggara, tahun benar, masih berlaku.

### Halal & dietary

- [ ] "Halal" hanya dengan sertifikat berlaku untuk outlet/produk.
- [ ] Vegan/gluten-free/allergen dikonfirmasi per menu.

### Harga & promo

- [ ] Mata uang, unit, periode, syarat lengkap.
- [ ] Net/++ jelas.
- [ ] Harga acuan diskon benar-benar pernah berlaku.
- [ ] Tidak ada fake scarcity/countdown.
- [ ] Konsisten dengan harga di OTA/website.

### Lokasi & fasilitas

- [ ] Jarak menyebut moda + estimasi; verifikasi lapangan bila meragukan.
- [ ] Beachfront / ocean view / private pool / private beach sesuai fakta.
- [ ] Fasilitas berbayar disebut berbayar; jam operasional benar.

### Spa & wellness

- [ ] Tidak ada klaim medis (menyembuhkan, detoks racun, melangsingkan, dll.).
- [ ] Kualifikasi terapis hanya bila terbukti.

### Experience

- [ ] Satwa/alam tidak dijamin.
- [ ] Aktivitas berisiko menyebut syarat & keselamatan.

## Blockers (otomatis Fail)

- Klaim non-**DATA FINAL** di konten publish.
- Klaim halal/bintang/sertifikasi tanpa bukti.
- Klaim medis spa.
- Harga tanpa periode/syarat/net-++.

## Record

| Verifier | Independen? (Ya / Tidak — self-review) | Tanggal | Versi konten | Hasil | Catatan |
|---|---|---|---|---|---|
| | | | | | |

Konten L2/L3 butuh minimal satu verifikasi **independen** ([rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md)). Self-review AI/creator hanya pre-check.

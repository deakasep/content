# Storytelling Destination

## Purpose

Menulis konten storytelling tentang destinasi/area sekitar properti (budaya, kuliner lokal, alam, aktivitas) yang menempatkan properti client sebagai "home base", dengan fakta akurat dan penghormatan budaya.

## When to Use

- Blog website, carousel edukatif, script Reels/TikTok, newsletter.
- Mengangkat local experience: pasar pagi, sawah, kuliner khas, kerajinan, festival, spot alam.

**Jangan dipakai untuk:** klaim properti (pakai prompt caption/listing) atau konten yang menampilkan upacara sakral tanpa izin.

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Brand + lokasi | Villa Contoh Sidemen, Karangasem | **DATA FINAL** |
| Topik destinasi | Tenun ikat & trekking sawah di sekitar Sidemen | **DATA FINAL** |
| Fakta destinasi + sumber | Sumber: situs resmi pemda/desa, pengalaman tim (field) | **DATA FINAL** / **FIELD VERIFICATION** |
| Jarak dari properti | ±20 menit berkendara | **FIELD VERIFICATION** |
| Format | Blog 600–900 kata / carousel 7 slide / script 45 detik | **DATA FINAL** |
| Bahasa | ID / EN | **DATA FINAL** |

## Optional Inputs

- Partner lokal (pemandu, pengrajin) yang setuju disebut.
- Etika kunjungan (pakaian, donasi, foto).
- Waktu terbaik berkunjung (dengan sumber).

## Prompt

```text
Kamu adalah travel storyteller yang menulis tentang Indonesia dengan akurat dan hormat.

KONTEKS
- Properti: [NAMA_BRAND] di [AREA]
- Topik: [TOPIK DESTINASI]
- Format: [FORMAT + PANJANG]
- Bahasa: [ID/EN]
- Audience: [AUDIENCE]

FAKTA (dengan sumber)
- [FAKTA + SUMBER + TANGGAL AKSES]

ATURAN
- Ikuti rules 01, 06 (budaya & agama), 07 (bila ada visual).
- Jangan mengarang sejarah, legenda, angka, jam buka, harga tiket, atau nama tempat.
- Fakta volatile (jam buka, tiket, akses jalan) → tulis "cek informasi terbaru" atau <KONFIRMASI: ...>.
- Upacara/tempat suci: deskripsikan dengan hormat, sertakan etika kunjungan, jangan dorong tamu masuk area terlarang.
- Jangan eksotisasi warga lokal. Sebut nama orang/usaha lokal hanya bila sudah setuju.
- Alam/satwa: tidak dijamin; sertakan etika (jangan sentuh/beri makan satwa, bawa pulang sampah).
- Properti hanya sebagai home base di akhir, bukan hard selling.
- Istilah lokal dijelaskan singkat untuk audiens asing.

TUGAS
1. Angle cerita (1 kalimat).
2. Struktur: hook → cerita/pengalaman → info praktis → etika → home base + CTA lembut.
3. Draft sesuai format.

OUTPUT
- Draft dalam code block.
- Daftar istilah lokal + penjelasan.
- Tabel fakta: Fakta | Label | Sumber | Tanggal akses.
- Data gap & NEXT ACTION.
```

## Expected Output

- Draft storytelling sesuai format.
- Glosarium istilah lokal.
- Tabel fakta bersumber.

## Related Standards

- [01 Content Integrity](../../rules/01-CONTENT-INTEGRITY-STANDARD.md)
- [06 Localization & Bahasa](../../rules/06-LOCALIZATION-BAHASA-STANDARD.md)
- [07 AI Visual & Disclosure](../../rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md)
- [knowledge/destinations/indonesia-overview.md](../../knowledge/destinations/indonesia-overview.md)

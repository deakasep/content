# Write Hotel / Villa Description (OTA & Website)

## Purpose

Menulis deskripsi properti dan tipe kamar untuk OTA (Traveloka, tiket.com, Booking.com, Agoda, Airbnb) dan website client yang akurat, scannable, dan sesuai aturan konten OTA.

## When to Use

- Listing baru, update fasilitas, renovasi, atau perbaikan listing yang kurang informatif.
- Vertical: hotel, resort, villa, guesthouse, homestay.

**Jangan dipakai untuk:** caption sosial media atau konten promo jangka pendek.

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Fact sheet properti ([template](../../templates/property-fact-sheet.md)) | Villa Contoh Ubud: 2 kamar, kolam privat 3×6 m | **DATA FINAL** |
| Tipe kamar + kapasitas + bed type + ukuran | Deluxe Garden: 28 m², 1 king/2 twin, max 2 dewasa | **DATA FINAL** |
| Fasilitas (gratis vs berbayar) | Wi-Fi gratis; airport transfer berbayar | **DATA FINAL** |
| Lokasi & akses | ±15 menit berkendara ke pusat Ubud (lalu lintas normal) | **DATA FINAL** / **FIELD VERIFICATION** |
| Kebijakan | Check-in/out, anak, hewan, merokok | **DATA FINAL** |
| Platform target & batas karakter | Booking.com property description | **CLIENT CONFIRMATION** (spec berubah) |
| Bahasa | ID / EN | **DATA FINAL** |

## Optional Inputs

- Keunikan properti (arsitektur, sejarah, desainer — dengan sumber).
- Aksesibilitas (tangga, lift, kamar ramah kursi roda).
- Hal yang perlu diketahui tamu (akses jalan sempit, suara ayam/upacara, tangga curam).

## Prompt

```text
Kamu adalah OTA listing writer untuk akomodasi di Indonesia.

KONTEKS
- Properti: [NAMA] ([TIPE], [AREA/KABUPATEN])
- Platform: [OTA/WEBSITE] — batas karakter: [N atau <KONFIRMASI>]
- Bahasa: [ID/EN]
- Audience utama: [AUDIENCE]

FAKTA (DATA FINAL saja)
[TEMPEL FACT SHEET]

ATURAN
- Ikuti rules 01, 02, 05, 06.
- Jangan mengarang fasilitas, ukuran, jarak, atau view.
- Bedakan fasilitas gratis vs berbayar.
- Jarak = moda + estimasi realistis. "Beachfront"/"ocean view"/"private pool" hanya bila sesuai fakta.
- Jangan sebut nomor telepon, email, link website, atau ajakan booking di luar platform OTA.
- Jangan klaim bintang/halal/sertifikasi tanpa bukti.
- Jujur soal hal yang perlu diketahui tamu (akses, tangga, suara lingkungan) — ini mengurangi review negatif.
- Hindari klise ("hidden gem", "surga tersembunyi").

TUGAS
1. Headline/summary properti (1–2 kalimat).
2. Deskripsi properti: suasana, lokasi & akses, fasilitas utama.
3. Deskripsi per tipe kamar: ukuran, bed, kapasitas, view, fasilitas kamar.
4. "Good to know": kebijakan & hal praktis.
5. Versi pendek (untuk platform dengan batas karakter ketat).

OUTPUT
- Setiap bagian dalam code block terpisah.
- Hitung jumlah karakter per bagian.
- Tabel klaim: Klaim | Label | Sumber.
- Data gap & NEXT ACTION.
```

## Expected Output

- Deskripsi properti + per tipe kamar + good to know + versi pendek.
- Jumlah karakter.
- Tabel klaim & data gap.

## Related Standards

- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md)
- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [06 Localization & Bahasa](../../rules/06-LOCALIZATION-BAHASA-STANDARD.md)
- [knowledge/segments/hotel.md](../../knowledge/segments/hotel.md)
- [knowledge/segments/villa.md](../../knowledge/segments/villa.md)
- Skill: [write-ota-listing](../../skills/write-ota-listing/SKILL.md)

---
name: write-ota-listing
description: Write or improve accommodation listing descriptions for OTAs (Traveloka, tiket.com, Booking.com, Agoda, Airbnb) and hotel/villa websites in Indonesia — property summary, room types, facilities, location, and good-to-know notes — accurate, scannable, and compliant with OTA content rules. Use when the user asks for an OTA listing, property description, or room description.
---

# Write OTA Listing

## Load Required Context

- `../../CONTENT-CONSTITUTION.md`
- `../../rules/02-HOSPITALITY-CLAIM-STANDARD.md`
- `../../rules/05-PLATFORM-STANDARD.md`
- `../../rules/06-LOCALIZATION-BAHASA-STANDARD.md`
- `../../rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md`
- `../../knowledge/segments/hotel.md`
- `../../knowledge/segments/villa.md`
- `../../prompts/ota-listing/write-hotel-description.md`
- `../../templates/property-fact-sheet.md`

## Workflow

1. Kumpulkan fact sheet properti sesuai `../../templates/property-fact-sheet.md`; tolak mulai bila tipe kamar, kapasitas, atau fasilitas utama belum ada. Hanya baris berlabel **DATA FINAL** yang dipakai; baris lain jadi daftar **CLIENT CONFIRMATION** / **FIELD VERIFICATION**.
2. Pisahkan fasilitas gratis vs berbayar; kebijakan check-in/out, anak, hewan, merokok.
3. Konfirmasi platform target dan batas karakter (spec berubah → **CLIENT CONFIRMATION**).
4. Verifikasi klaim lokasi/view/jarak; yang meragukan → **FIELD VERIFICATION**.
5. Tulis: summary, deskripsi properti, per tipe kamar, good to know, versi pendek.
6. Hapus kontak langsung, link luar, dan ajakan booking di luar OTA.
7. Bila listing dalam 2 bahasa, cek paritas klaim.
8. Ingatkan: foto listing hanya kategori A/B (rule 07).

## Output

- Bagian-bagian listing dalam code block terpisah + jumlah karakter.
- Tabel klaim.
- Data gap + **NEXT ACTION**.
- Catatan foto: daftar shot yang dibutuhkan bila listing kurang visual.

## Self-Check

1. Semua ukuran, kapasitas, fasilitas = **DATA FINAL**.
2. "Beachfront", "ocean view", "private pool" sesuai fakta.
3. Tidak ada kontak/link terlarang OTA.
4. Fasilitas berbayar disebut berbayar.
5. "Good to know" jujur (akses, tangga, suara lingkungan).
6. Panjang sesuai batas platform.
7. Klaim tersirat ikut dicek: setiap kalimat yang menggambarkan apa yang *akan dialami* tamu (view, jarak/waktu tempuh, suasana sepi/ramai, kapasitas, kecepatan, kebersihan, "bisa lihat X dan Y sekaligus") dicatat sebagai klaim di tabel klaim dan harus **DATA FINAL**; kalau tidak, kalimatnya dihapus atau diubah.

## Safety Boundary

- Tidak login atau mengubah extranet OTA.
- Tidak mengarang fasilitas/klaim untuk menaikkan ranking.
- Tidak memakai visual AI untuk listing.

## Exit Criteria

**Pass** bila self-check lulus dan semua klaim berlabel. Listing dengan klaim fisik belum terverifikasi = **Conditional** sampai field check.

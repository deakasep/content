---
name: draft-caption
description: Draft on-brand social media captions (Instagram feed/carousel/Reels, TikTok, Facebook) for Indonesian hospitality businesses — villas, hotels, restaurants, cafes, beach clubs, spas — with verified claims, one clear CTA, and a claim table. Use when the user asks for a caption, post copy, or Reels/TikTok text for a hospitality client.
---

# Draft Caption

## Load Required Context

Baca sebelum bekerja:

- `../../CONTENT-CONSTITUTION.md`
- `../../rules/01-CONTENT-INTEGRITY-STANDARD.md`
- `../../rules/02-HOSPITALITY-CLAIM-STANDARD.md`
- `../../rules/03-CLIENT-BRAND-VOICE-STANDARD.md`
- `../../rules/05-PLATFORM-STANDARD.md`
- `../../knowledge/voice-guides/hospitality-voice.md`
- `../../knowledge/platforms/instagram.md` atau `../../knowledge/platforms/tiktok.md` sesuai channel
- `../../prompts/caption/draft-instagram-caption.md`

## Workflow

1. Pastikan input minimum: brand, vertical, lokasi umum, Voice Card, topik/visual, objective, CTA, bahasa. Voice Card diambil dari field `voice` di brief (arketipe, kata sifat, "bukan", sapaan, emoji) plus `restrictions` (kata wajib/terlarang). Bila `voice.evidence_label` = **CLIENT CONFIRMATION**, pakai arketipe di brief dan catat di output bahwa voice belum disetujui client. Input lain yang kurang → tanya, atau tandai **CLIENT CONFIRMATION**.
2. Daftar fakta yang boleh dipakai; hanya **DATA FINAL**.
3. Cek segment knowledge vertical (`../../knowledge/segments/`) untuk angle konten yang relevan.
4. Tulis hook sensory dan spesifik di baris pertama.
5. Buat 3 varian (storytelling, informatif, conversational) sesuai Voice Card.
6. Tambahkan 1 CTA dan 3–8 hashtag relevan.
7. Tulis alt text.
8. Isi tabel klaim, termasuk **klaim tersirat**: baca ulang setiap varian kalimat per kalimat dan catat semua gambaran pengalaman (view, jarak, suasana, kapasitas) sebagai klaim. Lalu jalankan self-check.

## Output

- 3 varian caption, masing-masing dalam code block terpisah.
- Alt text.
- Tabel klaim: Klaim | Label | Sumber.
- Data gap (**CLIENT CONFIRMATION** / **FIELD VERIFICATION**) + **NEXT ACTION**.
- Level approval yang dibutuhkan (L1/L2/L3).

## Self-Check

1. Setiap klaim di caption ada di tabel klaim dengan label **DATA FINAL**.
2. Tidak ada superlatif tanpa bukti, klise AI, klaim halal/bintang/medis tanpa bukti.
3. Harga (bila ada) lengkap: Rp, unit, periode, syarat, net/++.
4. Hanya 1 CTA.
5. Tidak ada nama/foto tamu tanpa consent.
6. Konten berbayar → disclosure tercantum.
7. Klaim tersirat ikut dicek: setiap kalimat yang menggambarkan apa yang *akan dialami* tamu (view, jarak/waktu tempuh, suasana sepi/ramai, kapasitas, kecepatan, kebersihan, "bisa lihat X dan Y sekaligus") dicatat sebagai klaim di tabel klaim dan harus **DATA FINAL**; kalau tidak, kalimatnya dihapus atau diubah. Contoh pilot: "view sawah dan kolam dua-duanya kelihatan" adalah klaim view yang butuh foto bukti.

## Safety Boundary

- Tidak publish, schedule, atau boost.
- Tidak mengarang fasilitas, harga, rating, testimoni.
- Tidak menyebut kompetitor.
- Tidak memproses credential atau data pribadi tamu.

## Exit Criteria

**Pass** bila self-check lulus semua dan open items tercatat. **Fail** bila ada klaim non-**DATA FINAL** di teks caption.

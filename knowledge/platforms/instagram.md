# Platform: Instagram

## Scope

Feed post, carousel, Reels, Stories, Highlights, dan bio untuk akun bisnis hospitality.

> **Spec platform berubah.** Semua nilai teknis di bawah berstatus **ASSUMPTION** sampai diverifikasi ke Instagram Help Center / Meta Business Help Center. Saat memverifikasi, isi kolom "Diverifikasi" dengan tanggal akses dan ubah status menjadi **DATA FINAL**.

## Spec Teknis

| Item | Nilai kerja | Sumber | Status | Diverifikasi |
|---|---|---|---|---|
| Panjang caption maksimum | 2.200 karakter | Instagram Help Center | **ASSUMPTION** | — |
| Hashtag maksimum per post | 30 | Instagram Help Center | **ASSUMPTION** | — |
| Rasio feed portrait | 4:5 (1080×1350 px) | Meta Business Help Center | **ASSUMPTION** | — |
| Rasio Reels / Stories | 9:16 (1080×1920 px) | Meta Business Help Center | **ASSUMPTION** | — |
| Bagian caption terlihat sebelum "more" | ±125 karakter (tergantung perangkat) | Observasi umum | **ASSUMPTION** | — |
| Durasi maksimum Reels | — | Instagram Help Center | **CLIENT CONFIRMATION** | — |

## Praktik Konten Hospitality

| Format | Cocok untuk | Catatan |
|---|---|---|
| Carousel | Room tour, menu, paket, "good to know" | Slide 1 = hook visual + teks singkat |
| Reels | Suasana, proses (masak, treatment), walkthrough | 3 detik pertama menentukan; subtitle untuk tonton tanpa suara |
| Stories | Info harian, availability, Q&A, polling | Info harga/availability wajib akurat hari itu; 3–5 frame, ≤8 kata/frame, ≤1 sticker/frame ([prompt](../../prompts/stories/stories-sequence.md)) |
| Highlights | Rooms, Menu, Spa, Location, FAQ, Reviews | Review update berkala; jangan biarkan promo kedaluwarsa |
| Bio | Positioning 1 kalimat + lokasi + CTA | Link ke booking/WhatsApp resmi |

## Struktur Caption yang Disarankan

1. **Hook** (baris 1): sensory & spesifik.
2. **Body**: 2–4 kalimat atau poin; satu ide utama.
3. **Info praktis** (bila promo): harga, periode, syarat, net/++.
4. **CTA**: satu saja.
5. **Hashtag**: di akhir atau komentar pertama (konsisten per client).

## Hashtag

Gunakan kombinasi:

| Jenis | Contoh fiktif | Catatan |
|---|---|---|
| Brand | #VillaContohUbud | Konsisten di semua post |
| Lokasi | #ubud #bali #sidemen | Lokasi benar, bukan yang "populer" saja |
| Niche | #balivilla #brunchcanggu #balispa | Relevan dengan isi post |
| Campaign | #RamadanDiVillaContoh | Unik per campaign |

Hindari hashtag tidak relevan, hashtag trending tanpa kaitan, dan daftar hashtag identik di setiap post.

## Disclosure & Kolaborasi

- Kolaborasi berbayar/gifting → gunakan label paid partnership (bila tersedia untuk akun) + teks jelas.
- Collab post dengan akun lain → izin tertulis dan approval L3.
- Konten AI → label AI bila tersedia + rule 07.

## Kesalahan Umum

- Link in bio mati atau mengarah ke promo lama.
- Highlight "Promo" berisi harga kedaluwarsa.
- Caption sama persis di IG, TikTok, dan GBP tanpa adaptasi.
- Repost foto tamu tanpa izin.

## References

- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [prompts/caption/draft-instagram-caption.md](../../prompts/caption/draft-instagram-caption.md)
- Instagram Help Center / Meta Business Help Center (sumber verifikasi)

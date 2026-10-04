---
name: draft-reel-script
description: Draft short vertical video scripts (Instagram Reels, TikTok) for Indonesian hospitality businesses — hook, per-second shot list, on-screen text, audio, caption, and per-shot claim and consent status. Use when the user asks for a reel, TikTok, short video script, or shot list for a villa, hotel, restaurant, cafe, beach club, or spa.
---

# Draft Reel Script

## Load Required Context

- `../../CONTENT-CONSTITUTION.md`
- `../../rules/01-CONTENT-INTEGRITY-STANDARD.md`
- `../../rules/02-HOSPITALITY-CLAIM-STANDARD.md`
- `../../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md`
- `../../rules/05-PLATFORM-STANDARD.md`
- `../../rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md`
- `../../knowledge/platforms/content-trends-hospitality-2026.md`
- `../../knowledge/voice-guides/hospitality-voice.md`
- `../../prompts/video/reel-script.md`

## Workflow

1. Baca brief (`voice`, `claims`, `assets`, `restrictions`) dan fact sheet. Fakta yang boleh tampil hanya **DATA FINAL**.
2. Petakan aset: kategori visual (A/B/C/D) dan status orang (`none` / `identifiable-with-consent` / `identifiable-pending-consent`). Aset dengan orang tanpa consent tidak dipakai; siapkan shot pengganti.
3. Tulis 2 opsi hook 0–3 detik: visual spesifik + on-screen text ≤6 kata.
4. Susun shot list per detik. Setiap shot yang menampilkan fakta dicatat sebagai klaim, termasuk klaim visual tersirat (view, ukuran, suasana, waktu seperti sunset).
5. Tentukan audio: library komersial akun bisnis atau musik berlisensi; tanpa voice-over AI yang meniru orang nyata.
6. Tulis caption reel: hook ≤125 karakter, 1 CTA, 3–8 hashtag.
7. Tulis daftar "sengaja tidak ditampilkan" beserta alasannya (klaim belum terbukti, consent, budaya).
8. Jalankan `python scripts/check_caption.py` pada caption bila tersedia, lalu self-check.

## Output

- 2 opsi hook.
- Tabel shot: detik | shot | aset | on-screen text | klaim (label) | orang/consent | catatan teknis.
- Caption reel dalam code block.
- Daftar dikecualikan, tabel klaim, data gap, **NEXT ACTION**, level approval.

## Self-Check

1. Setiap shot faktual berlabel **DATA FINAL**, termasuk klaim visual tersirat.
2. Tidak ada shot yang memperkuat klaim tersirat dari nama brand (rule 02 §Kata positioning & nama brand).
3. Tidak ada orang yang dapat dikenali tanpa consent.
4. On-screen text ada di setiap shot informatif; hook ≤6 kata.
5. Caption: hook ≤125 karakter, 1 CTA, 3–8 hashtag, tanpa kata terlarang.
6. Audio berlisensi untuk akun bisnis; tanpa voice clone.
7. Tidak ada lensa/editing yang mengubah kesan ukuran ruang atau kolam (rule 07).

## Safety Boundary

- Tidak publish, schedule, atau upload video.
- Tidak membuat atau meminta deepfake, voice clone, atau AI avatar orang nyata.
- Tidak merekomendasikan drone di atas rumah warga, pura, atau area terlarang.

## Exit Criteria

**Pass** hanya bila semua self-check lulus. Satu klaim visual tersirat non-**DATA FINAL** atau satu shot dengan orang tanpa consent = **Fail**: perbaiki atau ganti shot sebelum diserahkan, jangan hanya diberi tanda.

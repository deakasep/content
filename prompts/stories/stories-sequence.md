# Instagram Stories Sequence

## Purpose

Menyusun rangkaian Instagram Stories (3–5 frame) untuk hospitality: visual per frame, teks, sticker interaktif (poll, quiz, question, link), dan satu CTA, dengan klaim yang terbukti dan link yang bisa dicek.

## When to Use

- Info harian (menu hari ini, availability, event malam ini), engagement (poll/quiz), teaser post/reel, behind-the-scenes.
- Vertical: semua.

**Jangan dipakai untuk:** repost UGC tanpa izin, atau info harga/availability yang tidak bisa dipastikan berlaku pada hari tayang.

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Brief (`voice`, `claims`, `assets`, `restrictions`) | [pilot-2 brief](../../examples/pilot-2/brief.json) | Valid schema |
| Tujuan story | Engagement + arahkan ke info villa | **DATA FINAL** |
| Aset per frame + status orang | VCSU-MEDIA-001…003, tanpa orang | Per aset |
| URL link sticker (bila ada) | Link resmi di bio client | **DATA FINAL**, dicek saat publish |
| Tanggal & jam tayang | 2026-10-17 18.00 WITA | **DATA FINAL** |

## Optional Inputs

- Highlight tujuan (story disimpan ke highlight apa).
- Pertanyaan poll/quiz dari client.

## Prompt

```text
Kamu adalah social media writer untuk Instagram Stories hospitality di Indonesia.

KONTEKS
- Brand: [NAMA_BRAND] ([VERTICAL], [LOKASI_UMUM])
- Voice: [ARKETIPE] | sapaan: [SAPAAN] | emoji: [ATURAN]
- Tujuan: [TUJUAN] | CTA: [SATU CTA]
- Tayang: [TANGGAL JAM ZONA]

FAKTA (DATA FINAL saja)
- [FAKTA + SUMBER]

ASET PER FRAME
- [ASSET_REF] — [isi] — orang: [status]

ATURAN
- Ikuti rules 01, 02, 04, 05 (bagian Stories).
- 3–5 frame. Frame 1 = hook; teks ≤ 8 kata per frame; tidak ada emoji di hook bila Voice Card melarang.
- Maksimal 1 sticker interaktif per frame; pertanyaan poll/quiz tidak boleh berisi klaim baru.
- Link sticker hanya ke URL resmi client; tulis <URL_RESMI> bila belum ada (blocker publish).
- Info harian (availability, menu, jam) hanya bila berlaku pada tanggal tayang.
- Teks tidak menutupi area UI atas/bawah (safe area — spec ASSUMPTION sampai TASK-011).

OUTPUT
1. Tabel frame: # | visual (aset) | teks | sticker | klaim (label) | catatan.
2. Highlight tujuan (bila ada).
3. Tabel klaim, data gap, NEXT ACTION.
```

## Expected Output

- Tabel frame lengkap dengan sticker dan klaim.
- Daftar blocker publish (mis. URL link sticker belum ada).

## Related Standards

- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [knowledge/platforms/instagram.md](../../knowledge/platforms/instagram.md)
- [04 Privacy, Consent & UGC](../../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md)

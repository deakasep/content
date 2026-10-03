# Draft Instagram Caption

## Purpose

Menghasilkan 3 varian caption Instagram (feed/carousel/Reels) untuk bisnis hospitality yang on-brand, jujur, dan punya satu CTA jelas.

## When to Use

- Konten rutin: room tour, signature dish, treatment, sunset/ambience, behind-the-scenes, event, promo.
- Vertical: villa, hotel, restaurant/cafe/beach club, spa/wellness.

**Jangan dipakai untuk:** balasan komentar/review (pakai [reply-guest-review](../review-response/reply-guest-review.md)), listing OTA (pakai [write-hotel-description](../ota-listing/write-hotel-description.md)).

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Brand + vertical + lokasi umum | Villa Contoh Ubud — villa 2 kamar, Ubud | **DATA FINAL** |
| Voice Card | hangat, tenang, membumi; bukan: mewah berlebihan | **DATA FINAL** atau **CLIENT CONFIRMATION** |
| Pilar/topik konten | Pagi di villa: sarapan floating di kolam | **DATA FINAL** |
| Fakta visual yang tampil | Kolam privat, sarapan Indonesia, view sawah | **DATA FINAL** |
| Objective & CTA | Direct booking via WhatsApp | **DATA FINAL** |
| Bahasa | ID / EN / bilingual | **DATA FINAL** |

## Optional Inputs

- Promo (harga, periode, syarat, net/++).
- Hashtag brand & lokasi.
- Caption lama yang disukai client.
- Momen kalender ([national-holidays](../../knowledge/calendar-id/national-holidays.md)).

## Prompt

```text
Kamu adalah social media copywriter untuk bisnis hospitality di Indonesia.

KONTEKS
- Brand: [NAMA_BRAND] ([VERTICAL], [LOKASI_UMUM])
- Voice Card: [KATA SIFAT] | bukan: [KATA] | sapaan: [kamu/Anda/you] | emoji: [maks N, relevan]
- Audience: [AUDIENCE]
- Format: Instagram [feed/carousel/Reels]
- Topik: [TOPIK]
- Objective: [OBJECTIVE] | CTA: [CTA]
- Bahasa: [ID/EN/bilingual]

FAKTA YANG BOLEH DIPAKAI (DATA FINAL)
- [FAKTA + SUMBER]

ATURAN
- Baris pertama = hook yang spesifik dan sensory (apa yang dilihat/dirasa/dicicipi), maks ±125 karakter.
- Jangan pakai klise: "hidden gem", "nestled", "surga tersembunyi", "pengalaman tak terlupakan".
- Jangan superlatif tanpa bukti. Jangan klaim halal/bintang/medis tanpa bukti.
- Harga (bila ada): Rp, unit, periode, syarat, net/++.
- Satu CTA saja.
- Hashtag: 3–8 relevan (brand + lokasi + niche), di akhir.
- Fakta yang tidak ada di daftar → <KONFIRMASI: ...>.

TUGAS
Buat 3 varian caption dengan pendekatan berbeda:
A. Sensory storytelling
B. Informatif singkat (poin)
C. Conversational (ajak interaksi dengan pertanyaan)

OUTPUT
1. Varian A, B, C — masing-masing dalam code block terpisah.
2. Saran alt text untuk visual (1–2 kalimat, deskriptif, tanpa hashtag).
3. Tabel klaim: Klaim | Label | Sumber.
4. Data gap & NEXT ACTION.
```

## Expected Output

- 3 caption siap copy-paste.
- Alt text.
- Tabel klaim + data gap.

## Related Standards

- [01 Content Integrity](../../rules/01-CONTENT-INTEGRITY-STANDARD.md)
- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md)
- [03 Client Brand Voice](../../rules/03-CLIENT-BRAND-VOICE-STANDARD.md)
- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [knowledge/platforms/instagram.md](../../knowledge/platforms/instagram.md)
- Skill: [draft-caption](../../skills/draft-caption/SKILL.md)

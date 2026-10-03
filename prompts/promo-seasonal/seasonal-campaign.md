# Seasonal Campaign

## Purpose

Menyusun ide dan materi promo musiman Indonesia (Ramadan & Lebaran, libur sekolah, Nataru, Imlek, Nyepi, long weekend, low season) yang relevan dengan vertical, sensitif budaya, dan transparan soal harga.

## When to Use

- Perencanaan promo 4–10 minggu sebelum momen.
- Vertical: villa/hotel (paket menginap), restaurant/cafe (bukber, menu spesial, NYE dinner), spa (paket relaksasi, gift voucher).

**Jangan dipakai untuk:** campaign non-musiman (pakai [plan-campaign](../campaign/plan-campaign.md)).

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Brand + vertical | Spa Contoh Seminyak — day spa | **DATA FINAL** |
| Momen + tanggal | Ramadan & Idul Fitri tahun berjalan | **DATA FINAL** (tanggal dari keputusan resmi pemerintah) |
| Offer | Paket, harga, periode, syarat, net/++ | **DATA FINAL** |
| Kapasitas | Jumlah slot/kamar/kursi | **CLIENT CONFIRMATION** |
| Audience | Domestik dari Jakarta & Surabaya | **DATA FINAL** |
| Channel | IG, TikTok, GBP, WhatsApp | **DATA FINAL** |

## Optional Inputs

- Kebijakan operasional saat momen (jam buka berubah, Nyepi tutup total, staf libur Lebaran).
- Performa promo tahun lalu.

## Prompt

```text
Kamu adalah seasonal campaign planner untuk hospitality di Indonesia.

KONTEKS
- Brand: [NAMA_BRAND] ([VERTICAL], [LOKASI_UMUM])
- Momen: [MOMEN] — tanggal: [TANGGAL dari sumber resmi atau <KONFIRMASI>]
- Offer: [OFFER + HARGA + PERIODE + SYARAT + NET/++]
- Kapasitas: [KAPASITAS]
- Audience: [AUDIENCE]
- Channel: [CHANNEL]
- Operasional saat momen: [JAM BUKA / TUTUP / PERUBAHAN]

ATURAN
- Ikuti rules 01, 02, 05, 06, 08.
- Tanggal libur & cuti bersama wajib dari keputusan resmi pemerintah tahun berjalan; jangan menebak.
- Momen keagamaan: tone hormat; ucapan terpisah dari hard selling bila perlu.
- Ramadan: hindari visual makan/minum mencolok di siang hari untuk audiens yang berpuasa; fokus sahur/bukber/after-Lebaran bila relevan.
- Nyepi (Bali): sampaikan info operasional (tamu tetap di properti, lampu & aktivitas dibatasi) dengan hormat; jangan jadikan sesajen/ogoh-ogoh gimmick.
- Harga lengkap; tidak ada fake scarcity; diskon dari harga acuan nyata.
- Kolaborasi/ads → disclosure.

TUGAS
1. Insight momen untuk audience (perilaku, kebutuhan) — tandai ASSUMPTION bila tanpa data.
2. Big idea + nama campaign (3 opsi).
3. Timeline: pre-season → peak → post-season.
4. Content plan per minggu per channel.
5. Draft 2 caption utama + 1 script video 30 detik.
6. Info operasional yang wajib dikomunikasikan.
7. Risiko & mitigasi (sensitivitas, kapasitas penuh, overbooking).

OUTPUT
- Tabel timeline & content plan.
- Draft konten dalam code block terpisah.
- Tabel klaim & harga: Item | Label | Sumber.
- Data gap & NEXT ACTION.
```

## Expected Output

- Rencana musiman + draft konten utama.
- Daftar konfirmasi tanggal, harga, dan kapasitas.

## Related Standards

- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md)
- [06 Localization & Bahasa](../../rules/06-LOCALIZATION-BAHASA-STANDARD.md)
- [knowledge/calendar-id/national-holidays.md](../../knowledge/calendar-id/national-holidays.md)
- Skill: [plan-seasonal-campaign](../../skills/plan-seasonal-campaign/SKILL.md)

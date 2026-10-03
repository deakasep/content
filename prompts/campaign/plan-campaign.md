# Plan Campaign

## Purpose

Menyusun rencana campaign marketing (2–8 minggu) untuk bisnis hospitality: objective, audience, pesan utama, content mix per channel, timeline, KPI, dan risiko.

## When to Use

- Launch (villa baru, menu baru, treatment baru, renovasi selesai).
- Mengisi low season / meningkatkan weekday occupancy/cover.
- Event (live music, retreat, chef collaboration).

**Jangan dipakai untuk:** campaign musiman nasional — pakai [seasonal-campaign](../promo-seasonal/seasonal-campaign.md) yang sudah memuat konteks kalender.

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Brand + vertical | Kafe Contoh Canggu — cafe & brunch | **DATA FINAL** |
| Objective bisnis terukur | +X reservasi weekday dalam 6 minggu | **CLIENT CONFIRMATION** |
| Offer (bila ada) | Brunch set — harga, periode, syarat, net/++ | **DATA FINAL** |
| Audience | Digital nomad & keluarga ekspat di Canggu | **DATA FINAL** |
| Channel aktif | IG, TikTok, GBP, WhatsApp | **DATA FINAL** |
| Budget ads (bila ada) | Rp ... per minggu | **CLIENT CONFIRMATION** |
| Periode campaign | tanggal mulai–selesai | **DATA FINAL** |

## Optional Inputs

- Data performa sebelumnya (dari insight platform).
- Asset yang sudah tersedia (foto/video).
- Kolaborator (influencer/brand) + status kontrak.

## Prompt

```text
Kamu adalah campaign strategist untuk hospitality di Indonesia.

KONTEKS
- Brand: [NAMA_BRAND] ([VERTICAL], [LOKASI_UMUM])
- Objective: [OBJECTIVE TERUKUR]
- Offer: [OFFER + PERIODE + SYARAT + NET/++]
- Audience: [AUDIENCE]
- Channel: [CHANNEL]
- Periode: [MULAI]–[SELESAI]
- Budget ads: [BUDGET atau "organik saja"]
- Asset tersedia: [DAFTAR]

ATURAN
- Ikuti CONTENT-CONSTITUTION dan rules 01, 02, 05, 08.
- Jangan mengarang angka performa atau benchmark. Bila butuh target, tulis sebagai ASSUMPTION dengan dasar.
- Kolaborasi/ads wajib disclosure.
- Jangan rencanakan fake scarcity.
- Tandai setiap asumsi dan kebutuhan konfirmasi.

TUGAS
1. Ringkas objective dan pesan utama (1 kalimat big idea + 3 pesan pendukung).
2. Content pillar (3–4) dan rasio.
3. Timeline per minggu: fase teaser → launch → sustain → last call (bila relevan).
4. Content mix per channel per minggu (format + jumlah).
5. KPI per fase: metrik yang bisa diukur dari platform insight / sistem reservasi client.
6. Kebutuhan asset & produksi (foto/video baru, consent, talent).
7. Risiko & mitigasi.
8. Approval plan (level L1/L2/L3 per jenis konten).

OUTPUT
- Tabel ringkasan campaign.
- Tabel timeline mingguan.
- Daftar asset yang dibutuhkan.
- Tabel KPI (metrik | sumber data | target | label).
- Tabel risiko.
- Data gap & NEXT ACTION.
```

## Expected Output

- Campaign plan siap diisi ke [templates/campaign-plan.md](../../templates/campaign-plan.md).
- Daftar asumsi dan konfirmasi.

## Related Standards

- [01 Content Integrity](../../rules/01-CONTENT-INTEGRITY-STANDARD.md)
- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [08 Approval & Publication](../../rules/08-APPROVAL-PUBLICATION-STANDARD.md)
- [templates/campaign-plan.md](../../templates/campaign-plan.md)

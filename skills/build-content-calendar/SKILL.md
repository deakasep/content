---
name: build-content-calendar
description: Build a monthly social media content calendar for an Indonesian hospitality client (villa, hotel, restaurant, cafe, beach club, spa) using content pillars, Indonesian holidays and local moments, platform cadence, and approval levels. Use when the user asks for a content calendar, posting schedule, or monthly content plan.
---

# Build Content Calendar

## Load Required Context

- `../../CONTENT-CONSTITUTION.md`
- `../../rules/05-PLATFORM-STANDARD.md`
- `../../rules/06-LOCALIZATION-BAHASA-STANDARD.md`
- `../../rules/08-APPROVAL-PUBLICATION-STANDARD.md`
- `../../knowledge/calendar-id/national-holidays.md`
- `../../knowledge/segments/` (file sesuai vertical client)
- `../../templates/content-calendar.md`

## Workflow

1. Konfirmasi: client, vertical, bulan, channel aktif, kapasitas produksi (jumlah post/minggu yang realistis), objective bulan ini, offer aktif.
2. Ambil momen bulan tersebut dari kalender: libur nasional, cuti bersama, momen lokal (mis. Galungan/Kuningan di Bali), libur sekolah, long weekend. Tanggal wajib dari sumber resmi tahun berjalan; bila belum dikonfirmasi tulis **CLIENT CONFIRMATION**.
3. Tentukan 3–5 content pillar dari segment knowledge dan rasio per pillar.
4. Susun slot per minggu per channel sesuai kapasitas (jangan over-commit).
5. Isi tiap slot: tanggal, channel, format, pillar, topik, CTA, asset dibutuhkan, status asset, level approval.
6. Tandai slot yang butuh asset baru, consent, atau field visit.
7. Hitung beban kerja & deadline approval (mundur dari tanggal publish).

## Output

- Tabel kalender sesuai `../../templates/content-calendar.md`.
- Ringkasan rasio pillar & channel.
- Daftar kebutuhan asset/produksi.
- Daftar momen + sumber tanggal + label.
- **NEXT ACTION** dengan owner & deadline.

## Self-Check

1. Tanggal momen punya sumber atau label **CLIENT CONFIRMATION**.
2. Jumlah slot ≤ kapasitas produksi yang dikonfirmasi.
3. Setiap slot punya level approval dan deadline approval.
4. Momen keagamaan ditangani sensitif (rule 06).
5. Tidak ada promo tanpa offer yang dikonfirmasi.

## Safety Boundary

- Kalender adalah rencana; tidak menjadwalkan di scheduler.
- Tidak mengarang tanggal libur atau event lokal.
- Tidak mengarang offer/harga.

## Exit Criteria

**Pass** bila kalender lengkap, realistis terhadap kapasitas, dan semua tanggal/offer berlabel.

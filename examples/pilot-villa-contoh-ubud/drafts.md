# Pilot Drafts — Villa Contoh Ubud (FIKTIF)

> **Contoh fiktif untuk pilot TASK-012.** Properti, harga, aset, dan approver tidak nyata. Jangan dipakai sebagai konten client.

Brief: [brief.json](./brief.json) (`VCU-202610-01`). Alur: [WORKFLOW.md](../../WORKFLOW.md).

## Step 2 — Classify

| Klaim | Label | Sumber | Boleh tampil di konten? |
|---|---|---|---|
| 2 kamar tidur, maks 4 dewasa | **DATA FINAL** | Fact sheet fiktif VCU v1 | Ya |
| Kolam privat 3 × 6 m | **DATA FINAL** | Fact sheet + foto kategori A | Ya |
| Teras timur menghadap sawah | **DATA FINAL** | Foto kategori A bertanggal | Ya |
| Sarapan Indonesia diantar ke teras | **DATA FINAL** | Fact sheet | Ya |
| Parkir di ujung gang, jalan kaki ±80 m | **DATA FINAL** | Fact sheet | Ya — wajib disebut (mengurangi review negatif) |
| ±15 menit berkendara ke pusat Ubud | **FIELD VERIFICATION** | — | **Tidak** sampai diukur |
| Wi-Fi cepat untuk kerja remote | **ASSUMPTION** | — | **Tidak** (tidak ada speed test) |
| Persentase pajak & service charge | **CLIENT CONFIRMATION** | — | Ditulis generik: "belum termasuk pajak & service charge" |
| Offer Long Stay Sawah | **DATA FINAL** | Brief `offer` | Ya, lengkap dengan periode, syarat, dan status ++ |

## Step 3a — Skill `draft-caption` (Instagram carousel)

Voice: arketipe **Tenang & Membumi** (default dari [hospitality-voice](../../knowledge/voice-guides/hospitality-voice.md)). Voice Card client berstatus **CLIENT CONFIRMATION** karena brief tidak punya field untuk itu (lihat temuan F-01).

### Varian A — Sensory storytelling (bilingual)

```text
Pagi di Villa Contoh Ubud dimulai dari teras timur: sawah di depan, sarapan Indonesia diantar ke meja.

Long Stay Sawah · 1 Nov–15 Des 2026
• Rp1.500.000/villa/malam, minimal 3 malam
• Termasuk sarapan untuk 2 orang
• Belum termasuk pajak & service charge
• Tidak bisa digabung promo lain

2 kamar tidur dan kolam privat 3 × 6 m. Parkir mobil di ujung gang, lalu jalan kaki ±80 m ke villa.

EN — Slow mornings on the east terrace, rice fields in front, Indonesian breakfast brought to your table. Long Stay Sawah: IDR 1,500,000 per villa per night, minimum 3 nights, 1 Nov–15 Dec 2026, breakfast for 2 included, excluding tax & service charge.

Info & booking: WhatsApp via link di bio 🌾

#VillaContohUbud #ubud #gianyar #balivilla #longstaybali
```

### Varian B — Informatif singkat

```text
Long Stay Sawah di Villa Contoh Ubud 🌾

📅 1 Nov–15 Des 2026
🏡 1 villa: 2 kamar tidur, maks 4 dewasa, kolam privat 3 × 6 m
🍳 Sarapan Indonesia untuk 2 orang, diantar ke teras
💰 Rp1.500.000/villa/malam, minimal 3 malam (belum termasuk pajak & service charge; tidak bisa digabung promo lain)
🚶 Parkir di ujung gang, jalan kaki ±80 m ke villa

Booking via WhatsApp di link bio.

#VillaContohUbud #ubud #balivilla #longstaybali
```

### Varian C — Conversational

```text
Kalau kerja dari Bali, kamu lebih suka view sawah atau view kolam? Di teras timur Villa Contoh Ubud, dua-duanya kelihatan.

Long Stay Sawah berlaku 1 Nov–15 Des 2026: Rp1.500.000/villa/malam, minimal 3 malam, sudah termasuk sarapan untuk 2 orang (belum termasuk pajak & service charge; tidak bisa digabung promo lain).

Catatan kecil: mobil parkir di ujung gang, lalu jalan kaki ±80 m ke villa.

Tanya ketersediaan lewat WhatsApp di link bio ☕

#VillaContohUbud #ubud #gianyar #balivilla #workfrombali
```

**Alt text (slide 1):** Teras kayu menghadap sawah hijau di pagi hari, dengan nampan sarapan berisi nasi goreng dan teh di atas meja kecil.

> **ASSUMPTION** pada alt text: isi foto VCU-MEDIA-001 diasumsikan seperti di atas, karena aset fiktif. Pada client nyata, alt text ditulis dari foto aktual.

## Step 3b — Skill `write-ota-listing` (Booking.com, EN)

Batas karakter Booking.com: **CLIENT CONFIRMATION** (terkait TASK-011). Kontak langsung, link, dan harga sengaja tidak dicantumkan (rule 05; harga dikelola di rate plan OTA).

### Summary

```text
A two-bedroom private villa with its own 3 × 6 m pool and an east-facing terrace over the rice fields of Gianyar, with Indonesian breakfast served on the terrace.
```

### Property description

```text
Villa Contoh Ubud sits among working rice fields in Gianyar. The east terrace looks straight onto the paddies and is where breakfast is served each morning.

The villa has two bedrooms for up to four adults, a private 3 × 6 m pool, and a shared living area. <KONFIRMASI: bed type per kamar, ukuran kamar, kamar mandi, AC, dapur>

Getting here: cars park at the end of a narrow lane, followed by an approximately 80 m walk to the villa. <KONFIRMASI: bantuan bawa koper oleh staf?>
```

### Good to know

```text
- Cars cannot reach the villa door; parking is at the end of the lane, about 80 m away on foot.
- Breakfast is included only in rates that list it.
- <KONFIRMASI: check-in/check-out time, children, pets, smoking, quiet hours>
```

### Tabel klaim listing

| Klaim | Label | Sumber |
|---|---|---|
| Two bedrooms, up to four adults | **DATA FINAL** | Fact sheet |
| Private 3 × 6 m pool | **DATA FINAL** | Fact sheet + foto |
| East terrace over rice fields | **DATA FINAL** | Foto kategori A |
| ~80 m walk from parking | **DATA FINAL** | Fact sheet |
| Bed type, ukuran kamar, kebijakan | **CLIENT CONFIRMATION** | Tidak ada di brief/fact sheet (temuan F-02) |
| Jarak ke pusat Ubud | Sengaja tidak dicantumkan | **FIELD VERIFICATION** belum dilakukan |

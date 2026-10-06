# Wireframe — Studio (Dashboard Internal)

> **ID:** Wireframe lo-fi 8 halaman untuk owner agency dan tim konten. Desktop adalah tempat kerja utama, tapi semua halaman tetap bisa dipakai di HP untuk cek status dan follow-up. Data contoh fiktif.
> **EN:** Lo-fi wireframes for 8 Studio pages. Desktop is the main workspace; every page still works on mobile for status checks and follow-ups.

**Navigasi:** desktop = sidebar `Ringkasan · Klien · Konten · AI Agent · Kalender · Laporan` + bawah `Tim · Pengaturan`. Mobile = bottom nav `Ringkasan · Klien · Konten · Agent · Lainnya` (Kalender, Laporan, Tim, Pengaturan ada di *Lainnya*).

**Shortcut keyboard (desktop):** `G` lalu `O/K/C/A/L` untuk pindah halaman · `/` cari · `N` konten baru · `?` daftar shortcut.

---

## 1. Ringkasan / Overview

### Desktop

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ ◯ CLAU Studio│ ⌕ Cari klien, konten…  (/)                       ID|EN   (!)5   (D)   │
│              ├───────────────────────────────────────────────────────────────────────┤
│ ◉ Ringkasan  │ Selamat pagi, Kak Dea                        Okt 2026 ▾   [+ Konten]  │
│ ○ Klien    12│                                                                       │
│ ○ Konten   48│ ┌─ Klien aktif ─┐ ┌─ Konten bln ini ┐ ┌─ Pendapatan ─┐ ┌─ Agent ───┐  │
│ ○ AI Agent   │ │ 12            │ │ 48 / 60 target  │ │ Rp42.000.000 │ │ 5/6 siap  │  │
│ ○ Kalender   │ │ +2 vs Sep     │ │ ████████░░ 80%  │ │ 10 invoice   │ │ 1 error   │  │
│ ○ Laporan    │ └───────────────┘ └─────────────────┘ └──────────────┘ └───────────┘  │
│              │                                                                       │
│              │ ┌─ Menunggu manusia (9) ────────────────┐ ┌─ Pipeline ───────────┐    │
│              │ │ ! Review independen L2 Villa Contoh 2 │ │ Backlog     ████  12 │    │
│              │ │ ! Fakta belum dikonfirm Cafe Senja  3 │ │ Dikerjakan  ███    9 │    │
│              │ │ ! Approval > 48 jam    Hotel Lorong 1 │ │ Review QA   ██     6 │    │
│              │ │ ! Tandai tayang (URL)  Spa Tirta   3  │ │ Di klien    ██     7 │    │
│              │ │                        [Lihat semua ›]│ │ Tayang      ██████14 │    │
│              │ └───────────────────────────────────────┘ └──────────────────────┘    │
│ ──────────── │ ┌─ Tayang 7 hari ke depan ──────────────────────────────────────────┐ │
│ ○ Tim        │ │ Sen 12  Villa Contoh · IG carousel [Disetujui]  18.00 WITA        │ │
│ ○ Pengaturan │ │ Sel 13  Cafe Senja · TikTok        [Di klien]   12.00 WIB         │ │
│ (D) Dea      │ └───────────────────────────────────────────────────────────────────┘ │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

### Mobile

```text
┌──────────────────────────────────┐
│ CLAU Studio       ⌕   (!)5  (D)  │
├──────────────────────────────────┤
│ Selamat pagi, Kak Dea            │
│ Oktober 2026                     │
│ ┌─────────────┐ ┌─────────────┐  │
│ │ 12 klien    │ │ 48/60 konten│  │
│ └─────────────┘ └─────────────┘  │
│ ┌─────────────┐ ┌─────────────┐  │
│ │ Rp42 jt     │ │ Agent 5/6   │  │
│ └─────────────┘ └─────────────┘  │
│ Menunggu manusia (9)          ›  │
│ ┌──────────────────────────────┐ │
│ │ ! Review L2 · Villa Contoh 2 │ │
│ │ ! Fakta · Cafe Senja       3 │ │
│ │ ! Approval > 48j · Hotel   1 │ │
│ └──────────────────────────────┘ │
├──────────────────────────────────┤
│  ◉      ○      ○      ○      ≡   │  ← Ringkasan · Klien · Konten · Agent · Lainnya
└──────────────────────────────────┘
```

**Catatan:** kartu *Menunggu manusia* adalah pusat Studio. Isinya adalah hal yang **tidak boleh** dikerjakan AI: review independen L2/L3, approval, publish, dan konfirmasi fakta ke klien. Kartu *Pendapatan* hanya terlihat oleh peran Owner.

---

## 2. Klien / Clients

### Desktop

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Klien (12)                                          [+ Tambah klien]  │
│              ├───────────────────────────────────────────────────────────────────────┤
│              │ ⌕ Cari…   Industri ▾   Paket ▾   Status ▾   Wilayah ▾                 │
│              ├─────────────────────┬────────────┬─────────┬───────────┬─────────┬────┤
│              │ Nama ↕              │ Industri   │ Paket   │ Wilayah   │ Status  │    │
│              ├─────────────────────┼────────────┼─────────┼───────────┼─────────┼────┤
│              │ Villa Contoh Ubud   │ Villa      │ Growth  │ Bali      │ Onboard │ ⋮  │
│              │ Cafe Senja (3)      │ Cafe       │ Pro     │ Jakarta   │ Aktif   │ ⋮  │
│              │ Hotel Lorong Kota   │ Hotel      │ Pro     │ Yogyakarta│ Aktif   │ ⋮  │
│              │ Spa Tirta           │ Spa        │ Starter │ Bandung   │ Aktif   │ ⋮  │
│              │ Kapal Phinisi Komodo│ Cruise     │ Growth  │ Labuan Bj │ Jeda    │ ⋮  │
│              ├─────────────────────┴────────────┴─────────┴───────────┴─────────┴────┤
│              │ Menampilkan 1–5 dari 12                  ‹ Sebelumnya  1 2 3  Berik › │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

### Detail Klien (desktop)

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Klien / Villa Contoh Ubud                   [Onboard]   [Aksi ▾]      │
│              ├───────────────────────────────────────────────────────────────────────┤
│              │ [Ringkasan] [Fakta 6/8] [Konten] [Brand & voice] [Akses] [Riwayat]    │
│              ├───────────────────────────────────────────────────────────────────────┤
│              │ Fakta properti (fact sheet v1)                 Disetujui owner: belum │
│              │  3 kamar tidur              [CLIENT CONFIRMATION]  dikirim 5 Okt      │
│              │  Harga Rp2.750.000/malam    [CLIENT CONFIRMATION]  net/++ ?           │
│              │  Promo 10% min 2 malam      [RISK] periode & syarat belum ada         │
│              │                       [Kirim pengingat ke klien]  [Edit fakta]        │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

### Mobile

```text
┌──────────────────────────────────┐
│ Klien (12)          ⌕   [+]      │
├──────────────────────────────────┤
│ [Semua][Aktif][Onboard][Jeda]    │
│ ┌──────────────────────────────┐ │
│ │ Villa Contoh Ubud  [Onboard] │ │
│ │ Villa · Growth · Bali        │ │
│ │ Fakta 6/8 · 0 konten tayang  │ │
│ └──────────────────────────────┘ │
│ ┌──────────────────────────────┐ │
│ │ Cafe Senja (3)       [Aktif] │ │
│ │ Cafe · Pro · Jakarta         │ │
│ │ 14 konten bulan ini          │ │
│ └──────────────────────────────┘ │
├──────────────────────────────────┤
│  ○      ◉      ○      ○      ≡   │
└──────────────────────────────────┘
```

Status klien: **Onboard** (fakta belum lengkap) · **Aktif** · **Jeda** · **Selesai**. Aksi (`⋮`): lihat portal sebagai klien (read-only), undang approver, jeda, arsipkan.

---

## 3. Konten — Pipeline / Content Pipeline

### Desktop (Kanban)

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Konten  [Kanban|Tabel]   Klien ▾  Channel ▾  Level ▾      [+ Konten]  │
│              ├─────────────────┬─────────────────┬─────────────────┬─────────────────┤
│              │ Backlog (12)    │ Dikerjakan (9)  │ Review QA (6)   │ Di klien (7)    │
│              │                 │                 │                 │                 │
│              │ ┌─────────────┐ │ ┌─────────────┐ │ ┌─────────────┐ │ ┌─────────────┐ │
│              │ │Cafe Senja   │ │ │Villa Contoh │ │ │Villa Contoh │ │ │Hotel Lorong │ │
│              │ │TikTok menu  │ │ │Story promo  │ │ │Carousel     │ │ │Reel kamar   │ │
│              │ │L1 · 18 Okt  │ │ │L2 · agent:  │ │ │L2 · 11 Okt  │ │ │L2 · 2 hari  │ │
│              │ │             │ │ │Copywriter   │ │ │Self-review  │ │ │menunggu     │ │
│              │ └─────────────┘ │ └─────────────┘ │ │! butuh rev. │ │ └─────────────┘ │
│              │ ┌─────────────┐ │                 │ │  manusia    │ │                 │
│              │ │Spa Tirta    │ │                 │ └─────────────┘ │                 │
│              │ │GBP update   │ │                 │                 │                 │
│              │ └─────────────┘ │                 │                 │                 │
│              ├─────────────────┴─────────────────┴─────────────────┴─────────────────┤
│              │ → kolom Disetujui (5) dan Tayang (14) ada di kanan; geser / pakai tab │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

Kolom pipeline: **Backlog → Dikerjakan → Review QA → Di klien → Disetujui → Tayang**. Kartu bisa di-drag, **kecuali** perpindahan yang butuh syarat:

| Perpindahan | Syarat (diblok bila tidak terpenuhi) |
|---|---|
| Review QA → Di klien | QA lulus; untuk L2/L3 ada **review independen manusia** |
| Di klien → Disetujui | **Hanya klien** yang bisa menyetujui (dari Portal) |
| Disetujui → Tayang | Manusia mengisi **URL post + jam tayang** ("Tandai sudah tayang") |

### Detail Konten (desktop, panel kanan)

```text
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ Villa Contoh · Carousel kolam & taman         [Review QA]  [L2]            [×]        │
├───────────────────────────────────────┬───────────────────────────────────────────────┤
│ [ Preview IG 4:5 ]                    │ [Caption] [Klaim 13] [QA] [Versi] [Komentar]  │
│                                       │ Tabel klaim per kalimat                       │
│                                       │ #  Kalimat                      Label   Hasil │
│                                       │ 1  Sarapan di bale, lalu…       CLIENT  Tunggu│
│                                       │ 6  Simpan post ini…             —       OK    │
│                                       │ check_caption: PASS (mekanis)                 │
│                                       │ Review independen: [ ] Belum  → [Tugaskan]    │
├───────────────────────────────────────┴───────────────────────────────────────────────┤
│ Agent: Copywriter · skill draft-caption v1.0 · 4 Okt 21.10      [Minta revisi agent]  │
│                                                    [Kirim ke klien] (nonaktif: L2)    │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

### Mobile

```text
┌──────────────────────────────────┐
│ Konten       Filter ▾     [+]    │
├──────────────────────────────────┤
│ [Backlog 12][Dikerjakan 9][QA 6]›│  ← satu kolom per tab
│ ┌──────────────────────────────┐ │
│ │ Villa Contoh · Carousel      │ │
│ │ L2 · 11 Okt · Review QA      │ │
│ │ ! Butuh review manusia       │ │
│ └──────────────────────────────┘ │
│ ┌──────────────────────────────┐ │
│ │ Hotel Lorong · Reel kamar    │ │
│ │ L2 · Di klien · 2 hari       │ │
│ └──────────────────────────────┘ │
├──────────────────────────────────┤
│  ○      ○      ◉      ○      ≡   │
└──────────────────────────────────┘
```

---

## 4. AI Agent

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ AI Agent                        Semua sistem: 5 siap · 1 error        │
│              ├───────────────────────────────────────────────────────────────────────┤
│              │ ┌─ Strategy ─────────┐ ┌─ Copywriter ───────┐ ┌─ Image ────────────┐  │
│              │ │ ● Siap             │ │ ● Bekerja (3)      │ │ ● Siap             │  │
│              │ │ Kalender, campaign │ │ Caption, OTA, story│ │ Brief visual, alt  │  │
│              │ │ Terakhir: 08.12    │ │ Antrean: 5         │ │ Terakhir: kemarin  │  │
│              │ │ 7 hari: 14 tugas   │ │ 7 hari: 61 tugas   │ │ 7 hari: 9 tugas    │  │
│              │ └────────────────────┘ └────────────────────┘ └────────────────────┘  │
│              │ ┌─ Video ────────────┐ ┌─ QA ───────────────┐ ┌─ Reply ────────────┐  │
│              │ │ ● Siap             │ │ ● Menunggu manusia │ │ x Error            │  │
│              │ │ Reel & TikTok      │ │ 4 konten L2 perlu  │ │ Template review    │  │
│              │ │ script             │ │ review independen  │ │ gagal dimuat       │  │
│              │ │ 7 hari: 6 tugas    │ │ 7 hari: 40 cek     │ │ [Lihat log]        │  │
│              │ └────────────────────┘ └────────────────────┘ └────────────────────┘  │
│              │ Aturan: agent menyiapkan draft & cek. Approval, publish, dan kirim ke │
│              │ tamu tetap manusia (AI-CONSTITUTION §4).                              │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

Status agent: `● Siap` (success) · `● Bekerja (n)` (info, berdenyut) · `● Menunggu manusia` (warning) · `x Error` (error). Detail agent: antrean, riwayat tugas, skill/prompt yang dipakai (dari `agents/registry.json`), error log.

Mobile: kartu agent ditumpuk 1 kolom; status agent error muncul di kartu paling atas.

---

## 5. Kalender / Production Calendar

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Kalender produksi  ‹ Okt 2026 ›   [Bulan|Minggu]   Klien ▾  Tim ▾     │
│              ├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬───────────┤
│              │ Sen 12  │ Sel 13  │ Rab 14  │ Kam 15  │ Jum 16  │ Sab 17  │ Min 18    │
│              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼───────────┤
│              │ Tayang  │ Tayang  │ Draft   │ Tayang  │ Tenggat │         │ Tayang    │
│              │ Contoh  │ Senja   │ Tirta   │ Lorong  │ laporan │         │ Senja     │
│              │ 18.00   │ 12.00   │ (draft) │ 07.00   │ Sep     │         │ 19.00 WIB │
│              │ WITA    │ WIB     │         │ WIB     │         │         │           │
└──────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴───────────┘
```

Tiga jenis item: **Tayang** (jam + zona waktu klien), **Tenggat draft**, **Tenggat laporan**. Warna per klien (maks 8 warna dari palet chart) + nama klien selalu ditulis. Hari libur nasional ditampilkan di header tanggal.

---

## 6. Laporan / Reports

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Laporan bulanan        Periode: September 2026 ▾                      │
│              ├─────────────────────┬──────────┬──────────┬────────────┬──────────────┤
│              │ Klien               │ Konten   │ Saves    │ Status     │              │
│              ├─────────────────────┼──────────┼──────────┼────────────┼──────────────┤
│              │ Cafe Senja          │ 14       │ 2.310    │ Terkirim   │ [PDF] [CSV]  │
│              │ Hotel Lorong Kota   │ 10       │ 1.102    │ Draft      │ [Edit]       │
│              │ Spa Tirta           │ 8        │ 640      │ Data kurang│ [Lengkapi]   │
│              ├─────────────────────┴──────────┴──────────┴────────────┴──────────────┤
│              │ [Export semua (ZIP)]          Data: Instagram Insights, 1 Okt 08.00   │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

Status laporan: **Data kurang** (ada konten tayang tanpa URL/metrik) → **Draft** (dibuat otomatis, perlu diedit manusia) → **Terkirim**. Editor laporan: ringkasan 3 kalimat di atas, angka di bawah, setiap angka menyebut sumber.

---

## 7. Pengaturan / Settings

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Pengaturan                                                            │
│              ├──────────────────┬────────────────────────────────────────────────────┤
│              │ Brand agency     │ Brand agency                                       │
│              │ Paket & harga    │ Nama        [CLAU Content Studio           ]       │
│              │ Integrasi        │ Logo        [Unggah]  (SVG/PNG, maks 1 MB)         │
│              │ API & webhook    │ Warna utama [#0F766E] (preview kontras: 5.47 AA)   │
│              │ Notifikasi       │ Bahasa default portal  [Indonesia ▾]               │
│              │ Keamanan         │ Zona waktu agency      [WIB ▾]                     │
│              │ Audit log        │                                                    │
│              │                  │                          [Batal]  [Simpan]         │
└──────────────┴──────────────────┴────────────────────────────────────────────────────┘
```

| Section | Isi |
|---|---|
| Integrasi | Instagram/Meta, TikTok, Google Business Profile (status: terhubung/tidak), WhatsApp Business, email. **Hanya baca insight**; tidak ada auto-publish |
| API & webhook | API key (tampil sekali, bisa dicabut), webhook keluar; untuk integrasi nanti |
| Keamanan | 2FA wajib untuk peran Owner/Admin; sesi aktif; credential klien **tidak disimpan** di sini (AI-BOUNDARY) |
| Audit log | Siapa melakukan apa, kapan: approve, tandai tayang, ubah fakta, ubah akses |

---

## 8. Tim / Team

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Tim (3)                                               [+ Undang]      │
│              ├─────────────────────┬────────────────┬─────────────┬──────────────────┤
│              │ Nama                │ Peran          │ Klien       │ Beban minggu ini │
│              ├─────────────────────┼────────────────┼─────────────┼──────────────────┤
│              │ (D) Dea Karisna     │ Owner          │ Semua       │ 6 review         │
│              │ (R) Rani            │ Content lead   │ 6 klien     │ 9 review         │
│              │ (A) Adi             │ Content staff  │ 4 klien     │ 12 draft         │
└──────────────┴─────────────────────┴────────────────┴─────────────┴──────────────────┘
```

| Peran | Bisa | Tidak bisa |
|---|---|---|
| **Owner** | Semua, termasuk pendapatan & keamanan | — |
| **Content lead** | Review independen, kirim ke klien, tandai tayang, laporan | Pendapatan, hapus klien |
| **Content staff** | Buat/edit draft, jalankan agent, self-check | Review independen atas draft sendiri, kirim ke klien |
| **Viewer** | Lihat | Mengubah apa pun |

Aturan penting: sistem **mencegah** orang yang membuat draft menandai review independen atas draft yang sama (rule 08).

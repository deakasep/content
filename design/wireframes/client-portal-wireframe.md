# Wireframe — Portal Klien / Client Portal

> **ID:** Wireframe lo-fi 7 halaman untuk klien hospitality (owner/GM/approver). Mobile 360 px dulu, lalu desktop 1280 px. Teks di wireframe memakai Bahasa Indonesia (default); padanan English ada di tabel copy tiap halaman. Contoh data memakai properti fiktif **Villa Contoh Ubud**.
> **EN:** Lo-fi wireframes for 7 Client Portal pages. Mobile (360 px) first, then desktop (1280 px). English copy is listed under each page.

**Navigasi:** mobile = bottom nav `Beranda · Konten · Kalender · Laporan · Profil`; Notifikasi lewat ikon lonceng di top bar. Desktop = sidebar kiri dengan item yang sama.

**Pilar:** Portal memakai shell yang sama untuk 5 pilar CLAU AI. Sekarang klien hanya melihat item Pilar 1 (konten). Saat pilar lain aktif, item baru (mis. konfirmasi harga & paket Pilar 2, template pesan tamu Pilar 3, SOP Pilar 4) masuk ke daftar *Konten* dan *Konfirmasi Fakta* dengan Pillar Badge, tanpa menu baru; Laporan menambah bagian per pilar aktif. Detail: [pillars.md](../pillars.md).

---

## 1. Login / Masuk

### Mobile

```text
┌──────────────────────────────────┐
│                         ID | EN  │
│                                  │
│          ◯ CLAU                  │
│                                  │
│   Selamat datang kembali         │  ← h2
│   Masuk untuk melihat konten     │
│   properti Anda.                 │
│                                  │
│   Email                          │
│   ┌──────────────────────────┐   │
│   │ nama@villa.com           │   │
│   └──────────────────────────┘   │
│   Kata sandi                     │
│   ┌──────────────────────┬───┐   │
│   │ ••••••••             │ o │   │
│   └──────────────────────┴───┘   │
│                  Lupa kata sandi?│
│                                  │
│   ┌──────────────────────────┐   │
│   │          Masuk           │   │  ← primary lg, full width
│   └──────────────────────────┘   │
│   ──────────── atau ──────────   │
│   ┌──────────────────────────┐   │
│   │  ✉  Kirim link masuk     │   │  ← secondary (magic link)
│   └──────────────────────────┘   │
│                                  │
│   Belum punya akun? Akun dibuat  │
│   oleh tim CLAU. Hubungi kami.   │
│                                  │
│  © 2026 CLAU · Privasi · Syarat  │
└──────────────────────────────────┘
```

### Desktop

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ ┌──────────────────────────────────────┐ ┌─────────────────────────────────────────┐ │
│ │                                      │ │                               ID | EN   │ │
│ │                                      │ │  ◯ CLAU                                 │ │
│ │      [ Foto properti klien /         │ │                                         │ │
│ │        ilustrasi lanskap ]           │ │  Selamat datang kembali                 │ │
│ │                                      │ │  Masuk untuk melihat konten properti    │ │
│ │                                      │ │  Anda.                                  │ │
│ │ "Konten yang jujur, disiapkan AI,    │ │  Email       [______________________]   │ │
│ │  diperiksa manusia, disetujui        │ │  Kata sandi  [__________________|o ]    │ │
│ │  Anda."                              │ │                     Lupa kata sandi?    │ │
│ │                                      │ │  [             Masuk              ]     │ │
│ │                                      │ │  [ ✉ Kirim link masuk ke email    ]     │ │
│ └──────────────────────────────────────┘ └─────────────────────────────────────────┘ │
│                         © 2026 CLAU · Kebijakan Privasi · Syarat Layanan             │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

| Elemen | ID | EN | Catatan |
|---|---|---|---|
| Judul | Selamat datang kembali | Welcome back | — |
| Tombol | Masuk · Kirim link masuk | Sign in · Email me a sign-in link | Magic link = opsi untuk user yang sering lupa password |
| Error login | Email atau kata sandi belum cocok. Coba lagi atau pakai link masuk. | Email or password doesn't match. Try again or use a sign-in link. | Jangan sebut field mana yang salah (keamanan) |
| Akun terkunci | Terlalu banyak percobaan. Coba lagi dalam 15 menit. | Too many attempts. Try again in 15 minutes. | Rate limit |

---

## 2. Beranda / Dashboard

Greeting mengikuti jam lokal user (zona dari profil): **pagi** 04.00–10.59 · **siang** 11.00–14.59 · **sore** 15.00–17.59 · **malam** 18.00–03.59.

### Mobile

```text
┌──────────────────────────────────┐
│ Villa Contoh Ubud ▾    (!)3  (S) │  ← switcher properti, notifikasi, avatar
├──────────────────────────────────┤
│ Selamat sore, Bu Ratna           │  ← h2
│ Oktober 2026                     │
│                                  │
│ ┌──────────────────────────────┐ │
│ │ ! 3 konten menunggu Ibu      │ │  ← kartu prioritas (warning tint)
│ │   Paling cepat tayang:       │ │
│ │   Min, 11 Okt · 18.00 WITA   │ │
│ │ ┌──────────────────────────┐ │ │
│ │ │      Lihat & setujui     │ │ │  ← primary
│ │ └──────────────────────────┘ │ │
│ └──────────────────────────────┘ │
│                                  │
│ ┌──────────────────────────────┐ │
│ │ ? 2 fakta perlu konfirmasi   │ │  ← Konfirmasi Fakta
│ │   Harga & syarat promo    ›  │ │
│ └──────────────────────────────┘ │
│                                  │
│ Bulan ini                        │  ← h6
│ ┌─────────────┐ ┌─────────────┐  │
│ │ 12          │ │ 7           │  │
│ │ Konten      │ │ Sudah tayang│  │
│ └─────────────┘ └─────────────┘  │
│ ┌─────────────┐ ┌─────────────┐  │
│ │ 1.284       │ │ 46          │  │
│ │ Saves       │ │ DM inquiry  │  │
│ │ ▲18% vs Sep │ │ ▲5 vs Sep   │  │
│ └─────────────┘ └─────────────┘  │
│                                  │
│ Tayang berikutnya              › │
│ ┌──────────────────────────────┐ │
│ │ [img] Carousel kolam & taman │ │
│ │       IG · Min 11 Okt 18.00  │ │
│ │       [Terjadwal]            │ │
│ └──────────────────────────────┘ │
├──────────────────────────────────┤
│  ⌂      ▦      ▣      ▤      ◯   │  ← bottom nav: Beranda · Konten · Kalender · Laporan · Profil
└──────────────────────────────────┘
```

### Desktop

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ ◯ CLAU       │ Villa Contoh Ubud ▾                               ID|EN   (!)3   (S)  │
│              ├───────────────────────────────────────────────────────────────────────┤
│ ⌂ Beranda    │ Selamat sore, Bu Ratna                                                │
│ ▦ Konten   3 │ Oktober 2026 · 3 konten menunggu persetujuan Ibu                      │
│ ▣ Kalender   │                                                                       │
│ ▤ Laporan    │ ┌─ Menunggu Ibu (8 kolom) ───────────────────────┐ ┌─ Okt 2026 (4) ─┐ │
│ (!) Notif   2│ │ [img] Carousel kolam & taman  L2  ?2 fakta     │ │ S S R K J S M  │ │
│              │ │       IG · Min 11 Okt 18.00 WITA  [Lihat ›]    │ │       1 2 3 4  │ │
│              │ │ [img] Story promo 3 malam     L2  ?1 fakta     │ │ 5 6 7 8 9 10 ● │ │
│              │ │       IG · Sel 13 Okt 19.00 WITA  [Lihat ›]    │ │ 12 ● 14 15 …   │ │
│              │ │ [img] Reel sarapan di taman   L1               │ │ ● = konten     │ │
│              │ │       IG · Kam 15 Okt 07.00 WITA  [Lihat ›]    │ └────────────────┘ │
│              │ └────────────────────────────────────────────────┘                    │
│              │ ┌─ Konten ──┐ ┌─ Sudah tayang ─┐ ┌─ Saves ──────┐ ┌─ DM inquiry ─┐    │
│ ─────────    │ │ 12        │ │ 7              │ │ 1.284 ▲18%   │ │ 46 ▲5        │    │
│ ◯ Profil     │ └───────────┘ └────────────────┘ └──────────────┘ └──────────────┘    │
│ ⇥ Keluar     │ Sumber angka: Instagram Insights, diperbarui 6 Okt 2026 08.00 WITA    │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

| Elemen | ID | EN |
|---|---|---|
| Greeting | Selamat pagi/siang/sore/malam, {sapaan} {nama} | Good morning/afternoon/evening, {name} |
| Kartu prioritas | {n} konten menunggu {Ibu/Bapak/Kakak} | {n} posts awaiting your approval |
| Fakta | {n} fakta perlu konfirmasi | {n} facts need your confirmation |
| Sumber data | Sumber angka: {platform}, diperbarui {waktu} | Source: {platform}, updated {time} |

**Catatan:** angka statistik **selalu** menampilkan sumber dan waktu pembaruan (rule laporan: tidak dibulatkan ke atas, tidak dikarang). Bila belum ada data: "Belum ada data. Angka muncul setelah konten pertama tayang."

---

## 3. Konten / Content

### 3a. List — Mobile

```text
┌──────────────────────────────────┐
│ ←  Konten                ⌕  ⋮    │
├──────────────────────────────────┤
│ [Perlu Anda 3][Ditinjau][Diset›  │ ← tabs scroll horizontal: Perlu Anda · Ditinjau · Disetujui · Tayang
├──────────────────────────────────┤
│ ┌──────────────────────────────┐ │
│ │ ┌──────┐ Carousel kolam &    │ │
│ │ │ img  │ taman               │ │
│ │ │ 4:5  │ IG feed · 11 Okt    │ │
│ │ └──────┘ [Ditinjau] [L2]     │ │
│ │          ? 2 fakta perlu     │ │
│ │             konfirmasi       │ │
│ └──────────────────────────────┘ │
│ ┌──────────────────────────────┐ │
│ │ ┌──────┐ Story promo 3 malam │ │
│ │ │ 9:16 │ IG story · 13 Okt   │ │
│ │ └──────┘ [Ditinjau] [L2]     │ │
│ └──────────────────────────────┘ │
│        [ Muat lebih banyak ]     │
├──────────────────────────────────┤
│  ⌂      ▦      ▣      ▤      ◯   │
└──────────────────────────────────┘
```

Status yang dipakai: **Draf** (tidak terlihat oleh klien) → **Ditinjau** / In review → **Disetujui** / Approved → **Tayang** / Published, plus **Perlu revisi** / Changes requested.

### 3b. Detail & Approval — Mobile

```text
┌──────────────────────────────────┐
│ ←  Carousel kolam & taman    ⋮   │
├──────────────────────────────────┤
│ ┌──────────────────────────────┐ │
│ │                              │ │
│ │     [ Preview IG 4:5 ]       │ │  ← geser untuk slide 1/5
│ │                              │ │
│ │          ● ○ ○ ○ ○           │ │
│ └──────────────────────────────┘ │
│ Instagram feed · Min, 11 Okt 2026│
│ 18.00 WITA · [Ditinjau] [L2]     │
│                                  │
│ Caption                    Salin │
│ ┌──────────────────────────────┐ │
│ │ Sarapan di bale, lalu        │ │
│ │ berenang sebelum siang di    │ │
│ │ Villa Contoh Ubud. …         │ │
│ │                 Lihat semua ▾│ │
│ └──────────────────────────────┘ │
│                                  │
│ Fakta yang dipakai (5)           │  ← kunci approval L2
│ ┌──────────────────────────────┐ │
│ │ 3 kamar tidur   [DATA FINAL] │ │
│ │ Kolam privat    [DATA FINAL] │ │
│ │ AC di semua kamar            │ │
│ │ [CLIENT CONFIRMATION]        │ │
│ │  [✓ Benar]   [✎ Perbaiki]    │ │
│ └──────────────────────────────┘ │
│ ✓ Diperiksa tim CLAU (manusia)   │  ← status review independen
│ ✉ Komentar (0)                 › │
├──────────────────────────────────┤
│ ┌────────────┐┌────────────────┐ │  ← approval bar sticky
│ │✎ Minta revisi││ ✓ Setujui    │ │
│ └────────────┘└────────────────┘ │
│  Setujui aktif setelah semua     │
│  fakta dikonfirmasi.             │
└──────────────────────────────────┘
```

### 3c. Detail — Desktop

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Konten / Carousel kolam & taman                      ID|EN  (!)  (S)  │
│              ├────────────────────────────────┬──────────────────────────────────────┤
│              │ ┌────────────────────────────┐ │ Instagram feed · Min 11 Okt 18.00    │
│              │ │                            │ │ WITA   [Ditinjau]  [L2]              │
│              │ │     [ Preview IG 4:5 ]     │ │                                      │
│              │ │   ‹                    ›   │ │ Caption                      Salin   │
│              │ │                            │ │ Sarapan di bale, lalu berenang       │
│              │ └────────────────────────────┘ │ sebelum siang di Villa Contoh. …     │
│              │  [1][2][3][4][5] thumbnail     │                                      │
│              │                                │ Fakta yang dipakai (5)               │
│              │  Alt text slide 1:             │  3 kamar tidur        [DATA FINAL]   │
│              │  Kolam renang Villa Contoh…    │  AC di semua kamar [CLIENT CONF.]    │
│              │                                │        [✓ Benar] [✎ Perbaiki]        │
│              │                                │ ✓ Diperiksa tim CLAU · 5 Okt 14.20   │
│              │                                │ Riwayat versi: v2 (aktif) · v1       │
│              │                                ├──────────────────────────────────────┤
│              │                                │ [✎ Minta revisi]        [✓ Setujui]  │
└──────────────┴────────────────────────────────┴──────────────────────────────────────┘
```

| Elemen | ID | EN |
|---|---|---|
| Tombol | Setujui · Minta revisi | Approve · Request changes |
| Fakta | Fakta yang dipakai · Benar · Perbaiki | Facts used · Correct · Fix |
| Helper | Setujui aktif setelah semua fakta dikonfirmasi. | Approve unlocks once all facts are confirmed. |
| Review | Diperiksa tim CLAU (manusia) | Reviewed by the CLAU team (human) |
| Sukses | Konten disetujui. Tim akan menjadwalkan tayang sesuai tanggal. | Approved. The team will schedule it for the planned date. |

**Aturan:** tombol *Setujui* **nonaktif** bila masih ada fakta `CLIENT CONFIRMATION` atau review independen belum ada (L2/L3). Tidak ada tombol *Publish* di Portal Klien.

---

## 4. Kalender / Calendar

### Mobile (tampilan agenda)

```text
┌──────────────────────────────────┐
│ ←  Kalender      [Bulan|Agenda]  │
├──────────────────────────────────┤
│ ‹      Oktober 2026      ›       │
│ S  S  R  K  J  S  M              │  ← Senin-Minggu
│          1  2  3  4              │
│ 5  6  7  8  9  10 11●            │
│ 12 13● 14 15● 16 17 18           │
│ …                                │
├──────────────────────────────────┤
│ Minggu, 11 Okt                   │
│ ┌──────────────────────────────┐ │
│ │ 18.00 WITA  [img] Carousel   │ │
│ │ IG feed · [Ditinjau] [L2]    │ │
│ └──────────────────────────────┘ │
│ Selasa, 13 Okt                   │
│ ┌──────────────────────────────┐ │
│ │ 19.00 WITA  [img] Story promo│ │
│ │ IG story · [Ditinjau]        │ │
│ └──────────────────────────────┘ │
│ ▣ Hari libur: 20 Okt — tidak ada │  ← info hari libur nasional
├──────────────────────────────────┤
│  ⌂      ▦      ▣      ▤      ◯   │
└──────────────────────────────────┘
```

### Desktop (bulan)

```text
┌──────────────┬───────────────────────────────────────────────────────────────────────┐
│ (sidebar)    │ Kalender      ‹ Oktober 2026 ›       [Bulan|Minggu|Agenda]  Filter ▾  │
│              ├─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬───────────┤
│              │ Sen     │ Sel     │ Rab     │ Kam     │ Jum     │ Sab     │ Min       │
│              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼───────────┤
│              │         │         │         │ 1       │ 2       │ 3       │ 4         │
│              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼───────────┤
│              │ 5       │ 6       │ 7       │ 8       │ 9       │ 10      │ 11        │
│              │         │         │         │         │         │         │▣ Carousel │
│              │         │         │         │         │         │         │ 18.00 L2  │
│              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼───────────┤
│              │ 12      │ 13      │ 14      │ 15      │ …       │         │           │
│              │         │▣ Story  │         │▣ Reel   │         │         │           │
└──────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴───────────┘
```

- Minggu dimulai **Senin** (kebiasaan kalender Indonesia).
- Hari libur nasional dan cuti bersama ditampilkan sebagai info (sumber: `knowledge/calendar-id`), karena memengaruhi jadwal tayang.
- Klien **hanya melihat**; pindah jadwal dilakukan lewat *Minta revisi* dengan komentar.

---

## 5. Laporan / Reports

### Mobile

```text
┌──────────────────────────────────┐
│ ←  Laporan                       │
├──────────────────────────────────┤
│ Periode  [ September 2026 ▾ ]    │
│                                  │
│ Ringkasan                        │
│ ┌──────────────────────────────┐ │
│ │ Saves naik 18% dibanding     │ │
│ │ Agustus. Carousel kolam jadi │ │
│ │ konten paling banyak disimpan│ │
│ │ (412 saves). 46 DM inquiry   │ │
│ │ tercatat.                    │ │
│ └──────────────────────────────┘ │
│ ┌─────────────┐ ┌─────────────┐  │
│ │ 12 konten   │ │ 38.420 reach│  │
│ └─────────────┘ └─────────────┘  │
│ Saves per minggu                 │
│ ┌──────────────────────────────┐ │
│ │ ▁▃▅█  (grafik batang)        │ │
│ └──────────────────────────────┘ │
│ Konten terbaik              ›    │
│ Sumber: Instagram Insights,      │
│ diambil 1 Okt 2026 08.00 WITA    │
│ ┌──────────────────────────────┐ │
│ │  ⬇  Unduh PDF                │ │
│ └──────────────────────────────┘ │
├──────────────────────────────────┤
│  ⌂      ▦      ▣      ▤      ◯   │
└──────────────────────────────────┘
```

Desktop: ringkasan di kiri (8 kolom), daftar laporan bulanan sebelumnya di kanan (4 kolom) dengan tombol unduh per bulan.

| Elemen | ID | EN |
|---|---|---|
| Tombol | Unduh PDF | Download PDF |
| Belum ada | Laporan pertama tersedia setelah 1 bulan konten tayang. | Your first report appears after one month of published content. |
| Bahasa PDF | Mengikuti bahasa UI saat diunduh; bisa dipilih ulang | Follows UI language; selectable |

---

## 6. Profil / Profile

### Mobile

```text
┌──────────────────────────────────┐
│ ←  Profil                        │
├──────────────────────────────────┤
│        (R)  Ratna Dewi           │
│             Owner · Villa Contoh │
│                                  │
│ Akun                             │
│  Nama           Ratna Dewi     › │
│  Email          ratna@… ›        │
│  Kata sandi     Ubah ›           │
│ Preferensi                       │
│  Bahasa         [ID ● | EN ○]    │
│  Sapaan         Ibu ▾            │
│  Zona waktu     WITA ▾           │
│  Tema           Terang ▾         │
│ Notifikasi                       │
│  Konten baru via WhatsApp  [●━]  │
│  Konten baru via email     [●━]  │
│  Pengingat approval        [●━]  │
│  Laporan bulanan via email [●━]  │
│ Properti saya                    │
│  Villa Contoh Ubud        Aktif  │
│                                  │
│  ⇥ Keluar                        │
├──────────────────────────────────┤
│  ⌂      ▦      ▣      ▤      ◯   │
└──────────────────────────────────┘
```

Toggle notifikasi langsung tersimpan (toast "Tersimpan"). Nama, email, dan kata sandi dibuka di layar edit tersendiri dengan tombol *Simpan*.

---

## 7. Notifikasi / Notifications

### Mobile

```text
┌──────────────────────────────────┐
│ ←  Notifikasi     Tandai dibaca  │
├──────────────────────────────────┤
│ [Semua] [Perlu tindakan 2]       │
├──────────────────────────────────┤
│ Hari ini                         │
│ ● ! Konten menunggu persetujuan  │  ← ● = belum dibaca
│     Carousel kolam & taman ·     │
│     tayang 11 Okt     10.12      │
│ ● ? 2 fakta perlu konfirmasi     │
│     Harga & syarat promo  09.40  │
│ Kemarin                          │
│   ✓ Konten tayang                │
│     Reel sarapan · lihat di IG   │
│   ▤ Laporan September siap       │
├──────────────────────────────────┤
│  ⌂      ▦      ▣      ▤      ◯   │
└──────────────────────────────────┘
```

| Jenis | ID | EN | Aksi |
|---|---|---|---|
| Approval | Konten menunggu persetujuan | Content awaiting approval | Buka detail konten |
| Fakta | {n} fakta perlu konfirmasi | {n} facts need confirmation | Buka Konfirmasi Fakta |
| Revisi selesai | Revisi siap ditinjau | Revision ready for review | Buka detail konten |
| Tayang | Konten tayang | Content published | Buka link post |
| Laporan | Laporan {bulan} siap | {Month} report ready | Buka laporan |
| Pengingat | Tayang dalam 24 jam, belum disetujui | Goes live in 24h, not yet approved | Buka detail konten |

Desktop: panel dropdown dari ikon lonceng (lebar 400 px), plus halaman penuh `Lihat semua`.

---

## Halaman Tambahan (disarankan) / Recommended Extra Screen

**Konfirmasi Fakta** (dibuka dari Beranda & notifikasi): daftar kartu fakta per properti, dikelompokkan *Harga & promo · Fasilitas · Kebijakan · Foto & izin*. Setiap kartu: pertanyaan, nilai saat ini, `[✓ Benar] [✎ Perbaiki]`. Hasilnya tercatat sebagai approval tertulis owner (nama, waktu) dan mengubah label menjadi **DATA FINAL**.

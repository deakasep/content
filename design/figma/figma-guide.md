# Figma Guide — Step-by-step

> **ID:** Langkah membuat file Figma CLAU Content Studio dari nol sampai prototype siap dites, dan cara kolaborasi dengan Pak Indra. Nama menu Figma bisa berubah antar versi; bila berbeda, cari fitur dengan nama yang sama di dokumentasi Figma. Panduan testing lanjutan ada di [prototype-guide](../prototype/prototype-guide.md).
> **EN:** Step-by-step for building the Figma file, from setup to a testable prototype, plus collaboration with Indra.

**Estimasi:** 5 hari kerja (lihat [ROADMAP](../ROADMAP.md) Fase 2).

---

## Langkah 1 — Setup File (± 1 jam)

1. Buat **Team** `CLAU` → **Project** `CLAU Content Studio`.
2. Buat file **`CLAU Content Studio — Design`** dengan halaman berikut:

| Halaman | Isi |
|---|---|
| `📘 Cover` | Nama, versi, status (`Draft / In review / Approved`), tanggal, pemilik |
| `🎨 Foundations` | Warna, tipografi, spacing, radius, shadow, ikon (preview token) |
| `🧩 Components` | 22 komponen + 5 komponen khusus CLAU ([components-list](./components-list.md)) |
| `📱 Portal — Mobile` | 7 halaman + Konfirmasi Fakta, 360 × 800 |
| `🖥 Portal — Desktop` | 7 halaman, 1280 × 800 |
| `🖥 Studio — Desktop` | 8 halaman, 1440 × 900 |
| `📱 Studio — Mobile` | 5 halaman utama, 360 × 800 |
| `▶️ Prototype` | Salinan frame yang di-link untuk flow test |
| `🗄 Archive` | Versi lama, eksplorasi yang tidak dipakai |

(Emoji di nama halaman Figma hanya penanda visual di panel kiri.)

3. Pasang font: **Plus Jakarta Sans**, **Inter**, **JetBrains Mono** (tersedia sebagai Google Fonts di Figma).
4. Pasang plugin: **Tokens Studio for Figma** (import token), **Lucide Icons** (ikon), **Stark** atau **Contrast** (cek contrast).

## Langkah 2 — Import Design Tokens (± 1–2 jam)

Sumber: [`design/tokens/tokens.json`](../tokens/tokens.json).

### Opsi A — Tokens Studio (direkomendasikan)

1. Buka plugin **Tokens Studio** → *Load from file/folder* (atau *Sync* ke repo GitHub bila memakai paket yang mendukung sync).
2. Pilih `tokens.json`. Format sudah W3C DTCG (`$value`, `$type`); bila plugin bertanya, pilih format **W3C DTCG**.
3. Buat **Themes**: `Light` = set `color` + `semantic.light` + sisanya; `Dark` = set `color` + `semantic.dark` + sisanya.
4. *Export to Figma* → **Variables** (buat collection `Primitives` dan `Semantic` dengan mode Light/Dark) dan **Styles** (text styles, effect styles untuk shadow).

### Opsi B — Manual (bila plugin tidak tersedia)

1. Panel kanan (tanpa seleksi) → **Local variables** → *Create collection*:
   - `Primitives`: semua `color.*` (satu mode).
   - `Semantic`: semua `semantic.*`, **2 mode**: Light & Dark; nilai = alias ke Primitives.
   - `Space` & `Radius`: number variables.
2. Text styles: `Display`, `H2`…`H6`, `Body`, `Small`, `Tiny`, masing-masing varian `Mobile` & `Desktop` (nilai di [tokens.md](../tokens/tokens.md) §3).
3. Effect styles: `Shadow/sm`, `Shadow/md`, `Shadow/lg`.

### Aturan setelah import

- Komponen **hanya** memakai variables `Semantic` untuk warna (bukan `Primitives` dan bukan hex manual). Dengan begitu, mengganti mode Light → Dark pada frame langsung mengubah semuanya.
- Spacing di auto layout memakai variable `Space`.
- Cek: pilih frame → panel kanan → *Selection colors*. Tidak boleh ada hex yang bukan variable.

## Langkah 3 — Component Library (± 2 hari)

Urutan pembuatan (komponen dasar dulu, karena dipakai komponen lain):

```text
 1 Icon wrapper ─► 2 Button ─► 3 Badge ─► 4 Input/Textarea/Select ─► 5 Checkbox/Radio/Toggle
 ─► 6 Avatar ─► 7 Card ─► 8 Tabs/Breadcrumb/Pagination ─► 9 Table ─► 10 Toast/Tooltip
 ─► 11 Modal/Bottom sheet ─► 12 Navigation (bottom nav, rail, sidebar, top bar) ─► 13 States
 ─► 14 Komponen CLAU (Evidence Badge, Fact Confirm Row, Content Preview, Approval Bar, Agent Pill)
```

Aturan untuk setiap komponen:

| Aturan | Detail |
|---|---|
| Nama | `Kategori/Nama`, mis. `Button`, `Form/Input`, `CLAU/Evidence Badge` |
| Variant properties | `Type`, `Size`, `State` (Default/Hover/Focus/Pressed/Disabled/Loading), plus boolean `Icon left`, `Icon right` |
| Auto layout | Wajib; padding & gap memakai variable `Space` |
| Text | Memakai text style; teks contoh **Bahasa Indonesia** terpanjang (mis. "Kirim link masuk ke email") untuk menguji ruang |
| Area sentuh | Layer transparan 44 × 44 bila komponen visual lebih kecil |
| Deskripsi | Isi kolom *Description* komponen: kapan dipakai + link ke [components.md](../design-system/components.md) |
| Publish | Setelah stabil: *Assets → Publish library* (butuh paket berbayar untuk library tim; di paket gratis, komponen tetap bisa dipakai di file yang sama) |

## Langkah 4 — Layar (± 1,5 hari)

1. Buat frame dari [wireframe Portal](../wireframes/client-portal-wireframe.md) dan [wireframe Studio](../wireframes/dashboard-wireframe.md), **mobile dulu**.
2. Layout grid: mobile 4 kolom/16 px gutter, tablet 8/24, desktop 12/24 (sesuai [spacing.md](../design-system/spacing.md)).
3. Isi data contoh dari properti **fiktif** (`Villa Contoh Ubud`, `Cafe Senja`, dst.). **Jangan** memakai nama, foto, harga, atau caption client nyata.
4. Setiap layar dibuat dalam 4 state bila relevan: **isi**, **kosong**, **loading**, **error**.
5. Duplikat layar kunci (Login, Beranda, Detail Konten) ke versi **English** untuk menguji panjang teks.
6. Duplikat 3 layar ke mode **Dark** (ganti mode variable di frame) untuk cek visual.

## Langkah 5 — Prototype (± 1 hari)

Detail interaksi ada di [prototype-guide §1.2–1.3](../prototype/prototype-guide.md). Ringkasnya:

| Flow | Frame awal | Jalur |
|---|---|---|
| `F1 Approve` (prioritas) | Notifikasi WA | → Detail → Konfirmasi fakta → Setujui → Sukses |
| `F2 Kalender` | Beranda | → Kalender → item → Detail |
| `F3 Laporan` | Notifikasi laporan | → Laporan → Unduh PDF |
| `F4 Profil` | Beranda | → Profil → Bahasa EN |
| `F5 Reset` | Login | → Lupa kata sandi → Email → Kata sandi baru → Login |
| `S1 Pipeline` (Studio) | Ringkasan | → Konten → Review QA → Tugaskan reviewer → Tandai tayang |

Test di HP: aplikasi Figma (mirror) di **Android 360 px**. Catat link di [prototype-link.md](./prototype-link.md).

## Langkah 6 — Kolaborasi dengan Pak Indra / Collaborating with Indra

| Kebutuhan | Cara |
|---|---|
| **Akses** | *Share* → email Pak Indra → **can view** (paket gratis: viewer & commenter tidak dihitung sebagai editor berbayar). Bila Pak Indra perlu mengedit, beri *can edit* (cek batas editor di paket) |
| **Review terjadwal** | Setiap akhir fase (lihat ROADMAP): kirim **link ke halaman/frame spesifik** + 3 pertanyaan yang perlu diputuskan, bukan "tolong dicek semua" |
| **Komentar** | Tekan `C` → klik di frame → tulis, `@Indra` untuk mention. Satu komentar = satu masalah. Tandai *Resolve* setelah diperbaiki |
| **Keputusan** | Keputusan dari komentar dicatat di halaman `📘 Cover` (tabel *Decision log*: tanggal, keputusan, oleh siapa) dan di repo bila memengaruhi spec |
| **Versi** | *File → Save to version history* dengan nama `v0.2 — Components done`, `v0.3 — Prototype F1`, dst. Pak Indra bisa membandingkan versi |
| **Status frame** | Beri label di atas frame: `🟡 WIP`, `🔵 Ready for review`, `🟢 Approved`. Fitur *Dev Mode → Ready for dev* bisa dipakai bila tersedia di paket |
| **Branching** | Fitur branch Figma butuh paket berbayar. Tanpa itu: duplikat halaman ke `🗄 Archive` sebelum perubahan besar |
| **Sinkron ke repo** | Perubahan token dibuat di `tokens.json` (repo), lalu di-import ulang ke Figma. Jangan mengubah warna di Figma saja |

## Checklist Selesai Fase Figma

- [ ] Semua warna memakai variables Semantic; mode Light/Dark berfungsi.
- [ ] 27 komponen (22 + 5 CLAU) dengan variant & state lengkap.
- [ ] Portal mobile 8 layar + desktop 7 layar; Studio desktop 8 + mobile 5.
- [ ] State kosong/loading/error untuk layar utama.
- [ ] 3 layar versi English, 3 layar versi Dark.
- [ ] Contrast dicek dengan plugin (teks ≥ 4.5:1, komponen ≥ 3:1).
- [ ] Tidak ada data client nyata.
- [ ] Review Pak Indra selesai; keputusan tercatat.

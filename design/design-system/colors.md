# Colors — Palet & Token Warna

> **ID:** Palet hangat bernuansa hospitality: **Teal Laut** (primary) dan **Terracotta** (accent) di atas netral **Stone** yang sedikit hangat. Semua angka contrast ratio di file ini **dihitung** dengan rumus WCAG 2.x (relative luminance), bukan perkiraan.
> **EN:** A warm hospitality palette: **Sea Teal** (primary) and **Terracotta** (accent) on warm **Stone** neutrals. Every contrast ratio below is **calculated** with the WCAG 2.x relative-luminance formula.

## Kenapa bukan contoh di brief / Why not the brief's example colors

Brief memberi contoh `#10B981` (emerald) sebagai primary, plus `#3B82F6`, `#F59E0B`, `#EF4444`. Warna-warna itu tidak dipakai sebagai warna teks/tombol karena:

| Warna contoh | Teks di atas putih | Masalah |
|---|---|---|
| `#10B981` emerald | **2.54 : 1** | Gagal AA (butuh 4.5:1). Tombol putih-di-emerald juga 2.54:1 |
| `#3B82F6` blue | 3.68 : 1 | Gagal AA untuk teks normal |
| `#F59E0B` amber | 2.15 : 1 | Gagal AA |
| `#EF4444` red | 3.76 : 1 | Gagal AA untuk teks normal |
| Primary = Success (sama-sama `#10B981`) | — | User tidak bisa membedakan "tombol utama" dan "status berhasil" |

Hue-nya dipertahankan (hijau, biru, kuning, merah) untuk semantic, tapi memakai shade yang lulus AA. Primary dipindah ke teal supaya tidak bentrok dengan success.

## 1. Primary — Teal Laut / Sea Teal

Laut dan sawah: dua lanskap yang ada di hampir semua destinasi Indonesia. Dipakai untuk aksi utama, link, fokus, dan navigasi aktif.

| Token | HEX | Pakai untuk |
|---|---|---|
| `primary-50` | `#F0FDFA` | Background baris terpilih, highlight lembut |
| `primary-100` | `#CCFBF1` | Background badge/chip primary |
| `primary-200` | `#99F6E4` | Border elemen terpilih (dekoratif) |
| `primary-300` | `#5EEAD4` | Dark mode: link hover |
| `primary-400` | `#2DD4BF` | **Dark mode: primary** |
| `primary-500` | `#14B8A6` | Ilustrasi, grafik (bukan teks) |
| **`primary-600`** | **`#0F766E`** | **Light mode: tombol primary, link, focus ring** |
| `primary-700` | `#115E59` | Hover/pressed tombol primary |
| `primary-800` | `#134E4A` | Teks di atas `primary-100` |
| `primary-900` | `#042F2E` | Header gelap (opsional) |

> Catatan: `primary-600` sengaja lebih gelap dari skala teal Tailwind standar (`#0D9488`), supaya teks putih di atasnya lulus AA (5.47:1).

## 2. Accent — Terracotta

Genteng, gerabah, dan senja: sentuhan hangat yang dipakai **hemat**. Untuk highlight promo, badge "Baru", dan ilustrasi. **Bukan** untuk tombol utama, supaya tidak bersaing dengan primary.

| Token | HEX | Pakai untuk |
|---|---|---|
| `accent-50` | `#FFF7ED` | Background banner promo |
| `accent-100` | `#FFEDD5` | Background badge accent |
| `accent-400` | `#FB923C` | **Dark mode: accent** |
| **`accent-600`** | **`#C2410C`** | **Light mode: teks/ikon accent, badge "Baru"** |
| `accent-700` | `#9A3412` | Teks di atas `accent-50` |

## 3. Neutral — Stone (hangat / warm gray)

Abu-abu dengan sedikit warna cokelat. Terasa lebih ramah daripada abu-abu biru yang dingin.

| Token | HEX | Light mode | Dark mode |
|---|---|---|---|
| `neutral-0` | `#FFFFFF` | Surface (kartu, modal) | — |
| `neutral-50` | `#FAFAF9` | **Background halaman** | Teks utama (alt) |
| `neutral-100` | `#F5F5F4` | Background input disabled, hover baris | **Teks utama** (`#F5F5F4`) |
| `neutral-200` | `#E7E5E4` | **Border dekoratif** (kartu, divider) | — |
| `neutral-300` | `#D6D3D1` | Skeleton | — |
| `neutral-400` | `#A8A29E` | Ikon non-esensial (dekoratif) | **Teks sekunder** |
| `neutral-500` | `#78716C` | **Teks sekunder/meta, border input**, placeholder | Border input (`#8A847F`) |
| `neutral-600` | `#57534E` | — | Border dekoratif |
| `neutral-700` | `#44403C` | **Teks body** | Border/divider |
| `neutral-800` | `#292524` | — | Surface elevated |
| `neutral-850` | `#1F1C19` | — | **Surface** (kartu) |
| `neutral-900` | `#1C1917` | **Teks heading** | — |
| `neutral-950` | `#141210` | — | **Background halaman** |

## 4. Semantic

Selalu pakai **warna + ikon + teks**. Warna saja tidak cukup (WCAG 1.4.1, dan ±8% pria punya buta warna merah-hijau).

| Peran | Teks/ikon (light) | Background tint | Teks di atas tint | Dark mode | Ikon (Lucide) |
|---|---|---|---|---|---|
| **Success** / Berhasil | `#15803D` | `#F0FDF4` | `#166534` | `#4ADE80` | `circle-check` |
| **Warning** / Perhatian | `#B45309` | `#FFFBEB` | `#92400E` | `#FBBF24` | `triangle-alert` |
| **Error** / Gagal | `#B91C1C` (teks), `#DC2626` (fill tombol danger) | `#FEF2F2` | `#991B1B` | `#F87171` | `circle-x` |
| **Info** | `#1D4ED8` | `#EFF6FF` | `#1E40AF` | `#60A5FA` | `info` |

## 5. Label Evidence CLAU

Enam label canonical tampil sebagai badge. Teks label **tidak diterjemahkan**.

| Label | Arti singkat (ID / EN) | Warna (light: tint + teks) | Ikon |
|---|---|---|---|
| `DATA FINAL` | Fakta terverifikasi / Verified fact | Success: `#F0FDF4` + `#166534` | `badge-check` |
| `CLIENT CONFIRMATION` | Menunggu konfirmasi client / Awaiting client | Warning: `#FFFBEB` + `#92400E` | `message-circle-question` |
| `FIELD VERIFICATION` | Perlu cek lapangan / Needs site check | Info: `#EFF6FF` + `#1E40AF` | `map-pin` |
| `ASSUMPTION` | Asumsi / Assumption | Neutral: `#F5F5F4` + `#44403C` | `circle-dashed` |
| `RISK` | Risiko / Risk | Error: `#FEF2F2` + `#991B1B` | `shield-alert` |
| `NEXT ACTION` | Tindakan berikut / Next action | Primary: `#CCFBF1` + `#115E59` | `circle-arrow-right` |

## 6. Status Konten / Content Status

| Status | ID / EN | Warna | Ikon |
|---|---|---|---|
| Draft | Draf / Draft | Neutral | `file-pen` |
| In Review | Ditinjau / In review | Info | `eye` |
| Needs Changes | Perlu revisi / Changes requested | Warning | `pencil-line` |
| Approved | Disetujui / Approved | Success | `circle-check` |
| Scheduled | Terjadwal / Scheduled | Primary | `calendar-clock` |
| Published | Tayang / Published | Success (solid) | `send` |
| Rejected | Ditolak / Rejected | Error | `circle-x` |

## 7. Contrast Ratio (dihitung / calculated)

### Light mode

| Pasangan | Ratio | WCAG |
|---|---|---|
| `neutral-900` `#1C1917` di atas putih | 17.49 | AAA |
| `neutral-700` `#44403C` (body) di atas putih | 10.27 | AAA |
| `neutral-500` `#78716C` (meta) di atas putih | 4.80 | AA |
| `neutral-500` di atas `neutral-50` (bg halaman) | 4.59 | AA |
| `neutral-400` `#A8A29E` di atas putih | 2.52 | ❌ hanya dekoratif, **jangan untuk teks** |
| Putih di atas `primary-600` `#0F766E` (tombol) | 5.47 | AA |
| Putih di atas `primary-700` (hover) | 7.58 | AAA |
| `primary-600` (link) di atas `neutral-50` | 5.24 | AA |
| `primary-700` di atas `primary-100` (badge) | 6.73 | AA |
| Putih di atas `accent-600` `#C2410C` | 5.18 | AA |
| `accent-700` di atas `accent-50` | 6.88 | AA |
| Success `#15803D` / Warning `#B45309` di atas putih | 5.02 / 5.02 | AA |
| Error `#B91C1C` / Info `#1D4ED8` di atas putih | 6.47 / 6.70 | AA |
| Putih di atas error fill `#DC2626` (tombol danger) | 4.83 | AA |
| Teks tint semantic (800 di atas 50) | 6.81 – 8.01 | AA |
| **Border input** `#78716C` di atas putih | 4.80 | ✅ ≥ 3:1 (WCAG 1.4.11) |
| Border dekoratif `#E7E5E4` | — | Tidak wajib 3:1 karena tidak membawa informasi |

### Dark mode

| Pasangan | Ratio | WCAG |
|---|---|---|
| Teks `#F5F5F4` di atas bg `#141210` | 17.13 | AAA |
| Teks sekunder `#A8A29E` di atas surface `#1F1C19` | 6.72 | AA |
| Primary `#2DD4BF` di atas surface `#1F1C19` | 9.11 | AAA |
| Teks `#141210` di atas tombol `#2DD4BF` | 10.04 | AAA |
| Accent `#FB923C` di atas surface | 7.49 | AAA |
| Success / Warning / Error / Info di atas surface | 9.73 / 10.16 / 6.13 / 6.67 | AA+ |
| Border input `#8A847F` di atas surface | 4.59 | ✅ ≥ 3:1 |

## 8. Aturan Pakai / Usage Guidelines

| Kapan | Pakai | Jangan |
|---|---|---|
| Aksi utama di satu layar (Setujui, Simpan, Masuk) | `primary-600` solid, **maks 1 per layar** | Dua tombol primary berdampingan |
| Aksi kedua (Batal, Lihat detail) | Secondary: outline `neutral-500`, teks `neutral-900` | Accent untuk aksi kedua |
| Promo, "Baru", sorotan musim | `accent` hemat (badge, ikon, garis) | Accent sebagai background besar |
| Status & feedback | Semantic + ikon + teks | Hijau untuk dekorasi (nanti dikira "berhasil") |
| Aksi berbahaya (Hapus, Tolak konten) | `error` fill + dialog konfirmasi | Merah untuk tombol biasa |
| Teks | `neutral-900` heading, `neutral-700` body, `neutral-500` meta | `neutral-400` untuk teks apa pun |
| Grafik (chart) | Urutan seri: `primary-500`, `accent-400` (`#FB923C`), `#6366F1`, `#EAB308`, `neutral-400`; selalu ada label/legend | Membedakan seri hanya dari warna |

## 9. Theme

- **Light mode = default.** Mayoritas pemakaian di siang hari dan di luar ruangan (resepsionis, lobi, lapangan).
- **Dark mode = opsional**, ikut setting sistem (`prefers-color-scheme`) dan bisa dipaksa dari Profil (`Terang / Gelap / Ikuti sistem`).
- Foto properti **tidak** diberi filter di dark mode. Kartu foto di dark mode memakai border `neutral-700` agar tepi foto terlihat.

## 10. Token (CSS variables)

```css
:root {
  --color-bg: #FAFAF9;          --color-surface: #FFFFFF;
  --color-text: #1C1917;        --color-text-body: #44403C;   --color-text-muted: #78716C;
  --color-border: #E7E5E4;      --color-border-input: #78716C;
  --color-primary: #0F766E;     --color-primary-hover: #115E59; --color-on-primary: #FFFFFF;
  --color-primary-subtle: #CCFBF1;
  --color-accent: #C2410C;      --color-accent-subtle: #FFF7ED;
  --color-success: #15803D;     --color-success-subtle: #F0FDF4;
  --color-warning: #B45309;     --color-warning-subtle: #FFFBEB;
  --color-error: #B91C1C;       --color-error-fill: #DC2626;   --color-error-subtle: #FEF2F2;
  --color-info: #1D4ED8;        --color-info-subtle: #EFF6FF;
  --color-focus: #0F766E;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --color-bg: #141210;        --color-surface: #1F1C19;
    --color-text: #F5F5F4;      --color-text-body: #E7E5E4;   --color-text-muted: #A8A29E;
    --color-border: #44403C;    --color-border-input: #8A847F;
    --color-primary: #2DD4BF;   --color-primary-hover: #5EEAD4; --color-on-primary: #141210;
    --color-accent: #FB923C;
    --color-success: #4ADE80;   --color-warning: #FBBF24;     --color-error: #F87171;  --color-info: #60A5FA;
    --color-focus: #2DD4BF;
  }
}
:root[data-theme="dark"] { /* nilai sama dengan blok dark di atas */ }
```

Nilai resmi ada di [`tokens/tokens.json`](../tokens/tokens.json); CSS di atas hanya ringkasan. Untuk kode, pakai file generated [`tokens/tokens.css`](../tokens/tokens.css).

# Spacing & Layout — Jarak, Grid, Breakpoint

> **ID:** Basis **8 px**, dengan langkah 4 px dan 12 px untuk detail kecil. Semua jarak memakai token, tidak ada angka acak seperti 13 px atau 22 px.
> **EN:** **8 px** base with 4 px and 12 px half-steps for fine detail. Every gap uses a token, never arbitrary values.

## 1. Skala / Scale

| Token | px | rem | Pakai untuk |
|---|---|---|---|
| `space-1` | 4 | 0.25 | Jarak ikon ↔ teks di badge, gap antar-chip rapat |
| `space-2` | 8 | 0.5 | Ikon ↔ label tombol, padding badge vertikal |
| `space-3` | 12 | 0.75 | Padding input vertikal, gap item list rapat |
| `space-4` | 16 | 1 | **Gutter mobile**, padding kartu mobile, gap form field |
| `space-6` | 24 | 1.5 | Padding kartu desktop, gap antar-kartu |
| `space-8` | 32 | 2 | Jarak antar-section dalam halaman |
| `space-12` | 48 | 3 | **Section padding mobile** |
| `space-16` | 64 | 4 | Jarak blok besar desktop |
| `space-24` | 96 | 6 | **Section padding desktop** (halaman login/landing) |

Nama token mengikuti kelipatan 4 px (`space-N` = N × 4 px), jadi nilai di luar skala ini (mis. `space-5` = 20 px) boleh ditambah tanpa mengganti nama yang sudah ada.

## 2. Breakpoint

| Nama | Lebar | Device acuan | Navigasi |
|---|---|---|---|
| `xs` (baseline) | 360–599 | HP Android mayoritas (360 × 800) | **Bottom navigation** 4–5 item |
| `sm` | 600–767 | HP besar, landscape | Bottom navigation |
| `md` | 768–1023 | Tablet | **Rail** kiri (ikon + label kecil, 80 px) |
| `lg` | 1024–1439 | Laptop | **Sidebar** 256 px (bisa dilipat ke 72 px) |
| `xl` | ≥ 1440 | Desktop lebar | Sidebar 256 px, konten max 1440 |

Desain dimulai dari **360 px**. Layout diuji di 320 px (HP kecil) dan harus tetap terbaca tanpa horizontal scroll.

## 3. Grid

| Breakpoint | Kolom | Gutter (antar kolom) | Margin samping |
|---|---|---|---|
| Mobile (< 768) | **4** | 16 px | 16 px |
| Tablet (768–1023) | **8** | 24 px | 24 px |
| Desktop (≥ 1024) | **12** | 24 px | 32 px |

Contoh pemakaian kolom:

```text
Desktop 12 kolom — Beranda Portal Klien
┌──────────────────────────────── 12 ────────────────────────────────┐
│ ┌──────── 8: Menunggu persetujuan ───────┐ ┌──── 4: Kalender ────┐ │
│ │                                        │ │                     │ │
│ └────────────────────────────────────────┘ └─────────────────────┘ │
│ ┌─ 4: Stat ─┐ ┌─ 4: Stat ─┐ ┌─ 4: Stat ─┐                          │
└────────────────────────────────────────────────────────────────────┘

Mobile 4 kolom — semua kartu 4/4 (full width), ditumpuk vertikal
┌──── 4 ────┐
│ Menunggu  │
├───────────┤
│ Stat│Stat │  ← kartu statistik kecil boleh 2/4
├───────────┤
│ Kalender  │
└───────────┘
```

## 4. Container

| Konteks | Lebar maks |
|---|---|
| Mobile | `100% − 32px` (gutter 16 px kiri-kanan) |
| Tablet | `720px` |
| Desktop | `1200px` (area konten di samping sidebar) |
| Wide | `1440px` (tabel lebar, kalender bulan di Studio) |
| Teks panjang (laporan, detail konten) | `68ch` di dalam container |
| Form (login, profil) | `440px` |

## 5. Section Padding

| | Mobile | Desktop |
|---|---|---|
| Halaman login / landing | 48 px atas-bawah | 96 px |
| Halaman aplikasi (setelah login) | 16 px atas, 24 px antar-section | 32 px atas, 32 px antar-section |
| Kartu | 16 px | 24 px |
| Modal | 20 px (mobile full-screen sheet) | 24–32 px |

## 6. Ukuran Elemen Tetap / Fixed Sizes

| Elemen | Ukuran |
|---|---|
| Target sentuh minimum | **44 × 44 px** (termasuk ikon tombol, checkbox, link di tabel) |
| Tinggi tombol | 40 px (sm), **44 px (md, default)**, 52 px (lg, CTA mobile) |
| Tinggi input | 44 px |
| Top bar | 56 px (mobile), 64 px (desktop) |
| Bottom navigation | 64 px + `env(safe-area-inset-bottom)` |
| Sidebar | 256 px (buka), 72 px (lipat) |
| Avatar | 24 / 32 / 40 / 56 px |

## 7. Radius, Shadow, Z-index

| Token | Nilai | Pakai untuk |
|---|---|---|
| `radius-sm` | 6 px | Badge, chip, checkbox |
| `radius-md` | 8 px | Tombol, input |
| `radius-lg` | 12 px | **Kartu**, dropdown |
| `radius-xl` | 16 px | Modal, bottom sheet (sudut atas) |
| `radius-full` | 9999 px | Avatar, pill, toggle |
| `shadow-sm` | `0 1px 2px rgba(28,25,23,.06)` | Kartu default |
| `shadow-md` | `0 4px 12px rgba(28,25,23,.08)` | Kartu hover, dropdown |
| `shadow-lg` | `0 12px 32px rgba(28,25,23,.12)` | Modal, toast |
| `z-dropdown` / `z-sticky` / `z-modal` / `z-toast` | 10 / 20 / 40 / 50 | Urutan tumpukan |

Di dark mode, shadow hampir tidak terlihat. Elevasi ditunjukkan dengan surface yang lebih terang (`neutral-850` → `neutral-800`) dan border `neutral-700`.

## 8. Token (CSS)

```css
:root {
  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem; --space-4: 1rem;
  --space-6: 1.5rem;  --space-8: 2rem;   --space-12: 3rem;   --space-16: 4rem; --space-24: 6rem;
  --radius-sm: 6px; --radius-md: 8px; --radius-lg: 12px; --radius-xl: 16px; --radius-full: 9999px;
  --container-tablet: 720px; --container-desktop: 1200px; --container-wide: 1440px;
  --tap-min: 44px;
}
```

# Typography — Tipografi

> **ID:** Heading memakai **Plus Jakarta Sans**, typeface open-source karya foundry Indonesia (Tokotype), yang awalnya dibuat untuk identitas kota Jakarta. Body memakai **Inter** karena sangat terbaca di layar kecil. Keduanya gratis (SIL Open Font License) dan mendukung semua huruf Bahasa Indonesia serta Eropa Barat.
> **EN:** Headings use **Plus Jakarta Sans**, an open-source typeface by Indonesian foundry Tokotype, originally made for Jakarta's city identity. Body text uses **Inter** for small-screen legibility. Both are free (SIL OFL).

## 1. Font Family

| Peran | Font | Fallback | Kenapa |
|---|---|---|---|
| **Heading** | Plus Jakarta Sans | `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` | Sentuhan lokal, geometris tapi hangat, tetap profesional |
| **Body / UI** | Inter | `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` | x-height tinggi, angka jelas untuk harga & tanggal, tabular figures |
| **Mono** | JetBrains Mono | `ui-monospace, "SFMono-Regular", Menlo, monospace` | ID konten, hash, kode API di Settings |

**Pemuatan / Loading (performa):**

- Self-host file `woff2` (jangan bergantung CDN pihak ketiga untuk aplikasi utama).
- Subset `latin` + `latin-ext` saja. Bahasa Indonesia tidak butuh glyph khusus.
- Muat 2 weight untuk Plus Jakarta Sans (600, 700) dan variable font Inter (400–600). Target total font ≤ 120 KB.
- `font-display: swap` + `preload` untuk Inter 400. Heading boleh muncul sedikit terlambat; body tidak.

## 2. Skala Ukuran / Type Scale

Skala desktop mengikuti brief. Di mobile, heading besar **dikecilkan** supaya judul tidak pecah menjadi 4–5 baris di layar 360 px (kata Indonesia cenderung panjang, mis. "Persetujuan", "Pemberitahuan").

| Token | Desktop (≥ 1024) | Mobile (< 768) | Line height | Weight | Pakai untuk |
|---|---|---|---|---|---|
| `display` / H1 | 48px / 3rem | 32px / 2rem | 1.2 | 700 | Judul login, hero laporan |
| `h2` | 36px / 2.25rem | 28px / 1.75rem | 1.2 | 700 | Judul halaman |
| `h3` | 30px / 1.875rem | 24px / 1.5rem | 1.2 | 600 | Judul section besar |
| `h4` | 24px / 1.5rem | 20px / 1.25rem | 1.25 | 600 | Judul kartu besar, angka statistik |
| `h5` | 20px / 1.25rem | 18px / 1.125rem | 1.3 | 600 | Judul kartu, modal |
| `h6` | 18px / 1.125rem | 16px / 1rem | 1.35 | 600 | Sub-judul, label grup |
| `body` | 16px / 1rem | 16px / 1rem | 1.5 | 400 | Teks utama, caption konten |
| `small` | 14px / 0.875rem | 14px / 0.875rem | 1.4 | 400 / 500 | Meta, tabel, helper text |
| `tiny` | 12px / 0.75rem | 12px / 0.75rem | 1.4 | 500 | Badge, timestamp, label evidence |

Tablet (768–1023) memakai nilai tengah, atau fluid: `clamp(2rem, 1.2rem + 2.5vw, 3rem)` untuk H1.

**Aturan:** body tidak pernah di bawah 16 px di mobile. Ini juga mencegah iOS melakukan zoom otomatis saat input difokuskan.

## 3. Weight

| Token | Nilai | Pakai untuk |
|---|---|---|
| `regular` | 400 | Body, paragraf |
| `medium` | 500 | Label form, tombol kecil, teks tabel penting, badge |
| `semibold` | 600 | Tombol, judul kartu, H3–H6, navigasi aktif |
| `bold` | 700 | H1–H2, angka statistik besar |

Hindari 300 (light) dan 800+ (extra bold). Light terlalu tipis di layar HP murah dengan kepadatan piksel rendah.

## 4. Line Height & Paragraf

| Konteks | Line height | Lebar baris maks |
|---|---|---|
| Heading | 1.2 | 20–30 karakter per baris di mobile wajar |
| Body | 1.5 | **65–75 karakter** (`max-width: 68ch`) |
| Small / tabel | 1.4 | — |
| Caption konten (preview IG) | 1.5, `white-space: pre-wrap` | Ikuti lebar kartu; jaga line break asli caption |

Jarak paragraf = `0.75em`. Jarak heading ke konten di bawahnya **lebih kecil** daripada jarak ke konten di atasnya (heading "menempel" ke isinya).

## 5. Angka, Harga, Tanggal / Numbers & Dates

- Inter dengan `font-variant-numeric: tabular-nums` untuk tabel, statistik, dan harga, supaya angka sejajar.
- Format via `Intl` sesuai locale, jangan string manual:

| Data | `id-ID` | `en-GB` / `en-US` |
|---|---|---|
| Uang | `Rp1.250.000` | `IDR 1,250,000` |
| Persen | `15%` | `15%` |
| Tanggal pendek | `6 Okt 2026` | `6 Oct 2026` |
| Tanggal + hari | `Selasa, 6 Okt 2026` | `Tue, 6 Oct 2026` |
| Jam | `18.00 WITA` | `6:00 PM WITA` |
| Relatif | `2 jam lalu` | `2 hours ago` |

Catatan uang: `Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 })` menghasilkan `Rp 1.250.000` (dengan spasi tak terputus). Hapus spasi itu supaya sesuai EYD (`Rp1.250.000`). Buat helper `formatRupiah()` satu kali dan pakai di semua tempat.

Zona waktu (WIB/WITA/WIT) **selalu ditulis** di jadwal publish, karena klien dan agency bisa berada di zona berbeda.

## 6. Aturan Bilingual / Bilingual Rules

| Aturan | Alasan |
|---|---|
| Rancang layout untuk teks **±30% lebih panjang** dari versi terpendek | Teks Indonesia sering lebih panjang ("Simpan perubahan" vs "Save"). Tombol tidak boleh memotong teks |
| Tidak ada teks di dalam gambar/ikon | Supaya bisa diterjemahkan dan dibaca screen reader |
| Satu layar = satu bahasa UI | Tidak mencampur "Approve" dan "Setujui" di layar yang sama |
| **Konten klien tampil apa adanya** | Caption bilingual (ID + EN) tetap ditampilkan utuh, terlepas dari bahasa UI |
| Atribut `lang` di setiap blok | `<html lang="id">`, blok caption EN memakai `lang="en"`. Screen reader membaca dengan pelafalan yang benar |
| Hindari ALL CAPS untuk kalimat | Sulit dibaca. Pengecualian: label evidence (`DATA FINAL`) yang memang kode tetap |
| Ejaan EYD V | "Tayang", "Disetujui", "Pemberitahuan"; tidak memakai singkatan gaul di UI |

## 7. Contoh Hierarki / Hierarchy Example

```text
Selamat sore, Bu Ratna 👋                      ← h2 / 28px mobile, 700, Plus Jakarta Sans
Oktober 2026 · 3 konten menunggu Ibu         ← small / 14px, 400, neutral-500

┌─ Menunggu persetujuan ────────────────┐     ← h6 / 16px, 600
│ Carousel: Kolam & taman               │     ← body / 16px, 500, neutral-900
│ Instagram · Tayang Min, 11 Okt 18.00  │     ← small / 14px, neutral-500, tabular-nums
│ [L2] [2 fakta perlu konfirmasi]       │     ← tiny / 12px, 500 (badge)
└───────────────────────────────────────┘
```

## 8. Token (CSS)

```css
:root {
  --font-heading: "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-body: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;

  --text-display: clamp(2rem, 1.2rem + 2.5vw, 3rem);
  --text-h2: clamp(1.75rem, 1.3rem + 1.4vw, 2.25rem);
  --text-h3: clamp(1.5rem, 1.2rem + 0.9vw, 1.875rem);
  --text-h4: clamp(1.25rem, 1.1rem + 0.5vw, 1.5rem);
  --text-h5: clamp(1.125rem, 1.05rem + 0.25vw, 1.25rem);
  --text-h6: clamp(1rem, 0.95rem + 0.2vw, 1.125rem);
  --text-body: 1rem;  --text-small: 0.875rem;  --text-tiny: 0.75rem;

  --leading-tight: 1.2;  --leading-body: 1.5;  --leading-small: 1.4;
  --weight-regular: 400; --weight-medium: 500; --weight-semibold: 600; --weight-bold: 700;
}
```

# Design Tokens

> **ID:** Token adalah nilai desain bernama (warna, font, jarak, radius, bayangan, durasi) yang dipakai **sama persis** di Figma dan di kode. `tokens.json` adalah satu-satunya sumber kebenaran; file lain di-generate darinya.
> **EN:** Tokens are named design values shared by Figma and code. `tokens.json` is the single source of truth; everything else is generated from it.

## 1. File

| File | Isi | Diedit manual? |
|---|---|---|
| [`tokens.json`](./tokens.json) | Semua token, format [W3C Design Tokens](https://www.designtokens.org/) (`$value`, `$type`), dibaca Tokens Studio / Style Dictionary | ✅ **Ya, hanya file ini** |
| [`build_tokens.py`](./build_tokens.py) | Generator + pengecek contrast WCAG (Python stdlib) | Saat menambah jenis token |
| [`tokens.css`](./tokens.css) | CSS variables (light default, dark via `prefers-color-scheme` / `data-theme`, reduced motion) | ❌ Generated |
| [`tailwind.config.js`](./tailwind.config.js) | Theme Tailwind yang menunjuk ke CSS variables | ❌ Generated |

```bash
python design/tokens/build_tokens.py          # generate tokens.css + tailwind.config.js, cek contrast
python design/tokens/build_tokens.py --check  # CI: gagal bila file generated basi atau contrast < AA
```

Hasil saat ditulis: **PASS — 46 pasangan contrast memenuhi WCAG AA (light + dark).**

## 2. Tiga Lapis Token / Three Tiers

```text
 Primitive (palet)          Semantic (peran)              Komponen (pemakaian)
 color.primary.600  ───►  semantic.light.primary  ───►  Button primary background
 #0F766E                   = {color.primary.600}         var(--color-primary)
                           semantic.dark.primary
                           = {color.primary.400}
```

| Lapis | Contoh | Aturan |
|---|---|---|
| **Primitive** | `color.neutral.500`, `spacing.4`, `radius.lg` | Nilai mentah. Komponen **tidak** memakai warna primitive langsung |
| **Semantic** | `semantic.light.text-muted`, `semantic.dark.surface` | Peran warna; berganti otomatis di dark mode |
| **Komponen** | (di kode) `.btn-primary { background: var(--color-primary) }` | Memakai semantic + spacing/radius/shadow |

## 3. Daftar Token / Token Reference

### Warna primitive

| Grup | Step | Catatan |
|---|---|---|
| `color.primary` (Teal Laut) | 50–900 | `600` = primary light, `400` = primary dark |
| `color.secondary` (Terracotta) | 50, 100, 400, 600, 700 | Accent hemat; **bukan** tombol utama |
| `color.neutral` (Stone) | 0, 50–950 (+ `550`) | `550` khusus border input dark mode |
| `color.success/warning/error/info` | 50, (200), 400, (600), 700, 800 | 700 = teks di light, 400 = di dark, 50/800 = tint badge |
| `color.chart` | 1–5 | Urutan seri grafik |

### Warna semantic (light → dark)

| Token | Light | Dark | Dipakai untuk |
|---|---|---|---|
| `bg` | `#FAFAF9` | `#141210` | Background halaman |
| `surface` / `surface-raised` | `#FFFFFF` / `#FFFFFF` | `#1F1C19` / `#292524` | Kartu, modal / dropdown, elevated |
| `text` / `text-body` / `text-muted` | `#1C1917` / `#44403C` / `#78716C` | `#F5F5F4` / `#E7E5E4` / `#A8A29E` | Heading / body / meta |
| `border` / `border-input` | `#E7E5E4` / `#78716C` | `#44403C` / `#8A847F` | Dekoratif / input (≥ 3:1) |
| `primary` / `primary-hover` / `on-primary` | `#0F766E` / `#115E59` / `#FFFFFF` | `#2DD4BF` / `#5EEAD4` / `#141210` | Tombol & link utama |
| `primary-subtle` / `on-primary-subtle` | `#CCFBF1` / `#115E59` | `#123A37` / `#5EEAD4` | Badge, item nav aktif |
| `secondary` (+ `-subtle`, `on-…`) | `#C2410C` | `#FB923C` | Accent |
| `success` · `warning` · `error` · `info` (+ `-subtle`, `on-…-subtle`) | 700 / 50 / 800 | 400 / tint gelap / 400 | Status, badge evidence |
| `error-fill` | `#DC2626` | `#B91C1C` | Tombol danger (teks putih) |
| `focus` | `#0F766E` | `#2DD4BF` | Focus ring |

### Tipografi, jarak, bentuk, gerak

| Grup | Token | Nilai |
|---|---|---|
| `font.family` | `heading` · `body` · `mono` | Plus Jakarta Sans · Inter · JetBrains Mono (+ fallback) |
| `font.size` | `display` `h2`…`h6` | Fluid `clamp(mobile, …, desktop)`, mis. display 2rem → 3rem |
| `font.size` | `body` · `small` · `tiny` | 1rem · 0.875rem · 0.75rem |
| `font.weight` | `regular` `medium` `semibold` `bold` | 400 · 500 · 600 · 700 |
| `font.lineHeight` | `tight` `snug` `small` `body` | 1.2 · 1.3 · 1.4 · 1.5 |
| `spacing` | `0` `1` `2` `3` `4` `5` `6` `8` `12` `16` `24` | N × 4 px (`4` = 16 px) |
| `radius` | `sm` `md` `lg` `xl` `full` | 6 · 8 · 12 · 16 · 9999 px |
| `shadow` | `sm` `md` `lg` | Bayangan hangat (`rgba(28,25,23,…)`) |
| `size` | `tap-min`, `button-*`, `input`, `topbar-*`, `sidebar*`, `icon-*` | 44 px target sentuh, dst. |
| `breakpoint` | `sm` `md` `lg` `xl` | 600 · 768 · 1024 · 1440 px |
| `container` | `form` `tablet` `desktop` `wide` `prose` | 440 · 720 · 1200 · 1440 px · 68ch |
| `zIndex` | `dropdown` `sticky` `modal` `toast` | 10 · 20 · 40 · 50 |
| `motion` | `duration.*`, `easing.standard` | 80–250 ms, `cubic-bezier(0.2, 0, 0, 1)`; 0 ms bila reduced motion |

## 4. Nama di CSS dan Tailwind / Naming

| Token JSON | CSS variable | Tailwind class |
|---|---|---|
| `color.primary.600` | `--color-primary-600` | `bg-primary-600` |
| `semantic.*.primary` | `--color-primary` | `bg-primary`, `text-primary` |
| `semantic.*.text-muted` | `--color-text-muted` | `text-ui-text-muted` |
| `semantic.*.surface` | `--color-surface` | `bg-ui-surface` |
| `semantic.*.border-input` | `--color-border-input` | `border-ui-border-input` |
| `spacing.4` | `--spacing-4` | `p-4`, `gap-4` (= 16 px) |
| `radius.lg` | `--radius-lg` | `rounded-lg` |
| `font.size.h2` | `--font-size-h2` | `text-h2` |
| `font.lineHeight.body` | `--font-line-height-body` | `leading-body` |
| `motion.duration.fast` | `--motion-duration-fast` | `duration-fast` |

Aturan: segmen camelCase di JSON menjadi kebab-case di CSS (`lineHeight` → `line-height`).

## 5. Dark Mode

- Default mengikuti sistem (`prefers-color-scheme`).
- Paksa dari Profil: set `document.documentElement.dataset.theme = "light" | "dark"`; hapus atribut untuk "Ikuti sistem".
- Karena Tailwind menunjuk ke CSS variables, **tidak perlu** prefix `dark:` untuk warna peran. Prefix `dark:` hanya untuk kasus khusus (mis. border foto).

## 6. Mengubah Token / Changing Tokens

1. Ubah `tokens.json` (bukan CSS/Tailwind).
2. Jalankan `python design/tokens/build_tokens.py`. Bila contrast gagal, script menolak dengan pesan pasangan mana yang kurang.
3. Perbarui Figma Variables (import ulang lewat Tokens Studio, lihat [figma-guide](../figma/figma-guide.md)).
4. Catat di tabel versi di bawah. Mengganti/menghapus token = **MAJOR**; menambah = **MINOR**; mengubah nilai tanpa mengubah peran = **PATCH**.

| Versi | Tanggal | Perubahan |
|---|---|---|
| 1.0.0 | 2026-10-06 | Rilis awal dari design-system v0.1 (colors, typography, spacing); tambah tint dark mode untuk badge, `neutral.550`, `chart`, `motion`, `size`, `zIndex` |

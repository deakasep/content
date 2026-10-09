# Developer Guide — Handoff

> **ID:** Panduan developer untuk mengubah spesifikasi di `design/` menjadi kode: memakai token, membangun komponen, bilingual, menguji, dan aturan penamaan. Stack yang diasumsikan mengikuti scaffold yang sudah ada di `clau-ai-agents/frontend` (**Next.js App Router + TypeScript**). Bila stack berubah, prinsipnya tetap sama.
> **EN:** How developers turn the `design/` specs into code: tokens, components, i18n, testing, and naming. Assumes the existing Next.js + TypeScript scaffold.

## 0. Prinsip / Principles

1. **Token, bukan angka.** Tidak ada hex, px, atau ms mentah di komponen. Semua lewat CSS variables / Tailwind theme dari `design/tokens`.
2. **Mobile-first.** Gaya default untuk 360 px; breakpoint `md`/`lg` menambah, bukan mengurangi.
3. **Aksesibel sejak awal.** Primitive dengan keyboard & ARIA yang benar (Radix UI), bukan ditambal belakangan.
4. **Bilingual dari hari pertama.** Tidak ada string UI hardcode; semua di file pesan `id` & `en`.
5. **Aturan CLAU di UI = aturan di server.** Tombol nonaktif (mis. *Setujui* saat fakta belum dikonfirmasi) **juga** ditolak oleh API. UI saja tidak cukup.
6. **Pilar & agent dari registry.** Nama pilar, status, nama agent, dan avatar dibaca dari `agents/registry.json` (`pillars`, `agents`) atau `GET /pillars`; tidak ada daftar pilar/agent hardcode di komponen. Lihat [pillars.md](../pillars.md).

## 1. Memakai Design Tokens / Using Tokens

```bash
# Jangan edit tokens.css / tailwind.config.js — edit tokens.json lalu:
python design/tokens/build_tokens.py
```

| Langkah | Detail |
|---|---|
| 1 | Salin/import `design/tokens/tokens.css` sekali di root layout (`app/layout.tsx` → `import "@/styles/tokens.css"`) |
| 2 | Tailwind **v3.4**: `presets: [require("./tokens/tailwind.config.js")]` di `tailwind.config.js` proyek. Tailwind **v4**: tambahkan `@config "./tokens/tailwind.config.js";` di CSS utama (atau port ke `@theme`) |
| 3 | Pakai warna **peran**: `bg-primary`, `text-ui-text-muted`, `bg-ui-surface`, `border-ui-border-input`. Skala mentah (`bg-primary-600`) hanya untuk kasus khusus seperti ilustrasi |
| 4 | Dark mode otomatis lewat variables. Set `document.documentElement.dataset.theme = "dark"` untuk memaksa; hapus atribut untuk "Ikuti sistem" |
| 5 | Sinkron: CI menjalankan `python design/tokens/build_tokens.py --check` (gagal bila file generated basi atau contrast < AA) |

Contoh CSS tanpa Tailwind:

```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--spacing-4);
  box-shadow: var(--shadow-sm);
}
@media (min-width: 1024px) { .card { padding: var(--spacing-6); } }
```

## 2. Implementasi Komponen / Implementing Components

### Struktur folder (usulan)

```text
frontend/
├── app/[locale]/(portal)/…        # Portal Klien: beranda, konten, kalender, laporan, profil
├── app/[locale]/(studio)/…        # Studio: ringkasan, klien, konten, agent, …
├── components/ui/                 # 22 komponen inti (Button, Input, Card, …)
├── components/clau/               # EvidenceBadge, FactConfirmRow, ContentPreview, ApprovalBar, AgentStatusPill
├── lib/format.ts                  # formatRupiah, formatDate, formatTime (+ zona WIB/WITA/WIT)
├── lib/greeting.ts                # pagi/siang/sore/malam per zona waktu user
├── messages/id.json · en.json     # semua string UI
└── styles/tokens.css              # salinan dari design/tokens (atau import langsung)
```

### Contoh: Button

```tsx
// components/ui/button.tsx
import { forwardRef, type ButtonHTMLAttributes } from "react";
import { Loader2 } from "lucide-react";
import { cn } from "@/lib/cn";

type Variant = "primary" | "secondary" | "ghost" | "danger";
type Size = "sm" | "md" | "lg";

const variants: Record<Variant, string> = {
  primary: "bg-primary text-ui-on-primary hover:bg-ui-primary-hover",
  secondary: "bg-ui-surface text-ui-text border border-ui-border-input hover:bg-neutral-100",
  ghost: "text-primary hover:bg-ui-primary-subtle",
  danger: "bg-ui-error-fill text-white hover:opacity-90",
};
const sizes: Record<Size, string> = {
  sm: "h-[var(--size-button-sm)] px-3 text-small",
  md: "h-[var(--size-button-md)] px-4 text-body",
  lg: "h-[var(--size-button-lg)] px-6 text-body w-full md:w-auto",
};

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant; size?: Size; loading?: boolean; loadingLabel?: string;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { variant = "primary", size = "md", loading, loadingLabel, disabled, children, className, ...rest }, ref,
) {
  return (
    <button
      ref={ref}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      className={cn(
        "inline-flex min-h-tap items-center justify-center gap-2 rounded-md font-semibold",
        "transition-colors duration-fast ease-standard active:scale-[0.98]",
        "focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--color-focus)]",
        "disabled:cursor-not-allowed disabled:opacity-50",
        variants[variant], sizes[size], className,
      )}
      {...rest}
    >
      {loading && <Loader2 aria-hidden className="size-4 animate-spin motion-reduce:animate-none" />}
      {loading ? loadingLabel ?? children : children}
    </button>
  );
});
```

### Aturan komponen

| Aturan | Detail |
|---|---|
| Primitive | Dialog, Dropdown, Select, Tabs, Tooltip, Toast, Checkbox, Switch → **Radix UI** primitives + styling token |
| State | Setiap komponen mendukung state di [components.md](../design-system/components.md): hover, focus-visible, active, disabled, loading |
| Target sentuh | `min-h-tap min-w-tap` (44 px) pada semua elemen interaktif |
| Ikon | `lucide-react`, ukuran via token (`size-4`/`size-5`/`size-6`), `aria-hidden` bila dekoratif |
| Teks | Tidak ada string di komponen; terima `children`/props, atau ambil dari `messages/*` |
| Motion | `duration-*` dari token; `motion-reduce:` untuk mematikan animasi |
| Evidence Badge | Satu sumber kebenaran: `EVIDENCE = { "DATA FINAL": { tone: "success", icon: BadgeCheck }, … }`. Label **tidak diterjemahkan** |

## 3. Bilingual & Format Lokal / i18n & Locale

| Hal | Implementasi |
|---|---|
| Routing | `/id/...` (default) dan `/en/...`; simpan pilihan di profil user (bukan hanya cookie) |
| Library | `next-intl` (rekomendasi) atau setara; pesan di `messages/id.json` & `messages/en.json` dengan **kunci yang sama** |
| Cek kelengkapan | Script CI: setiap kunci di `id.json` harus ada di `en.json` dan sebaliknya |
| Uang | `formatRupiah(1250000)` → `Rp1.250.000` (ID) / `IDR 1,250,000` (EN). Lihat catatan `Intl` di [typography.md](../design-system/typography.md) |
| Tanggal & jam | `Intl.DateTimeFormat` + zona dari profil (`Asia/Jakarta` WIB, `Asia/Makassar` WITA, `Asia/Jayapura` WIT); tampilkan singkatan zona |
| Sapaan | `getGreeting(now, tz)`: pagi 04.00–10.59 · siang 11.00–14.59 · sore 15.00–17.59 · malam 18.00–03.59 |
| `lang` | `<html lang>` sesuai locale; blok caption EN di dalam konten ID memakai `lang="en"` |

## 4. Aturan Bisnis yang Wajib di Server / Server-enforced Rules

| Aturan | UI | API |
|---|---|---|
| Tidak ada publish otomatis | Tidak ada tombol Publish | Tidak ada endpoint publish ke platform sosial |
| *Setujui* butuh semua fakta dikonfirmasi | Tombol nonaktif + helper | `409 facts_unconfirmed` |
| L2/L3 butuh review independen | Tombol *Kirim ke klien* nonaktif | `409 independent_review_required` |
| Reviewer ≠ pembuat draft | Pembuat tidak muncul di pilihan reviewer | `403 self_review_not_allowed` |
| Approval terikat versi | Banner "Ada versi baru" | Approval menyimpan `content_version_id`; versi beda → `409 version_mismatch` |
| Tandai tayang butuh URL valid | Field wajib + validasi domain | Validasi ulang di server |
| Agent pilar belum aktif tidak dijalankan | Tanpa tombol *Jalankan*; status "Belum aktif" | `POST /route` → `status: planned`, `next_step: escalate_to_owner` (**Implemented**) |

Kontrak API mengikuti `clau-ai-core/shared/api-contracts.md`. Endpoint di atas belum ada di scaffold (**NEXT ACTION**).

## 5. Testing

| Lapis | Tool | Cakupan minimum |
|---|---|---|
| Unit | Vitest + Testing Library | `formatRupiah`, `getGreeting`, mapping evidence, logika tombol Setujui (enabled/disabled) |
| Komponen | Testing Library + `jest-axe` / `vitest-axe` | Setiap komponen: render tiap variant, keyboard (Tab/Enter/Space/Esc), tanpa pelanggaran axe |
| E2E | Playwright | Flow Portal F1–F5 dan Studio S1–S5 di viewport 360 × 800 & 1280 × 800, ID & EN |
| Aksesibilitas E2E | `@axe-core/playwright` | 0 pelanggaran *serious/critical* di setiap halaman |
| Visual | Screenshot Playwright (atau Chromatic bila memakai Storybook) | Light & dark, mobile & desktop untuk halaman utama |
| Performa | Lighthouse CI | LCP < 2 s (throttle 4G), CLS < 0.1, JS awal ≤ 170 KB gzip |
| Token | `build_tokens.py --check` | Generated up to date, contrast AA |

Checklist rilis lengkap ada di [qa-checklist.md](./qa-checklist.md).

## 6. Naming Convention

| Hal | Konvensi | Contoh |
|---|---|---|
| File komponen | kebab-case | `fact-confirm-row.tsx` |
| Komponen React | PascalCase | `FactConfirmRow`, `EvidenceBadge` |
| Props boolean | `is…` / `has…` / kata sifat | `isOpen`, `hasError`, `loading` |
| Event handler | `on…` (prop) / `handle…` (internal) | `onApprove`, `handleSubmit` |
| CSS variable | `--{kategori}-{nama}` kebab | `--color-text-muted`, `--spacing-4` |
| Kunci i18n | `area.layar.elemen`, camelCase per segmen | `portal.contentDetail.approveButton` |
| Route | Bahasa Inggris, kebab-case (stabil lintas bahasa) | `/id/content/[id]`, `/en/reports` |
| Test id | `data-testid="{area}-{elemen}"` hanya bila selector role/teks tidak memungkinkan | `approval-bar-approve` |
| Branch & commit | Ikuti repo: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`, `test:` | `feat(portal): approval bar` |
| Status konten (kode) | Bahasa Inggris snake_case; label UI lewat i18n | `in_review` → "Ditinjau" / "In review" |

## 7. Definition of Done (per halaman)

- [ ] Sesuai mockup di mobile 360, tablet 768, desktop 1280.
- [ ] State isi, kosong, loading (skeleton), error tersedia.
- [ ] ID & EN lengkap; teks terpanjang tidak terpotong.
- [ ] Keyboard & screen reader bisa menyelesaikan task utama.
- [ ] Aturan bisnis dicek juga di server.
- [ ] Lulus [qa-checklist](./qa-checklist.md).

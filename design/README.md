# CLAU AI — UI/UX Standalone

> **ID:** Spesifikasi UI/UX untuk aplikasi CLAU sendiri: **Portal Klien** (untuk owner hotel, villa, resto, spa) dan **Studio** (dashboard internal agency). Aplikasi ini berdiri sendiri, tidak bergantung pada Rekan-AI atau platform lain, dan bisa diintegrasikan nanti lewat API.
>
> **EN:** UI/UX specification for CLAU's own app: a **Client Portal** (for hotel, villa, restaurant, and spa owners) and **Studio** (the agency's internal dashboard). It runs on its own, with no dependency on Rekan-AI or any other platform, and can be integrated later through an API.

| Item | Nilai / Value |
|---|---|
| Status | **v0.2 — siap handoff ke Figma & development**: spec, design tokens, brand, rencana riset, panduan handoff. Belum ada file Figma, hasil user test, atau kode UI |
| Nama produk | **CLAU AI** — merek payung 5 pilar; modul aktif: **Content Studio** (AI Marketing) (**DATA FINAL, opsi B issue #46 — Dea Karisna (d34faiza), 2026-10-09**) |
| Bahasa UI | **Bahasa Indonesia (default)** + English, toggle `ID / EN` di header dan Profil |
| Target | Klien hospitality di seluruh Indonesia (Bali, Jawa, Sumatra, Sulawesi, Nusa Tenggara, Papua) |
| Device | **Mobile-first** (360 × 800 sebagai baseline), lalu tablet dan desktop |
| Aksesibilitas | WCAG 2.2 AA (contrast ratio dihitung, lihat [colors.md](./design-system/colors.md)) |
| Performa | Halaman utama siap dipakai < 2 detik di 4G (budget di [§ Prinsip](#prinsip-desain--design-principles)) |

## Kenapa Standalone / Why Standalone

| | Standalone (sekarang) | Integrasi (nanti) |
|---|---|---|
| Login & akun | Milik CLAU sendiri | Bisa SSO dengan platform lain |
| Data | Database CLAU (`clau-core/shared/database-schema.md`) | Sinkron lewat API (`clau-core/shared/api-contracts.md`) |
| Desain | Design system CLAU (folder ini) | Token diekspor sebagai CSS variables / JSON, jadi bisa dipakai host lain |
| Rilis | Tidak menunggu roadmap pihak lain | Integrasi hanya bila ada kebutuhan nyata |

Prinsip integrasi: **komponen tidak tahu siapa host-nya**. Semua warna, jarak, dan teks lewat token dan file i18n, bukan hardcode, jadi integrasi nanti cukup ganti token dan endpoint.

## Dua Permukaan / Two Surfaces

| Permukaan | Pengguna | Tujuan utama | Wireframe |
|---|---|---|---|
| **Portal Klien** / Client Portal | Owner/GM properti, approver client | Cek & approve konten, **konfirmasi fakta**, lihat kalender & laporan | [client-portal-wireframe.md](./wireframes/client-portal-wireframe.md) |
| **Studio** / Internal Dashboard | Owner agency, content lead, tim | Kelola klien, pipeline konten, AI agent, QA, laporan | [dashboard-wireframe.md](./wireframes/dashboard-wireframe.md) |

### Yang membuat produk ini beda / What makes it different

UI ini **mengikuti aturan CLAU**, bukan sekadar CMS konten:

1. **AI tidak pernah publish.** Tombol publish tidak ada. Yang ada: *"Tandai sudah tayang"* + URL post, diisi manusia (`AI-CONSTITUTION` §4).
2. **Konfirmasi Fakta** di Portal Klien. Owner mengonfirmasi fakta (harga, fasilitas, promo) langsung di aplikasi. Fakta yang dikonfirmasi berubah dari **CLIENT CONFIRMATION** ke **DATA FINAL**. Ini menjawab masalah nyata di pilot client nyata pertama: konten tertahan karena fakta menunggu jawaban WA.
3. **Label evidence terlihat.** Setiap klaim punya label (DATA FINAL, ASSUMPTION, CLIENT CONFIRMATION, FIELD VERIFICATION, RISK, NEXT ACTION) dengan warna dan ikon konsisten.
4. **Level approval L1/L2/L3** dan status review independen tampil di setiap konten.

## 5 Pilar / Five Pillars

Portal & Studio adalah **satu shell untuk 5 pilar v2** CLAU AI (AI-CONSTITUTION v3.0.0, `clau-core/docs/5-pillar-architecture.md`). Sekarang hanya **Pilar 1 AI Marketing** yang aktif dan dirancang penuh. Pilar 2–5 sudah punya tempat di spec: filter **Pilar** + **Pillar Badge** di Pipeline & Kalender, halaman AI Agent yang dikelompokkan per pilar (12 agent dari `clau-agent/agents/registry.json`, agent pilar belum aktif tampil "Belum aktif", badge **otonomi** A/B/C), dan tab **Per pilar** di Laporan. Rencana layar khusus pilar 2–5 dan checklist aktivasinya: [pillars.md](./pillars.md).

| # | Pilar | Status | Di UI sekarang |
|---|---|---|---|
| 1 | AI Marketing | **Aktif** | Semua halaman Portal & Studio |
| 2 | AI Sales | Planned | Agent Galih & Sari "Belum aktif"; rencana antrean Inquiry, pesan tamu, eskalasi keluhan, template Level A |
| 3 | AI Admin | Planned | Agent Teguh "Belum aktif"; rencana Library SOP & antrean dokumen |
| 4 | AI Business Intelligence | Planned | Agent Intan aktif (template Pilar 1); Laporan tab Per pilar |
| 5 | AI Automation | Planned | Rencana halaman Alur (run log, dry run, tombol berhenti) |

Nama produk: merek payung **CLAU AI**; "Content Studio" = modul AI Marketing (opsi B, TASK-043, lihat [pillars.md § Nama Produk](./pillars.md#nama-produk)).

## Isi Folder / Contents

| File | Isi |
|---|---|
| [wireframes/client-portal-wireframe.md](./wireframes/client-portal-wireframe.md) | 7 halaman Portal Klien, ASCII mobile + desktop |
| [wireframes/dashboard-wireframe.md](./wireframes/dashboard-wireframe.md) | 8 halaman Studio, ASCII mobile + desktop |
| [mockups/client-portal-mockup.md](./mockups/client-portal-mockup.md) | Spek visual per halaman: warna, font, spacing, state, animasi |
| [mockups/dashboard-mockup.md](./mockups/dashboard-mockup.md) | Spek visual Studio |
| [user-flow/client-portal-flow.md](./user-flow/client-portal-flow.md) | 5 flow klien: approve, kalender, laporan, profil, reset password |
| [user-flow/dashboard-flow.md](./user-flow/dashboard-flow.md) | 5 flow internal: klien, tandai tayang, monitor agent, export, settings |
| [design-system/colors.md](./design-system/colors.md) | Palet, token, contrast ratio, light & dark |
| [design-system/typography.md](./design-system/typography.md) | Font, skala, line height, aturan bilingual |
| [design-system/spacing.md](./design-system/spacing.md) | Skala 4/8 px, grid, container, breakpoint |
| [design-system/icons.md](./design-system/icons.md) | Lucide, ukuran, kategori, ikon label evidence |
| [design-system/components.md](./design-system/components.md) | 22 komponen: anatomi, varian, state, do & don't |
| [user-research/persona.md](./user-research/persona.md) | 3 proto-persona |
| [user-research/journey.md](./user-research/journey.md) | Journey klien & owner agency, pain point per tahap |
| [prototype/prototype-guide.md](./prototype/prototype-guide.md) | Figma prototype, user testing (Maze), iterasi |
| [pillars.md](./pillars.md) | **5 pilar di UI**: prinsip satu shell, peta pilar → layar Studio/Portal, rencana pilar 2–5, opsi nama produk, checklist aktivasi |
| **v0.2 — siap handoff** | |
| [ROADMAP.md](./ROADMAP.md) | 6 fase: Spec ✅ → Figma → Prototype → User test → Iterate → Handoff (± 4 minggu) |
| [tokens/tokens.json](./tokens/tokens.json) | **Sumber tunggal** design tokens (W3C DTCG), light & dark |
| [tokens/build_tokens.py](./tokens/build_tokens.py) | Generator `tokens.css` + `tailwind.config.js` + cek contrast WCAG (dijalankan di CI) |
| [tokens/tokens.css](./tokens/tokens.css) · [tokens/tailwind.config.js](./tokens/tailwind.config.js) | Generated: CSS variables & theme Tailwind |
| [tokens/tokens.md](./tokens/tokens.md) | Dokumentasi token, penamaan, dark mode, versioning |
| [figma/figma-guide.md](./figma/figma-guide.md) | Step-by-step Figma: setup, import token, library, prototype, kolaborasi |
| [figma/components-list.md](./figma/components-list.md) | 22 + 5 komponen: nama Figma, variant, size, state, ASCII |
| [figma/prototype-link.md](./figma/prototype-link.md) | Registry link Figma/Maze (placeholder) |
| [research/interview-guide.md](./research/interview-guide.md) | Wawancara 30–45 menit, 20 pertanyaan kunci, consent |
| [research/survey.md](./research/survey.md) | Survey 15 pertanyaan, siap Google Form |
| [research/recruitment.md](./research/recruitment.md) | Kuota 5 responden, channel, template pesan, insentif |
| [brand/brand-guideline.md](./brand/brand-guideline.md) | Nama, warna & font final, voice & tone, do & don't |
| [brand/logo-concept.md](./brand/logo-concept.md) | 3 konsep logo + filosofi + prompt AI (eksplorasi) |
| [handoff/developer-guide.md](./handoff/developer-guide.md) | Token di kode, contoh komponen, i18n, aturan server, testing, naming |
| [handoff/qa-checklist.md](./handoff/qa-checklist.md) | Visual, functional, accessibility, performance QA (blocker 🔴) |

## Alur Kerja Desain / Design Process

```text
 Riset ringan        Wireframe          Mockup             Prototype          Test             Iterasi
 (persona,     ──►  (ASCII → Figma ──► (Figma hi-fi, ──► (Figma, link   ──► (Maze, 5    ──► (prioritas
  journey)           lo-fi)             design system)     antar frame)       orang)           & revisi)
   1–2 jam           2–4 jam            4–8 jam            2–4 jam            1–2 jam          1–2 jam
```

**Total estimasi: 11–22 jam** kerja desainer untuk versi Figma pertama. Dokumen di folder ini adalah input untuk jam pertama sampai ke-4. Mockup hi-fi di Figma **belum dibuat**.

### Tools

| Tool | Dipakai untuk | Biaya |
|---|---|---|
| **Figma** | Wireframe, mockup hi-fi, prototype, design token (Variables) | Paket gratis cukup untuk 1 editor |
| **Excalidraw** | Sketsa cepat, user flow saat diskusi | Gratis |
| **Maze** | Unmoderated user testing dari prototype Figma | Paket gratis (jumlah test terbatas) |
| **Markdown (repo ini)** | Sumber kebenaran spesifikasi; Figma mengikuti dokumen ini | — |

## Deliverable

| # | Deliverable | Status |
|---|---|---|
| 1 | Spesifikasi UI/UX (15 file v0.1) + 17 file v0.2 + `pillars.md` (v0.2.1) | ✅ |
| 2 | Design token (JSON, CSS variables, Tailwind) + cek contrast otomatis | ✅ `tokens/` |
| 2b | Brand guideline, konsep logo, rencana riset, panduan Figma & developer, QA checklist | ✅ |
| 3 | Figma: library + layar | ⬜ Fase 2 ([ROADMAP](./ROADMAP.md)) |
| 4 | Figma: prototype | ⬜ Fase 3 |
| 5 | Hasil wawancara + user test 5 orang | ⬜ Fase 4 |
| 6 | Logo final (vektor) | ⬜ Setelah konsep dipilih |
| 7 | Implementasi kode (Next.js di `clau-agent/frontend`) | ⬜ Setelah handoff |

## Prinsip Desain / Design Principles

| # | Prinsip | Artinya di layar | Ukuran |
|---|---|---|---|
| 1 | **Simple** | Satu tujuan utama per layar; maks 1 tombol primary | Task utama ≤ 3 tap dari Beranda |
| 2 | **Modern** | Banyak ruang putih, sudut 12 px, bayangan halus, tanpa gradien norak | Review visual vs referensi |
| 3 | **Hospitality** | Warna hangat (teal laut + terracotta), foto properti jadi pusat, bahasa ramah | Copy tanpa jargon teknis |
| 4 | **Responsive** | Desain dari 360 px dulu; bottom navigation di mobile | Tidak ada horizontal scroll di 360 px |
| 5 | **Accessible** | WCAG 2.2 AA, target sentuh ≥ 44 px, fokus terlihat | Contrast ≥ 4.5:1 teks, ≥ 3:1 komponen |
| 6 | **Fast** | Skeleton, gambar `srcset` + lazy load, font subset | LCP < 2 dtk (4G), JS awal ≤ 170 KB gzip |
| 7 | **Indonesia** | Format lokal: `Rp1.250.000`, `6 Okt 2026`, WIB/WITA/WIT, sapaan waktu | Semua string lewat i18n |
| 8 | **Local touch** | Plus Jakarta Sans (karya foundry Indonesia), ilustrasi alam Nusantara, contoh copy lokal | — |
| 9 | **Bilingual** | ID default, EN lengkap; tidak ada campuran setengah-setengah di satu layar | 100% string punya pasangan ID/EN |
| 10 | **Enterprise** | Audit trail (siapa approve apa, kapan), peran & izin, export | Setiap aksi penting tercatat |

## Referensi / References

| Referensi | Yang diambil | Yang tidak diambil |
|---|---|---|
| **Airbnb** | Foto sebagai pusat, kartu hangat, tipografi ramah | Kepadatan marketplace |
| **Stripe** | Dashboard bersih, tabel data rapi, dokumentasi status | Nuansa dingin fintech |
| **Linear** | Pipeline cepat, shortcut keyboard, status jelas | Tema gelap sebagai default |
| **Notion** | Empty state ramah, editor sederhana | Fleksibilitas tanpa batas yang membingungkan |
| **Traveloka** | Pola yang familiar untuk user Indonesia: bottom nav, format harga & tanggal lokal | Banner promo padat |

Referensi dipakai sebagai **arah**, bukan disalin. Tidak ada aset, logo, atau UI yang diambil dari produk tersebut.

## Bahasa & Format Lokal / Language & Locale

| Hal | Bahasa Indonesia | English |
|---|---|---|
| Uang | `Rp1.250.000` | `IDR 1,250,000` |
| Tanggal | `Selasa, 6 Okt 2026` | `Tue, 6 Oct 2026` |
| Jam | `18.00 WITA` | `6:00 PM WITA` |
| Sapaan | Selamat pagi/siang/sore/malam, Kak/Bapak/Ibu (pilihan di Profil) | Good morning/afternoon/evening |
| Label evidence | Tetap dalam bahasa aslinya: `DATA FINAL`, `CLIENT CONFIRMATION`, … | Sama |

Label evidence **tidak diterjemahkan**, karena label itu bahasa kerja bersama tim dan dipakai di dokumen QA.

## Hubungan dengan Repo Lain / Relation to Other Repos

- Aturan konten: `clau-core` (AI-CONSTITUTION, AI-BOUNDARY) dan `clau-market` (rules, QA).
- Kontrak data & API: `clau-core/shared/`.
- Implementasi kode UI nantinya di `clau-agent/frontend` (Next.js), atau di repo frontend tersendiri bila owner memutuskan (**CLIENT CONFIRMATION**, lihat laporan).

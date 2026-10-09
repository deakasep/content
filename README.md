# CLAU-AI-CONTENT

**AI Content Marketing Studio untuk Hospitality & Tourism Indonesia.**

Repository private berisi governance, rules, prompt library, AI agent skills, knowledge base, template, dan QA gate untuk memproduksi konten marketing hospitality yang **jujur, legal, on-brand, dan siap publish** — dengan AI sebagai content partner, bukan pengganti approval manusia.

> [!IMPORTANT]
> **ARSIP sejak 2026-10-04.** Repo ini sudah di-split menjadi tiga repo. Kerjaan baru masuk ke sana, bukan ke sini:
>
> | Repo | Isi |
> |---|---|
> | [clau-ai-core](https://github.com/d34faiza-commits/clau-ai-core) | Fondasi: AI-CONSTITUTION, AI-BOUNDARY, orchestrator, shared contracts |
> | [clau-ai-marketing](https://github.com/d34faiza-commits/clau-ai-marketing) | Pilar 1: rules, prompts, skills, knowledge, templates, QA, examples |
> | [clau-ai-agents](https://github.com/d34faiza-commits/clau-ai-agents) | Platform: registry agent, backend FastAPI, frontend Next.js |
>
> **Peta otak AI:** semua pondasi (constitution, boundary, router, registry agent, rules pilar) ada di repo sumbernya; lihat dari satu halaman: [`docs/peta-otak.md`](./docs/peta-otak.md).
>
> **Konsep 5 pilar (AI-CONSTITUTION v3.0.0):** core (fondasi) → repo per pilar `clau-ai-<pilar>` → platform. **Pilar 1 AI Marketing** aktif di clau-ai-marketing; Pilar 2 AI Sales, 3 AI Admin, 4 AI Business Intelligence, 5 AI Automation masih Planned. Otonomi bertingkat A/B/C (default B). Vertical fokus: villa, restoran/cafe, wedding, travel. Peta lengkap: [clau-ai-core/docs/5-pillar-architecture.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/5-pillar-architecture.md); di UI: [`design/pillars.md`](./design/pillars.md); rencana aktivasi: [`tasks/backlog.md`](./tasks/backlog.md).
>
> **Pengecualian 2026-10-06:** spesifikasi UI/UX standalone ([`design/`](./design/README.md)) dibuat di repo ini atas perintah owner.
>
> Yang tetap tinggal di sini: board `tasks/` dan `docs/` (dirujuk dari repo baru lewat URL), serta [`scripts/split_repo.py`](./scripts/split_repo.py) dan `split/` sebagai jejak proses split. Isi lain di bawah ini adalah snapshot terakhir sebelum split.

> **Status:** Arsip (read-only secara disiplin) — snapshot Foundation release (versi per dokumen: lihat [Versi Dokumen](#versi-dokumen))
> **Dokumen induk:** [CONTENT-CONSTITUTION.md](./CONTENT-CONSTITUTION.md)
> **Boundary:** [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md)
> **Credit:** [ACKNOWLEDGMENT.md](./ACKNOWLEDGMENT.md)

## Versi Dokumen

| Dokumen | Versi | Status |
|---|---|---|
| [CONTENT-CONSTITUTION.md](./CONTENT-CONSTITUTION.md) | 1.0.0 | Superseded |
| [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md) | 0.1.4 | Draft |
| [WORKFLOW.md](./WORKFLOW.md) | 0.1.3 | Draft |
| [AGENTS.md](./AGENTS.md) | 0.1.3 | Draft |

Setiap dokumen di-version terpisah (SemVer). Validator mengecek tabel ini cocok dengan frontmatter dan Revision History tiap dokumen.

## Kenapa repo ini ada

Konten hospitality punya risiko spesifik yang sering diabaikan saat pakai AI:

- klaim yang tidak bisa dibuktikan ("best sunset view in Bali", "bintang 5", "halal", "eco-friendly");
- foto AI yang terlihat seperti properti asli dan menyesatkan calon tamu;
- foto/review tamu dipakai tanpa consent;
- harga promo tanpa info pajak, service charge, periode, dan syarat;
- tone brand yang generik dan tidak terasa "Indonesia";
- konten dipublish tanpa approval owner properti.

Repo ini menetapkan cara kerja supaya AI mempercepat produksi konten tanpa menurunkan integritas, privacy, dan kepercayaan tamu.

## Target Industri

| # | Vertical | Status |
|---|---|---|
| 1 | Villa / Guesthouse / Homestay | **Fokus awal** |
| 2 | Hotel / Resort | **Fokus awal** |
| 3 | Restaurant / Cafe / Beach Club | **Fokus awal** |
| 4 | Spa / Wellness / Retreat | **Fokus awal** |
| 5 | Tourism Experience (surf, dive, tour, adventure, cruise) | Planned |

Villa dan Hotel diperlakukan sebagai satu vertical *Accommodation* dengan knowledge segment terpisah.

## Struktur Repository

```text
CLAU-AI-CONTENT/
├── README.md                 # Dokumen ini
├── ACKNOWLEDGMENT.md         # Credit dan sumber inspirasi pola
├── LICENSE                   # Proprietary — private use only
├── CONTENT-CONSTITUTION.md   # Aturan induk seluruh workflow konten AI
├── CONTENT-BOUNDARY.md       # Apa yang boleh/tidak boleh masuk repo
├── AGENTS.md                 # Instruksi gaya kerja & output untuk AI agent
├── WORKFLOW.md               # Alur wajib Brief → Publish → Monitor
├── rules/                    # 9 content standard hospitality
├── prompts/                  # Prompt library per jenis konten
├── skills/                   # Reusable AI agent workflow (SKILL.md + agents/openai.yaml)
├── knowledge/                # Knowledge base: segment, platform, kalender, destinasi, voice
├── templates/                # Brief, calendar, campaign, onboarding, approval, report
├── qa/                       # Review gate sebelum publish
├── schemas/                  # Machine-readable contract (content brief)
├── tasks/                    # Task board: Backlog → In Progress → Review → Done
├── examples/                 # Contoh & pilot dengan properti fiktif
├── automations/              # Tingkat otomasi workflow (Level 1 manual aktif)
├── docs/                     # Panduan operasional (task management)
├── scripts/validate.py       # Validator struktur repo (dipakai CI)
└── .github/workflows/        # CI validation
```

## Hierarki Otoritas

```text
1. Hukum & regulasi Indonesia, kontrak, kebijakan platform
2. Instruksi tertulis owner/authorized representative client
3. CONTENT-CONSTITUTION.md
4. CONTENT-BOUNDARY.md
5. rules/ (01–09)
6. Content brief & brand guide client yang sudah disetujui
7. Skill / prompt / task-level instruction
8. Default behavior AI tool
```

Aturan level bawah tidak boleh menurunkan kontrol di level atas.

## Klasifikasi Wajib

Setiap klaim dan keputusan di konten ditandai dengan **6 evidence/action label**:

| Label | Arti singkat di konteks konten |
|---|---|
| **DATA FINAL** | Fakta terverifikasi + ada sumber/approval (mis. jumlah kamar dari owner, sertifikat halal aktif) |
| **ASSUMPTION** | Dugaan kerja sementara — tidak boleh tampil di konten publish |
| **CLIENT CONFIRMATION** | Butuh konfirmasi owner/manager properti |
| **FIELD VERIFICATION** | Harus dicek langsung di lokasi (view, jarak ke pantai, kondisi kamar) |
| **RISK** | Potensi masalah legal, reputasi, atau misleading |
| **NEXT ACTION** | Tindakan spesifik + owner + target |

Plus **4 axis** data classification: **Sensitivity**, **Lifecycle**, **Scope**, **Evidence**. Detail: [rules/09-DATA-CLASSIFICATION.md](./rules/09-DATA-CLASSIFICATION.md).

## Quick Start

1. Baca [CONTENT-CONSTITUTION.md](./CONTENT-CONSTITUTION.md) dan [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md).
2. Onboard client pakai [templates/client-onboarding.md](./templates/client-onboarding.md).
3. Isi [templates/property-fact-sheet.md](./templates/property-fact-sheet.md) bersama owner (sumber fakta properti), lalu isi [templates/content-brief.md](./templates/content-brief.md) — valid terhadap [schemas/content-brief.schema.json](./schemas/content-brief.schema.json).
4. Jalankan alur di [WORKFLOW.md](./WORKFLOW.md).
5. Pakai skill atau prompt yang sesuai (lihat index di bawah).
6. Review dengan gate di [qa/](./qa/content-review.md).
7. Catat approval di [templates/approval-record.md](./templates/approval-record.md) sebelum publish.

## Index Rules

| No | Standard | Dipakai ketika |
|---|---|---|
| 01 | [Content Integrity](./rules/01-CONTENT-INTEGRITY-STANDARD.md) | Semua konten — selalu berlaku |
| 02 | [Hospitality Claim](./rules/02-HOSPITALITY-CLAIM-STANDARD.md) | Ada klaim fasilitas, rating, sertifikasi, harga, lokasi |
| 03 | [Client Brand Voice](./rules/03-CLIENT-BRAND-VOICE-STANDARD.md) | Menulis atas nama brand client |
| 04 | [Privacy, Consent & UGC](./rules/04-PRIVACY-CONSENT-UGC-STANDARD.md) | Ada foto/nama/review tamu, staf, atau UGC |
| 05 | [Platform](./rules/05-PLATFORM-STANDARD.md) | Format per platform (IG, TikTok, GBP, OTA, WA) |
| 06 | [Localization & Bahasa](./rules/06-LOCALIZATION-BAHASA-STANDARD.md) | Konten ID/EN atau multi-bahasa |
| 07 | [AI Visual & Disclosure](./rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md) | Ada gambar/video hasil AI atau editing berat |
| 08 | [Approval & Publication](./rules/08-APPROVAL-PUBLICATION-STANDARD.md) | Sebelum publish — selalu berlaku |
| 09 | [Data Classification](./rules/09-DATA-CLASSIFICATION.md) | Semua data client/konten — selalu berlaku |

## Index Skills

| Skill | Fungsi |
|---|---|
| [`draft-caption`](./skills/draft-caption/SKILL.md) | Draft caption IG/TikTok/FB sesuai brand voice & claim rule |
| [`reply-guest-review`](./skills/reply-guest-review/SKILL.md) | Balas review tamu (Google, OTA, TripAdvisor) secara aman |
| [`build-content-calendar`](./skills/build-content-calendar/SKILL.md) | Susun kalender konten bulanan berbasis kalender Indonesia |
| [`write-ota-listing`](./skills/write-ota-listing/SKILL.md) | Tulis deskripsi properti untuk OTA & website |
| [`localize-content`](./skills/localize-content/SKILL.md) | Lokalisasi ID ↔ EN tanpa kehilangan nuansa |
| [`plan-seasonal-campaign`](./skills/plan-seasonal-campaign/SKILL.md) | Rencana campaign musiman (Ramadan, Nataru, libur sekolah) |
| [`draft-reel-script`](./skills/draft-reel-script/SKILL.md) | Script Reels/TikTok: hook, shot list, on-screen text, klaim & consent per shot |

## Index Prompts

| Jenis | Prompt |
|---|---|
| Caption | [draft-instagram-caption](./prompts/caption/draft-instagram-caption.md) |
| Campaign | [plan-campaign](./prompts/campaign/plan-campaign.md) |
| OTA listing | [write-hotel-description](./prompts/ota-listing/write-hotel-description.md) |
| Review response | [reply-guest-review](./prompts/review-response/reply-guest-review.md) |
| Destination story | [storytelling-destination](./prompts/destination-story/storytelling-destination.md) |
| Seasonal promo | [seasonal-campaign](./prompts/promo-seasonal/seasonal-campaign.md) |
| Reel / short video | [reel-script](./prompts/video/reel-script.md) |
| Instagram Stories | [stories-sequence](./prompts/stories/stories-sequence.md) |
| Template | [prompt-template](./prompts/templates/prompt-template.md) |

## Automations

Workflow saat ini berjalan di **Level 1 (manual/semi-manual)**: rutinitas harian, mingguan, dan bulanan dijalankan manusia, dengan skill dan prompt dipakai di AI chat. AI tidak publish atau approve sendiri. Detail: [automations/level-1-manual/README.md](./automations/level-1-manual/README.md) · [semua level](./automations/README.md).

## Task Management

Pekerjaan repo dilacak dengan board Markdown **Backlog → In Progress → Review → Done**, dengan ID `TASK-XXX`, priority, assignee, dan acceptance criteria. Board ini dicek otomatis oleh validator.

| Link | Isi |
|---|---|
| [tasks/README.md](./tasks/README.md) | Overview board, ringkasan jumlah task, aturan |
| [tasks/backlog.md](./tasks/backlog.md) · [in-progress](./tasks/in-progress.md) · [review](./tasks/review.md) · [done](./tasks/done.md) | Kolom board |
| [docs/task-management.md](./docs/task-management.md) | Cara pakai, best practice, dan **setup GitHub Projects** (board visual + auto-add issues) |

## Validation

```text
python scripts/validate.py
```

Validator mengecek: file wajib, section wajib di rules/prompts/skills, frontmatter skill, `agents/openai.yaml`, konsistensi versi dokumen governance, task board, JSON schema valid, relative link valid, dan pola secret sederhana. CI menjalankan validator yang sama di setiap push dan pull request.

## Batasan

Repository ini **tidak** menggantikan:

- approval tertulis dari owner/representative client;
- legal review untuk klaim sensitif (halal, sertifikasi, harga, kompetitor);
- verifikasi lapangan untuk klaim fisik properti;
- kebijakan platform (Meta, TikTok, Google, OTA) yang berlaku saat publish.

Data client, foto asli, review mentah, dan credential akun social media **tidak** disimpan di repo ini — lihat [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md).

## Lisensi

Proprietary, private use. Lihat [LICENSE](./LICENSE).

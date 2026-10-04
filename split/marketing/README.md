# clau-ai-marketing

**Pilar 1 CLAU AI: Marketing & Content** untuk hospitality & tourism Indonesia. Berisi rules, prompt, skill, knowledge, template, dan QA gate untuk memproduksi konten yang **jujur, legal, on-brand, dan siap publish**, dengan AI sebagai content partner, bukan pengganti approval manusia.

> **Status:** Private — v0.1.0 (split dari `CLAU-AI-CONTENT`, 2026-10-04)
> **Fondasi:** submodule [`core/`](https://github.com/d34faiza-commits/clau-ai-core) → `AI-CONSTITUTION.md`, `AI-BOUNDARY.md`, pipeline, orchestrator
> **Workflow konten:** [CONTENT-WORKFLOW.md](./CONTENT-WORKFLOW.md) · **Agent:** [AGENTS.md](./AGENTS.md) · **Credit:** [ACKNOWLEDGMENT.md](./ACKNOWLEDGMENT.md)

> ⚠️ **Constitution:** `core/AI-CONSTITUTION.md` v2.0.0 masih **For Review**. Sampai disetujui, aturan induk yang berlaku untuk pilar ini adalah *CLAU AI Content Constitution v1.0.0* (Approved), arsip di repo [CLAU-AI-CONTENT](https://github.com/d34faiza-commits/CLAU-AI-CONTENT/blob/main/CONTENT-CONSTITUTION.md).

## Setup

```bash
git clone --recurse-submodules https://github.com/d34faiza-commits/clau-ai-marketing.git
# atau, bila sudah ter-clone:
git submodule update --init --recursive
```

Link ke `core/...` di dokumen repo ini baru berfungsi setelah submodule ter-init.

## Target Industri

| # | Vertical | Status |
|---|---|---|
| 1 | Villa / Guesthouse / Homestay | Fokus awal |
| 2 | Hotel / Resort | Fokus awal |
| 3 | Restaurant / Cafe / Beach Club | Fokus awal |
| 4 | Spa / Wellness / Retreat | Fokus awal |
| 5 | Tourism Experience (surf, dive, tour, adventure, cruise) | Planned |

## Struktur

```text
clau-ai-marketing/
├── README.md · AGENTS.md · CONTENT-WORKFLOW.md · ACKNOWLEDGMENT.md · LICENSE
├── core/              # submodule → clau-ai-core (jangan diedit di sini)
├── rules/             # 9 content standard
├── prompts/           # prompt library (caption, campaign, OTA, review, destination, seasonal, reel, stories)
├── skills/            # 7 AI agent skill (SKILL.md + agents/openai.yaml)
├── knowledge/         # segment, platform, kalender, destinasi, voice, market, regulasi
├── templates/         # brief, fact sheet, calendar, campaign, onboarding, approval, report
├── qa/                # 5 QA gate
├── schemas/           # content-brief.schema.json (v1.3)
├── automations/       # Level 1 manual
├── examples/          # pilot fiktif (SIMULASI)
└── scripts/           # validate.py, check_caption.py
```

## Versi Dokumen

| Dokumen | Versi | Status |
|---|---|---|
| [CONTENT-WORKFLOW.md](./CONTENT-WORKFLOW.md) | 0.2.0 | Draft |
| [AGENTS.md](./AGENTS.md) | 0.2.0 | Draft |

Constitution & boundary di-version di clau-ai-core.

## Klasifikasi Wajib

6 label: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**, plus 4 axis (Sensitivity, Lifecycle, Scope, Evidence): [rules/09](./rules/09-DATA-CLASSIFICATION.md).

## Quick Start

1. Baca `core/AI-CONSTITUTION.md`, `core/AI-BOUNDARY.md`, lalu [CONTENT-WORKFLOW.md](./CONTENT-WORKFLOW.md).
2. Onboard client: [templates/client-onboarding.md](./templates/client-onboarding.md).
3. Isi [templates/property-fact-sheet.md](./templates/property-fact-sheet.md), lalu [templates/content-brief.md](./templates/content-brief.md) (valid terhadap [schema](./schemas/content-brief.schema.json)).
4. Pakai skill/prompt yang sesuai (index di bawah).
5. Jalankan `python scripts/check_caption.py` dan QA gate di [qa/](./qa/claim-verification.md).
6. Catat approval di [templates/approval-record.md](./templates/approval-record.md).

## Index Rules

| No | Standard | Dipakai ketika |
|---|---|---|
| 01 | [Content Integrity](./rules/01-CONTENT-INTEGRITY-STANDARD.md) | Semua konten, selalu berlaku |
| 02 | [Hospitality Claim](./rules/02-HOSPITALITY-CLAIM-STANDARD.md) | Klaim fasilitas, rating, sertifikasi, harga, lokasi, positioning |
| 03 | [Client Brand Voice](./rules/03-CLIENT-BRAND-VOICE-STANDARD.md) | Menulis atas nama brand client |
| 04 | [Privacy, Consent & UGC](./rules/04-PRIVACY-CONSENT-UGC-STANDARD.md) | Ada foto/nama/review tamu, staf, atau UGC |
| 05 | [Platform](./rules/05-PLATFORM-STANDARD.md) | Format per platform, termasuk Reels, Stories, alt text |
| 06 | [Localization & Bahasa](./rules/06-LOCALIZATION-BAHASA-STANDARD.md) | Konten ID/EN atau multi-bahasa |
| 07 | [AI Visual & Disclosure](./rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md) | Ada visual AI atau editing berat |
| 08 | [Approval & Publication](./rules/08-APPROVAL-PUBLICATION-STANDARD.md) | Sebelum publish, selalu berlaku; review independen L2/L3 |
| 09 | [Data Classification](./rules/09-DATA-CLASSIFICATION.md) | Semua data, selalu berlaku |

## Index Skills

| Skill | Fungsi |
|---|---|
| [`draft-caption`](./skills/draft-caption/SKILL.md) | Caption IG/TikTok/FB sesuai brand voice & claim rule |
| [`draft-reel-script`](./skills/draft-reel-script/SKILL.md) | Script Reels/TikTok: hook, shot list, klaim & consent per shot |
| [`reply-guest-review`](./skills/reply-guest-review/SKILL.md) | Balas review tamu secara aman |
| [`build-content-calendar`](./skills/build-content-calendar/SKILL.md) | Kalender konten bulanan berbasis kalender Indonesia |
| [`write-ota-listing`](./skills/write-ota-listing/SKILL.md) | Deskripsi properti untuk OTA & website |
| [`localize-content`](./skills/localize-content/SKILL.md) | Lokalisasi ID ↔ EN |
| [`plan-seasonal-campaign`](./skills/plan-seasonal-campaign/SKILL.md) | Campaign musiman (Ramadan, Nataru, libur sekolah) |

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

Level 1 (manual/semi-manual) aktif: [automations/level-1-manual/README.md](./automations/level-1-manual/README.md).

## Task Management

Task board (Backlog → In Progress → Review → Done) tetap di repo arsip [CLAU-AI-CONTENT/tasks](https://github.com/d34faiza-commits/CLAU-AI-CONTENT/tree/main/tasks) dan GitHub Project **CLAU-AI-CONTENT Roadmap** (bisa menampung issue dari semua repo).

## Validation

```text
python scripts/validate.py
```

Mengecek file wajib, section rules/prompts/skills, frontmatter skill, versi dokumen, schema & contoh brief, link relatif, dan pola secret. Link ke `core/` dicek hanya bila submodule ter-init; CI tidak meng-clone submodule private.

## Lisensi

Proprietary, private use. Lihat [LICENSE](./LICENSE).

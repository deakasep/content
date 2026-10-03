# CLAU-AI-CONTENT

**AI Content Marketing Studio untuk Hospitality & Tourism Indonesia.**

Repository private berisi governance, rules, prompt library, AI agent skills, knowledge base, template, dan QA gate untuk memproduksi konten marketing hospitality yang **jujur, legal, on-brand, dan siap publish** — dengan AI sebagai content partner, bukan pengganti approval manusia.

> **Status:** Private — Foundation release (versi per dokumen: lihat [Versi Dokumen](#versi-dokumen))
> **Dokumen induk:** [CONTENT-CONSTITUTION.md](./CONTENT-CONSTITUTION.md)
> **Boundary:** [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md)
> **Credit:** [ACKNOWLEDGMENT.md](./ACKNOWLEDGMENT.md)

## Versi Dokumen

| Dokumen | Versi | Status |
|---|---|---|
| [CONTENT-CONSTITUTION.md](./CONTENT-CONSTITUTION.md) | 1.0.0 | Approved |
| [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md) | 0.1.4 | Draft |
| [WORKFLOW.md](./WORKFLOW.md) | 0.1.1 | Draft |
| [AGENTS.md](./AGENTS.md) | 0.1.2 | Draft |

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
3. Isi [templates/content-brief.md](./templates/content-brief.md) — valid terhadap [schemas/content-brief.schema.json](./schemas/content-brief.schema.json).
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

## Index Prompts

| Jenis | Prompt |
|---|---|
| Caption | [draft-instagram-caption](./prompts/caption/draft-instagram-caption.md) |
| Campaign | [plan-campaign](./prompts/campaign/plan-campaign.md) |
| OTA listing | [write-hotel-description](./prompts/ota-listing/write-hotel-description.md) |
| Review response | [reply-guest-review](./prompts/review-response/reply-guest-review.md) |
| Destination story | [storytelling-destination](./prompts/destination-story/storytelling-destination.md) |
| Seasonal promo | [seasonal-campaign](./prompts/promo-seasonal/seasonal-campaign.md) |
| Template | [prompt-template](./prompts/templates/prompt-template.md) |

## Validation

```text
python scripts/validate.py
```

Validator mengecek: file wajib, section wajib di rules/prompts/skills, frontmatter skill, `agents/openai.yaml`, JSON schema valid, relative link valid, dan pola secret sederhana. CI menjalankan validator yang sama di setiap push dan pull request.

## Batasan

Repository ini **tidak** menggantikan:

- approval tertulis dari owner/representative client;
- legal review untuk klaim sensitif (halal, sertifikasi, harga, kompetitor);
- verifikasi lapangan untuk klaim fisik properti;
- kebijakan platform (Meta, TikTok, Google, OTA) yang berlaku saat publish.

Data client, foto asli, review mentah, dan credential akun social media **tidak** disimpan di repo ini — lihat [CONTENT-BOUNDARY.md](./CONTENT-BOUNDARY.md).

## Lisensi

Proprietary, private use. Lihat [LICENSE](./LICENSE).

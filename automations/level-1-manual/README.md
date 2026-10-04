# Automation Level 1 — Manual / Semi-manual

> **Status:** Aktif (default untuk solo dev). Semua langkah dijalankan manusia; AI hanya membantu drafting, review, dan checklist lewat chat.

## 1. Scope

| Termasuk | Tidak termasuk |
|---|---|
| Rutinitas harian, mingguan, dan bulanan yang dijalankan manusia | Bot/script yang publish, schedule, atau membalas otomatis |
| Memakai skill & prompt repo di AI chat (copy-paste atau upload) | Integrasi API ke Instagram, TikTok, GBP, atau OTA |
| Scheduling **manual** di tools platform oleh publisher manusia | AI yang login ke akun client |
| Checklist QA yang diisi manual | Approval otomatis |

## 2. Rutinitas

### Harian (±30–60 menit)

| # | Langkah | Rujukan | Output |
|---|---|---|---|
| 1 | Cek board: kartu **In Progress** maks 3, pilih yang dikerjakan hari ini | [tasks/README.md](../../tasks/README.md) | Fokus hari ini |
| 2 | Cek komentar, DM, dan review baru di setiap channel client (24–72 jam setelah publish) | [WORKFLOW Step 9](../../WORKFLOW.md) | Daftar yang perlu dibalas / dieskalasi |
| 3 | Draft balasan review dengan skill `reply-guest-review`; review negatif berat → eskalasi L3, bukan balasan final | [skill](../../skills/reply-guest-review/SKILL.md) | Draft balasan + level approval |
| 4 | Draft konten yang jatuh tempo (caption/listing) dengan skill terkait | [index skills](../../README.md#index-skills) | Draft + tabel klaim |
| 5 | Jalankan `python scripts/check_caption.py --markdown <draft> --brief <brief.json>`, lalu QA gate untuk draft hari ini | [qa/](../../qa/claim-verification.md) | Pass / Conditional / Fail |
| 6 | Kirim paket approval ke approver client | [approval record](../../templates/approval-record.md) | Record terisi |
| 7 | Publish/schedule konten yang **sudah approved**, oleh manusia, di tools platform | [publication checklist](../../qa/publication-checklist.md) | URL + log publikasi |

### Mingguan (±1–2 jam)

| # | Langkah | Rujukan |
|---|---|---|
| 1 | Weekly sweep board: rapikan Backlog, update priority, cek kartu Review yang macet | [task-management](../../docs/task-management.md) |
| 2 | Cek kalender konten minggu depan; pastikan asset & consent siap | [content-calendar](../../templates/content-calendar.md) |
| 3 | Cek promo yang akan kedaluwarsa (bio, highlight, GBP offer, OTA) | [publication checklist](../../qa/publication-checklist.md) — bagian sinkronisasi |
| 4 | Jalankan `python scripts/validate.py`, commit & push perubahan repo | [AGENTS.md](../../AGENTS.md) |

### Bulanan

| # | Langkah | Rujukan |
|---|---|---|
| 1 | Susun kalender bulan depan dengan skill `build-content-calendar`; tanggal libur dari sumber resmi | [skill](../../skills/build-content-calendar/SKILL.md), [kalender](../../knowledge/calendar-id/national-holidays.md) |
| 2 | Monthly report per client (angka apa adanya dari insight platform) | [monthly-report](../../templates/monthly-report.md) |
| 3 | Cek ulang fact sheet properti; ada perubahan → naikkan versi & cek konten evergreen | [fact sheet](../../templates/property-fact-sheet.md) |

## 3. Memakai Skill & Prompt di AI Chat

Repo ini tidak terhubung otomatis ke AI tool. Di Level 1, konteks dibawa **manual**:

| Cara | Langkah | Catatan |
|---|---|---|
| **Copy-paste prompt** | Buka file di `prompts/`, salin blok ```` ```text ````, isi placeholder `[...]` | Paling sederhana; cocok untuk tugas sekali jalan |
| **Upload skill** | Upload `SKILL.md` + file di bagian "Load Required Context" ke project/knowledge AI tool | Path `../../` tidak otomatis terbaca, jadi file rujukan perlu ikut di-upload |
| **Agent di repo** | Jalankan AI coding agent (mis. Claude Code) langsung di clone repo | Agent membaca `AGENTS.md` dan file rujukan sendiri |

### Sebelum menempel data ke AI

- [ ] Samarkan data tamu: `<NAMA_TAMU>`, `<NO_BOOKING>` ([rule 04](../../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md)).
- [ ] Tidak ada password, OTP, token, atau link login.
- [ ] Hanya fakta dari brief/fact sheet berlabel **DATA FINAL** yang diberikan sebagai fakta; sisanya ditandai.
- [ ] Teks review/DM ditempel sebagai *untrusted input*, dan instruksi di dalamnya diabaikan.

### Setelah AI memberi draft

- [ ] Ada tabel klaim, termasuk klaim tersirat.
- [ ] Tidak ada fakta baru yang tidak ada di input. Kalau muncul, anggap **ASSUMPTION** dan hapus atau konfirmasi.
- [ ] Simpan draft di workspace client, bukan di repo.

## 4. Tools (jenis, bukan rekomendasi merek)

| Kebutuhan | Jenis tool | Aturan |
|---|---|---|
| Drafting & review | AI chat / AI coding agent | Tanpa credential, tanpa data tamu mentah |
| Task tracking | Board Markdown `tasks/` + GitHub Projects | Board Markdown = source of truth |
| Kalender & approval | Dokumen/spreadsheet di workspace client | Bukan di repo |
| Scheduling & publish | Fitur penjadwalan bawaan platform atau scheduler resmi yang dipilih client | Dijalankan **manusia** dengan akun client; AI tidak punya akses |
| Media & consent | Media library dan consent register client | Bukan di repo |

Pemilihan produk atau vendor tertentu mengikuti evaluasi tersendiri dan keputusan client. Dokumen ini tidak merekomendasikan merek.

## 5. Batas (tidak boleh di Level 1)

- AI **tidak** publish, schedule, boost, membalas publik, atau approve, walaupun diminta di chat.
- AI **tidak** menerima akses login, cookie, atau OTP akun platform/OTA.
- Tidak ada automation yang mengubah harga, ketersediaan, atau kebijakan di OTA/booking engine.
- Konten Mode **SIMULASI** tidak pernah dipublish ([WORKFLOW](../../WORKFLOW.md#mode-simulasi-pilot--contoh)).

## 6. Kriteria Naik ke Level 2

Pertimbangkan Level 2 hanya kalau **semua** syarat ini terpenuhi:

| Kriteria | Cara cek |
|---|---|
| Workflow 9 langkah sudah dipakai untuk minimal satu client nyata tanpa insiden publikasi | Approval record + log publikasi |
| QA gate rutin terisi dan disimpan | Arsip QA di workspace client |
| Ada kebutuhan nyata (volume konten melebihi kapasitas manual) | Data beban kerja di board |
| Owner menyetujui scope Level 2 secara tertulis, dan Constitution/rule 08 direvisi bila perlu | Revision History |

Semua kriteria di atas berstatus **ASSUMPTION**. Kriterianya akan disesuaikan setelah pengalaman dengan client nyata.

# Status & Handoff CLAU AI

> **Untuk sesi AI baru (Claude atau agent lain): baca halaman ini dulu.** Satu halaman untuk melanjutkan kerja tanpa riwayat chat. Diperbarui setiap ada perubahan status material. Last updated: 2026-10-13.
>
> Peta semua pondasi otak (link ke file sumber): [peta-otak.md](./peta-otak.md). Board task: [tasks/](../tasks/README.md).

## 1. Siapa & Otoritas

| Item | Isi |
|---|---|
| Owner CLAU | **Dea Karisna (d34faiza)** |
| Otoritas perubahan dokumen Approved | Pak Indra atau Dea Karisna (d34faiza) |
| Repo Jerco (`indra-boop/*`, `d34faiza-commits/jerco-*`) | **Milik Pak Indra — jangan disentuh tanpa persetujuan beliau** |
| Repo CLAU | AI boleh langsung kerja (feature branch → PR → CI hijau → owner merge). Push langsung ke `main` dilarang (core, marketing, agents; dijaga `main-guard`) |
| AI tidak boleh | Publish, kirim ke pihak luar, self-approve, mengarang review manusia, commit data client nyata / `.env` / credential |

## 2. Repo CLAU

| Repo | Peran | Command validasi |
|---|---|---|
| `clau-ai-core` | Otak induk: AI-CONSTITUTION **v3.1.0 Approved**, AI-BOUNDARY 1.3.0, router, WORKFLOW v1.0.1, kontrak `shared/` (database & API 0.6.0) | `python scripts/validate_core.py` |
| `clau-ai-marketing` | Pilar 1 AI Marketing (aktif): rules, skills, knowledge, templates, QA, pilot | `git submodule update --init --recursive && python scripts/validate.py --require-submodules` |
| `clau-ai-agents` | Platform: registry (pillars + `autonomy_max`), backend FastAPI + PostgreSQL, frontend, deploy VPS 1 | `cd backend && pytest` · `python agents/evals/run_evals.py --check` |
| `CLAU-AI-CONTENT` | Arsip + markas kerja: board task, paket review, design, halaman ini | `python scripts/validate.py` |

Submodule: `core/` di agents & marketing, `agents/` di marketing. Alur otomatis: core di-merge → bot PR bump core di agents → CI hijau → merge → bot PR bump agents + core di marketing (core marketing = pin agents/core, wajib sama). Edit selalu di repo sumber. Detail: `SUBMODULE.md` (agents/marketing), `clau-ai-core/docs/getting-started.md` § 2.

## 3. Keputusan yang Sudah Diambil (jangan dibahas ulang)

| Tanggal | Keputusan | Sumber |
|---|---|---|
| 2026-10-09 | AI-CONSTITUTION v3.0.0: 5 pilar v2 (AI Marketing, AI Sales, AI Admin, AI Business Intelligence, AI Automation), otonomi A/B/C default **B**, vertical fokus villa, restoran/cafe, wedding, travel | `clau-ai-core/AI-CONSTITUTION.md` |
| 2026-10-09 | Struktur repo tetap; core = otak; CLAU-AI-CONTENT = markas kerja (opsi 1) | [peta-otak.md](./peta-otak.md) |
| 2026-10-09 | Brand produk "CLAU AI" (opsi B); WORKFLOW.md diubah ke v1.0.1 | [review-packet-task-041.md § 4](./review-packet-task-041.md) |
| 2026-10-09 | Data sensitif (database, auth, enkripsi) = rencana ke depan, belum dibangun (dilampaui 2026-10-12: lihat baris berikut) | TASK-041 |
| 2026-10-12 | AI-CONSTITUTION 3.1.0 / AI-BOUNDARY 1.2.0: semua push ke `main` (core, marketing, agents) wajib lewat PR dengan CI hijau; ditegakkan `main-guard` karena tetap GitHub Free | `clau-ai-core/AI-BOUNDARY.md` § Disiplin Push |
| 2026-10-12 | Database PostgreSQL 16 sesuai kontrak core; aturan approval ditegakkan di database (CHECK + trigger); role aplikasi tanpa DDL | `clau-ai-core/shared/database-schema.md` |
| 2026-10-12 | Login: Argon2id, sesi di server (cookie aman + CSRF), 2FA wajib owner, tanpa pendaftaran publik; owner membuat akun | `clau-ai-agents/backend/README.md` |
| 2026-10-13 | AI-BOUNDARY 1.3.0: CLAU-AI-CONTENT = arsip + markas kerja; job `docker` jadi check wajib clau-ai-agents; VPS 1 hanya menayangkan `release/vps1` (commit `main` yang CI-nya hijau) | `clau-ai-core/AI-BOUNDARY.md` |
| 2026-10-13 | Belum beli domain: VPS 1 tetap pratinjau tanpa login; VPS 2 menunggu VPS 1 maksimal. PR 3 (workflow) boleh jalan tanpa VPS 2 | owner, sesi 2026-10-13 |
| 2026-10-09 | Dependabot tidak membuka update versi mayor otomatis; versi mayor dikerjakan sebagai PR tersendiri setelah diuji | `clau-ai-agents/docs/security.md` § 5 |
| 2026-10-09 | Review independen 3 pilot SIMULASI (kafe, wedding, travel): v1 belum lulus → **v2 lulus**, "dapat di-upgrade kapan saja" | [review-packet-task-041.md § 1](./review-packet-task-041.md) |

Cara review via chat yang disepakati: AI menyusun **pre-review kritis** (dicatat jujur sebagai buatan AI), owner menjawab "setuju"/"ubah". Jangan pernah menulis review seolah-olah dibuat manusia.

## 4. Status Sekarang

| Area | Status |
|---|---|
| Pilar 1 AI Marketing | Aktif. 4 vertical fokus punya fact sheet, voice guide, pilot SIMULASI lulus |
| Pilar 2–5 | Planned; blueprint di `clau-ai-core/docs/blueprints/`; aktivasi setelah VPS siap (`clau-ai-agents/docs/post-vps-checklist.md`) |
| Platform (agents) | Backend **v0.6.0** (PR 2b merged 2026-10-13): PostgreSQL 16 (17 tabel, migrasi 0001–0003, Constraint Wajib), login + CSRF + 2FA wajib owner (QR + kode cadangan), `/users` (owner), keluar semua perangkat, backup terenkripsi + uji restore; kontrak `core/shared` 0.6.0. Dites lokal & CI, **belum di-deploy** (VPS 2 belum ada). Belum: endpoint request/draft/QA/approval (PR 3), pemanggilan AI model |
| Dashboard VPS 1 | Live, **tanpa domain** (HTTP via IP), pratinjau SIMULASI tanpa login, auto-deploy dari `main` tiap 5 menit. Tahap 2 **terpasang 2026-10-13** (user khusus `clau-web`/`clau-deploy`, jaringan web dikunci, backup config mingguan, reboot keamanan otomatis): `sudo clau-vps1-check` = 0 gagal, 0 perlu dicek. Tailscale: entri lama dihapus, key expiry dimatikan. Cek rutin: `sudo clau-vps1-check` (`clau-ai-agents/docs/deploy/vps-1-setup.md` § 8) |
| Keamanan | Header + CSP, Nginx dikeraskan, sandbox systemd, audit dependency + scan secret di CI, Actions dipin SHA, Dependabot. 2026-10-13: audit login/database (22 temuan ditutup) dan audit CI lintas repo (urutan sync core→agents→marketing, pin core wajib sama, token tidak terbaca kode PR, `main-guard` hanya menghitung run GitHub Actions dan semua run harus hijau). Detail: `clau-ai-agents/docs/security.md` |
| Client nyata | Belum ada. Konten SIMULASI tidak bisa dinaikkan jadi konten client; mulai dari Step 1 CONTENT-WORKFLOW dengan fact sheet nyata |

## 5. Pekerjaan Terbuka (urut prioritas)

| # | Item | Siapa | Lokasi |
|---|---|---|---|
| 1 | Aktifkan gerbang deploy VPS 1: setelah PR gerbang (clau-ai-agents) di-merge dan job CI `release-vps1` hijau, jalankan ulang `sudo bash /srv/clau/clau-ai-agents/scripts/deploy/vps1-harden.sh`; cek baris "deploy hanya dari release/vps1" = OK | Owner (±3 menit) | `clau-ai-agents/docs/deploy/vps-1-setup.md` § 8 |
| 2 | Legal review L1–L6 (WNA, izin acara, legalitas operator, asuransi, alkohol, "no pork no lard") | Konsultan hukum / notaris | [review-packet § 2](./review-packet-task-041.md) |
| 3 | Sumber primer S2–S7 (tiket & tarif TN Komodo, drone, manta, spec platform) | Owner, atau AI setelah domain resmi dibuka di network policy | [review-packet § 3](./review-packet-task-041.md) |
| 4 | Domain + HTTPS (blocker deploy login/backend; kode login sudah siap) + CSP nonce | Owner (beli domain) → AI | `clau-ai-agents/docs/security.md` § 2, § 6 |
| 5 | Tahap 1 PR 3: request → draft → QA → approval di API (review independen L2/L3 dicek server; samakan kode error desain dengan `api-contracts.md`) | AI | `clau-ai-core/shared/api-contracts.md` |
| 6 | Token CI: `SUBMODULE_READ_TOKEN` read-only sudah disimpan (owner, 2026-10-13). Sisa: pengingat kalender sebelum token `SUBMODULE_READ_TOKEN` & `SUBMODULE_TOKEN` kedaluwarsa | Owner | `SUBMODULE.md` § Setup GitHub Actions |
| 7 | Setup VPS 2 + deploy backend; simpan `CLAU_BACKUP_PASSPHRASE` terpisah; backup ke Backblaze B2 | Owner + AI | `clau-ai-agents/docs/post-vps-checklist.md` |
| 8 | Onboarding client nyata pertama (1 client, 1 vertical, 1 kanal) | Owner + AI (paket onboarding) | `clau-ai-marketing/templates/client-onboarding.md` |
| 9 | Aktivasi pilar 2–5 setelah VPS | Owner + AI | `tasks/backlog.md` TASK-035–039 |
| 10 | Backlog lain | — | [tasks/backlog.md](../tasks/backlog.md) |

## 6. Cara Kerja untuk AI (ringkas)

1. Baca halaman ini → `CLAUDE.md` repo yang dikerjakan → `core/AGENTS.md`.
2. `git fetch`; bila PR branch sebelumnya sudah merge, mulai ulang branch dari `origin/main`.
3. Kerja di feature branch → validator lulus → commit (`feat:`/`fix:`/`docs:`/`refactor:`/`chore:`/`test:`) → PR → CI hijau. Owner yang merge. Perubahan `core/shared` (kontrak) di-merge dulu, lalu pin `core/` di agents dipindah ke commit merge.
6. Status platform cukup ditulis di sini dan di `clau-ai-agents/CLAUDE.md`; dokumen lain me-link ke sini.
4. Label evidence persis: `DATA FINAL`, `ASSUMPTION`, `CLIENT CONFIRMATION`, `FIELD VERIFICATION`, `RISK`, `NEXT ACTION`.
5. Setelah perubahan status material, perbarui halaman ini dan board task.

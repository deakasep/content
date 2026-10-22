# Status & Handoff CLAU AI

> **Untuk sesi AI baru (Claude atau agent lain): baca halaman ini dulu.** Satu halaman untuk melanjutkan kerja tanpa riwayat chat. Diperbarui setiap ada perubahan status material. Last updated: 2026-10-22.
>
> Peta semua pondasi otak (link ke file sumber): [peta-otak.md](./peta-otak.md). Board task: **ClickUp** → workspace Jerco Holding Company → Space **Clau AI** → folder **CLAU AI** (board utama sejak 2026-10-21); [tasks/](../tasks/README.md) = riwayat.

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
| `clau-core` | Otak induk: AI-CONSTITUTION **v3.1.0 Approved**, AI-BOUNDARY 1.5.0 (1.6.0 diusulkan di [core#17](https://github.com/d34faiza-commits/clau-core/pull/17)), router, WORKFLOW v1.0.1, kontrak `shared/` (database & API 0.9.0) | `python scripts/validate_core.py` |
| `clau-market` | Pilar 1 AI Marketing (aktif): rules, skills, knowledge, templates, QA, pilot | `git submodule update --init --recursive && python scripts/validate.py --require-submodules` |
| `clau-agent` | Platform: registry (pillars + `autonomy_max`), backend FastAPI + PostgreSQL, frontend, deploy VPS 1 | `cd backend && pytest` · `python agents/evals/run_evals.py --check` |
| `clau-content` | Arsip + markas kerja: board task, paket review, design, halaman ini | `python scripts/validate.py` |

Submodule: `core/` di agents & marketing, `agents/` di marketing. Alur otomatis: core di-merge → bot PR bump core di agents → CI hijau → merge → bot PR bump agents + core di marketing (core marketing = pin agents/core, wajib sama). Edit selalu di repo sumber. Detail: `SUBMODULE.md` (agents/marketing), `clau-core/docs/getting-started.md` § 2.

## 3. Keputusan yang Sudah Diambil (jangan dibahas ulang)

| Tanggal | Keputusan | Sumber |
|---|---|---|
| 2026-10-09 | AI-CONSTITUTION v3.0.0: 5 pilar v2 (AI Marketing, AI Sales, AI Admin, AI Business Intelligence, AI Automation), otonomi A/B/C default **B**, vertical fokus villa, restoran/cafe, wedding, travel | `clau-core/AI-CONSTITUTION.md` |
| 2026-10-09 | Struktur repo tetap; core = otak; clau-content = markas kerja (opsi 1) | [peta-otak.md](./peta-otak.md) |
| 2026-10-09 | Brand produk "CLAU AI" (opsi B); WORKFLOW.md diubah ke v1.0.1 | [review-packet-task-041.md § 4](./review-packet-task-041.md) |
| 2026-10-09 | Data sensitif (database, auth, enkripsi) = rencana ke depan, belum dibangun (dilampaui 2026-10-12: lihat baris berikut) | TASK-041 |
| 2026-10-12 | AI-CONSTITUTION 3.1.0 / AI-BOUNDARY 1.2.0: semua push ke `main` (core, marketing, agents) wajib lewat PR dengan CI hijau; ditegakkan `main-guard` karena tetap GitHub Free | `clau-core/AI-BOUNDARY.md` § Disiplin Push |
| 2026-10-12 | Database PostgreSQL 16 sesuai kontrak core; aturan approval ditegakkan di database (CHECK + trigger); role aplikasi tanpa DDL | `clau-core/shared/database-schema.md` |
| 2026-10-12 | Login: Argon2id, sesi di server (cookie aman + CSRF), 2FA wajib owner, tanpa pendaftaran publik; owner membuat akun | `clau-agent/backend/README.md` |
| 2026-10-13 | AI-BOUNDARY 1.3.0: clau-content = arsip + markas kerja; job `docker` jadi check wajib clau-agent; VPS 1 hanya menayangkan `release/vps1` (commit `main` yang CI-nya hijau) | `clau-core/AI-BOUNDARY.md` |
| 2026-10-13 | Belum beli domain: VPS 1 tetap pratinjau tanpa login; VPS 2 menunggu VPS 1 maksimal. PR 3 (workflow) boleh jalan tanpa VPS 2 | owner, sesi 2026-10-13 |
| 2026-10-16 | AI-BOUNDARY v1.4.0 § Data ke Provider AI: hanya fakta yang dikonfirmasi klien + request disamarkan ke model AI; panggilan dicatat tanpa isi; API key hanya di worker VPS 2; hasil AI selalu draft (owner: "setuju gas") | `clau-core/AI-BOUNDARY.md` |
| 2026-10-16 | Repo di-rename: clau-core, clau-agent, clau-market, clau-content (isi tetap) dan dijadikan **public, hanya untuk dilihat**: LICENSE source-available di keempat repo, AI-BOUNDARY v1.5.0 (semua yang di-commit termasuk riwayat dianggap publik, tanpa IP/host server). Download/clone/screenshot tidak bisa dicegah secara teknis; perlindungannya hukum (owner: "Gass B kak") | `LICENSE`, `clau-core/AI-BOUNDARY.md` |
| 2026-10-15 | Pemulihan database selalu **manual** (satu perintah `clau-vps2-restore` yang dijalankan manusia); server yang mati boleh hidup lagi otomatis, isi database tidak pernah diganti otomatis. Backup tiap 6 jam + salinan Backblaze B2 | owner, sesi 2026-10-15; `clau-agent/docs/deploy/vps-2-setup.md` § 2, § 5 |
| 2026-10-15 | VPS 2 jalan **tanpa domain** dulu: backend + database + frontend login di VPS 2, dibuka hanya lewat HTTPS Tailscale (tim internal). Setelah domain ada, frontend kembali ke VPS 1 (keputusan VPS #1) | owner, sesi 2026-10-15; `clau-agent/docs/deploy/vps-2-setup.md` § 2 |
| 2026-10-21 | Board kerja CLAU pindah ke **ClickUp** (Space **Clau AI**, terpisah dari Jerco; alur Open → in progress → review → Closed seperti board Rekan AI). Satu list per pilar + Platform + Release & Deploy; judul kartu memuat `TASK-xxx`. Board Markdown `tasks/` dibekukan sebagai riwayat; task baru mulai TASK-064 di ClickUp (arahan Pak Indra lewat telepon dengan owner) | [tasks/README.md § Board ClickUp](../tasks/README.md#board-clickup) |
| 2026-10-09 | Dependabot tidak membuka update versi mayor otomatis; versi mayor dikerjakan sebagai PR tersendiri setelah diuji | `clau-agent/docs/security.md` § 5 |
| 2026-10-09 | Review independen 3 pilot SIMULASI (kafe, wedding, travel): v1 belum lulus → **v2 lulus**, "dapat di-upgrade kapan saja" | [review-packet-task-041.md § 1](./review-packet-task-041.md) |

Cara review via chat yang disepakati: AI menyusun **pre-review kritis** (dicatat jujur sebagai buatan AI), owner menjawab "setuju"/"ubah". Jangan pernah menulis review seolah-olah dibuat manusia.

## 4. Status Sekarang

| Area | Status |
|---|---|
| Pilar 1 AI Marketing | Aktif. 4 vertical fokus punya fact sheet, voice guide, pilot SIMULASI lulus |
| Pilar 2–5 | Planned; blueprint di `clau-core/docs/blueprints/`; aktivasi setelah VPS siap (`clau-agent/docs/post-vps-checklist.md`) |
| Platform (agents) | Backend **v0.9.0** (PR 2b merged 2026-10-13, PR 3 & 3b merged 2026-10-14, antrean AI agents#54 + UI PR 4d): PostgreSQL 16 (21 tabel, migrasi 0001–0006, Constraint Wajib), login + CSRF + 2FA wajib owner (QR + kode cadangan), `/users` (owner), keluar semua perangkat, backup terenkripsi + uji restore; kontrak `core/shared` 0.8.0. Dites lokal & CI; **live di VPS 2 sejak 2026-10-15** (lihat baris VPS 2). Workflow ([agents#46](https://github.com/d34faiza-commits/clau-agent/pull/46)): request → draft → QA → approval, Rule 08 ditegakkan server + database (migrasi 0004), isolasi klien, 14 temuan audit adversarial diperbaiki. Fact sheet ([agents#48](https://github.com/d34faiza-commits/clau-agent/pull/48)): klien, fact sheet & Konfirmasi Fakta oleh klien (migrasi 0005, 18 tabel), UI `/requests` & `/fact-sheets`, 10 temuan audit adversarial diperbaiki. Antrean AI (migrasi 0006): job, worker terpisah, AI fact-check, batas biaya, provider tiruan. Belum: provider AI nyata (PR 4c) |
| Backend VPS 2 | Live **tanpa domain** di `https://clau-vps2.<tailnet>.ts.net` (hanya perangkat di tailnet, bukan klien). Versi 0.9.0 (antrean AI + worker, provider tiruan, AI mati). SSH hanya lewat Tailscale, auto-deploy `release/vps1` + rollback skema, backup terenkripsi **tiap 6 jam** + salinan **Backblaze B2** (Object Lock 30 hari), pemulihan manual `clau-vps2-restore` (termasuk server pengganti). Owner + 2FA; passphrase backup & `CLAU_SECRET_KEY` & key B2 di password manager owner. `sudo clau-vps2-check` = **0 gagal, 0 perlu dicek** (2026-10-19). Panduan: `clau-agent/docs/deploy/vps-2-setup.md` |
| Dashboard VPS 1 | Live, **tanpa domain** (HTTP via IP), pratinjau SIMULASI tanpa login, auto-deploy dari `main` tiap 5 menit. Tahap 2 **terpasang 2026-10-13** (user khusus `clau-web`/`clau-deploy`, jaringan web dikunci, backup config mingguan, reboot keamanan otomatis): `sudo clau-vps1-check` = 0 gagal, 0 perlu dicek. Tailscale: entri lama dihapus, key expiry dimatikan. Gerbang deploy aktif 2026-10-13: hanya `release/vps1` (commit `main` yang CI-nya hijau) yang tayang. Cek rutin: `sudo clau-vps1-check` (`clau-agent/docs/deploy/vps-1-setup.md` § 8) |
| Keamanan | Header + CSP, Nginx dikeraskan, sandbox systemd, audit dependency + scan secret di CI, Actions dipin SHA, Dependabot. 2026-10-13: audit login/database (22 temuan ditutup) dan audit CI lintas repo (urutan sync core→agents→marketing, pin core wajib sama, token tidak terbaca kode PR, `main-guard` hanya menghitung run GitHub Actions dan semua run harus hijau). Detail: `clau-agent/docs/security.md` |
| Client nyata | Belum ada. Konten SIMULASI tidak bisa dinaikkan jadi konten client; mulai dari Step 1 CONTENT-WORKFLOW dengan fact sheet nyata |

## 5. Pekerjaan Terbuka (urut prioritas)

| # | Item | Siapa | Lokasi |
|---|---|---|---|
| 1 | Legal review L1–L6 (WNA, izin acara, legalitas operator, asuransi, alkohol, "no pork no lard") | Konsultan hukum / notaris | [review-packet § 2](./review-packet-task-041.md) |
| 2 | Sumber primer S2–S7 (tiket & tarif TN Komodo, drone, manta, spec platform) | Owner, atau AI setelah domain resmi dibuka di network policy | [review-packet § 3](./review-packet-task-041.md) |
| 3 | Domain + HTTPS publik (blocker login klien; tim internal sudah login lewat HTTPS Tailscale di VPS 2) + CSP nonce; lalu kembali ke keputusan VPS #1 (frontend di VPS 1) | Owner (beli domain) → AI | `clau-agent/docs/security.md` § 2, § 6 |
| 4 | Tahap 2 (AI menulis draft, TASK-052): AI-BOUNDARY v1.4.0 disetujui owner 2026-10-16; kontrak 0.9.0 (core#16) + antrean, worker, AI fact-check, batas biaya, provider tiruan (agents#54) dibangun. UI PR 4d selesai (`/requests/[id]` *Buat draft dengan AI*, `/ai-usage`). Sisa: provider Claude PR 4c (butuh akun API, batas biaya, retensi data dari owner) | AI → Owner | TASK-052 |
| 5 | Token CI: `SUBMODULE_READ_TOKEN` read-only sudah disimpan (owner, 2026-10-13). Sisa: pengingat kalender sebelum token `SUBMODULE_READ_TOKEN` & `SUBMODULE_TOKEN` kedaluwarsa | Owner | `SUBMODULE.md` § Setup GitHub Actions |
| 6 | VPS 2 selesai: setup A–I, backup 6 jam + B2 aktif (2026-10-19; TASK-049 Done). VPS 1 pengganti satu perintah: `vps1-setup.sh` (agents#57). Sisa: uji coba "VPS 2 hilang total" di VPS sementara (±30 menit, sekali) | Owner + AI | `clau-agent/docs/deploy/vps-2-setup.md` § 5, `vps-1-setup.md` § 0 |
| 7 | Onboarding client nyata pertama (1 client, 1 vertical, 1 kanal) | Owner + AI (paket onboarding) | `clau-market/templates/client-onboarding.md` |
| 8 | Aktivasi pilar 2–5 setelah VPS | Owner + AI | `tasks/backlog.md` TASK-035–039 |
| 8a | AI-BOUNDARY 1.6.0 ([core#17](https://github.com/d34faiza-commits/clau-core/pull/17), TASK-064): kapan PR boleh disebut selesai + versi live hanya maju (pola Jerco rule 23 & 20, ditulis ulang). Sisa: owner merge, lalu bot sync membawa core ke agents & marketing | Owner | clau-core `AI-BOUNDARY.md` § Disiplin Push |
| 8b | TASK-050 CI hemat menit: run CI repo public tercatat 0 menit berbayar (2026-10-22), jadi workflow tidak diubah. Kartu di **review**: owner putuskan tutup. Bila repo kembali private, task dibuka ulang | Owner | Kartu ClickUp TASK-050 |
| 8c | TASK-054 keamanan sebelum klien login: 2FA wajib content lead, pembersihan sesi harian VPS 2, prosedur rotasi secret. PR [core#19](https://github.com/d34faiza-commits/clau-core/pull/19) (kontrak 0.9.1, merge dulu) lalu [agents#60](https://github.com/d34faiza-commits/clau-agent/pull/60). Setelah merge: ulangi `vps2-setup.sh` sekali di VPS 2 | Owner | `clau-agent/docs/deploy/vps-2-setup.md` § 4a |
| 8d | TASK-032 level approval otomatis (hospitality: review negatif, terjemahan, harga/promo, orang, iklan, agama/adat): menunggu keputusan owner K1–K6 | Owner → AI | [review-packet-task-032.md](./review-packet-task-032.md) |
| 9 | Backlog lain | — | ClickUp Space **Clau AI** (riwayat: [tasks/backlog.md](../tasks/backlog.md)) |

## 5a. Roadmap ke "maksimal" (urutan disepakati owner 2026-10-15)

Board: ClickUp Space **Clau AI** (riwayat: [tasks/](../tasks/README.md)). Urutan kerja; tahap berikutnya dipicu beban/jumlah klien, bukan tanggal.

| Tahap | Isi | Task |
|---|---|---|
| A. Segera | Backup 6 jam + B2 + pemulihan manual (agents#54, selesai), CI hemat menit (tidak diperlukan selama repo public: GitHub Actions gratis, dicek 2026-10-22), uji "VPS 2 hilang total" | TASK-049, 050, 051 |
| B. Sebelum klien nyata pertama | Domain + HTTPS, **Tahap 2 AI menulis draft** → **AI Content Agent "Paket Konten Bulanan"** (produk pertama yang menghasilkan uang), legal & UU PDP, keamanan tambahan, onboarding klien pertama | TASK-047, **052 (sedang dirancang)**, **063**, 053, 054, 055 |
| C. Menuju ±30 klien | Monitoring & alarm, staging, dashboard biaya & kualitas AI, SOP tim, penagihan | TASK-056–060 |
| D. 200+ klien | Worker terpisah, database terkelola, 2+ server aplikasi, pentest | TASK-061 |
| E. Non-teknis | Tim reviewer (batas kapasitas sebenarnya), bukti hasil, sumber primer S2–S7 | TASK-059, 062, 041 |

Prinsip produk (owner 2026-10-15): tidak ada AI → langsung publish; alur = AI menghasilkan → AI fact-check ke data klien → owner review → approve (+ klien) → final. Urutan agent: Content → Sales → Customer Service → SEO → Advertising → Business (peta ke pilar: usulan Tahap 2 § 1a).

Prinsip skala (owner 2026-10-15): 12 agent = satu aplikasi di VPS 2, bukan satu server per agent; server ditambah bertahap sesuai beban tanpa membangun ulang.

## 6. Cara Kerja untuk AI (ringkas)

1. Baca halaman ini → `CLAUDE.md` repo yang dikerjakan → `core/AGENTS.md`.
2. `git fetch`; bila PR branch sebelumnya sudah merge, mulai ulang branch dari `origin/main`.
3. Kerja di feature branch → validator lulus → commit (`feat:`/`fix:`/`docs:`/`refactor:`/`chore:`/`test:`) → PR → CI hijau. Owner yang merge. Perubahan `core/shared` (kontrak) di-merge dulu, lalu pin `core/` di agents dipindah ke commit merge.
4. Label evidence persis: `DATA FINAL`, `ASSUMPTION`, `CLIENT CONFIRMATION`, `FIELD VERIFICATION`, `RISK`, `NEXT ACTION`.
5. Setelah perubahan status material, perbarui halaman ini dan **kartu ClickUp** yang terkait (lewat konektor ClickUp bila ada; bila tidak, sebutkan ke owner kartu mana yang perlu dipindah). Kartu **Closed** hanya bila PR merge dan CI hijau, dicek langsung di GitHub.
6. Status platform cukup ditulis di sini dan di `clau-agent/CLAUDE.md`; dokumen lain me-link ke sini.

## 7. Pindah Akun Claude

Semua kerja tersimpan di GitHub, bukan di akun claude.ai. Akun Claude lain tetap bisa melanjutkan kerja selama:

1. Akun Claude baru disambungkan ke akun GitHub yang sama (`d34faiza-commits`) lewat claude.ai/connect-github. Kalau akun GitHub-nya berbeda, akun itu harus ditambahkan sebagai collaborator di repo CLAU (dan oleh Pak Indra untuk repo Jerco).
2. Semua kerja penting sudah di-commit, di-push, dan masuk `main` lewat PR. Yang hanya ada di chat tidak ikut pindah.
3. Halaman ini sudah mencerminkan status terakhir.

Tidak ikut pindah: riwayat chat/sesi, memory & Projects claude.ai, pengaturan environment Claude Code (network policy, secret, setup script), scheduled task, dan connector (mis. **ClickUp**, Google Drive; sambungkan ulang di claude.ai/customize/connectors lalu mulai sesi baru). Saat membuat sesi baru, pilih repo dengan nama baru (`clau-core`, `clau-agent`, `clau-market`, `clau-content`) supaya pemantauan PR berjalan. Siapkan ulang di akun baru; secret diambil dari password manager owner, tidak pernah dari repo.

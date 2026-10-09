# Status & Handoff CLAU AI

> **Untuk sesi AI baru (Claude atau agent lain): baca halaman ini dulu.** Satu halaman untuk melanjutkan kerja tanpa riwayat chat. Diperbarui setiap ada perubahan status material. Last updated: 2026-10-09.
>
> Peta semua pondasi otak (link ke file sumber): [peta-otak.md](./peta-otak.md). Board task: [tasks/](../tasks/README.md).

## 1. Siapa & Otoritas

| Item | Isi |
|---|---|
| Owner CLAU | **Dea Karisna (d34faiza)** |
| Otoritas perubahan dokumen Approved | Pak Indra atau Dea Karisna (d34faiza) |
| Repo Jerco (`indra-boop/*`, `d34faiza-commits/jerco-*`) | **Milik Pak Indra — jangan disentuh tanpa persetujuan beliau** |
| Repo CLAU | AI boleh langsung kerja (feature branch → PR → owner merge) |
| AI tidak boleh | Publish, kirim ke pihak luar, self-approve, mengarang review manusia, commit data client nyata / `.env` / credential |

## 2. Repo CLAU

| Repo | Peran | Command validasi |
|---|---|---|
| `clau-ai-core` | Otak induk: AI-CONSTITUTION **v3.0.0 Approved**, AI-BOUNDARY, router, WORKFLOW v1.0.1 | `python scripts/validate_core.py` |
| `clau-ai-marketing` | Pilar 1 AI Marketing (aktif): rules, skills, knowledge, templates, QA, pilot | `git submodule update --init --recursive && python scripts/validate.py --require-submodules` |
| `clau-ai-agents` | Platform: registry (pillars + `autonomy_max`), backend FastAPI, frontend | `cd backend && pytest` · `python agents/evals/run_evals.py --check` |
| `CLAU-AI-CONTENT` | Arsip + markas kerja: board task, paket review, design, halaman ini | `python scripts/validate.py` |

Submodule: `core/` di agents & marketing, `agents/` di marketing. Bot sync PR menaikkan pin; edit selalu di repo sumber.

## 3. Keputusan yang Sudah Diambil (jangan dibahas ulang)

| Tanggal | Keputusan | Sumber |
|---|---|---|
| 2026-10-09 | AI-CONSTITUTION v3.0.0: 5 pilar v2 (AI Marketing, AI Sales, AI Admin, AI Business Intelligence, AI Automation), otonomi A/B/C default **B**, vertical fokus villa, restoran/cafe, wedding, travel | `clau-ai-core/AI-CONSTITUTION.md` |
| 2026-10-09 | Struktur repo tetap; core = otak; CLAU-AI-CONTENT = markas kerja (opsi 1) | [peta-otak.md](./peta-otak.md) |
| 2026-10-09 | Brand produk "CLAU AI" (opsi B); WORKFLOW.md diubah ke v1.0.1 | [review-packet-task-041.md § 4](./review-packet-task-041.md) |
| 2026-10-09 | Data sensitif (database, auth, enkripsi) = rencana ke depan, belum dibangun | TASK-041 |
| 2026-10-09 | Dependabot tidak membuka update versi mayor otomatis; versi mayor dikerjakan sebagai PR tersendiri setelah diuji | `clau-ai-agents/docs/security.md` § 5 |
| 2026-10-09 | Review independen 3 pilot SIMULASI (kafe, wedding, travel): v1 belum lulus → **v2 lulus**, "dapat di-upgrade kapan saja" | [review-packet-task-041.md § 1](./review-packet-task-041.md) |

Cara review via chat yang disepakati: AI menyusun **pre-review kritis** (dicatat jujur sebagai buatan AI), owner menjawab "setuju"/"ubah". Jangan pernah menulis review seolah-olah dibuat manusia.

## 4. Status Sekarang

| Area | Status |
|---|---|
| Pilar 1 AI Marketing | Aktif. 4 vertical fokus punya fact sheet, voice guide, pilot SIMULASI lulus |
| Pilar 2–5 | Planned; blueprint di `clau-ai-core/docs/blueprints/`; aktivasi setelah VPS siap (`clau-ai-agents/docs/post-vps-checklist.md`) |
| Platform (agents) | Backend v0.4.0 scaffold: belum ada database, auth, atau pemanggilan AI model |
| Dashboard VPS 1 | Live (HTTP via IP, auto-deploy dari `main` tiap 5 menit). 2026-10-09: 16 bug UI/aksesibilitas diperbaiki (clau-ai-agents#21) |
| Keamanan | 2026-10-09: header keamanan + CSP, Nginx dikeraskan, sandbox systemd (exposure 1.4), backend dikunci, audit dependency + scan secret di CI, Actions dipin SHA, Dependabot (tanpa versi mayor) di 4 repo, proteksi `main` di agents. Detail & aturan VPS 2: `clau-ai-agents/docs/security.md` |
| Client nyata | Belum ada. Konten SIMULASI tidak bisa dinaikkan jadi konten client; mulai dari Step 1 CONTENT-WORKFLOW dengan fact sheet nyata |

## 5. Pekerjaan Terbuka (urut prioritas)

| # | Item | Siapa | Lokasi |
|---|---|---|---|
| 1 | Legal review L1–L6 (WNA, izin acara, legalitas operator, asuransi, alkohol, "no pork no lard") | Konsultan hukum / notaris | [review-packet § 2](./review-packet-task-041.md) |
| 2 | Sumber primer S2–S7 (tiket & tarif TN Komodo, drone, manta, spec platform) | Owner, atau AI setelah domain resmi dibuka di network policy | [review-packet § 3](./review-packet-task-041.md) |
| 3 | Domain + HTTPS untuk dashboard (wajib sebelum login/data client) | Owner | `clau-ai-agents/docs/security.md` § 6 |
| 4 | Onboarding client nyata pertama (1 client, 1 vertical, 1 kanal) | Owner + AI (paket onboarding) | `clau-ai-marketing/templates/client-onboarding.md` |
| 5 | Aktivasi pilar 2–5 setelah VPS | Owner + AI | `tasks/backlog.md` TASK-035–039 |
| 6 | Backlog lain | — | [tasks/backlog.md](../tasks/backlog.md) |

## 6. Cara Kerja untuk AI (ringkas)

1. Baca halaman ini → `CLAUDE.md` repo yang dikerjakan → `core/AGENTS.md`.
2. `git fetch`; bila PR branch sebelumnya sudah merge, mulai ulang branch dari `origin/main`.
3. Kerja di feature branch → validator lulus → commit (`feat:`/`fix:`/`docs:`/`refactor:`/`chore:`/`test:`) → PR. Owner yang merge.
4. Label evidence persis: `DATA FINAL`, `ASSUMPTION`, `CLIENT CONFIRMATION`, `FIELD VERIFICATION`, `RISK`, `NEXT ACTION`.
5. Setelah perubahan status material, perbarui halaman ini dan board task.

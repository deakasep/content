# Peta Otak CLAU AI

> Sesi AI baru: mulai dari [status.md](./status.md) (status, keputusan, pekerjaan terbuka).
>
> Satu halaman untuk melihat semua pondasi "otak" CLAU AI dari repo ini. **Isi aslinya tidak ada di sini**; halaman ini hanya peta + link. Edit selalu di repo sumbernya (keputusan owner 2026-10-09: struktur repo tetap, clau-content = markas kerja).

## Alur Aturan

```text
clau-core  ──►  clau-ai-<pilar>  ──►  clau-agent
(otak induk)       (aturan domain)       (yang menjalankan: registry, API, UI)
```

Aturan mengalir satu arah. Level bawah tidak boleh menurunkan kontrol level atas.

## 1. Otak Induk — clau-core

| Pondasi | File | Isi |
|---|---|---|
| Konstitusi | [AI-CONSTITUTION.md](https://github.com/d34faiza-commits/clau-core/blob/main/AI-CONSTITUTION.md) | Aturan induk semua pilar (v3.1.0 Approved: 5 pilar v2, otonomi A/B/C default B, 4 vertical fokus, `main` wajib lewat PR + CI hijau): AI tidak publish, tidak kirim ke pihak luar, tidak self-approve; 6 label evidence |
| Batas | [AI-BOUNDARY.md](https://github.com/d34faiza-commits/clau-core/blob/main/AI-BOUNDARY.md) | Peran tiap repo, storage zones, data apa yang boleh masuk repo, aturan submodule & push |
| Instruksi agent | [AGENTS.md](https://github.com/d34faiza-commits/clau-core/blob/main/AGENTS.md) | Cara kerja & format output agent lintas repo |
| Pipeline | [WORKFLOW.md](https://github.com/d34faiza-commits/clau-core/blob/main/WORKFLOW.md) | 8 langkah dari permintaan sampai monitor |
| Routing | [orchestrator/router.md](https://github.com/d34faiza-commits/clau-core/blob/main/orchestrator/router.md) | 12 intent → pilar → skill → approval minimum |
| Keputusan | [orchestrator/decision-tree.md](https://github.com/d34faiza-commits/clau-core/blob/main/orchestrator/decision-tree.md) · [priority-engine.md](https://github.com/d34faiza-commits/clau-core/blob/main/orchestrator/priority-engine.md) | Kapan eskalasi, urutan prioritas |
| Kontrak data | [shared/](https://github.com/d34faiza-commits/clau-core/tree/main/shared): [database-schema.md](https://github.com/d34faiza-commits/clau-core/blob/main/shared/database-schema.md) · [api-contracts.md](https://github.com/d34faiza-commits/clau-core/blob/main/shared/api-contracts.md) | **Sumber kebenaran** skema database & API (versi backend 0.6.0), alur data lintas pilar, integrasi. Ubah di sini dulu, baru kode |
| Alur sync antar repo | [docs/getting-started.md § 2](https://github.com/d34faiza-commits/clau-core/blob/main/docs/getting-started.md) | core → agents → marketing lewat PR bot setelah CI hijau |
| Masa depan | [docs/blueprints/](https://github.com/d34faiza-commits/clau-core/tree/main/docs/blueprints) · [docs/verticals.md](https://github.com/d34faiza-commits/clau-core/blob/main/docs/verticals.md) · [docs/proposals/autonomy-levels.md](https://github.com/d34faiza-commits/clau-core/blob/main/docs/proposals/autonomy-levels.md) | Cetak biru konsep v2 (AI Marketing, Sales, Admin, BI, Automation), jenis usaha (4 vertical fokus Approved, lainnya Planned), jejak usulan otonomi (Usulan 1 berlaku sejak v3.0.0, Usulan 2 Draft). Isi blueprint tetap Draft/ASSUMPTION |
| 5 pilar | [docs/5-pillar-architecture.md](https://github.com/d34faiza-commits/clau-core/blob/main/docs/5-pillar-architecture.md) · tabel di [README](https://github.com/d34faiza-commits/clau-core/blob/main/README.md#5-pilar-clau-ai) | Nama, status, repo, ketergantungan antar pilar |

## 2. Aturan Domain — Repo Pilar

| # | Pilar | Repo | Isi |
|---|---|---|---|
| 1 | AI Marketing | [clau-market](https://github.com/d34faiza-commits/clau-market) | [rules 01–09](https://github.com/d34faiza-commits/clau-market/tree/main/rules), [skills](https://github.com/d34faiza-commits/clau-market/tree/main/skills), [prompts](https://github.com/d34faiza-commits/clau-market/tree/main/prompts), [knowledge](https://github.com/d34faiza-commits/clau-market/tree/main/knowledge), [qa](https://github.com/d34faiza-commits/clau-market/tree/main/qa) |
| 2–5 | AI Sales, AI Admin, AI Business Intelligence, AI Automation | Belum ada (Planned) | Rencana: [tasks/backlog.md](../tasks/backlog.md) TASK-035–039, TASK-042 |

Vertical fokus (AI-CONSTITUTION v3.0.0+): **villa, restoran/cafe, wedding, travel** — fact sheet, pilot SIMULASI, dan eval tersedia di clau-market & clau-agent. Salon, retail, rental, kontraktor, jasa profesional = **Planned** (belum untuk client) di [knowledge/segments](https://github.com/d34faiza-commits/clau-market/tree/main/knowledge/segments).

## 3. Yang Menjalankan — clau-agent

| Pondasi | File | Isi |
|---|---|---|
| Registry | [agents/registry.json](https://github.com/d34faiza-commits/clau-agent/blob/main/agents/registry.json) | 5 pilar + 12 agent (nama, intent, skill, approval, avatar); dites sinkron dengan core |
| Persona | [agents/personas/](https://github.com/d34faiza-commits/clau-agent/tree/main/agents/personas) | Gaya bahasa, etika, batas & eskalasi per agent |
| Eval | [agents/evals/](https://github.com/d34faiza-commits/clau-agent/tree/main/agents/evals) | Kasus uji + rubrik "seperti manusia ahli" |
| API | [backend/README.md](https://github.com/d34faiza-commits/clau-agent/blob/main/backend/README.md) | v0.6.0: `/health`, `/agents`, `/pillars`, `/route`, `/auth/*` (login, 2FA), `/users` (owner); PostgreSQL 16; tanpa endpoint publish |
| Keamanan & server | [docs/security.md](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/security.md) · [docs/deploy/vps-1-setup.md](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/deploy/vps-1-setup.md) · [docs/post-vps-checklist.md](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/post-vps-checklist.md) | Ancaman & perlindungan, VPS 1 (pratinjau), langkah wajib setelah VPS siap |
| Submodule & CI | [SUBMODULE.md](https://github.com/d34faiza-commits/clau-agent/blob/main/SUBMODULE.md) | Update pin, workflow otomatis, setup token |

## 4. Markas Kerja — Repo Ini

| Path | Isi |
|---|---|
| [tasks/](../tasks/README.md) | Board task resmi semua repo CLAU |
| [design/](../design/README.md) | Spesifikasi UI/UX Portal Klien & Studio; [pillars.md](../design/pillars.md) = 5 pilar di UI |
| [docs/](./status.md) | [status.md](./status.md) (status & handoff), [task-management.md](./task-management.md) (cara kerja board); [paket review TASK-041](./review-packet-task-041.md) untuk langkah manusia vertical fokus |

File lain di repo ini (`CONTENT-CONSTITUTION.md`, `rules/`, `skills/`, `prompts/`, …) adalah **snapshot sebelum split 2026-10-04**. Jangan dibaca sebagai aturan berlaku dan jangan diedit.

## Mau Mengubah Apa? Edit di Mana?

| Perubahan | Edit di | Ikut diubah |
|---|---|---|
| Aturan induk AI | `clau-core/AI-CONSTITUTION.md` (perintah Pak Indra / Dea Karisna) | Revision History + README core |
| Intent baru | `clau-core/orchestrator/router.md` | `clau-agent/agents/registry.json` (test gagal bila beda) |
| Status/nama pilar | Tabel pilar `clau-core/README.md` | `registry.json` → `pillars`, `5-pillar-architecture.md`, `design/pillars.md` |
| Aturan konten (klaim, privacy, approval) | `clau-market/rules/` | Skill/QA terkait |
| Gaya bahasa agent | `clau-agent/agents/personas/` | Eval agent |
| Layar UI | `clau-content/design/` | Frontend `clau-agent/frontend` |
| Skema database | `clau-core/shared/database-schema.md` dulu | Migrasi Alembic **baru** di `clau-agent/backend/migrations/` (test mencocokkan tabel dengan kontrak) |
| Endpoint / versi backend | `clau-core/shared/api-contracts.md` | `backend/app/main.py` `__version__`, `backend/README.md`, `clau-agent/CLAUDE.md`, [status.md](./status.md); merge core dulu, lalu pin `core/` di agents |
| Check CI wajib | `main-guard.yml` (`REQUIRED_CHECKS`) + `sync-submodules.yml` (`required`) | Tabel Disiplin Push di `clau-core/AI-BOUNDARY.md` (Approved: perintah owner) |
| Versi governance | Dokumen di core (perintah owner) | README core, README marketing, [status.md](./status.md), halaman ini |

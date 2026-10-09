# Peta Otak CLAU AI

> Satu halaman untuk melihat semua pondasi "otak" CLAU AI dari repo ini. **Isi aslinya tidak ada di sini**; halaman ini hanya peta + link. Edit selalu di repo sumbernya (keputusan owner 2026-10-09: struktur repo tetap, CLAU-AI-CONTENT = markas kerja).

## Alur Aturan

```text
clau-ai-core  ──►  clau-ai-<pilar>  ──►  clau-ai-agents
(otak induk)       (aturan domain)       (yang menjalankan: registry, API, UI)
```

Aturan mengalir satu arah. Level bawah tidak boleh menurunkan kontrol level atas.

## 1. Otak Induk — clau-ai-core

| Pondasi | File | Isi |
|---|---|---|
| Konstitusi | [AI-CONSTITUTION.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/AI-CONSTITUTION.md) | Aturan induk semua pilar (v2.0.0 Approved): AI tidak publish, tidak kirim ke pihak luar, tidak self-approve; 6 label evidence |
| Batas | [AI-BOUNDARY.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/AI-BOUNDARY.md) | Peran tiap repo, storage zones, data apa yang boleh masuk repo, aturan submodule & push |
| Instruksi agent | [AGENTS.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/AGENTS.md) | Cara kerja & format output agent lintas repo |
| Pipeline | [WORKFLOW.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/WORKFLOW.md) | 8 langkah dari permintaan sampai monitor |
| Routing | [orchestrator/router.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/orchestrator/router.md) | 12 intent → pilar → skill → approval minimum |
| Keputusan | [orchestrator/decision-tree.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/orchestrator/decision-tree.md) · [priority-engine.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/orchestrator/priority-engine.md) | Kapan eskalasi, urutan prioritas |
| Kontrak data | [shared/](https://github.com/d34faiza-commits/clau-ai-core/tree/main/shared) | Skema database, kontrak API, alur data lintas pilar, integrasi |
| Masa depan (Draft) | [docs/blueprints/](https://github.com/d34faiza-commits/clau-ai-core/tree/main/docs/blueprints) · [docs/verticals.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/verticals.md) · [docs/proposals/autonomy-levels.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/proposals/autonomy-levels.md) | Cetak biru konsep v2 (AI Marketing, Sales, Admin, BI, Automation), jenis usaha aktif & planned, draf amandemen otonomi bertingkat — siap aktif setelah di-approve |
| 5 pilar | [docs/5-pillar-architecture.md](https://github.com/d34faiza-commits/clau-ai-core/blob/main/docs/5-pillar-architecture.md) · tabel di [README](https://github.com/d34faiza-commits/clau-ai-core/blob/main/README.md#5-pilar-clau-ai) | Nama, status, repo, ketergantungan antar pilar |

## 2. Aturan Domain — Repo Pilar

| # | Pilar | Repo | Isi |
|---|---|---|---|
| 1 | Marketing & Content | [clau-ai-marketing](https://github.com/d34faiza-commits/clau-ai-marketing) | [rules 01–09](https://github.com/d34faiza-commits/clau-ai-marketing/tree/main/rules), [skills](https://github.com/d34faiza-commits/clau-ai-marketing/tree/main/skills), [prompts](https://github.com/d34faiza-commits/clau-ai-marketing/tree/main/prompts), [knowledge](https://github.com/d34faiza-commits/clau-ai-marketing/tree/main/knowledge), [qa](https://github.com/d34faiza-commits/clau-ai-marketing/tree/main/qa) |
| 2–5 | Sales, Guest Experience, Operations, Analytics (konsep v2: Sales, Admin, BI, Automation) | Belum ada (Planned) | Rencana: [tasks/backlog.md](../tasks/backlog.md) TASK-034–042 |

Knowledge 7 jenis usaha berikutnya (wedding, travel, salon, retail, rental, kontraktor, jasa profesional) sudah disiapkan di [clau-ai-marketing/knowledge/segments](https://github.com/d34faiza-commits/clau-ai-marketing/tree/main/knowledge/segments) dengan status **Planned** (belum untuk client).

## 3. Yang Menjalankan — clau-ai-agents

| Pondasi | File | Isi |
|---|---|---|
| Registry | [agents/registry.json](https://github.com/d34faiza-commits/clau-ai-agents/blob/main/agents/registry.json) | 5 pilar + 12 agent (nama, intent, skill, approval, avatar); dites sinkron dengan core |
| Persona | [agents/personas/](https://github.com/d34faiza-commits/clau-ai-agents/tree/main/agents/personas) | Gaya bahasa, etika, batas & eskalasi per agent |
| Eval | [agents/evals/](https://github.com/d34faiza-commits/clau-ai-agents/tree/main/agents/evals) | Kasus uji + rubrik "seperti manusia ahli" |
| API | [backend/app/main.py](https://github.com/d34faiza-commits/clau-ai-agents/blob/main/backend/app/main.py) | `/health`, `/agents`, `/pillars`, `/route` (read-only, tanpa publish) |

## 4. Markas Kerja — Repo Ini

| Path | Isi |
|---|---|
| [tasks/](../tasks/README.md) | Board task resmi semua repo CLAU |
| [design/](../design/README.md) | Spesifikasi UI/UX Portal Klien & Studio; [pillars.md](../design/pillars.md) = 5 pilar di UI |
| [docs/](./task-management.md) | Panduan kerja |

File lain di repo ini (`CONTENT-CONSTITUTION.md`, `rules/`, `skills/`, `prompts/`, …) adalah **snapshot sebelum split 2026-10-04**. Jangan dibaca sebagai aturan berlaku dan jangan diedit.

## Mau Mengubah Apa? Edit di Mana?

| Perubahan | Edit di | Ikut diubah |
|---|---|---|
| Aturan induk AI | `clau-ai-core/AI-CONSTITUTION.md` (perintah Pak Indra / Dea Karisna) | Revision History + README core |
| Intent baru | `clau-ai-core/orchestrator/router.md` | `clau-ai-agents/agents/registry.json` (test gagal bila beda) |
| Status/nama pilar | Tabel pilar `clau-ai-core/README.md` | `registry.json` → `pillars`, `5-pillar-architecture.md`, `design/pillars.md` |
| Aturan konten (klaim, privacy, approval) | `clau-ai-marketing/rules/` | Skill/QA terkait |
| Gaya bahasa agent | `clau-ai-agents/agents/personas/` | Eval agent |
| Layar UI | `CLAU-AI-CONTENT/design/` | Frontend `clau-ai-agents/frontend` |

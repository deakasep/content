# CLAUDE.md — CLAU-AI-CONTENT (ARSIP)

> Peta repo untuk AI agent. Last updated: 2026-10-09

> 🔔 **Sesi baru: baca [`docs/status.md`](docs/status.md) dulu** (otoritas, keputusan yang sudah diambil, pekerjaan terbuka).

## Status

Repo ini **arsip** sejak 2026-10-04. Kerja baru masuk ke:

| Repo | Isi |
|---|---|
| `clau-ai-core` | Constitution, boundary, orchestrator, kontrak data |
| `clau-ai-marketing` | Pilar 1: rules, prompts, skills, knowledge, templates, QA |
| `clau-ai-agents` | Platform: registry, backend, frontend |

Arsitektur **5 pilar v2** (AI-CONSTITUTION v3.0.0: AI Marketing aktif; AI Sales, AI Admin, AI Business Intelligence, AI Automation planned; otonomi A/B/C default B; vertical fokus villa, restoran/cafe, wedding, travel): `clau-ai-core/docs/5-pillar-architecture.md`. Nama & status pilar sumbernya tabel di `clau-ai-core/README.md`, dicerminkan di `clau-ai-agents/agents/registry.json` → `pillars` (ada test).

## Yang Masih Aktif di Sini

| Path | Fungsi |
|---|---|
| `tasks/` | Board task (Backlog → In Progress → Review → Done); issue GitHub repo ini terhubung ke board |
| `docs/status.md` | **Status & handoff** lintas sesi AI: otoritas, keputusan, status, pekerjaan terbuka |
| `docs/` | Dokumen pendukung yang dirujuk repo baru lewat URL; `docs/peta-otak.md` = peta semua pondasi otak AI (link ke repo sumber) |
| `design/` | Spesifikasi UI/UX standalone + design tokens (pengecualian atas perintah owner, 2026-10-06); `design/pillars.md` = 5 pilar di UI |
| `scripts/validate.py` · `design/tokens/build_tokens.py --check` | Dijalankan CI |

File lain (rules, prompts, skills, dst.) adalah **snapshot sebelum split**. Jangan diedit; edit di repo baru. `CONTENT-CONSTITUTION.md` berstatus **Superseded** oleh `clau-ai-core/AI-CONSTITUTION.md` (sekarang v3.0.0). `scripts/split_repo.py` dan `split/` adalah jejak proses split dan tidak mencerminkan perubahan setelah 2026-10-04 (mis. submodule `agents/` di marketing).

## Command

```bash
python scripts/validate.py
python design/tokens/build_tokens.py          # setelah mengubah design/tokens/tokens.json
```

## Aturan

- Otoritas perubahan: **Pak Indra** atau **Dea Karisna (d34faiza)**.
- Jangan commit data client nyata, `.env`, atau credential.

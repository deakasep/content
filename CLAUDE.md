# CLAUDE.md — clau-content (ARSIP)

> Peta repo untuk AI agent. Last updated: 2026-10-27

> 🔔 **Sesi baru: baca [`docs/status.md`](docs/status.md) dulu** (otoritas, keputusan yang sudah diambil, pekerjaan terbuka).

## Status

Repo ini **arsip** sejak 2026-10-04. Kerja baru masuk ke:

| Repo | Isi |
|---|---|
| `clau-core` | Constitution, boundary, orchestrator, kontrak data |
| `clau-market` | Pilar 1: rules, prompts, skills, knowledge, templates, QA |
| `clau-agent` | Platform: registry, backend, frontend |

Arsitektur **5 pilar v2** (AI-CONSTITUTION v3.0.0, sekarang v3.1.0: AI Marketing aktif; AI Sales, AI Admin, AI Business Intelligence, AI Automation planned; otonomi A/B/C default B; vertical fokus villa, restoran/cafe, wedding, travel): `clau-core/docs/5-pillar-architecture.md`. Nama & status pilar sumbernya tabel di `clau-core/README.md`, dicerminkan di `clau-agent/agents/registry.json` → `pillars` (ada test).

## Yang Masih Aktif di Sini

| Path | Fungsi |
|---|---|
| `tasks/` | Board task Markdown, **dibekukan sebagai riwayat per 2026-10-21**. Board kerja utama: ClickUp Space **Clau AI** (aturan di `tasks/README.md` § Board ClickUp); task baru mulai TASK-064 di ClickUp |
| `AGENTS.md` | Entry point coding lintas AI (otorisasi merge sesuai core); bagian konten lama tetap snapshot |
| `docs/status.md` | **Status & handoff** lintas sesi AI: otoritas, keputusan, status, pekerjaan terbuka |
| `docs/` | Dokumen pendukung yang dirujuk repo baru lewat URL; `docs/peta-otak.md` = peta semua pondasi otak AI (link ke repo sumber) |
| `design/` | Spesifikasi UI/UX standalone + design tokens (pengecualian atas perintah owner, 2026-10-06); `design/pillars.md` = 5 pilar di UI |
| `scripts/validate.py` · `design/tokens/build_tokens.py --check` | Dijalankan CI |

File lain (rules, prompts, skills, dst.) adalah **snapshot sebelum split**. Jangan diedit; edit di repo baru. `CONTENT-CONSTITUTION.md` berstatus **Superseded** oleh `clau-core/AI-CONSTITUTION.md` (sekarang v3.1.0). `scripts/split_repo.py` dan `split/` adalah jejak proses split dan tidak mencerminkan perubahan setelah 2026-10-04 (mis. submodule `agents/` di marketing).

## Command

```bash
python scripts/validate.py
python design/tokens/build_tokens.py          # setelah mengubah design/tokens/tokens.json
```

## Aturan

- Otoritas perubahan: **Pak Indra** atau **Dea Karisna (d34faiza)**.
- Jangan commit data client nyata, `.env`, atau credential.

- ChatGPT/Codex dan Claude menyelesaikan coding PR yang sudah diizinkan sampai merge setelah CI hijau, sesuai `AGENTS.md` dan core AI-BOUNDARY 1.7.0. Approval konten client tetap manusia.

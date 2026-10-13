# Task Management

Board task CLAU-AI-CONTENT berbasis Markdown — adaptasi alur board (Backlog → In Progress → Review → Done) yang biasa dipakai di tools seperti ClickUp, tapi disimpan di repo supaya **trackable lewat git history** dan gratis di GitHub Free.

Panduan lengkap (termasuk GitHub Projects): [docs/task-management.md](../docs/task-management.md).

## Board

| Kolom | File | Isi |
|---|---|---|
| **Backlog** | [backlog.md](./backlog.md) | Task yang sudah didefinisikan, belum dikerjakan |
| **In Progress** | [in-progress.md](./in-progress.md) | Sedang dikerjakan (batasi maks 3 task sekaligus) |
| **Review** | [review.md](./review.md) | Draft/output sudah ada, menunggu cek & verifikasi |
| **Done** | [done.md](./done.md) | Selesai dan lolos acceptance criteria (arsip) |

```mermaid
flowchart LR
    B["Backlog"] --> P["In Progress"] --> R["Review"] --> D["Done"]
    R -- "gagal acceptance" --> P
```

## Alur Singkat

1. **Tambah task** — salin [templates/task-template.md](./templates/task-template.md) ke `backlog.md`, pakai ID berikutnya.
2. **Mulai kerja** — pindahkan blok task ke `in-progress.md`, ubah `Status: In Progress`.
3. **Selesai draft** — pindahkan ke `review.md`, ubah `Status: Review`.
4. **Lolos review** — pindahkan ke `done.md`, ubah `Status: Done`, isi `Completed` dan `Commit`.
5. **Commit perubahan board** bersama perubahan file kerjanya, sebut ID di commit message, mis. `docs(knowledge): verify instagram spec (TASK-006)`.

## Aturan

- Satu task = satu blok, ada di **satu** file board saja.
- `Status` wajib sama dengan file board tempatnya — dicek oleh `python scripts/validate.py`.
- ID unik dan tidak dipakai ulang.
- Jangan simpan data client, nama tamu, harga kontrak, atau credential di task (lihat [CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md)). Pakai kode client.

## Ringkasan Saat Ini

| Kolom | Jumlah |
|---|---|
| Backlog | 10 |
| In Progress | 1 |
| Review | 0 |
| Done | 33 |

ID terakhir dipakai: **TASK-047**. Per 2026-10-04 semua item Review di-approve owner; perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza).

# Task Management Guide

Panduan memakai task management CLAU-AI-CONTENT: board Markdown di repo dan (opsional) GitHub Projects sebagai tampilan visual.

## 1. Prinsip

| Prinsip | Artinya |
|---|---|
| **Satu source of truth** | Board Markdown di [`tasks/`](../tasks/README.md) adalah catatan resmi. GitHub Projects hanya tampilan visual, bukan tempat kedua untuk mencatat |
| **Trackable** | Setiap perpindahan status = perubahan file yang ter-commit, sehingga riwayatnya ada di `git log` |
| **Traceable** | ID task (`TASK-XXX`) disebut di commit message dan di field `Related` |
| **Verifiable** | Acceptance Criteria harus bisa dijawab ya/tidak |
| **Aman** | Tidak ada data client, nama tamu, harga kontrak, atau credential di task ([CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md)) |

## 2. Alur Board

```text
Backlog → In Progress → Review → Done
              ↑            │
              └── gagal ───┘
```

| Kolom | Masuk kalau | Keluar kalau |
|---|---|---|
| **Backlog** | Task sudah jelas: deskripsi + acceptance criteria | Mulai dikerjakan |
| **In Progress** | Sedang dikerjakan (maks 3 task) | Draft/output sudah ada di repo |
| **Review** | Perlu dicek owner / verifikasi sumber / QA gate | Semua acceptance criteria terpenuhi (→ Done) atau gagal (→ In Progress) |
| **Done** | Lolos acceptance criteria | Tidak keluar — arsip permanen |

## 3. Cara Pakai Sehari-hari

### Tambah task baru

1. Lihat "ID terakhir dipakai" di [tasks/README.md](../tasks/README.md), lalu pakai nomor berikutnya.
2. Salin [task-template.md](../tasks/templates/task-template.md) ke [backlog.md](../tasks/backlog.md).
3. Isi semua field. `Due` boleh `—` kalau belum diputuskan; jangan mengarang tanggal.
4. Update "Ringkasan Saat Ini" dan "ID terakhir dipakai" di `tasks/README.md`.

### Pindah status

1. Pindahkan **seluruh blok** task ke file board tujuan.
2. Ubah `- Status:` agar sama dengan board tujuan.
3. Saat pindah ke Done, tambahkan `- Completed: YYYY-MM-DD` dan `- Commit: <hash>`.
4. Update ringkasan di `tasks/README.md`.
5. Jalankan validator, lalu commit:

```text
python scripts/validate.py
git commit -m "docs(knowledge): verify instagram spec (TASK-011)"
```

### Commit message

Format sesuai [AGENTS.md](../AGENTS.md): `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`, dan sebut ID task dalam kurung di akhir.

## 4. Validator

`python scripts/validate.py` (juga dijalankan CI) mengecek setiap task:

- ID unik di keempat file board;
- semua field wajib ada (ID, Status, Priority, Assignee, Created, Due, Description, Acceptance Criteria, Related);
- `Status` sama dengan board tempat task berada;
- `Priority` salah satu dari Low / Normal / High / Urgent;
- `Created` dan `Due` berformat `YYYY-MM-DD` atau `—`.

## 5. GitHub Projects (opsional, tampilan visual)

GitHub Projects tersedia di akun personal GitHub Free dan bisa menampilkan issue repo private sebagai board.

**ASSUMPTION:** batas fitur per plan (misalnya jumlah workflow auto-add) bisa berubah. Cek di GitHub Docs saat setup.

### 5.1 Buat project board

1. Buka profil GitHub → tab **Projects** → **New project**.
2. Pilih template **Board**, beri nama **CLAU-AI-CONTENT Roadmap**, lalu **Create project**.
3. Di field **Status**, ubah/tambah opsi menjadi: `Backlog`, `In Progress`, `Review`, `Done` (hapus `Todo` bila ada).
4. Tambahkan field (⚙ → **New field**):
   - **Priority** — single select: `Low`, `Normal`, `High`, `Urgent`
   - **Due** — date
   - **Task ID** — text (isi `TASK-XXX`)

### 5.2 Hubungkan ke repo

1. Buka repo **CLAU-AI-CONTENT** → tab **Projects** → **Link a project** → pilih **CLAU-AI-CONTENT Roadmap**.

### 5.3 Auto-add issues ke board

1. Di project, buka menu **⋯** → **Workflows**.
2. Pilih **Auto-add to project** → **Edit**.
3. Repository: `CLAU-AI-CONTENT`; filter: `is:issue is:open`.
4. Aktifkan workflow **Item added to project** → set Status = `Backlog`.
5. Aktifkan **Item closed** dan **Pull request merged** → set Status = `Done`.
6. **Save and turn on workflow**.

### 5.4 Membuat issue task

Repo sudah punya issue form **Task** (`.github/ISSUE_TEMPLATE/task.yml`) dengan field yang sama dengan template Markdown.

1. Repo → **Issues** → **New issue** → **Task**.
2. Judul: `TASK-XXX: Judul task` — ID sama dengan di board Markdown.
3. Setelah issue dibuat, tambahkan URL issue ke field `Related` task di board Markdown.

### 5.5 Sinkronisasi (hindari dobel kerja)

| Situasi | Yang dilakukan |
|---|---|
| Solo, task kecil | Cukup board Markdown; issue tidak wajib |
| Task besar / butuh diskusi | Buat issue, ID sama, link di `Related` |
| Status berbeda antara Projects dan Markdown | Markdown yang benar; samakan Projects |
| Tim 2+ orang | Pertimbangkan GitHub Projects sebagai board utama dan pindahkan aturan source of truth lewat revisi dokumen ini |

## 6. Best Practice

1. **Kecil & selesai** — pecah task lebih dari ±1 hari kerja menjadi beberapa task.
2. **WIP limit** — maksimal 3 task In Progress.
3. **Acceptance criteria dulu** — task tanpa kriteria selesai tidak boleh masuk In Progress.
4. **Review bukan formalitas** — task yang menyentuh klaim/angka wajib cek sumber (label **DATA FINAL** / **ASSUMPTION** sesuai [rule 09](../rules/09-DATA-CLASSIFICATION.md)).
5. **Weekly sweep** — tiap minggu: rapikan backlog, update priority, cek task Review yang macet.
6. **Jangan hapus Done** — arsip adalah jejak audit.
7. **ID tidak dipakai ulang** — task batal tetap dipindah ke Done dengan catatan `Description: DIBATALKAN — <alasan>`.

## 7. Referensi

- [tasks/README.md](../tasks/README.md)
- [WORKFLOW.md](../WORKFLOW.md) — alur produksi konten (berbeda dari alur task)
- [CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md) — disiplin commit & push
- GitHub Docs: *About Projects*, *Using the built-in automations*, *Adding items automatically* (cek versi terbaru)

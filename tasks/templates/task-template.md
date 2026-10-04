# TASK: [Judul]

> Salin blok di bawah ke file board sesuai status ([backlog](../backlog.md), [in-progress](../in-progress.md), [review](../review.md), [done](../done.md)). Di file board, judul ditulis sebagai `## TASK-XXX: [Judul]`.

- ID: TASK-XXX
- Status: [Backlog/In Progress/Review/Done]
- Priority: [Low/Normal/High/Urgent]
- Assignee: [nama]
- Created: [YYYY-MM-DD]
- Due: [YYYY-MM-DD atau — bila belum ditentukan]
- Description: [deskripsi singkat: apa dan kenapa]
- Acceptance Criteria: [kriteria selesai yang bisa dicek, mis. "validator lulus", "semua angka punya sumber + tanggal akses"]
- Related: [link ke file/issue/commit]

## Aturan Pengisian

| Field | Aturan |
|---|---|
| ID | `TASK-` + 3 digit, urut, **tidak pernah dipakai ulang** walau task dibatalkan |
| Status | Harus sama dengan file board tempat task berada |
| Priority | `Urgent` = blocker/insiden; `High` = minggu ini; `Normal` = bulan ini; `Low` = kapan sempat |
| Due | Jangan mengarang tanggal; tulis `—` bila belum diputuskan |
| Acceptance Criteria | Harus bisa diverifikasi (ya/tidak), bukan "sudah bagus" |
| Related | Relative link ke file repo, atau URL issue/commit |

Opsional untuk task yang sudah selesai: `- Completed: YYYY-MM-DD` dan `- Commit: <hash>`.

# Paket Keputusan — TASK-032 (level approval otomatis untuk konten hospitality)

> Untuk owner (Dea Karisna / Pak Indra). Disiapkan 2026-10-22 oleh AI agent (Claude Code). Bagian "pre-review kritis" ditulis AI dan dicatat apa adanya sebagai buatan AI; keputusan di § 4 hanya diisi owner. Cukup balas **"setuju semua"**, atau sebut nomor yang ingin diubah. Setelah itu AI mengerjakan § 5. Kartu ClickUp: *[PLATFORM] TASK-032 Dynamic approval level di platform*.

## 1. Masalah: platform lebih longgar dari Rule 08

Rule 08 (`clau-market/rules/08-APPROVAL-PUBLICATION-STANDARD.md`) menetapkan level approval dari **isi** konten. Platform (backend 0.9.x) baru menghitung level dari dua hal: minimum intent di `registry.json`, dinaikkan ke L3 bila `risk = 3` saat request dibuat, dan ke L2 bila draft memuat klaim ber-`fact_key`. Hasil cek di kode per 2026-10-22 (**DATA FINAL**: `backend/app/workflow.py`, fungsi database `clau_draft_min_level` migrasi 0006):

| Situasi hospitality | Rule 08 | Platform sekarang | Celah |
|---|---|---|---|
| Balasan review **negatif** (intent `review-reply`) | L3 | L1, kecuali staf mengisi risk 3 | **Besar**: balasan publik ke tamu kecewa bisa di-approve di L1 |
| **Terjemahan** konten L3 (intent `localize`) | Ikut konten asal | L1 | **Besar**: versi bahasa Inggris balasan review negatif cukup L1 |
| Promo/harga ditulis di teks tanpa klaim `fact_key` | L2 | L1 untuk `caption`/`stories` | Sedang: aman hanya bila staf disiplin mencatat klaim |
| Konten dengan **orang** (tamu, staf, pengantin) | L2 | L1 untuk `caption`/`stories` | Sedang: menyangkut consent (Rule 04) |
| **Iklan berbayar**, kolaborasi **influencer**/endorse | L3 | Mengikuti intent (L1–L2) | Besar: menyangkut disclosure (Rule 01, 05) |
| Topik **agama/adat/tempat suci**, bencana, krisis | L3 + eskalasi | Mengikuti intent | Besar: risiko reputasi klien di Bali/NTT |
| Kampanye musiman (Ramadan, Nyepi, Natal) | L2–L3 | L2 | Kecil–sedang |

## 2. Usulan

### 2a. Penanda isi konten (`content_flags`) di setiap draft

Setiap draft membawa daftar penanda. Tiap penanda punya level minimum yang tetap, sesuai Rule 08:

| Penanda | Arti | Level minimum |
|---|---|---|
| `price_promo` | Ada harga, diskon, promo, paket, atau komitmen komersial | L2 |
| `people` | Ada orang yang bisa dikenali (foto/video/nama tamu, staf, pengantin) | L2 |
| `ota_listing` | Teks untuk listing OTA (Booking.com, Traveloka, Agoda, dll.) | L2 |
| `negative_review` | Membalas review/keluhan negatif | L3 |
| `paid_ads` | Iklan berbayar atau konten di-boost | L3 |
| `influencer` | Kolaborasi influencer, endorse, barter menginap | L3 |
| `religion_culture` | Agama, adat, tempat suci, upacara | L3 |
| `crisis` | Krisis, bencana, insiden, isu hukum/kesehatan/keselamatan | L3 (+ eskalasi Level C) |

### 2b. Siapa mengisi penanda: boleh menaikkan, tidak boleh menurunkan diam-diam

1. **Pembuat draft** (staf, atau worker AI dari output terstruktur) mengisi penanda saat draft dibuat.
2. **Server menambah penanda sendiri** sebagai jaring pengaman. Contoh: teks mengandung `Rp`, `%`, `diskon`, `promo`, atau `harga` → `price_promo`; intent `review-reply` dengan rating ≤ 3 → `negative_review` (field baru `review_rating` 1–5, wajib untuk request `review-reply`); intent `ota-listing` → `ota_listing`.
3. **Reviewer QA** boleh menambah penanda.
4. **Menghapus** penanda hanya oleh owner/content lead, dengan alasan tertulis, dan tercatat di audit log. Penanda dari jaring pengaman server tidak bisa dihapus. Bila salah, solusinya draft versi baru.

### 2c. Rumus level minimum (dihitung di server, ditegakkan database)

`level minimum draft = tertinggi dari:`

- minimum intent (`registry.json`), atau L3 bila risk 3 (sudah ada);
- L2 bila ada klaim ber-`fact_key` (sudah ada);
- level penanda tertinggi (§ 2a);
- untuk `localize`: level minimum **draft asal** yang diterjemahkan (request `localize` wajib menunjuk draft asal).

Database menolak approval di bawah level ini dengan kode yang sudah ada, `approval_level_too_low`, sehingga aturan tetap berlaku walau UI salah.

### 2d. Tampilan

- Halaman `/requests/[id]` menampilkan **level minimum + alasannya**, misalnya "L3 karena: balasan review negatif (otomatis dari rating 2)".
- Form approval memilih level itu secara default dan tidak menawarkan level di bawahnya.

## 3. Pre-review kritis (ditulis AI)

| Risiko | Dampak | Mitigasi dalam usulan |
|---|---|---|
| Terlalu banyak konten naik ke L3, owner klien jadi bottleneck | Konten terlambat tayang | Hanya 5 penanda L3, semuanya memang L3 menurut Rule 08. Pantau di dashboard kualitas (TASK-058) |
| Jaring pengaman kata kunci salah tangkap ("100% alami" → `price_promo`) | Naik ke L2 tanpa perlu | L2 tetap aman (salah ke arah ketat). Daftar kata kunci di kode + test, bisa diperbaiki lewat PR |
| Staf lupa mengisi `people` atau `religion_culture` | Level terlalu rendah | Wajib dicentang "tidak ada" secara eksplisit di form draft (bukan default kosong); reviewer QA wajib mengonfirmasi; AI fact-check memberi saran penanda |
| Penanda dihapus untuk mempercepat | Aturan dilewati | Hanya owner/content lead, alasan tertulis, audit log, penanda server tidak bisa dihapus |
| Data lama (draft sebelum fitur ini) | Tanpa penanda | Migrasi mengisi penanda dari jaring pengaman untuk draft yang belum diputuskan |

**RISK** tersisa: deteksi otomatis tidak akan menangkap semua kasus (misalnya foto orang tanpa teks). Kontrol utamanya tetap manusia: pembuat, reviewer QA independen, dan approver.

## 4. Keputusan owner

Rekomendasi AI: setujui semua. Balas "setuju semua", atau sebut nomornya.

| # | Keputusan | Rekomendasi AI | Jawaban owner |
|---|---|---|---|
| K1 | Daftar 8 penanda dan levelnya (§ 2a) | Setuju | |
| K2 | Aturan menaikkan/menghapus penanda (§ 2b) | Setuju | |
| K3 | Jaring pengaman kata kunci + rating oleh server | Setuju | |
| K4 | `localize` wajib menunjuk draft asal dan ikut levelnya; `review-reply` wajib mengisi rating 1–5 | Setuju | |
| K5 | Form draft wajib konfirmasi eksplisit "tidak ada orang / tidak ada topik agama-adat" | Setuju | |
| K6 | Kontrak naik ke API 0.10.0 + migrasi database 0007 | Setuju | |

## 5. Rencana kerja setelah disetujui

| PR | Repo | Isi |
|---|---|---|
| A | clau-core | Kontrak 0.10.0: `content_flags` di Draft, `review_rating` di request `review-reply`, `source_draft_id` di request `localize`, rumus level, kode aturan baru bila perlu. Router: catatan `localize` |
| B | clau-agent | Migrasi 0007 (kolom + fungsi `clau_draft_min_level` baru + isi data lama), API, jaring pengaman, worker AI mengisi penanda, UI level + alasan, test ke PostgreSQL untuk setiap baris tabel § 1 |
| C | clau-market | Rule 08 menyebut nama penanda (tanpa mengubah level), template brief/QA menambah centang penanda |

Kartu ClickUp TASK-032 dipindah ke **in progress** saat PR A dibuat dan **Closed** setelah ketiga PR merged dengan CI hijau (AI-BOUNDARY 1.6.0).

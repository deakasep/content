# Mockup Spec — Studio (Dashboard Internal)

> **ID:** Spesifikasi visual hi-fi untuk 8 halaman di [dashboard-wireframe](../wireframes/dashboard-wireframe.md). Spek global (warna, font, state, motion) sama dengan [client-portal-mockup](./client-portal-mockup.md) §0. File ini hanya mencatat **perbedaan dan tambahan** untuk Studio.
> **EN:** Hi-fi visual spec for the 8 Studio pages. Global spec is shared with the Client Portal; this file covers Studio-specific differences.

**Mood:** fokus dan efisien, seperti Linear/Stripe, tapi tetap hangat lewat palet stone + teal. Studio dipakai berjam-jam, jadi **kepadatan informasi lebih tinggi** daripada Portal, dengan kontras yang tetap nyaman di mata.

## 0. Perbedaan dari Portal Klien / Differences

| Aspek | Portal Klien | Studio |
|---|---|---|
| Kepadatan | Longgar (kartu besar, 1 tugas per layar) | **Padat**: tabel baris 44–52 px, kartu kanban 120 px |
| Device utama | HP | Laptop/desktop; mobile untuk cek cepat |
| Navigasi desktop | Sidebar 256 px | Sidebar 240 px, bisa dilipat ke 64 px (`[`) |
| Search | Tidak ada | Command palette `⌘K` / `Ctrl K` + search bar di top bar |
| Shortcut | Tidak ada | Ada (lihat wireframe) + tooltip menampilkan shortcut |
| Font body tabel | 16 px | **14 px** (`small`), angka `tabular-nums` |
| Dark mode | Opsional | Opsional, **diprioritaskan** (kerja malam); diuji sama ketatnya |
| Data sensitif | Hanya data properti sendiri | Banyak klien: **nama klien aktif selalu terlihat** di header detail |

---

## 1. Ringkasan / Overview

| Komponen | Spek |
|---|---|
| Kartu statistik (4) | Grid 4 kolom desktop / 2 kolom mobile, tinggi 112 px, angka `h4` 24/700 `tabular-nums`. Progress bar 8 px radius full, track `#E7E5E4`, fill `#0F766E` + label persen di sebelah kanan |
| **Menunggu manusia** | Kartu dengan border kiri 4 px `#B45309`; tiap baris 44 px: ikon `triangle-alert` 16 px, jenis tugas 14/500, nama klien 14 `#78716C`, count pill kanan. Baris bisa diklik → filter pipeline |
| Pipeline mini | Bar horizontal per tahap, warna `#14B8A6`, label + angka kanan. Klik → halaman Konten dengan filter tahap |
| Tayang 7 hari | List kronologis; zona waktu per item (klien bisa beda zona) |
| Pendapatan | Hanya untuk peran Owner; format `Rp42.000.000`; ikon `eye-off` untuk menyembunyikan angka saat layar dibagikan |
| Empty (agency baru) | Checklist onboarding agency: "1. Atur brand · 2. Tambah klien pertama · 3. Hubungkan Instagram" dengan progress |
| Loading | Skeleton per kartu, dimuat paralel (kartu yang cepat tidak menunggu yang lambat) |

## 2. Klien / Clients

| Komponen | Spek |
|---|---|
| Tabel | Header sticky 40 px bg `#FAFAF9` 12/600 `#44403C`; baris 52 px; hover `#F5F5F4`; klik baris → detail. Kolom nama: avatar/logo properti 24 + nama 14/500 |
| Filter bar | Chip filter (multi-select) + tombol "Reset filter"; jumlah hasil "12 klien" |
| Status badge | Onboard (warning) · Aktif (success) · Jeda (neutral) · Selesai (neutral outline) |
| Detail klien | Header: nama `h3`, badge status, wilayah + zona waktu. Tabs di bawah header |
| Tab Fakta | Tabel fakta: klaim · Evidence Badge · sumber · tanggal. Baris `CLIENT CONFIRMATION` bisa dipilih → *Kirim pengingat ke klien* (mengirim notifikasi Portal + WA/email) |
| Tab Akses | Daftar approver klien + level approval (L1/L2/L3) yang boleh mereka setujui |
| Empty | `building-2` → "Belum ada klien" → *+ Tambah klien pertama* (primary) |
| Mobile | Tabel jadi list kartu (lihat wireframe) |

## 3. Konten — Pipeline

| Komponen | Spek |
|---|---|
| Kolom kanban | Lebar 272 px, bg `#F5F5F4`, radius 12, header 14/600 + count; scroll horizontal di papan, scroll vertikal per kolom |
| Kartu kanban | Bg putih, radius 8, padding 12, `shadow-sm`; baris 1: nama klien 12/500 `#78716C`; baris 2: judul 14/500 maks 2 baris; baris 3: badge level + tanggal tayang + avatar penanggung jawab 24 |
| Kartu terblokir | Border kiri 3 px `#B45309` + baris "! Butuh review manusia" 12/500 `#92400E` |
| Drag & drop | Kartu diangkat: `shadow-lg`, rotate 2°; kolom tujuan valid: border dashed `#0F766E`; **tidak valid**: kolom redup + kursor `not-allowed` + toast alasan ("Konten L2 butuh review independen sebelum dikirim ke klien") |
| Keyboard | Pilih kartu → `Space` angkat → panah pindah kolom → `Space` taruh. `aria-live` mengumumkan perpindahan |
| Tampilan tabel | Kolom: klien, judul, channel, level, tahap, jadwal, PJ, agent terakhir |
| **Panel detail** | Slide-over kanan 720 px (desktop) / full screen (mobile); tabs `Caption · Klaim · QA · Versi · Komentar` |
| Tab Klaim | Tabel per kalimat (sesuai `qa/claim-verification` di clau-ai-marketing): no, kalimat, klaim tersirat, label, hasil. Filter "Hanya yang bukan DATA FINAL" |
| Tab QA | Hasil `check_caption` ditampilkan sebagai **"PASS (mekanis)"** + daftar item QA manual; kolom "Independen? Ya/Tidak" |
| Review independen | Tombol *Tugaskan reviewer* (pilih anggota tim; pembuat draft tidak muncul di pilihan). Reviewer menandai: *Lulus* / *Perlu perbaikan* + catatan |
| *Kirim ke klien* | Primary; nonaktif dengan tooltip alasan bila QA belum lulus atau review independen belum ada (L2/L3) |
| **Tandai sudah tayang** | Muncul di kolom Disetujui: dialog dengan field **URL post (wajib, divalidasi domain platform)**, tanggal & jam tayang aktual, zona waktu. Tidak ada tombol "Publish" |
| Versi | Timeline versi (v1, v2, …) dengan diff caption (hapus: coret `#B91C1C` bg `#FEF2F2`; tambah: `#166534` bg `#F0FDF4`) |

## 4. AI Agent

| Komponen | Spek |
|---|---|
| Kartu agent | Grid 3 kolom desktop / 1 kolom mobile; tinggi 160 px; nama agent `h6` + ikon `bot`; **Agent Status Pill** di kanan atas |
| Status pill | `Siap` success · `Bekerja (n)` info + dot berdenyut 1.5 s (berhenti bila reduced motion) · `Menunggu manusia` warning · `Error` error |
| Metrik | "7 hari: n tugas", "Terakhir aktif: …" 12/500 `#78716C` |
| Detail agent | Halaman: antrean (tabel), riwayat, skill/prompt yang dipakai (link ke repo), error log (mono 13 px, bg `#1C1917` teks `#F5F5F4`, bisa disalin) |
| Banner aturan | Info tint di bawah grid: "Agent menyiapkan draft & cek. Approval, publish, dan kirim ke tamu tetap manusia." |
| Error | Kartu agent error: border `#B91C1C`, tombol *Lihat log* + *Coba ulang tugas* |

## 5. Kalender Produksi

| Komponen | Spek |
|---|---|
| Grid minggu/bulan | Seperti Portal, tapi sel menampilkan **semua klien**; chip berwarna per klien (palet chart, maks 8) + nama klien singkat di chip |
| Jenis item | Tayang (ikon `send`), tenggat draft (`file-pen`), tenggat laporan (`chart-column`) |
| Zona waktu | Jam ditampilkan dalam zona klien + tooltip konversi ke zona agency |
| Drag jadwal | Hanya untuk tenggat internal; jadwal tayang yang sudah disetujui klien **tidak bisa** di-drag (butuh approval ulang) |

## 6. Laporan

| Komponen | Spek |
|---|---|
| Tabel laporan | Per klien per periode; status badge: Data kurang (warning) · Draft (neutral) · Terkirim (success) |
| Editor laporan | 2 kolom: kiri editor ringkasan (textarea + bantuan AI, ditandai `sparkles`), kanan preview PDF live |
| Validasi | Tombol *Kirim ke klien* nonaktif bila ada metrik tanpa sumber |
| Export | PDF per klien, CSV per klien, ZIP semua klien. Progres export di toast dengan bar |

## 7. Pengaturan

| Komponen | Spek |
|---|---|
| Layout | Nav section kiri 220 px + form kanan max 640 px |
| Warna brand | Color input + **preview kontras otomatis** (rasio terhadap putih; peringatan bila < 4.5:1) |
| Integrasi | Kartu per platform: logo (Simple Icons), status `Terhubung`/`Tidak terhubung`, scope yang diminta (**baca insight saja**), tombol *Hubungkan* / *Putuskan* |
| API key | Ditampilkan **sekali** saat dibuat dalam field mono + tombol salin; setelah itu hanya 4 karakter terakhir |
| Audit log | Tabel: waktu, pengguna, aksi, objek, IP (disamarkan sebagian). Filter per aksi. Tidak bisa diedit/dihapus dari UI |
| Simpan | Sticky footer *Batal* / *Simpan* muncul hanya bila ada perubahan; peringatan saat meninggalkan halaman dengan perubahan belum tersimpan |

## 8. Tim

| Komponen | Spek |
|---|---|
| Tabel | Avatar 32 + nama, peran (select inline untuk Owner), klien yang dipegang (chip), beban minggu ini (bar kecil) |
| Undang | Dialog: email, peran, klien (multi-select) → *Kirim undangan*; status undangan "Menunggu" sampai diterima |
| Beban kerja | Bar warning bila review > 10/minggu per orang (ambang bisa diatur) |
| Empty (solo) | "Anda bekerja sendiri saat ini" → *+ Undang anggota tim*. Catatan: review independen L2/L3 butuh minimal 2 orang (atau klien sebagai reviewer) |

---

## Data Density & Performance

| Aturan | Nilai |
|---|---|
| Virtualisasi list | Tabel/kanban > 100 item memakai virtual list |
| Pagination server | 25 baris default, maks 100 |
| Gambar thumbnail | 160 px WebP/AVIF, lazy load |
| Optimistic update | Drag kanban & toggle langsung terlihat; rollback + toast bila server menolak |
| Polling / realtime | Status agent & notifikasi lewat SSE/WebSocket; fallback polling 30 dtk |

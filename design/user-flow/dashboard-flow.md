# User Flow — Studio (Dashboard Internal)

> **ID:** 5 flow utama owner agency dan tim. Notasi sama dengan [client-portal-flow](./client-portal-flow.md): `[ ]` layar · `< >` keputusan · `( )` sistem · `==>` sukses · `-->` alternatif/error.
> **EN:** 5 core Studio flows with trigger, steps, decision points, error handling, and success state.

**Login Studio** memakai flow yang sama dengan Portal (Flow 5 di file klien), ditambah **2FA wajib** untuk peran Owner/Admin: kode dari authenticator app atau kunci keamanan. SMS OTP tidak dipakai untuk peran ini.

---

## Flow 1 — Kelola Klien / Manage a Client

`Login → Ringkasan → Klien → Detail → Aksi`

**Trigger:** klien baru tanda tangan kontrak, atau kartu "Fakta belum dikonfirmasi" di Ringkasan.

```text
 [Ringkasan] ──► [Klien] ──cari / filter──► [Detail klien]
                    │                             │
                    │ + Tambah klien              ├─ Tab Fakta ──► < Ada CLIENT CONFIRMATION? >
                    ▼                             │                   │ ya
 [Form klien baru]                                │                   ▼
  nama · industri · wilayah · zona waktu ·        │          [Pilih fakta] ──► Kirim pengingat
  paket · approver (email/WA)                     │                   │
        │ Simpan                                  │                   ▼
        ▼                                         │          (Notifikasi ke Portal klien +
 < Email approver sudah punya akun? >             │           WA/email) ==> toast "Pengingat
   │ ya ──► tautkan ke properti                   │           terkirim ke Bu Sari"
   │ tidak ──► kirim undangan Portal              │
        ▼                                         ├─ Tab Akses ──► tambah/hapus approver,
 ==> [Detail klien] status "Onboard"              │                atur level L1/L2/L3
     checklist: fakta · brand voice · foto ·      │
     akses IG insight                             └─ Aksi ▾ ──► Jeda / Arsipkan / Lihat sebagai klien
```

| Keputusan | Aturan |
|---|---|
| Status Onboard → Aktif | Otomatis saat fact sheet disetujui owner + minimal 1 approver aktif |
| Arsipkan klien | Dialog danger dengan mengetik nama klien. Data diarsipkan, tidak dihapus. Hapus permanen hanya oleh Owner, sesuai kebijakan retensi |
| Lihat sebagai klien | Mode read-only dengan banner "Anda melihat sebagai klien"; tidak bisa approve |

| Error | Penanganan |
|---|---|
| Email approver salah format / duplikat | Pesan inline per field |
| Undangan tidak diterima 72 jam | Badge "Undangan belum diterima" + *Kirim ulang* |

**Sukses:** klien punya ruang data sendiri, approver diundang, dan checklist onboarding terlihat.

---

## Flow 2 — Konten sampai Tayang / Content to Published

`Login → Ringkasan → Konten → (QA) → Kirim ke klien → … → Tandai sudah tayang`

**Trigger:** brief baru, atau kolom Disetujui berisi konten yang jadwal tayangnya hari ini.

```text
 [Konten: Backlog] ──► Jalankan agent (Copywriter dll.) ──► (Draft v1 dibuat; agent & skill dicatat)
        ▼
 [Review QA]  tab Klaim (per kalimat) · check_caption "PASS (mekanis)" · checklist QA
        ▼
 < QA lulus? > ──tidak──► Minta revisi agent / edit manual ──► kembali ke Review QA
        │ ya
        ▼
 < Level L2/L3? > ──ya──► [Tugaskan reviewer]  (pembuat draft tidak bisa dipilih)
        │ tidak (L1)              ▼
        │                 < Reviewer: Lulus? > ──tidak──► kembali ke Dikerjakan + catatan
        │                         │ ya
        ▼                         ▼
 [Kirim ke klien] ──► (Status: Di klien; notifikasi ke approver)
        ▼
 < Klien menyetujui? >  (terjadi di Portal Klien, Flow 1)
   │ minta revisi ──► kembali ke Dikerjakan (dengan catatan klien)
   │ setuju
   ▼
 [Disetujui]  ──► Manusia publish di Instagram/TikTok/GBP (di luar aplikasi)
        ▼
 [Tandai sudah tayang]  URL post (wajib) · tanggal & jam aktual · zona waktu
        ▼
 < URL valid & domain cocok channel? > ──tidak──► pesan inline "URL harus dari instagram.com"
        │ ya
        ▼
 ==> (Status: Tayang; pengingat monitor 24 & 72 jam dibuat; klien diberi tahu "Konten tayang")
```

| Aturan keras (diblok sistem) | Sumber aturan |
|---|---|
| Tidak ada tombol "Publish" / auto-post | AI-CONSTITUTION §4, CONTENT-WORKFLOW Step 8 |
| L2/L3 tidak bisa *Kirim ke klien* tanpa review independen | rule 08 |
| Pembuat draft tidak bisa me-review drafnya sendiri sebagai "independen" | rule 08 |
| Konten yang diubah setelah disetujui kembali ke *Di klien* | CONTENT-WORKFLOW Step 7 |

| Error | Penanganan |
|---|---|
| Agent gagal membuat draft | Kartu tetap di Backlog dengan badge error + *Lihat log* / *Coba ulang* |
| Jadwal tayang lewat tapi belum ditandai tayang | Notifikasi ke PJ: "Belum ditandai tayang (jadwal 18.00 WITA)" |

**Sukses:** setiap konten tayang punya jejak lengkap: draft → QA → reviewer → approval klien → URL & jam tayang.

---

## Flow 3 — Monitor AI Agent

`Login → Ringkasan → AI Agent → Monitor`

**Trigger:** kartu Agent di Ringkasan menunjukkan error, atau cek rutin pagi.

```text
 [Ringkasan] kartu "Agent 5/6 siap · 1 error" ──► [AI Agent]
        ▼
 < Ada agent Error? > ──ya──► [Detail agent] ──► Lihat log (mono, bisa disalin)
        │ tidak                     ▼
        │              < Penyebab jelas? >
        │                 │ ya: input/brief salah ──► perbaiki brief ──► Coba ulang tugas
        │                 │ ya: konfigurasi (API/integrasi) ──► [Pengaturan → Integrasi]
        │                 │ tidak ──► tandai "Butuh bantuan teknis" + salin log ke issue
        ▼
 < Ada agent "Menunggu manusia"? > ──ya──► klik ──► antrean tugas manusia (review, approval)
        │ tidak
        ▼
 ==> Semua agent Siap/Bekerja; antrean wajar
```

| Error | Penanganan |
|---|---|
| Halaman status gagal dimuat | Banner "Status agent belum bisa dimuat" + waktu data terakhir; tidak menampilkan "Siap" palsu |
| Realtime terputus | Indikator kecil "Terakhir diperbarui 2 menit lalu" + fallback polling |

**Sukses:** owner tahu dalam < 30 detik apakah produksi berjalan, dan apa yang menunggu manusia.

---

## Flow 4 — Export Laporan / Export Reports

`Login → Ringkasan → Laporan → Export`

**Trigger:** awal bulan (tanggal 1–5), notifikasi "Draft laporan September siap".

```text
 [Laporan] periode ▾ ──► tabel per klien
        ▼
 < Status klien? >
   │ Data kurang ──► [Lengkapi] daftar konten tanpa URL/metrik ──► isi ──► status jadi Draft
   │ Draft ──► [Editor laporan] ringkasan (manusia, boleh dibantu AI) + preview PDF
   │                 ▼ Kirim ke klien
   │           < Semua metrik punya sumber? > ──tidak──► tombol nonaktif + daftar yang kurang
   │                 │ ya
   │                 ▼
   │           ==> (PDF dibuat; notifikasi ke Portal klien; status Terkirim)
   ▼
 [Export semua (ZIP)] ──► (job background, progres di toast) ==> unduh ZIP
                                   --> gagal: toast + Coba lagi; file yang sudah jadi tetap bisa diunduh satu-satu
```

**Sukses:** laporan setiap klien terkirim dengan angka bersumber, dan arsip ZIP tersedia untuk agency.

---

## Flow 5 — Pengaturan / Settings → Config → Save

`Login → Pengaturan → Config → Simpan`

**Trigger:** setup awal agency, menambah integrasi, atau rotasi API key.

```text
 [Pengaturan] ──► pilih section (Brand · Paket · Integrasi · API · Notifikasi · Keamanan · Audit)
        ▼
 [Form section] ──ubah──► (Sticky footer Batal/Simpan muncul)
        ▼ Simpan
 < Valid? > ──tidak──► error inline (mis. "Warna ini 3.1:1 terhadap putih, di bawah AA 4.5:1")
        │ ya
        ▼
 < Perubahan sensitif? (keamanan, API key, hapus integrasi) >
        │ ya ──► [Konfirmasi ulang identitas] (kata sandi / 2FA) ──gagal──► dibatalkan
        │ tidak
        ▼
 ==> (Simpan; catat ke Audit log) ──► toast "Pengaturan disimpan"

 Integrasi:  [Hubungkan Instagram] ──► (OAuth platform, scope baca insight) ──►
             < Diizinkan? > ya ==> "Terhubung" · tidak --> "Dibatalkan; tidak ada data diambil"
```

| Error | Penanganan |
|---|---|
| Meninggalkan halaman dengan perubahan | Dialog "Simpan perubahan sebelum keluar?" |
| Token integrasi kedaluwarsa | Badge "Perlu dihubungkan ulang" di kartu integrasi + notifikasi ke Owner |
| API key bocor | *Cabut* key (langsung tidak berlaku) → buat baru; tercatat di audit log |

**Sukses:** konfigurasi tersimpan, perubahan sensitif terverifikasi, dan semuanya tercatat di audit log.

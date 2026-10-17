# Pilar di UI — Portal Klien & Studio

> **ID:** Cara 5 pilar CLAU AI (v2, AI-CONSTITUTION v3.0.0) tampil di Portal Klien dan Studio. Pilar 1 AI Marketing sudah dirancang penuh di wireframe; pilar 2–5 baru **rencana permukaan** (**ASSUMPTION**) sampai task tiap pilar dikerjakan (TASK-035–039).
> **EN:** How the 5 CLAU AI pillars (v2) appear in the Client Portal and Studio. Pillar 1 is fully specified; pillars 2–5 are planned surfaces.

| Item | Nilai |
|---|---|
| Arsitektur induk | `clau-core/docs/5-pillar-architecture.md` (Approved, v3.0.0) |
| Sumber data pilar & agent | `clau-agent/agents/registry.json` → `pillars` + `agents` + `autonomy_max` (juga `GET /pillars`, `POST /route`) |
| Status | Draft v0.2 (2026-10-09) |

## 5 Pilar v2

Disetujui owner (Dea Karisna / d34faiza) di AI-CONSTITUTION v3.0.0: **AI Marketing · AI Sales · AI Admin · AI Business Intelligence · AI Automation**, dengan **otonomi bertingkat A/B/C** (default B) dan vertical fokus villa, restoran/cafe, wedding, travel. Shell UI di dokumen ini tidak berubah: pilar hanya atribut, jadi nama/jumlah pilar cukup lewat registry. Tambahan UI karena v3.0.0: **badge level otonomi** per agent/aksi, pengaturan **template Level A** di Portal Klien (nanti, saat AI Sales aktif), dan halaman **Alur** (AI Automation) di Studio dengan audit log & tombol berhenti (TASK-039).

## Prinsip

| # | Prinsip | Artinya |
|---|---|---|
| 1 | **Satu shell untuk semua pilar** | Navigasi Portal & Studio tidak berubah saat pilar baru aktif. Pilar adalah **atribut** item (konten, permintaan, laporan, agent), bukan aplikasi terpisah |
| 2 | **Data dari registry, bukan hardcode** | Nama pilar, status, nama agent, avatar, dan level otonomi dibaca dari `registry.json`. Mengaktifkan pilar = ubah registry + core, bukan ubah komponen |
| 3 | **Pilar belum aktif terlihat jujur** | Agent pilar belum aktif tampil abu-abu "Belum aktif", tanpa tombol *Jalankan*; permintaannya dieskalasi ke owner. Tidak ada angka 0 palsu di laporan; tulis "Belum ada data: pilar belum aktif" |
| 4 | **Otonomi terlihat & dibatasi** | Default **Level B**: AI menyiapkan, manusia menekan kirim. **Level A** (kirim otomatis) hanya untuk template yang disetujui client + fakta DATA FINAL, dengan audit log & tombol berhenti; **Level C** = eskalasi. Tidak ada tombol publish ke platform sosial di pilar mana pun (AI-CONSTITUTION §4.7, §4a) |
| 5 | **Level approval bisa naik, tidak turun** | Level minimum per intent dari router; isi konten bisa menaikkan (harga → min L2, keluhan serius → L3). Lihat TASK-032 |
| 6 | **Pillar Badge netral** | `P1`–`P5` outline neutral + nama lengkap di tooltip. Tidak memakai warna per pilar supaya tidak bentrok dengan warna status & evidence |

## Peta Pilar → Permukaan

| # | Pilar | Status | Agent · intent | Studio | Portal Klien | Approval min | Otonomi |
|---|---|---|---|---|---|---|---|
| 1 | AI Marketing | **Aktif** | Tara, Raka, Sekar, Bayu, Laras, Dimas, Ayu, Nara | Pipeline Konten, Kalender, AI Agent | Konten + approval, Konfirmasi Fakta, Kalender, Laporan | L1–L3 | B |
| 2 | AI Sales | Planned | Galih · `inquiry-reply`; Sari · `guest-message` | Antrean **Inquiry**, **Pesan tamu**, **Eskalasi keluhan**, lead | Konfirmasi **harga & paket**; persetujuan **template Level A** | L2 / L3 | B (A per template & client) |
| 3 | AI Admin | Planned | Teguh · `sop` (+ intent usulan quotation, invoice-draft) | **Library SOP**, antrean **Dokumen** (quotation/invoice draft) | Approval SOP & dokumen | L1–L2 | B |
| 4 | AI Business Intelligence | Planned (agent Intan aktif, template Pilar 1) | Intan · `report` | Laporan tab **Per pilar**, KPI | Laporan bulanan, bagian per pilar aktif | L1 | B |
| 5 | AI Automation | Planned (tanpa agent) | — (menyambung intent pilar lain) | Halaman **Alur**: daftar alur, run log, dry run, tombol berhenti | Ringkasan alur aktif untuk client | Per langkah | Per langkah |

## Detail per Pilar (rencana)

### Pilar 2 — AI Sales

| Aspek | Rencana |
|---|---|
| Item | Inquiry (DM/WA/email) → draft balasan Galih; pesan pre-arrival & FAQ (Sari); eskalasi keluhan; lead & follow-up |
| Aturan UI | Harga, tanggal, dan ketersediaan **hanya** dari fakta **DATA FINAL** (fact sheet klien). Fakta lain tampil sebagai **CLIENT CONFIRMATION** dan memblok tombol *Siap dikirim manusia*. Data tamu minimum: inisial + kode reservasi, bukan nama lengkap/nomor HP. Keluhan serius (keselamatan, kesehatan, diskriminasi, ancaman hukum) → **RISK** + L3 + Level C |
| Level A (nanti) | Hanya jawaban yang **persis** template disetujui client (jam buka, lokasi, katalog). Badge "Otomatis (A)" pada pesan terkirim; 2 minggu pertama semua pesan A masuk antrean review manusia |
| Tidak ada | Ubah harga/ketersediaan (`change_price_or_availability` di `default_forbidden_actions`), menyimpan identitas tamu di platform |
| Ke pilar lain | Paket/promo disetujui → campaign Pilar 1; order → quotation Pilar 3; jumlah inquiry & tema keluhan → Pilar 4 (tanpa data pribadi) |

### Pilar 3 — AI Admin

| Aspek | Rencana |
|---|---|
| Item | SOP & checklist; quotation & invoice **draft**; data entry; ringkasan keuangan; stok |
| Aturan UI | Setiap angka bisa diklik ke baris data sumber. Nomor dokumen dari sistem, bukan dibuat AI. SOP punya versi, pemilik, tanggal review, status; langkah keselamatan wajib **FIELD VERIFICATION** sebelum Approved |
| Ke pilar lain | SOP & katalog → jawaban FAQ Pilar 2; transaksi & stok → Pilar 4 |

### Pilar 4 — AI Business Intelligence

| Aspek | Rencana |
|---|---|
| Item | Laporan bulanan, KPI lintas pilar, insight, forecast |
| Aturan UI | Setiap angka menyebut sumber + waktu tarik data. Tidak ada atribusi tanpa tracking ("konten ini menghasilkan 12 booking"). Forecast diberi label **ASSUMPTION** + rentang. Pilar belum aktif: "Belum ada data", bukan 0 |
| Sekarang | Agent Intan memakai template `monthly-report` Pilar 1; template Pilar 4 sendiri = TASK-038 |

### Pilar 5 — AI Automation

| Aspek | Rencana |
|---|---|
| Item | Alur end-to-end (mis. WA → lead → Sheets → quotation draft → notifikasi approver) |
| Aturan UI | Setiap langkah alur menampilkan level otonomi; satu langkah B = alur berhenti di antrean "Menunggu manusia". Run log per eksekusi, **dry run** sebelum aktif, **tombol berhenti** per alur & per client |
| Engine | Keputusan = TASK-039 |

## Nama Produk

**Diputuskan: opsi B** (**DATA FINAL, opsi B issue #46 — Dea Karisna (d34faiza), 2026-10-09**, atas rekomendasi agent; TASK-043).

| Level | Nama | Contoh di UI |
|---|---|---|
| Merek payung | **CLAU AI** | Logo, judul tab browser, email, Pengaturan → Nama |
| Modul (per pilar) | **Content Studio** (AI Marketing, aktif) · AI Sales · AI Admin · AI Business Intelligence · AI Automation | Deskriptor di bawah logo dan judul halaman modul |

Riwayat: 2026-10-07 nama tunggal "CLAU AI Content Studio" (**DATA FINAL** saat itu) → 2026-10-09 digantikan opsi B. Komponen tidak berubah; nama lewat string i18n `app.name` + `module.name`.

## Checklist Aktivasi Pilar di UI

1. Struktur pilar disetujui (✅ v3.0.0) dan task pilar dimulai (TASK-035–039).
2. `registry.json`: status agent + `pillars[].status`/`repo` → `active`; README & 5-pillar-architecture di core ikut diubah (test registry gagal bila tidak sama). Level A hanya bila kolom Otonomi router diubah atas perintah owner.
3. Desain layar khusus pilar (antrean, library, alur) mengikuti tabel di atas; tambahkan ke wireframe & mockup.
4. Filter Pilar & Pillar Badge di Pipeline/Kalender otomatis menampilkan pilar baru.
5. Tambah baris QA di [handoff/qa-checklist.md](./handoff/qa-checklist.md) untuk aturan khusus pilar.
6. Pilot SIMULASI end-to-end sebelum dipakai klien.

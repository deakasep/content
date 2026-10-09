# Pilar di UI — Portal Klien & Studio

> **ID:** Cara 5 pilar CLAU AI tampil di Portal Klien dan Studio. Pilar 1 sudah dirancang penuh di wireframe; pilar 2–5 baru **rencana permukaan** (**ASSUMPTION**) yang menunggu keputusan scope dari owner (TASK-034) dan task tiap pilar (TASK-035–038).
> **EN:** How the 5 CLAU AI pillars appear in the Client Portal and Studio. Pillar 1 is fully specified; pillars 2–5 are planned surfaces awaiting owner decisions.

| Item | Nilai |
|---|---|
| Arsitektur induk | `clau-ai-core/docs/5-pillar-architecture.md` |
| Sumber data pilar & agent | `clau-ai-agents/agents/registry.json` → `pillars` + `agents` (juga `GET /pillars`, `POST /route`) |
| Status | Draft v0.1 (2026-10-09) |

## Konsep v2 (masa depan)

Owner menyiapkan konsep 5 pilar v2: **AI Marketing · AI Sales · AI Admin · AI Business Intelligence · AI Automation** (cetak biru `clau-ai-core/docs/blueprints/`). Shell UI di dokumen ini tetap berlaku: pilar hanya atribut, jadi mengganti nama/jumlah pilar cukup lewat registry. Tambahan UI saat v2 aktif: badge **level otonomi A/B/C** per aksi, pengaturan template Level A di Portal Klien, dan halaman **Alur (Automation)** di Studio dengan audit log & tombol berhenti (TASK-039, TASK-040).

## Prinsip

| # | Prinsip | Artinya |
|---|---|---|
| 1 | **Satu shell untuk semua pilar** | Navigasi Portal & Studio tidak berubah saat pilar baru aktif. Pilar adalah **atribut** item (konten, permintaan, laporan, agent), bukan aplikasi terpisah |
| 2 | **Data dari registry, bukan hardcode** | Nama pilar, status, nama agent, dan avatar dibaca dari `registry.json`. Mengaktifkan pilar = ubah registry + core, bukan ubah komponen |
| 3 | **Pilar belum aktif terlihat jujur** | Agent pilar belum aktif tampil abu-abu "Belum aktif", tanpa tombol *Jalankan*; permintaannya dieskalasi ke owner. Tidak ada angka 0 palsu di laporan; tulis "Belum ada data: pilar belum aktif" |
| 4 | **Aturan manusia sama di semua pilar** | AI tidak publish, tidak mengirim ke tamu/pihak luar, tidak self-approve (AI-CONSTITUTION §4). Tombol kirim/publish tidak ada di pilar mana pun |
| 5 | **Level approval bisa naik, tidak turun** | Level minimum per intent dari router; isi konten bisa menaikkan (harga → min L2, keluhan serius → L3). Lihat TASK-032 |
| 6 | **Pillar Badge netral** | `P1`–`P5` outline neutral + nama lengkap di tooltip. Tidak memakai warna per pilar supaya tidak bentrok dengan warna status & evidence |

## Peta Pilar → Permukaan

| # | Pilar | Status | Agent · intent | Studio | Portal Klien | Approval min |
|---|---|---|---|---|---|---|
| 1 | Marketing & Content | **Aktif** | Tara, Raka, Sekar, Bayu, Laras, Dimas, Ayu, Nara | Pipeline Konten, Kalender, AI Agent | Konten + approval, Konfirmasi Fakta, Kalender, Laporan | L1–L3 |
| 2 | Sales & Reservations | Planned | Galih · `inquiry-reply` | Antrean **Inquiry** (filter Pilar 2 di Pipeline) | Konfirmasi **harga & paket** (pakai Fact Confirm Row) | L2 |
| 3 | Guest Experience & Reputation | Planned | Sari · `guest-message` | Antrean **Pesan tamu** + **Eskalasi keluhan** | Persetujuan template pesan; keluhan serius = L3 owner | L2 / L3 |
| 4 | Operations | Planned | Teguh · `sop` | **Library SOP** (versi, pemilik, tanggal review) | Approval SOP oleh manager properti | L1–L2 |
| 5 | Analytics & Insights | Planned (agent Intan aktif, template Pilar 1) | Intan · `report` | Laporan tab **Per pilar** | Laporan bulanan, bagian per pilar aktif | L1 |

## Detail per Pilar (rencana)

### Pilar 2 — Sales & Reservations

| Aspek | Rencana |
|---|---|
| Item | *Inquiry* (DM/WA/email) → draft balasan Galih |
| Aturan UI | Harga, tanggal, dan ketersediaan **hanya** dari fakta berstatus **DATA FINAL** (fact sheet klien). Fakta lain tampil sebagai **CLIENT CONFIRMATION** dan memblok tombol *Siap dikirim manusia* |
| Tidak ada | Tombol kirim ke tamu, ubah harga/ketersediaan (`change_price_or_availability` ada di `default_forbidden_actions`) |
| Ke pilar lain | Paket/promo yang disetujui → materi campaign Pilar 1; jumlah inquiry → Pilar 5 (tanpa data pribadi) |

### Pilar 3 — Guest Experience & Reputation

| Aspek | Rencana |
|---|---|
| Item | Pesan pre-arrival, FAQ in-stay, eskalasi keluhan |
| Aturan UI | Data tamu minimum: tampilkan inisial + kode reservasi dari sistem klien, bukan nama lengkap/nomor HP. Keluhan serius (keselamatan, kesehatan, diskriminasi, ancaman hukum) → label **RISK** + level L3 otomatis |
| Tidak ada | Kirim pesan ke tamu, menyimpan identitas tamu di platform |
| Ke pilar lain | Insight review → angle konten Pilar 1; tema keluhan → Pilar 5 |

### Pilar 4 — Operations

| Aspek | Rencana |
|---|---|
| Item | SOP, checklist housekeeping/F&B, materi onboarding staf |
| Aturan UI | Setiap SOP punya versi, pemilik, tanggal review berikutnya, dan status (Draft/In Review/Approved). Langkah keselamatan wajib **FIELD VERIFICATION** sebelum Approved |
| Ke pilar lain | SOP terbaru → jawaban FAQ in-stay Pilar 3 |

### Pilar 5 — Analytics & Insights

| Aspek | Rencana |
|---|---|
| Item | Laporan bulanan, KPI lintas pilar |
| Aturan UI | Setiap angka menyebut sumber + waktu tarik data. Tidak ada atribusi tanpa tracking ("konten ini menghasilkan 12 booking"). Pilar belum aktif: "Belum ada data", bukan 0 |
| Sekarang | Agent Intan memakai template `monthly-report` Pilar 1; template Pilar 5 sendiri = TASK-038 |

## Nama Produk

Nama **CLAU AI Content Studio** tetap (**DATA FINAL**, 2026-10-07). Karena platform akan melayani 5 pilar, pilihan berikut dicatat untuk keputusan owner di TASK-034 (**CLIENT CONFIRMATION**):

| Opsi | Struktur | Catatan |
|---|---|---|
| A (sekarang) | Satu nama "CLAU AI Content Studio" untuk semua pilar | Tidak ada perubahan; nama terasa sempit saat Pilar 2–4 aktif |
| B (usulan) | Merek payung **CLAU AI**; "Content Studio" = modul Pilar 1; modul lain mengikuti nama pilar | Komponen tidak berubah; cukup ganti string i18n `app.name` |

Spec ini sudah **netral nama**: komponen memakai string i18n, jadi keputusan nama tidak memblok Figma maupun development.

## Checklist Aktivasi Pilar di UI

1. Owner menyetujui scope pilar (TASK-034) dan task pilar dimulai (TASK-035–038).
2. `registry.json`: status agent + `pillars[].status`/`repo` → `active`; README & 5-pillar-architecture di core ikut diubah (test registry gagal bila tidak sama).
3. Desain layar khusus pilar (antrean, library) mengikuti tabel di atas; tambahkan ke wireframe & mockup.
4. Filter Pilar & Pillar Badge di Pipeline/Kalender otomatis menampilkan pilar baru.
5. Tambah baris QA di [handoff/qa-checklist.md](./handoff/qa-checklist.md) untuk aturan khusus pilar.
6. Pilot SIMULASI end-to-end sebelum dipakai klien.

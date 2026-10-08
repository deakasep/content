# Brand Guideline — CLAU AI Content Studio

> **ID:** Identitas brand untuk produk CLAU (Portal Klien + Studio). Status: **v1.0 Draft**. Nama, warna, dan font siap dipakai untuk Figma dan kode. **Logo final belum ada**, baru konsep di [logo-concept.md](./logo-concept.md). Brand ini milik CLAU sendiri, terpisah dari brand mentor/klien mana pun.
> **EN:** Brand identity for the CLAU product. v1.0 Draft: name, colors, and fonts are ready; the final logo is pending.

## 1. Nama / Name

| Item | Keputusan |
|---|---|
| Nama produk | **CLAU AI Content Studio** (**DATA FINAL**, diputuskan Dea Karisna 2026-10-07) |
| Penulisan | `CLAU` selalu huruf besar semua; "Content Studio" title case. Singkatan di UI sempit: **CLAU** |
| Permukaan produk | **CLAU Portal** (untuk klien) · **CLAU Studio** (untuk agency) |
| Tagline (usulan) | ID: **"Konten jujur, tamu datang."** · EN: **"Honest content. Real guests."** |
| Deskriptor | ID: *Studio konten AI untuk hospitality Indonesia* · EN: *AI content studio for Indonesian hospitality* |
| Jangan | "Clau", "C.L.A.U", "CLAU AI Bot", atau terjemahan nama |

**RISK / NEXT ACTION:** sebelum dipakai publik, cek ketersediaan nama di pangkalan data merek DJKI (Direktorat Jenderal Kekayaan Intelektual), domain, dan handle media sosial.

## 2. Esensi Brand / Brand Essence

| | |
|---|---|
| **Misi** | Membantu bisnis hospitality di seluruh Indonesia tampil konsisten dan jujur di media sosial, dengan AI yang menyiapkan dan manusia yang memutuskan |
| **Janji** | Setiap konten bisa dipertanggungjawabkan ke tamu |
| **Kepribadian** | Hangat · Teliti · Tenang · Lokal tapi profesional |
| **Bukan** | Hype AI, "viral instan", jargon teknologi, gaya agency yang berlebihan |
| **Pembeda** | Fakta dikonfirmasi owner, label evidence terlihat, AI tidak pernah publish sendiri |

## 3. Warna Final / Final Colors

Sumber: [`tokens.json`](../tokens/tokens.json). Semua kombinasi teks diuji WCAG AA.

| Peran | Nama | HEX | Proporsi pemakaian |
|---|---|---|---|
| Primary | **Teal Laut** | `#0F766E` | ± 10%: tombol utama, link, aksen logo |
| Secondary | **Terracotta** | `#C2410C` | ± 3–5%: highlight promo, badge "Baru" |
| Netral terang | **Pasir** (Stone 50) | `#FAFAF9` | ± 60%: background |
| Netral gelap | **Arang** (Stone 900) | `#1C1917` | ± 20%: teks |
| Netral tengah | **Batu** (Stone 500) | `#78716C` | Teks meta, garis |

**Filosofi:** teal = laut dan sawah, dua lanskap yang ada di hampir semua destinasi Indonesia. Terracotta = genteng, gerabah, dan senja: hangat dan buatan tangan. Stone = pasir dan batu alam. Palet ini sengaja **tidak** memakai merah-putih, supaya tidak terbaca sebagai brand pemerintah atau BUMN.

## 3b. Palet UI Produk v2 / Product UI Palette (DATA FINAL, 2026-10-07)

Diputuskan Dea Karisna (2026-10-07) untuk **antarmuka aplikasi** (dashboard, Portal, Studio), mengikuti `clau-ai-agents/docs/design/2026-10-07-enterprise-ui-brief.txt`. Palet §3 tetap dipakai untuk materi brand non-aplikasi (proposal, PDF, media sosial CLAU) sampai ada keputusan lain.

| Peran | Nama | HEX | Proporsi |
|---|---|---|---|
| Aksi utama & aksen | Deep Teal | `#0F766E` (hover `#115E59`, latar muda `#CCFBF1`) | ± 5–10% |
| Sidebar & teks utama | Deep Navy | `#0F172A` (sekunder `#1E3A5F`) | ± 15–20% |
| Latar | Slate 50 | `#F8FAFC` | ± 70–80% bersama permukaan putih |
| Permukaan / kartu | Putih | `#FFFFFF` | |
| Teks sekunder / muted | Slate | `#475569` / `#64748B` | `#94A3B8` hanya untuk elemen non-teks (kontras 2,56:1 di atas putih) |
| Garis | Slate 200 | `#E2E8F0` | |
| Status saja | Success / Warning / Error / Info | `#16A34A` / `#D97706` / `#DC2626` / `#2563EB` | Hanya untuk status, selalu disertai label |

Aturan: oranye/terracotta **tidak** dipakai sebagai warna brand di aplikasi (hanya warning). Font aplikasi: **Inter**. Agent ditampilkan dengan monogram, bukan karakter kartun. Implementasi: `clau-ai-agents/frontend/app/globals.css`.

Token: `../tokens/tokens.json` v1.1.0, `semantic.app-v2` (cek kontras WCAG AA lulus).

### 3c. UI v3 "AI Workforce" (DATA FINAL, 2026-10-08)

Dipasang Dea Karisna (2026-10-08) di atas palet §3b: bahasa UI **English default** dengan pilihan **EN / ID tanpa ikon bendera**, **dark mode** (Light / Dark / System), dan agent ditampilkan sebagai **avatar siluet geometris** dengan satu warna aksen per agent dari keluarga teal/biru/indigo/violet (bukan karakter kartun; **digantikan §3d** untuk avatar agent). Nilai warna dark mode dan aksen agent: `clau-ai-agents/frontend/README.md` (Snapshot v3). Snapshot kode: branch `ui-v3-workforce`.

### 3d. Avatar agent 3D (2026-10-08)

Menggantikan aturan avatar di §3c: setiap agent di registry tampil sebagai **figur 3D chibi** (latar mint `#DDF4EE`, satu karakter fiktif per agent). Diterapkan lewat `clau-ai-agents` PR #1 (di-merge 2026-10-08); perubahan guideline ini diizinkan di sesi yang sama. Agent konsep (belum di registry) tetap karakter SVG. Master dan status per gambar: `clau-ai-agents/agents/avatars/README.md`.

Batas yang tetap berlaku: karakter fiktif (bukan wajah staf/orang nyata), UI tetap menandai agent sebagai AI, batik hanya sebagai pakaian, tanpa simbol sakral (§6–7).

Status gambar (2026-10-08): ke-12 agent dan 3 agent konsep (Nova, Aruna, Dara) sudah sesuai nama, jenis kelamin, dan peran (`clau-ai-agents` PR #2–#4). Agent baru wajib punya avatar; dijaga test CI `clau-ai-agents/backend/tests/test_avatars.py`.

Token dark mode: `../tokens/tokens.json` v1.2.0 `semantic.app-v3-dark` (cek kontras WCAG AA otomatis, lihat tokens.md §5c).

## 4. Font Final / Final Typefaces

| Peran | Font | Lisensi | Kenapa |
|---|---|---|---|
| Heading & logotype | **Plus Jakarta Sans** (600, 700) | SIL OFL, gratis | Karya foundry Indonesia (Tokotype); geometris tapi hangat |
| Body & UI | **Inter** (400–600) | SIL OFL | Sangat terbaca di HP; angka tabular untuk harga & tanggal |
| Data & kode | **JetBrains Mono** | SIL OFL | ID konten, API |

Untuk dokumen Office (proposal, invoice) tanpa font tersebut: fallback **Arial** (heading bold) + **Arial** (body).

## 5. Voice & Tone

### Voice (tetap / constant)

| Sifat | Artinya | Contoh |
|---|---|---|
| **Hangat** | Menyapa seperti tuan rumah, bukan mesin | "Selamat sore, Bu Sari" |
| **Jelas** | Kalimat pendek, kata sehari-hari, tanpa jargon | "Konten ini menunggu persetujuan Ibu" (bukan "Pending approval workflow") |
| **Jujur** | Tidak melebih-lebihkan, termasuk tentang AI | "Disiapkan AI, diperiksa tim kami" |
| **Hormat** | Sapaan sesuai pilihan user (Bapak/Ibu/Kak); tidak menggurui | "Mohon konfirmasi harga sebelum tayang" |

### Tone (menyesuaikan situasi / adapts to context)

| Situasi | Tone | Contoh ID | Contoh EN |
|---|---|---|---|
| Sukses | Singkat, lega | "Konten disetujui. Tim akan menjadwalkan tayang." | "Approved. The team will schedule it." |
| Butuh tindakan | Tenang, spesifik | "2 fakta perlu Ibu konfirmasi sebelum konten bisa tayang." | "2 facts need your confirmation before this can go live." |
| Error | Bertanggung jawab, beri jalan keluar | "Belum tersimpan. Periksa koneksi lalu coba lagi. Data Anda aman." | "Not saved yet. Check your connection and try again. Your data is safe." |
| Kosong | Ramah, menjelaskan apa yang terjadi | "Konten pertama sedang disiapkan." | "Your first post is being prepared." |
| Risiko/peringatan | Lugas, tanpa menakut-nakuti | "Promo ini belum punya periode berlaku." | "This promotion has no validity period yet." |

### Aturan microcopy

- Tombol = kata kerja + objek: *Setujui konten*, *Unduh PDF*, *Kirim pengingat*.
- Hindari "Anda" berulang dalam satu kalimat; pakai sapaan dari profil bila natural.
- Angka & tanggal selalu format lokal (`Rp1.250.000`, `6 Okt 2026`, `18.00 WITA`).
- Emoji: maks 1, hanya di greeting atau state sukses/kosong. Tidak ada emoji di error.
- Label evidence (`DATA FINAL`, dll.) tidak diterjemahkan.

## 6. Elemen Visual / Visual Elements

| Elemen | Aturan |
|---|---|
| Fotografi | Foto **properti klien asli** menjadi pusat. Cahaya alami, tanpa filter berlebihan, tanpa orang yang belum memberi consent |
| Ilustrasi | Flat, garis sederhana, motif lanskap Nusantara (sawah bertingkat, garis laut, bukit, perahu). Maks 3 warna dari palet. **Tanpa** motif sakral/upacara keagamaan sebagai dekorasi |
| Ikon | Lucide, garis 2 px, sudut membulat (lihat [icons.md](../design-system/icons.md)) |
| Bentuk | Sudut 12 px untuk kartu; tidak ada sudut tajam 0 px dan tidak ada bentuk "blob" acak |
| Pola | Opsional: pola garis kontur sawah tipis (`primary-100` di atas `neutral-50`), hanya di halaman login & cover PDF |

## 7. Do & Don't

| Do ✅ | Don't ❌ |
|---|---|
| Pakai teal untuk satu aksi utama per layar | Teal & terracotta sama banyak (brand jadi ramai) |
| Tampilkan peran manusia: "diperiksa tim", "disetujui Ibu" | Klaim "100% otomatis oleh AI" |
| Foto properti klien sebagai visual utama | Stock photo orang bule tersenyum di kolam |
| Bahasa Indonesia yang baik dan santai-sopan | Campur Inggris-Indonesia setengah-setengah di satu kalimat UI |
| Sentuhan lokal lewat warna, ilustrasi lanskap, dan contoh copy | Ornamen batik/wayang/pura sebagai tempelan dekorasi |
| Logo dengan ruang kosong minimal setinggi huruf "C" | Logo diberi efek bayangan, gradien, atau diputar |
| Merek klien tetap jadi bintang di Portal | Logo CLAU lebih besar dari nama properti klien di Portal |

## 8. Aplikasi Brand / Applications

| Media | Catatan |
|---|---|
| Portal & Studio | Logo kecil di sidebar/top bar; nama properti klien lebih menonjol di Portal |
| Laporan PDF | Cover: logo CLAU + nama properti + periode; aman dicetak hitam-putih |
| Email/WA notifikasi | Pengirim "CLAU Portal"; tanpa gambar berat; 1 tombol/link |
| Favicon/app icon | Simbol logo saja (konsep di logo-concept.md), 32/180/512 px |
| Media sosial CLAU | Ikuti aturan konten CLAU sendiri (clau-ai-marketing), termasuk label evidence |

## Revision History

| Versi | Tanggal | Status | Ringkasan |
|---|---|---|---|
| 1.0 | 2026-10-06 | Draft | Nama kerja, warna & font final dari tokens v1.0.0, voice & tone, do & don't. Logo final menunggu konsep dipilih |

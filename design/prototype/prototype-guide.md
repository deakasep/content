# Prototype Guide — Figma, User Testing, Iterasi

> **ID:** Panduan praktis dari spesifikasi di folder ini ke prototype Figma yang bisa dites user. Fitur Figma dan Maze bisa berubah; nama menu di bawah sesuai versi saat ditulis (Okt 2026), jadi cek dokumentasi resmi bila ada yang berbeda.
> **EN:** A practical guide from these specs to a testable Figma prototype. Tool menus may change; check the official docs if something differs.

**Prioritas prototype pertama:** *Portal Klien mobile*, alur **Notifikasi → Detail Konten → Konfirmasi Fakta → Setujui**. Ini momen paling penting di [journey](../user-research/journey.md) dan paling berisiko gagal untuk persona Ibu Ratna.

---

## 1. Bikin Prototype di Figma

### 1.1 Siapkan file

| Langkah | Detail |
|---|---|
| 1 | Buat file `CLAU AI Content Studio` dengan halaman: `00 Cover`, `01 Design System`, `02 Portal — Mobile`, `03 Portal — Desktop`, `04 Studio — Desktop`, `05 Studio — Mobile`, `99 Arsip` |
| 2 | **Variables** (panel kanan → Local variables): buat koleksi `color` dengan mode **Light** dan **Dark** dari [colors.md](../design-system/colors.md); koleksi `space` & `radius` dari [spacing.md](../design-system/spacing.md) |
| 3 | **Text styles** dari [typography.md](../design-system/typography.md): `Display/H1`, `H2`…`H6`, `Body`, `Small`, `Tiny`, masing-masing versi Mobile & Desktop |
| 4 | Font: pasang **Plus Jakarta Sans**, **Inter**, **JetBrains Mono** (Google Fonts, tersedia di Figma) |
| 5 | Icon: plugin **Lucide Icons** untuk ikon; logo platform dari Simple Icons |
| 6 | Komponen dari [components.md](../design-system/components.md) dengan **variants** (`type=primary/secondary/…`, `size`, `state`) dan **auto layout** di semua komponen |
| 7 | Frame mobile **360 × 800** (Android baseline), desktop **1280 × 800**. Layout grid sesuai spacing.md (4/8/12 kolom) |
| 8 | Teks: buat semua layar di **Bahasa Indonesia** dulu, lalu duplikat frame kunci untuk versi **English** (cek teks yang memanjang) |

### 1.2 Link antar frame / Linking frames

1. Pindah ke tab **Prototype** (panel kanan).
2. Pilih elemen (mis. tombol *Lihat & setujui*), lalu tarik titik biru ke frame tujuan (*Detail Konten*).
3. Atur **Interaction**: `On tap` → `Navigate to` → frame tujuan.
4. Untuk tombol kembali: `On tap` → `Back`.
5. Tentukan **Flow starting point** di frame pertama setiap flow (mis. `Notifikasi WA`) dan beri nama flow: `F1 Approve`, `F2 Kalender`, `F3 Laporan`, `F4 Profil`, `F5 Reset password`.

### 1.3 Bikin interaksi / Interactions

| Interaksi | Cara di Figma |
|---|---|
| Tombol pressed | Variant `state=pressed` + `While pressing` → `Change to` |
| Toggle notifikasi | Komponen interaktif: `On tap` → `Change to` variant on/off |
| Bottom sheet | Frame sheet sebagai **overlay**: `Open overlay`, posisi *Bottom center*, animasi `Move in` dari bawah, 250 ms, `Ease out`; centang *Close when clicking outside* |
| Carousel preview IG | Frame dengan **horizontal scrolling** + snap; atau `Drag` → `Smart animate` antar-variant slide |
| Fakta *Benar* | Variant kartu `status=pending` → `status=confirmed` (badge berubah ke DATA FINAL), `Smart animate` 200 ms |
| *Setujui* nonaktif → aktif | Gunakan **variables boolean** (`allFactsConfirmed`) + *Set variable* saat semua fakta dikonfirmasi; tombol memakai **conditional** untuk navigasi |
| Toast | Overlay *Top center*, lalu `After delay 3000 ms` → `Close overlay` |
| Loading | Frame skeleton → `After delay 800 ms` → `Navigate to` frame berisi data, `Dissolve` |
| Bahasa ID/EN | Mode variable string (ID/EN) bila tim memakai variables untuk teks; bila tidak, frame terpisah |

### 1.4 Test di HP / Test on mobile

1. Instal aplikasi **Figma** (Android/iOS), login dengan akun yang sama.
2. Buka file → **Mirror** / tampilan prototype. Atau dari desktop: **Present** → *Share prototype* → buka link di browser HP.
3. Pilih device frame sesuai ukuran (Android 360 × 800).
4. Tes di **HP Android kelas menengah** dengan sinyal biasa, bukan hanya di HP desainer.
5. Cek: target sentuh ≥ 44 px, teks 16 px terbaca di luar ruangan, tombol utama terjangkau jempol.

### 1.5 Share

| Untuk | Cara | Izin |
|---|---|---|
| Pak Indra / reviewer internal | *Share* → link prototype | **Can view** |
| Tester (user test) | Link prototype tanpa akses file desain | View prototype only |
| Developer | Link file + **Dev Mode** (bila tersedia di paket) | Can view |
| Komentar | Mode komentar di prototype; minta reviewer menandai layar langsung | — |

Jangan memakai data client nyata di prototype. Pakai properti fiktif (**Villa Contoh Ubud**) supaya link aman dibagikan.

---

## 2. User Testing (Maze)

### 2.1 Siapkan

1. Buat akun **Maze** (paket gratis cukup untuk mulai; cek batas jumlah test/responden di paket yang aktif).
2. *New maze* → **Import Figma prototype** (tempel link prototype; flow starting point harus sudah ada).
3. Pilih bahasa instruksi: **Bahasa Indonesia** untuk klien lokal, English untuk persona owner asing.

### 2.2 Bikin task

Task ditulis sebagai **tujuan**, bukan instruksi klik ("Setujui konten…", bukan "Klik tombol hijau…").

| # | Task (ID) | Jalur sukses | Metrik |
|---|---|---|---|
| T1 | "Anda menerima pesan bahwa ada konten baru. Periksa dan setujui konten carousel kolam." | Notif → Detail → Konfirmasi 1 fakta → Setujui → Sukses | Success rate, waktu, misclick |
| T2 | "Harga di konten ternyata belum termasuk pajak. Beri tahu tim." | Detail → fakta harga → *Perbaiki* → kirim | Success rate |
| T3 | "Kapan story promo akan tayang?" | Kalender → item 13 Okt | Waktu |
| T4 | "Unduh laporan bulan September." | Laporan → Unduh PDF | Success rate |
| T5 | "Ubah bahasa aplikasi ke English." | Profil → Bahasa | Waktu |
| Q1 | Pertanyaan: "Apa arti label kuning 'CLIENT CONFIRMATION' menurut Anda?" | — | Jawaban terbuka |
| Q2 | Skala 1–5: "Seberapa mudah menyetujui konten?" (SEQ) | — | Rata-rata |

### 2.3 Kirim ke 5 orang

Lima orang cukup untuk menemukan sebagian besar masalah usability besar di satu putaran (pedoman umum Nielsen Norman Group). Lebih baik **3 putaran × 5 orang** daripada 1 putaran × 15.

| Slot | Profil | Kenapa |
|---|---|---|
| 2 | Owner/GM villa atau homestay (mirip Ibu Ratna), pakai Android | Persona paling berisiko |
| 1 | Owner cafe/resto (mirip Mas Budi) | Pengguna multi-cabang |
| 1 | Staf front office / marketing hotel | Sering menjadi approver sehari-hari |
| 1 | Owner properti di luar Bali (mis. Labuan Bajo, Danau Toba, Yogyakarta) | Cek asumsi bahwa desain tidak "Bali-sentris" |

Rekrut lewat jaringan klien dan komunitas owner. Beri insentif kecil (voucher/pulsa) dan izin tertulis bahwa hasil test dipakai untuk riset. Rekaman layar/suara hanya bila tester menyetujuinya.

### 2.4 Lihat hasil

| Lihat | Ambang perhatian |
|---|---|
| Success rate per task | < 80% → masalah serius |
| Misclick rate / heatmap | Klik berulang di elemen yang bukan tombol (mis. badge fakta dikira tombol) |
| Waktu per task | T1 > 2 menit → terlalu panjang untuk persona Ibu Ratna |
| Drop-off | Layar tempat tester berhenti |
| Jawaban Q1 | > 2 dari 5 salah paham → label evidence butuh penjelasan/ikon `info` |

---

## 3. Iterasi / Iterate

```text
 Kumpulkan ──► Prioritaskan ──► Revisi ──► Test lagi
   feedback       (severity ×      (Figma +     (5 orang
   (Maze +         frekuensi)       update       baru, task
   catatan)                         dokumen ini) yang sama)
```

### 3.1 Kumpulkan feedback

Satu tabel untuk semua temuan (bisa di Figma/FigJam atau spreadsheet):

| ID | Layar | Temuan | Bukti (task, % tester) | Severity |
|---|---|---|---|---|
| U-01 | Detail Konten | Tester tidak sadar ada fakta yang harus dikonfirmasi | T1, 3/5 langsung mencari tombol Setujui | Tinggi |

### 3.2 Prioritas

| Severity | Arti | Tindakan |
|---|---|---|
| **Tinggi** | Task gagal / data salah bisa lolos | Perbaiki sebelum putaran berikutnya |
| **Sedang** | Task berhasil tapi lambat/bingung | Perbaiki bila murah, atau di putaran berikutnya |
| **Rendah** | Kosmetik / preferensi | Backlog |

Prioritas = severity × jumlah tester yang mengalami. Temuan dari 1 orang tetap dicatat, tapi jangan langsung mengubah desain hanya karena satu orang.

### 3.3 Revisi

1. Ubah komponen di **halaman Design System** (bukan di tiap layar), supaya perubahan ikut ke semua layar.
2. Perbarui dokumen di repo ini (wireframe/mockup/flow) dan catat di **Revision log** di bawah.
3. Jangan ubah lebih dari yang dibutuhkan temuan, supaya hasil test berikutnya bisa dibandingkan.

### 3.4 Test lagi

- Task sama, **tester baru** (5 orang).
- Bandingkan success rate & waktu dengan putaran sebelumnya.
- Berhenti iterasi bila T1–T5 ≥ 80% sukses dan SEQ ≥ 4, lalu serahkan ke development.

## Revision Log

| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1 | 2026-10-06 | Dokumen awal (belum ada prototype Figma) |

# Components — Komponen

> **ID:** 22 komponen inti untuk Portal Klien dan Studio. Setiap komponen memakai token dari [colors](./colors.md), [typography](./typography.md), [spacing](./spacing.md), dan [icons](./icons.md). Rekomendasi implementasi: **Radix UI primitives** (aksesibilitas keyboard & ARIA sudah ditangani) + styling sendiri, bukan library UI jadi yang tampilannya generik.
> **EN:** 22 core components shared by the Client Portal and Studio. Suggested build: **Radix UI primitives** for accessibility, with our own styling.

## State Standar / Standard States

Berlaku untuk semua komponen interaktif kecuali disebut lain.

| State | Visual | Catatan |
|---|---|---|
| Default | Sesuai varian | — |
| Hover (desktop) | Background 1 tingkat lebih gelap/terang, `cursor: pointer` | Tidak ada hover di touch; jangan sembunyikan info di hover |
| Focus-visible | Ring 2 px `--color-focus` + offset 2 px | **Wajib** terlihat di keyboard; tidak dihapus dengan `outline: none` |
| Active / pressed | `transform: scale(0.98)`, 80 ms | Feedback sentuh di mobile |
| Disabled | Opacity 0.5, `cursor: not-allowed`, `aria-disabled` | Sertakan alasan di tooltip/helper bila memungkinkan |
| Loading | Spinner 16 px + label tetap (mis. "Menyimpan…") | Lebar tombol tidak berubah |

Transisi standar: `150ms cubic-bezier(0.2, 0, 0, 1)`. Hormati `prefers-reduced-motion`: animasi diganti fade 0 ms.

---

## 1. Button / Tombol

**Anatomi:** `[ikon opsional] Label [ikon opsional]` · padding horizontal 16 px · radius 8 px · font 16/600 (md).

| Varian | Tampilan | Pakai untuk |
|---|---|---|
| **Primary** | Fill `primary-600`, teks putih | Satu aksi utama per layar: *Setujui*, *Simpan*, *Masuk* |
| **Secondary** | Outline 1 px `neutral-500`, teks `neutral-900`, bg surface | Aksi kedua: *Minta revisi*, *Batal* |
| **Ghost** | Tanpa border, teks `primary-600` | Aksi ringan di toolbar: *Lihat semua* |
| **Danger** | Fill `#DC2626`, teks putih | *Hapus*, *Tolak konten* (selalu dengan dialog konfirmasi) |
| **Disabled** | Lihat state standar | — |

| Size | Tinggi | Font | Pakai |
|---|---|---|---|
| sm | 40 px* | 14/600 | Tabel, toolbar desktop |
| md | 44 px | 16/600 | Default |
| lg | 52 px | 16/600 | CTA utama mobile (full width di bottom bar) |

\*Tombol sm tetap punya area sentuh 44 px (padding transparan) di touch device.

**Contoh:** `[✓ Setujui konten]` primary + `[✎ Minta revisi]` secondary, berdampingan di footer detail konten.

| Do ✅ | Don't ❌ |
|---|---|
| Label kata kerja yang jelas: "Setujui konten" | "OK", "Submit", "Klik di sini" |
| Primary di kanan (desktop), di atas/full-width (mobile) | Dua primary dalam satu layar |
| Tombol mobile utama menempel di bawah (sticky) | Tombol utama di tengah halaman panjang |

## 2. Input (text, email, password, number)

**Anatomi:** Label (14/500, di atas) → field 44 px (border `neutral-500`, radius 8) → helper/error text (14/400).

| Tipe | Detail |
|---|---|
| text | `autocomplete` diisi sesuai konteks |
| email | `type="email"`, `inputmode="email"`, `autocapitalize="off"` |
| password | Tombol mata `eye`/`eye-off` (aria-label "Tampilkan kata sandi"), dukung password manager |
| number | `inputmode="numeric"`; untuk harga pakai input teks + format `Rp` otomatis, bukan `type="number"` |

**State tambahan:** error = border `#B91C1C` + ikon `circle-x` + pesan; success (validasi inline) = ikon `circle-check`.

| Do ✅ | Don't ❌ |
|---|---|
| Label selalu terlihat | Placeholder sebagai pengganti label |
| Pesan error yang menjelaskan solusi: "Email belum terdaftar. Cek ejaan atau hubungi agency." | "Input tidak valid" |
| Validasi saat blur, bukan setiap ketikan | Error merah sebelum user selesai mengetik |

## 3. Textarea

Sama seperti input; tinggi minimal 3 baris, `resize: vertical`, auto-grow sampai 10 baris. **Penghitung karakter** di kanan bawah untuk caption (mis. `1.240 / 2.200`). Warna penghitung berubah ke warning saat > 90%.

## 4. Select / Dropdown

**Anatomi:** trigger seperti input + `chevron-down` → listbox (radius 12, `shadow-md`, maks 320 px lalu scroll).

| Varian | Pakai |
|---|---|
| Native `<select>` | Mobile, pilihan ≤ 7 (paling cepat & aksesibel) |
| Combobox dengan search | Pilihan > 7 (daftar klien, kota) |
| Multi-select dengan chip | Filter channel (IG, TikTok, GBP) |

Don't: dropdown untuk 2 pilihan, pakai radio atau segmented control.

## 5. Checkbox / Radio

Kotak 20 px (radius 6) / lingkaran 20 px, **area sentuh 44 px termasuk label**. Checked = fill `primary-600` + `check` putih. Checkbox mendukung *indeterminate* (pilih sebagian di tabel). Label bisa diklik.

## 6. Toggle / Switch

Track 44 × 24 px, thumb 20 px. **Hanya untuk setting yang langsung berlaku** (notifikasi email on/off). Off = track `neutral-500`; On = `primary-600`. Label di kiri, switch di kanan. Don't: pakai toggle untuk aksi yang butuh tombol Simpan.

## 7. Card / Kartu

| Varian | Tampilan | Pakai |
|---|---|---|
| **Default** | Surface putih, border `neutral-200`, radius 12, `shadow-sm` | Kontainer info |
| **Interactive** | + hover `shadow-md` dan border `neutral-300`, seluruh kartu bisa diklik | Kartu konten, kartu klien |
| **Elevated** | `shadow-md`, tanpa border | Ringkasan penting di Beranda |
| **Media** | Foto 4:5 atau 1:1 di atas, radius atas 12 | Preview konten IG |

**Anatomi kartu konten:** thumbnail → judul (16/500) → meta channel + jadwal (14, `neutral-500`) → baris badge (status, level L1/L2/L3, jumlah fakta perlu konfirmasi).

Don't: tombol primary di setiap kartu dalam list.

## 8. Table / Tabel

**Fitur:** sortable (ikon `arrow-up-down` → `arrow-up`/`arrow-down`, `aria-sort`), filterable (toolbar di atas), paginated (25 baris default).

| Bagian | Spek |
|---|---|
| Header | 14/600, `neutral-700`, bg `neutral-50`, sticky saat scroll |
| Baris | Tinggi 52 px, border bawah `neutral-200`, hover `neutral-100` |
| Angka | Rata kanan, `tabular-nums` |
| Aksi baris | Menu `ellipsis-vertical` di kolom terakhir |

**Mobile (< 768):** tabel **berubah jadi list kartu** (kolom utama jadi judul, sisanya baris meta). Jangan pakai tabel lebar dengan horizontal scroll sebagai solusi utama.

## 9. Modal / Dialog

| Varian | Desktop | Mobile |
|---|---|---|
| Dialog konfirmasi | 440 px, tengah, overlay `rgba(28,25,23,.5)` | Bottom sheet |
| Form modal | 560–640 px | Full-screen sheet dengan tombol tutup kiri atas |

Wajib: focus trap, `Esc` menutup, fokus kembali ke pemicu, judul jadi `aria-labelledby`. Dialog berbahaya: tombol danger di kanan, **fokus awal di tombol Batal**.

## 10. Toast / Notification

Muncul di kanan bawah (desktop) atau atas (mobile, di bawah top bar). Lebar 360 px, radius 12, `shadow-lg`. Ikon semantic + pesan 1 baris + aksi opsional ("Urungkan"). Auto-hilang 5 detik (error: tetap sampai ditutup). `role="status"` (info/success) atau `role="alert"` (error). Maks 3 bertumpuk.

Contoh: `✓ Konten disetujui. Tim akan menjadwalkan tayang. [Urungkan]`

## 11. Badge / Tag

Tinggi 24 px, padding 4 × 8, radius 6, font 12/500, ikon 16 px. Varian: neutral, primary, accent, success, warning, error, info, **evidence** (6 label CLAU, lihat colors §5), **level** (`L1`/`L2`/`L3` outline), **pillar** (`P1`–`P5` outline neutral; nama pilar lengkap di tooltip & `aria-label`, mis. "Pilar 2 · Sales & Reservasi"; tidak memakai warna per pilar supaya tidak bentrok dengan warna status/evidence). Tag (bisa dihapus) = badge + tombol `x` 16 px dengan area 44 px.

## 12. Avatar

Ukuran 24/32/40/56. Foto bulat; fallback inisial (2 huruf, bg `primary-100`, teks `primary-800`). Grup avatar menumpuk maks 3 + `+N`. Status online dot 8 px di kanan bawah (Studio, untuk tim).

## 13. Tooltip

Muncul setelah 300 ms hover / saat fokus keyboard. Bg `neutral-900`, teks putih 12/500, maks 240 px. **Bukan untuk info penting** (tidak ada hover di HP). Untuk penjelasan di mobile, pakai ikon `info` yang membuka popover saat di-tap.

## 14. Breadcrumb

Hanya desktop/tablet, untuk halaman ≥ 3 level: `Klien / Villa Contoh Ubud / Konten / Carousel kolam`. Pemisah `chevron-right` 16 px. Item terakhir tidak bisa diklik (`aria-current="page"`). Mobile: diganti tombol `arrow-left` + judul induk.

## 15. Tabs

Garis bawah 2 px `primary-600` untuk tab aktif; teks 14/600. Mobile: scroll horizontal dengan fade di tepi, maks 5 tab. Keyboard: panah kiri/kanan berpindah tab. Contoh: `Semua · Perlu persetujuan · Disetujui · Tayang`.

## 16. Pagination

Desktop: `‹ Sebelumnya  1 2 3 … 8  Berikutnya ›` + info "Menampilkan 1–25 dari 184". Mobile: tombol "Muat lebih banyak" (lebih mudah daripada nomor halaman kecil). Infinite scroll **tidak** dipakai untuk tabel data (sulit kembali ke posisi).

## 17. Sidebar / Navigation

| Breakpoint | Bentuk |
|---|---|
| Mobile | **Bottom navigation** 4–5 item (ikon 24 + label 12), item aktif `primary-600` + indikator pill |
| Tablet | Rail 80 px |
| Desktop | Sidebar 256 px: logo, nav utama, nav sekunder (Settings), user di bawah; bisa dilipat ke 72 px |

Item aktif: bg `primary-50`, teks/ikon `primary-700`, `aria-current="page"`. Badge jumlah (mis. Notifikasi 3) di kanan item.

## 18. Header / Top Bar

56 px mobile / 64 px desktop. Isi: judul halaman (mobile) atau breadcrumb (desktop) · search (Studio) · toggle bahasa `ID | EN` · lonceng notifikasi · avatar. Portal Klien yang mengelola beberapa properti: **switcher properti** di kiri ("Villa Contoh Ubud ▾").

## 19. Footer

Hanya di halaman publik (login, reset password): `© 2026 CLAU · Kebijakan Privasi · Syarat Layanan · ID | EN`. Di dalam aplikasi tidak ada footer, supaya ruang mobile tidak terpakai.

## 20. Empty State

**Anatomi:** ilustrasi/ikon 48 px → judul (18/600) → 1 kalimat penjelasan → 1 tombol aksi (opsional).

| Halaman | Copy (ID / EN) |
|---|---|
| Konten (klien) | **Belum ada konten bulan ini** — Tim CLAU sedang menyiapkan konten pertama Anda. Kami kabari lewat notifikasi. / *No content this month yet — we'll notify you when the first draft is ready.* |
| Notifikasi | **Semua sudah dibaca** 🎉 / *You're all caught up* |
| Klien (Studio) | **Belum ada klien** — [+ Tambah klien pertama] |

Don't: halaman kosong putih tanpa penjelasan, atau "No data".

## 21. Loading Skeleton

Blok `neutral-200` dengan shimmer halus (1.5 s, dimatikan bila `prefers-reduced-motion`). Bentuk skeleton **sama dengan konten akhir** (kartu, baris tabel), supaya layout tidak lompat (CLS < 0.1). Tampilkan skeleton bila loading > 300 ms. Jangan tampilkan apa pun untuk < 300 ms (menghindari kedip).

## 22. Error State

| Jenis | Tampilan | Copy contoh |
|---|---|---|
| Inline (field) | Lihat Input | "Kata sandi minimal 8 karakter." |
| Section (satu kartu gagal muat) | Ikon `triangle-alert` + pesan + tombol "Coba lagi" di dalam kartu | "Kalender belum bisa dimuat. [Coba lagi]" |
| Halaman (404/500) | Ikon 48 px + judul + penjelasan + "Kembali ke Beranda" | "Halaman tidak ditemukan" / "Ada gangguan di sisi kami. Data Anda aman; coba lagi beberapa menit lagi." |
| Offline | Banner atas `warning`: "Anda sedang offline. Perubahan akan disimpan saat koneksi kembali." | Penting untuk area dengan sinyal lemah (Labuan Bajo, Raja Ampat) |

Pesan error **tidak menyalahkan user** dan tidak menampilkan kode teknis (kode ada di detail yang bisa dibuka, untuk dukungan teknis).

---

## Komponen Khusus CLAU / CLAU-specific

| Komponen | Fungsi |
|---|---|
| **Evidence Badge** | Badge 6 label evidence dengan ikon & warna tetap |
| **Fact Confirm Row** | Baris fakta: teks klaim + label + tombol `[Benar]` `[Perbaiki]`. Dipakai di Portal Klien (Konfirmasi Fakta) |
| **Content Preview** | Mockup tampilan IG (feed 4:5, story 9:16) dengan caption asli; slide carousel bisa digeser |
| **Approval Bar** | Footer sticky: level (L1/L2/L3), status review independen, tombol *Setujui* / *Minta revisi* |
| **Agent Status Pill** | Status agent: `Siap` / `Bekerja` / `Menunggu manusia` / `Error` / `Belum aktif` (agent pilar yang belum disetujui owner), dengan waktu terakhir aktif |

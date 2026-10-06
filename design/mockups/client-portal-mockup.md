# Mockup Spec — Portal Klien / Client Portal

> **ID:** Spesifikasi visual hi-fi untuk 7 halaman di [client-portal-wireframe](../wireframes/client-portal-wireframe.md). Ini dokumen acuan untuk desainer Figma dan developer. Semua nilai memakai token dari [design-system](../design-system/colors.md). Mockup Figma **belum dibuat**.
> **EN:** Hi-fi visual spec for the 7 Client Portal pages. Source of truth for the Figma designer and developers; all values reference design tokens.

**Mood:** hangat, tenang, terpercaya. Seperti resepsionis hotel yang ramah dan rapi: tidak ramai, tidak dingin. Foto properti klien adalah elemen visual terkuat. UI tidak bersaing dengannya.

## 0. Spek Global / Global Spec

| Aspek | Mobile (360–767) | Tablet (768–1023) | Desktop (≥ 1024) |
|---|---|---|---|
| Background halaman | `#FAFAF9` | `#FAFAF9` | `#FAFAF9` |
| Surface (kartu) | `#FFFFFF`, border `#E7E5E4`, radius 12, `shadow-sm` | sama | sama |
| Gutter / margin | 16 px | 24 px | 32 px |
| Navigasi | Bottom nav 64 px, bg putih, border atas `#E7E5E4` | Rail 80 px | Sidebar 256 px, bg `#FFFFFF`, border kanan `#E7E5E4` |
| Top bar | 56 px, sticky, bg putih 95% + `backdrop-filter: blur(8px)` | 56 px | 64 px |
| Judul halaman | `h2` 28 px / 700 Plus Jakarta Sans, `#1C1917` | 32 px | 36 px |
| Body | 16 / 400 Inter, `#44403C`, line height 1.5 | sama | sama |
| Meta | 14 / 400, `#78716C` | sama | sama |
| Jarak antar-section | 24 px | 32 px | 32 px |

### Interaksi global

| Interaksi | Spek |
|---|---|
| Hover kartu interaktif (desktop) | `shadow-sm → shadow-md`, border `#D6D3D1`, 150 ms |
| Tap (mobile) | `scale(0.98)` 80 ms + ripple tidak dipakai (terlalu Material) |
| Pindah halaman | Fade + geser 8 px ke atas, 200 ms `cubic-bezier(0.2,0,0,1)` |
| Bottom sheet | Naik dari bawah 250 ms; drag handle 36 × 4 px `#D6D3D1`; swipe down menutup |
| Toast | Masuk dari atas (mobile) / kanan bawah (desktop), 200 ms; keluar fade 150 ms |
| Reduced motion | Semua transisi → 0 ms, skeleton tanpa shimmer |

### State global

| State | Spek |
|---|---|
| **Loading** | Skeleton bentuk sama dengan konten akhir, `#E7E5E4`, shimmer 1.5 s. Muncul hanya bila > 300 ms |
| **Empty** | Ikon Lucide 48 px `#A8A29E` (dekoratif) → judul 18/600 `#1C1917` → 1 kalimat 14 `#78716C` → tombol opsional. Rata tengah, padding atas 48 px |
| **Error section** | Kartu bg `#FEF2F2`, border `#FECACA`, ikon `triangle-alert` `#B91C1C`, teks `#991B1B`, tombol secondary "Coba lagi" |
| **Offline** | Banner sticky di bawah top bar, bg `#FFFBEB`, teks `#92400E`, ikon `wifi-off` |

---

## 1. Login / Masuk

| Aspek | Spek |
|---|---|
| Layout mobile | Satu kolom, form max 440 px, padding atas 48 px. Logo 32 px di atas judul |
| Layout desktop | Split 50/50: kiri foto/ilustrasi full-height (radius 16, margin 16 px), kanan form di tengah vertikal |
| Judul | "Selamat datang kembali" `display` 32/700 (mobile), 48/700 (desktop) |
| Input | 44 px, border `#78716C` 1 px, radius 8, padding 12 × 16. Fokus: border `#0F766E` 2 px + ring `rgba(15,118,110,.2)` 4 px |
| Tombol *Masuk* | Primary lg 52 px, full width, `#0F766E`, teks putih 16/600. Hover `#115E59`. Loading: spinner + "Masuk…" |
| Tombol *Kirim link masuk* | Secondary lg, ikon `mail` 20 px |
| Link *Lupa kata sandi?* | 14/500 `#0F766E`, underline saat hover/fokus, area sentuh 44 px |
| Toggle bahasa | Segmented `ID | EN` di kanan atas, 32 px tinggi, aktif bg `#CCFBF1` teks `#115E59` |
| Error | Banner inline di atas tombol: bg `#FEF2F2`, ikon `circle-x`, teks `#991B1B`. Field tidak diberi merah (tidak memberi tahu field mana yang salah) |
| Ilustrasi | Lanskap Nusantara abstrak (sawah bertingkat + garis laut) dengan teal & terracotta, **flat, tanpa gradien**. Dirotasi per musim/destinasi (opsional) |

## 2. Beranda / Dashboard

| Komponen | Spek |
|---|---|
| Greeting | `h2` + 1 baris meta. Waktu sapaan dihitung dari zona waktu profil |
| **Kartu prioritas** "n konten menunggu" | Bg `#FFFBEB`, border `#FDE68A`, radius 12, padding 16. Ikon `triangle-alert` `#B45309` 20 px. Tombol primary full width di dalam kartu |
| Kartu "Fakta perlu konfirmasi" | Surface putih, ikon `message-circle-question` `#B45309`, chevron kanan, seluruh kartu bisa di-tap |
| Kartu statistik | Grid 2 kolom (mobile) / 4 kolom (desktop). Angka `h4` 24/700 `tabular-nums` `#1C1917`; label 14 `#78716C`; tren ▲ `#15803D` / ▼ `#B91C1C` dengan teks ("▲18% vs Sep"), bukan warna saja |
| Sumber data | 12/500 `#78716C` di bawah grid: "Sumber angka: Instagram Insights, diperbarui …" |
| Tayang berikutnya | Kartu media: thumbnail 64 × 80 (4:5) radius 8, judul 16/500, meta 14, badge status |
| Empty (klien baru) | Ikon `sparkles` → "Konten pertama sedang disiapkan" → "Kami kabari lewat WhatsApp saat siap ditinjau." |
| Loading | Skeleton: 1 kartu besar 120 px + 4 kotak statistik 88 px |

## 3. Konten / Content

### List

| Komponen | Spek |
|---|---|
| Tabs | 14/600, aktif garis bawah 2 px `#0F766E`; tab "Perlu Anda" punya counter pill `#C2410C` teks putih |
| Kartu konten | Thumbnail kiri 80 × 100 (feed 4:5) atau 56 × 100 (story 9:16), radius 8. Judul 16/500 maks 2 baris (`line-clamp`). Meta 14. Baris badge: status, level (outline), "? n fakta" (warning) |
| Pagination | Tombol "Muat lebih banyak" secondary, full width (mobile) |
| Empty per tab | "Perlu Anda": `circle-check` → "Tidak ada yang menunggu Anda" · "Tayang": `send` → "Belum ada konten yang tayang bulan ini" |

### Detail & Approval

| Komponen | Spek |
|---|---|
| **Preview IG** | Frame mockup HP sederhana: header akun (avatar 32 + nama), media 4:5 atau 9:16, dot indikator slide. Swipe horizontal (scroll-snap). Desktop: tombol ‹ › + thumbnail strip |
| Caption | Kartu, font body 16, `white-space: pre-wrap`, collapse setelah 6 baris + "Lihat semua". Tombol *Salin* (ghost, ikon `copy`) → toast "Caption disalin" |
| Blok bahasa | Caption EN di dalam caption ditandai `lang="en"`; tidak diterjemahkan otomatis |
| **Fakta yang dipakai** | List baris: teks fakta 14/500 + Evidence Badge. Baris `CLIENT CONFIRMATION` diberi bg `#FFFBEB` dan tombol `[✓ Benar]` (secondary sm) `[✎ Perbaiki]` (ghost sm) |
| Perbaiki fakta | Bottom sheet: nilai sekarang (read-only) → field "Yang benar" → catatan opsional → *Kirim koreksi* |
| Status review | Baris 14/500 dengan ikon `badge-check` `#15803D`: "Diperiksa tim CLAU (manusia) · 5 Okt 14.20". Bila belum: ikon `clock` `#78716C` "Menunggu pemeriksaan tim" |
| **Approval bar** | Sticky bawah, bg putih, border atas, padding 12 × 16 + safe area. 2 tombol 50/50: *Minta revisi* (secondary) · *Setujui* (primary). Desktop: di kolom kanan, rata kanan |
| Setujui nonaktif | Opacity 0.5 + helper 12 px di bawah tombol: "Setujui aktif setelah semua fakta dikonfirmasi." |
| Konfirmasi setujui | Bottom sheet ringkas: "Setujui konten ini untuk tayang Min, 11 Okt 18.00 WITA?" + daftar channel → *Ya, setujui* |
| Sukses | Animasi `circle-check` 48 px digambar (stroke draw) 400 ms → teks "Konten disetujui" → otomatis kembali ke list setelah 1.5 s, toast "Disetujui. Tim akan menjadwalkan tayang." |
| Minta revisi | Bottom sheet: textarea "Apa yang perlu diubah?" (wajib, min 10 karakter) + chip cepat: "Ganti foto", "Ubah jadwal", "Perbaiki caption" |
| Error simpan | Toast error tetap, "Belum tersimpan. Periksa koneksi lalu coba lagi." + tombol *Coba lagi*; input user **tidak hilang** |

## 4. Kalender / Calendar

| Komponen | Spek |
|---|---|
| Mini kalender (mobile) | Sel 44 × 40 px, hari ini lingkaran outline `#0F766E`, tanggal terpilih fill `#0F766E` teks putih, dot konten 6 px `#14B8A6` di bawah angka |
| Hari libur | Angka `#B91C1C`, tooltip/keterangan di agenda ("Hari Raya …"); data dari `knowledge/calendar-id` |
| Agenda | Group per tanggal (header 14/600 `#44403C`), item = kartu konten ringkas dengan jam `tabular-nums` |
| Grid bulan (desktop) | Sel min 120 px tinggi, border `#E7E5E4`; chip konten 12/500 bg `#F0FDFA` teks `#115E59`, maks 3 chip + "+2 lainnya" |
| Empty | `calendar-days` → "Belum ada jadwal bulan ini" |
| Loading | Skeleton grid + 3 baris agenda |

## 5. Laporan / Reports

| Komponen | Spek |
|---|---|
| Pemilih periode | Select native (mobile), dropdown (desktop) |
| **Ringkasan** | Kartu bg `#F0FDFA`, border kiri 4 px `#0F766E`, teks 16/400 `#1C1917`, maks 3 kalimat, ditulis manusia (bisa dibantu AI) |
| Grafik | Bar chart sederhana, warna seri `#14B8A6`; sumbu 12 px `#78716C`; label nilai di atas bar; **tabel data tersedia** di bawah grafik (aksesibilitas). Tanpa 3D, tanpa gradien |
| Konten terbaik | List 3 teratas dengan thumbnail + angka metrik utama |
| Sumber | 12/500 `#78716C`: platform + waktu pengambilan data |
| Tombol *Unduh PDF* | Primary (satu-satunya primary di halaman), ikon `download`. Loading: "Menyiapkan PDF…" (bisa 2–5 detik, tampilkan progres) |
| PDF | A4 portrait, logo agency + nama properti, font sama, warna sama; aman dicetak hitam-putih (tidak bergantung warna) |
| Empty | `chart-column` → "Laporan pertama tersedia setelah 1 bulan konten tayang." |

## 6. Profil / Profile

| Komponen | Spek |
|---|---|
| Header profil | Avatar 56 + nama 18/600 + peran & properti 14 |
| Group setting | Judul group 14/600 `#78716C` uppercase **tidak** dipakai; pakai sentence case. Baris 56 px, label kiri, nilai/kontrol kanan, chevron untuk sub-halaman |
| Bahasa | Segmented control `Indonesia | English`; perubahan langsung berlaku tanpa reload (fade 150 ms) + toast di bahasa baru ("Language changed to English") |
| Sapaan | Select: Bapak / Ibu / Kak / Nama saja |
| Tema | Select: Terang / Gelap / Ikuti sistem |
| Notifikasi | Toggle (langsung simpan); toast "Tersimpan" |
| Keluar | Ghost danger (teks `#B91C1C`), dengan konfirmasi |

## 7. Notifikasi / Notifications

| Komponen | Spek |
|---|---|
| Item | 72 px min; dot belum dibaca 8 px `#0F766E` di kiri; ikon jenis 20 px dalam lingkaran 36 px bg tint; judul 14/600; detail 14/400; waktu 12 `#78716C` kanan atas |
| Belum dibaca | Bg `#F0FDFA` |
| Swipe (mobile) | Swipe kiri → "Tandai dibaca" (opsional, ada juga di menu `⋮`) |
| Panel desktop | Dropdown 400 × maks 560 px, radius 12, `shadow-lg`, footer "Lihat semua" |
| Empty | `bell` → "Semua sudah dibaca" |
| Real-time | Item baru masuk dari atas dengan fade 200 ms; badge lonceng bertambah. `aria-live="polite"` |

---

## Responsive Checklist

- [ ] 320 px: tidak ada horizontal scroll, tombol tidak terpotong (teks ID terpanjang: "Kirim link masuk ke email").
- [ ] 360 px: bottom nav 5 item dengan label 12 px tetap terbaca.
- [ ] 768 px: rail + konten 8 kolom.
- [ ] 1280 px: sidebar + konten 12 kolom, preview & detail berdampingan.
- [ ] Landscape HP: approval bar tetap terlihat, preview mengecil.
- [ ] Zoom 200%: konten tetap bisa dipakai (WCAG 1.4.4).
- [ ] Dark mode: semua token tertukar, foto tidak difilter.

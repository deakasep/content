# Icons — Ikon

> **ID:** Icon set utama **Lucide** (lisensi ISC, gratis, ±1.500 ikon, gaya garis konsisten). Logo platform (Instagram, TikTok, dll.) **tidak** diambil dari Lucide, lihat §5.
> **EN:** Primary icon set is **Lucide** (ISC license, free, ~1,500 consistent outline icons). Platform logos are **not** taken from Lucide; see §5.

## 1. Kenapa Lucide / Why Lucide

| Kriteria | Lucide | Feather | Heroicons |
|---|---|---|---|
| Jumlah ikon | ±1.500, aktif bertambah | ±290, praktis tidak bertambah | ±300 |
| Gaya | Garis 2 px, sudut membulat | Sama (Lucide adalah fork Feather) | Garis & solid |
| Paket React/Vue/Svelte | ✅ tree-shakeable | Terbatas | ✅ |
| Lisensi | ISC | MIT | MIT |
| Keputusan | **Utama** | Tidak (sudah tercakup Lucide) | Alternatif bila butuh varian solid |

Nama ikon di dokumen ini mengikuti Lucide saat ditulis (Okt 2026). Lucide kadang mengganti nama ikon, jadi cek di lucide.dev saat implementasi.

## 2. Ukuran / Sizes

| Ukuran | Stroke | Pakai untuk |
|---|---|---|
| **16 px** | 2 | Di dalam badge, tabel padat, inline dengan teks `small` |
| **20 px** | 2 | **Default UI**: tombol, input, menu, sidebar |
| **24 px** | 2 | Bottom navigation, top bar, aksi utama di mobile |
| **32 px** | 1.75 | Kartu statistik, ilustrasi kecil |
| **48 px** | 1.5 | Empty state, error state |

Ikon 16–20 px **tetap** berada di dalam area sentuh 44 × 44 px. Ukuran ikon tidak sama dengan ukuran tombol.

## 3. Kategori & Nama Ikon / Categories

| Kategori | Ikon (Lucide) |
|---|---|
| **Navigasi** | `house` (Beranda), `layout-grid` (Konten), `calendar-days` (Kalender), `chart-column` (Laporan), `user-round` (Profil), `bell` (Notifikasi), `menu`, `chevron-left`, `chevron-right`, `arrow-left`, `x` |
| **Aksi** | `pencil` (edit), `trash-2` (hapus), `save`, `share-2`, `download`, `upload`, `copy`, `search`, `filter`, `sliders-horizontal`, `plus`, `ellipsis-vertical` (lainnya) |
| **Approval** | `circle-check` (setujui), `pencil-line` (minta revisi), `circle-x` (tolak), `history` (riwayat versi), `message-square` (komentar) |
| **Status** | `circle-check`, `circle-x`, `triangle-alert`, `info`, `loader-circle` (memuat, berputar), `clock` |
| **Konten** | `image`, `images` (carousel), `film` (reel/video), `smartphone` (story), `file-text`, `type` (caption), `hash` (hashtag) |
| **Bisnis** | `chart-line`, `trending-up`, `wallet` (pendapatan), `calendar-clock` (terjadwal), `building-2` (properti), `bed-double` (kamar), `utensils` (F&B), `flower-2` (spa) |
| **AI agent** | `bot` (agent), `sparkles` (dibuat AI, dipakai hemat), `cpu` (status sistem), `scan-search` (QA) |
| **Sistem** | `settings`, `key-round` (API), `plug` (integrasi), `users` (tim), `globe` (bahasa), `sun` / `moon` (tema), `log-out`, `lock`, `eye` / `eye-off` (password) |

## 4. Ikon Label Evidence

Selalu tampil **bersama teks label**, tidak pernah ikon saja.

| Label | Ikon | Warna |
|---|---|---|
| `DATA FINAL` | `badge-check` | Success |
| `CLIENT CONFIRMATION` | `message-circle-question` | Warning |
| `FIELD VERIFICATION` | `map-pin` | Info |
| `ASSUMPTION` | `circle-dashed` | Neutral |
| `RISK` | `shield-alert` | Error |
| `NEXT ACTION` | `circle-arrow-right` | Primary |

## 5. Logo Platform / Social Logos

Lucide sudah tidak menambah logo brand baru, dan beberapa logo brand lamanya berstatus deprecated. TikTok, Traveloka, dan logo OTA juga tidak tersedia. Karena itu:

| Kebutuhan | Sumber | Catatan |
|---|---|---|
| Instagram, TikTok, Facebook, WhatsApp, Google, YouTube | **Simple Icons** (CC0) | Pakai sesuai brand guideline masing-masing platform: warna asli atau monokrom, tanpa diubah bentuk |
| OTA (Traveloka, tiket.com, Booking.com, Agoda, Airbnb) | Logo resmi dari media kit masing-masing | Hanya sebagai **penanda channel**, bukan klaim kemitraan |
| Fallback bila logo tidak tersedia | Chip teks: `[Traveloka]` | Lebih aman daripada logo buatan sendiri |

## 6. Aturan Pakai / Usage

| Do ✅ | Don't ❌ |
|---|---|
| Ikon + label teks di navigasi dan tombol penting | Ikon tanpa label untuk aksi yang jarang dipakai |
| Tombol ikon-saja wajib punya `aria-label` (ID/EN) dan tooltip di desktop | Ikon dekoratif tanpa `aria-hidden="true"` |
| Warna ikon = warna teks di sebelahnya (`currentColor`) | Ikon warna-warni di dalam UI |
| Warna semantic hanya untuk ikon status | Ikon hijau di tombol yang bukan "berhasil" |
| Rata tengah vertikal dengan baris teks pertama | Ikon 24 px di sebelah teks 14 px |
| `sparkles` hanya untuk menandai konten **dibuat AI** | `sparkles` sebagai dekorasi di mana-mana |
| Spinner `loader-circle` hanya untuk aksi < 3 detik; lebih lama pakai skeleton/progress | Spinner di seluruh halaman |

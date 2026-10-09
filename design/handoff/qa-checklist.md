# QA Checklist — UI Release

> **ID:** Checklist sebelum halaman/fitur UI dianggap selesai dan dirilis. Isi per halaman atau per rilis. Item bertanda 🔴 = **blocker** (gagal = tidak rilis).
> **EN:** Pre-release checklist for UI pages/features. 🔴 items are blockers.

**Halaman/fitur:** ________ · **Versi/commit:** ________ · **Tester:** ________ · **Tanggal:** ________
**Device diuji:** ☐ Android 360 × 800 (Chrome) ☐ iPhone (Safari) ☐ Tablet 768 ☐ Desktop 1280 (Chrome/Edge/Firefox/Safari)

---

## 1. Visual QA

| # | Cek | ✓ |
|---|---|---|
| V1 | Sesuai mockup/Figma di 360, 768, 1280 px (jarak, ukuran, warna, radius) | ☐ |
| V2 | 🔴 Tidak ada hex/px mentah di kode; semua dari token (`build_tokens.py --check` lulus) | ☐ |
| V3 | Tipografi: heading Plus Jakarta Sans, body Inter; ukuran sesuai skala mobile/desktop | ☐ |
| V4 | Maks 1 tombol primary per layar | ☐ |
| V5 | Teks Bahasa Indonesia terpanjang tidak terpotong/overflow (tombol, tab, badge) | ☐ |
| V6 | Versi English tidak merusak layout | ☐ |
| V7 | Dark mode: semua warna tertukar dengan benar; foto tidak difilter; tidak ada teks gelap di atas surface gelap | ☐ |
| V8 | State **kosong**, **loading (skeleton)**, **error** tampil sesuai spec | ☐ |
| V9 | Skeleton berbentuk sama dengan konten akhir; tidak ada lompatan layout | ☐ |
| V10 | Ikon Lucide konsisten (ukuran 16/20/24, stroke 2), rata dengan teks | ☐ |
| V11 | Label evidence: warna + ikon + teks benar untuk keenam label; teks label tidak diterjemahkan | ☐ |
| V12 | 🔴 Tidak ada data client nyata di build demo/staging/screenshot | ☐ |

## 2. Functional QA

| # | Cek | ✓ |
|---|---|---|
| F1 | Semua flow terkait di [client-portal-flow](../user-flow/client-portal-flow.md) / [dashboard-flow](../user-flow/dashboard-flow.md) berhasil, termasuk jalur error | ☐ |
| F2 | 🔴 Tidak ada tombol/endpoint **publish** ke platform sosial | ☐ |
| F3 | 🔴 *Setujui* nonaktif (UI) **dan** ditolak API bila ada fakta `CLIENT CONFIRMATION` | ☐ |
| F4 | 🔴 Konten L2/L3 tidak bisa dikirim ke klien tanpa review independen; pembuat draft tidak bisa menjadi reviewer (UI **dan** API) | ☐ |
| F5 | 🔴 Approval tersimpan dengan nama, waktu, dan **versi konten**; versi berubah setelah approval → kembali ke "Di klien" | ☐ |
| F6 | "Tandai sudah tayang" mewajibkan URL valid sesuai channel + jam + zona | ☐ |
| F7 | Format lokal benar: `Rp1.250.000` / `IDR 1,250,000`, `6 Okt 2026`, `18.00 WITA`, minggu dimulai Senin | ☐ |
| F8 | Sapaan pagi/siang/sore/malam benar untuk zona WIB, WITA, WIT (uji jam batas: 10.59, 11.00, 14.59, 15.00, 17.59, 18.00, 03.59, 04.00) | ☐ |
| F9 | Ganti bahasa ID ↔ EN tanpa reload; pilihan tersimpan di profil | ☐ |
| F10 | Form: validasi saat blur; pesan error menjelaskan solusi; input tidak hilang saat gagal simpan | ☐ |
| F11 | Request penting idempotent (tap ganda *Setujui* tidak membuat 2 approval) | ☐ |
| F12 | Offline/sinyal lemah: banner offline muncul; aksi gagal bisa dicoba ulang | ☐ |
| F13 | Notifikasi: deep link membuka konten yang benar; link kedaluwarsa ditangani | ☐ |
| F14 | Izin peran (Owner/Content lead/Staff/Viewer, approver klien) sesuai tabel di wireframe Studio | ☐ |
| F15 | 🔴 Klien hanya melihat data properti miliknya (uji akses lintas klien via URL/ID lain) | ☐ |
| F16 | Audit log mencatat approve, tandai tayang, ubah fakta, ubah akses | ☐ |
| F17 | 🔴 Agent pilar belum aktif tidak bisa dijalankan dari UI maupun API; tampil "Belum aktif" | ☐ |
| F18 | Nama pilar & agent sama dengan `agents/registry.json` (ganti nama di registry → UI ikut tanpa ubah kode) | ☐ |

## 3. Accessibility QA (WCAG 2.2 AA)

| # | Cek | ✓ |
|---|---|---|
| A1 | 🔴 axe: 0 pelanggaran *serious/critical* | ☐ |
| A2 | 🔴 Contrast teks ≥ 4.5:1, teks besar/komponen/border input ≥ 3:1 (token sudah dicek; cek juga teks di atas foto) | ☐ |
| A3 | 🔴 Semua task utama bisa diselesaikan dengan **keyboard saja** (Tab, Shift+Tab, Enter, Space, Esc, panah) | ☐ |
| A4 | Focus ring terlihat di semua elemen interaktif; urutan fokus logis | ☐ |
| A5 | Modal/sheet: focus trap, Esc menutup, fokus kembali ke pemicu | ☐ |
| A6 | Target sentuh ≥ 44 × 44 px (WCAG 2.5.8 minimal 24 px; standar CLAU 44 px) | ☐ |
| A7 | Screen reader (TalkBack Android, VoiceOver iOS): label tombol ikon, status badge, dan toast diumumkan | ☐ |
| A8 | Informasi tidak hanya lewat warna (status = warna + ikon + teks) | ☐ |
| A9 | `lang` benar: halaman `id`/`en`, blok caption EN `lang="en"` | ☐ |
| A10 | Zoom 200% dan teks diperbesar sistem: tidak ada konten terpotong; tidak ada horizontal scroll di 320 px | ☐ |
| A11 | `prefers-reduced-motion`: animasi & shimmer mati | ☐ |
| A12 | Gambar punya alt text bermakna (preview konten memakai alt text dari brief); gambar dekoratif `alt=""` | ☐ |
| A13 | Form: setiap input punya label terlihat; error terhubung lewat `aria-describedby` | ☐ |
| A14 | Grafik laporan punya tabel data/ringkasan teks alternatif | ☐ |

## 4. Performance QA

| # | Cek | Target | ✓ |
|---|---|---|---|
| P1 | 🔴 LCP halaman utama (Beranda, Detail Konten) | < 2,0 s di 4G throttle, HP menengah | ☐ |
| P2 | CLS | < 0.1 | ☐ |
| P3 | INP | < 200 ms | ☐ |
| P4 | JS awal (gzip) per route | ≤ 170 KB | ☐ |
| P5 | Font | ≤ 120 KB total, `woff2` subset latin/latin-ext, `font-display: swap` | ☐ |
| P6 | Gambar | WebP/AVIF, `srcset`, lazy load di bawah fold, dimensi diset (tanpa CLS) | ☐ |
| P7 | Skeleton muncul hanya bila loading > 300 ms | — | ☐ |
| P8 | List/tabel > 100 item memakai virtualisasi/pagination | — | ☐ |
| P9 | Lighthouse (mobile) Performance & Accessibility | ≥ 90 | ☐ |

## 5. Hasil / Result

| Bagian | Lulus / Gagal | Catatan |
|---|---|---|
| Visual | | |
| Functional | | |
| Accessibility | | |
| Performance | | |
| **Keputusan rilis** | ☐ Rilis ☐ Rilis dengan catatan (non-blocker) ☐ Tidak rilis | |

Tester **bukan** orang yang membuat halaman tersebut, bila tim memungkinkan (prinsip review independen yang sama dengan konten).

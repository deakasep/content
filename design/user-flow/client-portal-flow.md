# User Flow — Portal Klien / Client Portal

> **ID:** 5 flow utama klien. Setiap flow memuat trigger, langkah, titik keputusan, penanganan error, dan kondisi sukses. Notasi: `[ ]` layar · `< >` keputusan · `( )` sistem · `==>` jalur sukses · `-->` jalur alternatif/error.
> **EN:** 5 core client flows with trigger, steps, decision points, error handling, and success state.

---

## Flow 1 — Approve Konten / Approve Content

**Trigger:** notifikasi WhatsApp/email "Konten menunggu persetujuan" **atau** kartu prioritas di Beranda.
**Aktor:** approver client (owner/GM). **Target:** dari tap notifikasi ke keputusan dalam ≤ 2 menit.

```text
 (Notifikasi WA/email: "Carousel kolam & taman menunggu persetujuan")
        │ tap link (deep link berisi id konten)
        ▼
 < Sudah login? > ──tidak──► [Login / link masuk] ──sukses──┐
        │ ya                                                 │
        ▼                                                    ▼
 [Detail Konten]  preview · caption · fakta · status review
        │
        ▼
 < Ada fakta CLIENT CONFIRMATION? >
        │ ya                                     │ tidak
        ▼                                        │
 [Kartu fakta]  --Perbaiki-->  [Sheet koreksi]   │
        │ Benar                    │ kirim       │
        │                          ▼             │
        │              (Tim diberi tahu; konten  │
        │               kembali ke "Perlu        │
        │               revisi"; flow selesai)   │
        ▼                                        ▼
 < Review independen ada? (wajib L2/L3) >
        │ tidak ──► [Setujui nonaktif] "Menunggu pemeriksaan tim" (flow berhenti, klien diberi tahu nanti)
        │ ya
        ▼
 < Klien puas dengan konten? >
        │ ya                                  │ tidak
        ▼                                     ▼
 [Konfirmasi Setujui]                  [Minta revisi]  catatan wajib + chip cepat
   "Setujui untuk tayang                      │ kirim
    Min, 11 Okt 18.00 WITA?"                  ▼
        │ Ya, setujui                  (Status → Perlu revisi; tim diberi tahu)
        ▼                                     ▼
 (Simpan approval: nama, waktu, versi)   [Toast] "Catatan terkirim ke tim"
        ▼
 ==> [Sukses] "Konten disetujui. Tim akan menjadwalkan tayang."
```

| Titik keputusan | Aturan |
|---|---|
| Fakta belum dikonfirmasi | *Setujui* nonaktif. Klien harus *Benar* atau *Perbaiki* setiap fakta `CLIENT CONFIRMATION` |
| Review independen | L2/L3 tidak bisa disetujui sebelum tim (manusia) memeriksa (rule 08). L1 boleh langsung |
| Versi berubah | Bila tim mengunggah versi baru saat klien membuka halaman: banner "Ada versi baru (v3). [Muat ulang]"; approval selalu terikat ke **versi yang dilihat** |

| Error | Penanganan |
|---|---|
| Link kedaluwarsa / konten dihapus | [Info] "Konten ini sudah tidak tersedia" + tombol ke daftar Konten |
| Klien bukan approver properti ini | [Info] "Akun Anda tidak punya akses ke konten ini" + kontak agency |
| Gagal simpan (jaringan) | Toast error tetap + *Coba lagi*; pilihan & catatan tidak hilang; tidak ada approval ganda (request idempotent) |
| Sudah disetujui orang lain | [Info] "Sudah disetujui oleh Pak Made, 10.42" (tidak error) |

**Sukses:** approval tercatat (siapa, kapan, versi). Status → *Disetujui*. Konten tidak langsung tayang. Tayang dilakukan manusia di agency, sesuai jadwal.

---

## Flow 2 — Lihat Kalender / View Calendar

**Trigger:** tab *Kalender* di bottom nav, atau tombol "Lihat kalender" di Beranda.

```text
 [Beranda] ──tap Kalender──► [Kalender: tampilan Agenda (mobile) / Bulan (desktop)]
                                   │
                    ┌──────────────┼──────────────────┐
                    ▼              ▼                  ▼
            ‹ › ganti bulan   tap tanggal        Filter channel
                    │              │                  │
                    ▼              ▼                  ▼
            (muat bulan;     [Agenda tanggal]   (list ter-filter)
             skeleton)             │
                                   ▼ tap item
                             [Detail Konten]  ==> (lanjut Flow 1 bila perlu approve)
```

| Keputusan | Aturan |
|---|---|
| Item butuh approval | Chip punya badge `?`/warning; tap → Detail Konten |
| Ingin ganti jadwal | Klien tidak bisa drag. Di detail: *Minta revisi* → chip "Ubah jadwal" + tanggal usulan |
| Tanggal = hari libur nasional | Info di agenda ("Libur: …"); tidak memblokir |

| Error | Penanganan |
|---|---|
| Bulan gagal dimuat | Kartu error di area kalender + *Coba lagi*; navigasi bulan tetap bisa dipakai |
| Bulan tanpa konten | Empty state "Belum ada jadwal bulan ini" |

**Sukses:** klien tahu apa yang tayang, kapan (tanggal + jam + zona waktu), dan mana yang butuh tindakan.

---

## Flow 3 — Unduh Laporan / Download Report

**Trigger:** notifikasi "Laporan September siap" atau tab *Laporan*.

```text
 [Laporan] ──► < Laporan untuk periode ini sudah ada? >
                   │ tidak ──► [Empty] "Laporan tersedia setelah 1 bulan konten tayang"
                   │ ya
                   ▼
            [Ringkasan + grafik + konten terbaik]
                   │ tap "Unduh PDF"
                   ▼
            < Bahasa PDF? >  default = bahasa UI; bisa pilih ID / EN di sheet kecil
                   │
                   ▼
            (Server membuat PDF; progres "Menyiapkan PDF…")
                   │
          ┌────────┴─────────┐
          ▼ < 10 dtk          ▼ > 10 dtk / gagal
 ==> (File terunduh:         --> [Toast] "PDF sedang disiapkan. Kami kirim link ke email
      Laporan-VillaContoh-        Anda saat selesai." (job di background)
      2026-09.pdf)
```

| Error | Penanganan |
|---|---|
| Gagal membuat PDF | Toast error + *Coba lagi*; laporan tetap bisa dibaca di layar |
| Penyimpanan HP penuh / unduhan diblok | Tawarkan *Kirim ke email* sebagai alternatif |

**Sukses:** file PDF bernama jelas (`Laporan-{properti}-{YYYY-MM}.pdf`), siap diteruskan ke pemilik lain/investor.

---

## Flow 4 — Ubah Profil / Update Profile

**Trigger:** tab *Profil*.

```text
 [Profil]
    │
    ├─ Toggle notifikasi ──► (langsung simpan) ==> [Toast] "Tersimpan"
    │                              --> gagal: toggle kembali ke posisi awal + toast error
    │
    ├─ Bahasa ID/EN ──► (ganti bahasa seluruh UI tanpa reload) ==> [Toast di bahasa baru]
    │
    ├─ Nama / Sapaan / Zona waktu / Tema ──► [Layar edit] ──Simpan──► < Valid? >
    │                                                  ya ==> [Toast] "Profil diperbarui"
    │                                                  tidak --> pesan error inline per field
    │
    └─ Email ──► [Edit email] ──► (kirim link verifikasi ke email baru)
                                    ──► < Diklik dalam 24 jam? >
                                          ya ==> email berubah; email lama diberi tahu
                                          tidak --> email lama tetap dipakai
```

| Error | Penanganan |
|---|---|
| Keluar dari layar edit dengan perubahan belum disimpan | Dialog "Buang perubahan?" *Buang* / *Lanjut edit* |
| Email sudah dipakai akun lain | "Email ini sudah terdaftar. Hubungi agency bila ini email Anda." |

**Sukses:** preferensi tersimpan dan langsung berlaku (bahasa, sapaan di greeting, zona waktu di jadwal).

---

## Flow 5 — Lupa Kata Sandi / Forgot Password

**Trigger:** link *Lupa kata sandi?* di halaman Login.

```text
 [Login] ──"Lupa kata sandi?"──► [Masukkan email] ──Kirim──►
        (Selalu tampilkan pesan yang sama, terdaftar atau tidak:
         "Bila email terdaftar, kami kirim link reset dalam beberapa menit.")
                                   │
                                   ▼
 (Email: "Atur ulang kata sandi" — link berlaku 30 menit, sekali pakai)
                                   │ klik link
                                   ▼
                     < Link valid & belum kedaluwarsa? >
                       │ tidak ──► [Link kedaluwarsa] + tombol "Kirim link baru"
                       │ ya
                       ▼
 [Kata sandi baru]  min 8 karakter · indikator kekuatan · tampilkan/sembunyikan
                       │ Simpan
                       ▼
                < Memenuhi syarat? > ──tidak──► pesan inline ("Minimal 8 karakter")
                       │ ya
                       ▼
 (Semua sesi lain dikeluarkan; email notifikasi "Kata sandi Anda diubah")
                       ▼
 ==> [Login] dengan banner sukses "Kata sandi diperbarui. Silakan masuk."
```

| Error | Penanganan |
|---|---|
| Email tidak sampai | Setelah 60 dtk tombol *Kirim ulang* aktif; tips "Cek folder Spam/Promosi" |
| Terlalu sering meminta reset | Rate limit 5x/jam: "Terlalu banyak permintaan. Coba lagi dalam 1 jam." |
| Alternatif | Link "Masuk dengan link email" (tanpa kata sandi) di layar yang sama |

**Sukses:** user bisa masuk kembali; sesi lama tidak bisa dipakai lagi (keamanan).

---

## Flow Tambahan (disarankan) — Konfirmasi Fakta / Confirm Facts

**Trigger:** notifikasi "n fakta perlu konfirmasi" atau kartu di Beranda.

```text
 [Konfirmasi Fakta]  dikelompokkan: Harga & promo · Fasilitas · Kebijakan · Foto & izin
        │ per kartu
        ▼
 < Nilai benar? > ──ya──► (label → DATA FINAL; tercatat: nama, waktu)  ==> kartu berikutnya
        │ tidak
        ▼
 [Perbaiki]  isi nilai yang benar ──► (label tetap CLIENT CONFIRMATION, tim meninjau koreksi)
        ▼
 ==> [Selesai] "Terima kasih, Bu Ratna. 6 dari 8 fakta terkonfirmasi. 2 sedang ditinjau tim."
```

Flow ini menggantikan pesan WA berisi 8 pertanyaan yang dipakai di pilot client nyata pertama.

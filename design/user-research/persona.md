# Persona

> **ID:** Tiga **proto-persona**, disusun dari brief owner dan pengalaman pilot. Ini **ASSUMPTION**, bukan hasil wawancara. Validasi dengan minimal 5 wawancara user nyata (lihat [prototype-guide](../prototype/prototype-guide.md)) sebelum dipakai untuk keputusan besar.
> **EN:** Three **proto-personas** based on the owner's brief and pilot experience. These are **assumptions**, not interview findings; validate with at least 5 real-user interviews.

---

## Persona 1 — Ibu Sari · Owner Villa, Ubud

```text
┌──────────────────────────────────────────────────────────────┐
│  IBU SARI, 45                                                │
│  Owner Villa 5 kamar · Ubud, Bali                            │
│  "Saya mau villa penuh terus, tapi saya nggak sempat         │
│   ngurus Instagram."                                         │
└──────────────────────────────────────────────────────────────┘
```

| Atribut | Detail |
|---|---|
| Bisnis | Villa 5 kamar, dikelola keluarga; staf 4 orang |
| Device | HP Android kelas menengah, layar 6,5"; jarang buka laptop |
| Kemampuan tech | Medium: lancar WhatsApp, Instagram, mobile banking; bingung dengan dashboard yang banyak menu |
| Bahasa | Bahasa Indonesia; bisa English dasar untuk tamu |
| Waktu pakai | Sela-sela kerja: pagi sebelum tamu sarapan, malam setelah check-in |
| Goal | Okupansi stabil sepanjang tahun, tidak terlalu bergantung pada OTA (komisi tinggi) |
| Pain point | Tidak punya waktu & ide konten; takut konten "lebay" atau salah info; lupa membalas permintaan approval yang masuk lewat chat |
| Kekhawatiran | Harga/promo salah tayang → komplain tamu; foto tamu dipakai tanpa izin |
| Yang dia butuhkan dari Portal | Lihat konten di HP, setujui dengan 1 tap, konfirmasi fakta (harga, fasilitas) tanpa harus mengetik panjang |

**Implikasi desain / Design implications**

- Beranda menampilkan **satu hal paling penting**: "3 konten menunggu Ibu".
- Tombol besar (52 px), teks 16 px, bahasa sehari-hari tanpa istilah seperti "pipeline" atau "asset".
- **Konfirmasi Fakta** berupa pertanyaan Ya/Perbaiki, bukan form panjang.
- Notifikasi lewat **WhatsApp/email** dengan link langsung ke konten. Ibu Sari tidak akan membuka aplikasi tanpa alasan.
- Login tanpa mengingat password: opsi **magic link email / OTP WhatsApp** (lihat catatan ambiguity di laporan).

---

## Persona 2 — Mas Budi · Owner Cafe, Jakarta Selatan

```text
┌──────────────────────────────────────────────────────────────┐
│  MAS BUDI, 32                                                │
│  Owner Cafe 3 cabang · Jakarta Selatan                       │
│  "Konten kita harus konsisten dan bisa viral, tapi jangan    │
│   sampai beda info antar cabang."                            │
└──────────────────────────────────────────────────────────────┘
```

| Atribut | Detail |
|---|---|
| Bisnis | Cafe 3 cabang (Kemang, Senopati, BSD); marketing dikerjakan sendiri + 1 staf |
| Device | iPhone untuk approve cepat; MacBook untuk lihat laporan |
| Kemampuan tech | High: aktif di IG & TikTok, paham insight, pernah pakai Canva & scheduler |
| Bahasa | Bahasa Indonesia, banyak campur istilah English ("engagement", "reach") |
| Goal | Konten konsisten 3–5x/minggu, ada yang viral, traffic ke tiap cabang naik |
| Pain point | Ide habis; posting tidak konsisten; menu/harga beda antar cabang sering tertukar |
| Kekhawatiran | Klaim yang berlebihan ("kopi terbaik se-Jakarta") memancing komentar negatif |
| Yang dia butuhkan dari Portal | Kalender multi-cabang, filter per cabang, laporan engagement yang jujur, approve batch |

**Implikasi desain**

- **Switcher properti/cabang** di header; filter "Semua cabang".
- **Approve batch** untuk konten L1 (rutin, tanpa klaim baru), sesuai rule 08.
- Laporan menampilkan angka dari platform apa adanya, dengan periode & sumber, tanpa pembulatan ke atas.
- Toggle bahasa tersedia, tapi default tetap ID.

---

## Persona 3 — Kak Dea · Owner Agency (AI Content Studio), Bandung

```text
┌──────────────────────────────────────────────────────────────┐
│  KAK DEA, 28                                                 │
│  Owner AI Content Studio · Bandung                           │
│  "Sekarang semuanya manual, capek. Saya mau pegang 10–20     │
│   klien tanpa kualitas turun."                               │
└──────────────────────────────────────────────────────────────┘
```

| Atribut | Detail |
|---|---|
| Bisnis | Agency AI content untuk hospitality; klien tersebar di Bali, Jawa, NTT, dan kota lain |
| Device | Laptop untuk produksi; HP untuk follow-up klien |
| Kemampuan tech | Very high: GitHub, AI tools, automation |
| Goal | 10–20 klien aktif, produksi konten sebagian besar dibantu AI, QA tetap ketat |
| Pain point | Konfirmasi fakta ke klien lewat WA bolak-balik; status konten tersebar di chat, Drive, dan repo; laporan bulanan dibuat manual |
| Kekhawatiran | Konten salah klaim lolos karena terburu-buru; data klien bercampur antar klien |
| Yang dia butuhkan dari Studio | Pipeline semua klien di satu layar, status AI agent, antrean QA, review independen, export laporan |

**Implikasi desain**

- **Pipeline Kanban** lintas klien dengan filter klien/channel/status, plus shortcut keyboard.
- Antrean **"Menunggu manusia"**: hal yang tidak boleh dikerjakan AI (approval, publish, review L2/L3).
- Setiap klien punya ruang data terpisah. UI selalu menampilkan **nama klien aktif** supaya tidak salah posting.
- Laporan bulanan otomatis dari data, diedit manusia sebelum dikirim.

---

## Ringkasan / Summary

| | Ibu Sari | Mas Budi | Kak Dea |
|---|---|---|---|
| Permukaan | Portal Klien | Portal Klien | Studio |
| Device utama | Android | iPhone + Mac | Laptop |
| Tech | Medium | High | Very high |
| Task utama | Approve + konfirmasi fakta | Kalender multi-cabang + laporan | Pipeline + QA + laporan |
| Metrik sukses UI | Approve dalam < 2 menit dari notifikasi | Lihat performa per cabang < 1 menit | Status 20 klien dalam 1 layar |

### Persona yang belum dibuat (next step)

- **Approver korporat** (GM hotel bintang 4 di Jakarta/Surabaya): approval berlapis, butuh audit trail.
- **Staf content** di agency (bukan owner): fokus produksi, izin terbatas.
- **Klien internasional** (owner asing di Bali/Lombok): UI English.

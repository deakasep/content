# Journey Map

> **ID:** Dua journey: **klien hospitality** (6 tahap) dan **owner agency** (8 tahap). Pain point di sini adalah **ASSUMPTION** dari persona dan pilot (termasuk pilot Villa Contoh Ubud), kecuali yang ditandai *terbukti di pilot*.
> **EN:** Two journeys: the **hospitality client** (6 stages) and the **agency owner** (8 stages). Pain points are assumptions unless marked *seen in pilot*.

## Legenda Emosi / Emotion Legend

`😊` positif · `😐` netral · `😟` frustrasi

---

## A. Journey Klien / Client Journey

```text
 1 Discovery ──► 2 Research ──► 3 Onboard ──► 4 Pakai ──► 5 Lapor ──► 6 Renew
    😐              😐             😟            😊           😊          😐
                                    ▲
                     titik rawan: banyak pertanyaan fakta
```

| Tahap | Yang dilakukan klien | Touchpoint | Pain point | Peluang di UI/UX | Emosi |
|---|---|---|---|---|---|
| **1. Discovery** / Menemukan | Dengar dari sesama owner, lihat konten di IG | Rekomendasi, IG agency | Ragu apakah AI = konten generik | Halaman publik (nanti) dengan contoh konten nyata yang sudah disetujui client | 😐 |
| **2. Research** / Menimbang | Cek website, IG, minta contoh & harga paket | Website, WA | Tidak jelas apa bedanya dengan freelancer | Tampilkan proses: *AI menyiapkan, manusia memeriksa, Anda menyetujui* | 😐 |
| **3. Onboard** / Mulai | Isi form, brief, fact sheet; kirim foto | Form onboarding, WA | **Pertanyaan fakta bolak-balik di WA** (*terbukti di pilot*); bingung istilah "net/++", "consent" | **Onboarding di Portal**: fact sheet dalam bentuk pertanyaan per langkah, simpan otomatis, bisa dilanjutkan nanti; istilah dijelaskan dengan ikon `info` | 😟 |
| **4. Pakai** / Menggunakan | Terima notifikasi, lihat draft, **konfirmasi fakta**, approve atau minta revisi | Notifikasi WA/email → Portal | Lupa membalas; tidak tahu konten mana yang mendesak | Notifikasi dengan link langsung; Beranda "Menunggu Anda" diurutkan berdasarkan tanggal tayang; approve 1 tap | 😊 |
| **5. Lapor** / Laporan | Baca laporan bulanan, unduh PDF | Portal, email | Laporan penuh angka tanpa arti | Ringkasan 3 kalimat di atas ("Saves naik 18% dibanding September"), lalu detail; PDF siap diteruskan | 😊 |
| **6. Renew** / Perpanjang | Putuskan lanjut atau tidak | Portal, invoice | Tidak ingat nilai yang didapat selama periode | Ringkasan periode: jumlah konten, inquiry/DM yang tercatat, waktu yang dihemat; tombol "Hubungi tim" | 😐 |

---

## B. Journey Owner Agency / Agency Owner Journey

```text
 1 Setup ─► 2 Onboard ─► 3 Produksi ─► 4 Review ─► 5 Publish ─► 6 Monitor ─► 7 Report ─► 8 Scale
   😐          😟            😊            😟           😐            😐           😟          😊
               ▲                           ▲                                      ▲
         data klien tersebar        QA manual berat                     laporan manual
```

| Tahap | Yang dilakukan | Pain point | Peluang di UI/UX | Emosi |
|---|---|---|---|---|
| **1. Setup** / Persiapan | Atur brand agency, paket, integrasi, anggota tim | Konfigurasi tersebar di banyak tool | **Settings** satu tempat: brand, paket, integrasi (status terhubung/tidak), peran tim | 😐 |
| **2. Onboard** / Klien masuk | Undang klien, buat brief & fact sheet | Fakta datang lewat WA, harus disalin manual (*terbukti di pilot*) | Klien mengisi sendiri di Portal; Studio melihat progres onboarding per klien (mis. "Fact sheet 6/8 terisi") | 😟 |
| **3. Produksi** / Produksi | AI agent membuat draft dari brief | Sulit tahu agent mana yang sedang jalan atau macet | Halaman **AI Agents**: status, antrean, error; setiap draft mencatat agent & versi skill yang dipakai | 😊 |
| **4. Review** / QA | Tabel klaim per kalimat, check_caption, review independen | Berat bila manual; self-review mudah meloloskan klaim tersirat (*terbukti di pilot 2*) | **Panel QA** per konten: tabel klaim otomatis, label evidence, kolom "Independen? Ya/Tidak", konten L2/L3 tidak bisa dikirim ke klien tanpa review manusia | 😟 |
| **5. Publish** / Tayang | Manusia publish di platform, catat URL | Lupa mencatat URL/jam → laporan tidak lengkap | Tombol **"Tandai sudah tayang"** dengan field URL + jam (wajib); bukan publish otomatis | 😐 |
| **6. Monitor** / Pantau | Pantau komentar/DM 24–72 jam | Tidak ada pengingat | Pengingat otomatis di jam ke-24 dan ke-72 setelah tayang | 😐 |
| **7. Report** / Laporan | Susun laporan bulanan per klien | Copy-paste angka dari Insights, makan waktu berjam-jam | Draft laporan otomatis dari data yang dicatat; manusia mengedit lalu mengirim; ekspor PDF | 😟 |
| **8. Scale** / Tumbuh | Tambah klien, tambah tim | Kualitas turun saat klien bertambah | Dashboard kapasitas: konten per orang, antrean review, SLA approval per klien | 😊 |

---

## C. Momen Paling Penting / Moments that Matter

| # | Momen | Kenapa penting | Target UX |
|---|---|---|---|
| 1 | Klien membuka notifikasi pertama | Kesan pertama terhadap Portal | Dari tap notifikasi ke preview konten: **≤ 2 tap, < 5 detik** |
| 2 | Konfirmasi fakta | Menentukan konten bisa tayang atau tertahan | Satu fakta = satu kartu Ya/Perbaiki; selesai < 2 menit untuk 8 fakta |
| 3 | Approval L2 | Tanggung jawab hukum & reputasi | Klien melihat **fakta yang dipakai** sebelum menekan *Setujui* |
| 4 | Laporan bulanan | Dasar keputusan perpanjang | Ringkasan dapat dipahami dalam 30 detik |
| 5 | Agency QA | Mencegah klaim salah lolos | Konten L2/L3 tidak bisa lanjut tanpa review independen |

## D. Asumsi yang Harus Diuji / Assumptions to Test

| Asumsi | Cara uji |
|---|---|
| Owner properti mau membuka Portal, tidak hanya membalas di WA | Prototype test: berapa yang menyelesaikan approve dari link notifikasi |
| Konfirmasi fakta per kartu lebih cepat daripada membalas daftar pertanyaan di WA | Bandingkan waktu tugas: Portal vs pesan WA (pilot client nyata pertama sebagai baseline) |
| Klien paham label evidence | Tanya setelah test: "Apa arti label kuning ini?" |
| Owner ingin approve batch untuk konten rutin | Wawancara 3–5 owner dengan ≥ 8 konten/bulan |

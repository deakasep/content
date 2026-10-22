# Paket Keputusan — TASK-067 (Pilar 1 AI Marketing hospitality siap jual)

> Untuk owner (Dea Karisna / Pak Indra). Disiapkan 2026-10-22 oleh AI agent (Claude Code) atas arahan owner: "pilar 2–5 skip untuk ke depannya, fokus pilar 1 hospitality, sempurnakan agar siap jual". Bagian "pre-review kritis" ditulis AI dan dicatat apa adanya sebagai buatan AI; kolom jawaban di § 4 hanya diisi dari jawaban owner. Cukup balas **"setuju semua"**, atau sebut nomor yang ingin diubah. Kartu ClickUp: *[MARKETING] TASK-067 Pilar 1 siap jual*. Rekomendasi angka harga **tidak** ditulis di sini (repo public); ada di kartu ClickUp.

## 1. Kesiapan sekarang (dicek 2026-10-22)

Rubrik kesiapan client nyata ([`clau-market/qa/scoring-rubric.md`](https://github.com/d34faiza-commits/clau-market/blob/main/qa/scoring-rubric.md) § Kesiapan Client Nyata) mengambil **nilai terendah**:

| Syarat | Status | Nilai bila belum |
|---|---|---|
| Review independen manusia atas pilot | **Belum**: semua QA pilot masih self-review AI (TASK-028) | **60** ← penentu |
| Spec platform terverifikasi | Sebagian (market PR 67): hashtag & durasi Reels IG, label AI & konten berbayar TikTok, jenis post GBP = DATA FINAL; panjang caption IG/TikTok, 1.500 karakter GBP, rasio feed = masih ASSUMPTION | 70 |
| Knowledge yang dipakai direview manusia | Belum | 70 |
| Semua klaim di konten publish DATA FINAL | Dijaga per konten (fact sheet + Konfirmasi Fakta) | 0 bila dilanggar |

Di luar rubrik, untuk **bisa menagih**: belum ada paket & harga yang disetujui, kontrak, DPA (UU PDP), badan usaha/pajak yang tercatat untuk tagihan, dan review legal L1–L6 (TASK-053).

## 2. Yang sudah dikerjakan AI (market PR 67, menunggu merge)

| Area | Isi |
|---|---|
| Commercial kit `clau-market/commercial/` | Katalog 3 paket (Esensial, Growth, Signature) + add-on + "tidak termasuk" + SLA; discovery checklist dengan red flag; template proposal; FAQ klien; SOP delivery bulanan (peran, siklus, kapasitas, mutu, insiden, offboarding); template perjanjian layanan; lampiran pemrosesan data UU PDP |
| Kalender 2027 | 18 libur + 8 cuti bersama SKB 2027; cluster Nyepi + Lebaran **6–15 Mar (10 hari)**, Iduladha–Waisak 15–23 Mei; perkiraan Ramadan 8 Feb; Galungan/Kuningan; tabel lead time. **Konsekuensi jual:** klien yang ingin kampanye Ramadan/Lebaran 2027 harus onboarding paling lambat **awal Desember 2026** |
| Perbaikan bug | Instagram hanya menerima **maks 5 hashtag** per post/Reels sejak 18 Des 2025; standar kita 3–8 (post dengan 6–8 hashtag bisa gagal tayang). Skill, prompt, dan `check_caption.py` sekarang 3–5, dengan test |
| Spec platform (TASK-011) | Diverifikasi sebagian lewat pencarian ke help center resmi (halaman tidak bisa dibuka langsung dari environment AI) |
| README | Vertical fokus diperbaiki (villa, resto/cafe, wedding, travel sesuai AI-CONSTITUTION v3.1.0), board ClickUp |

## 3. Pre-review kritis (ditulis AI)

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Menjual sebelum ada satu pun review manusia atas output | Mutu nyata belum terbukti; klaim "diperiksa manusia" belum teruji | K6a: owner menilai 1 pilot (±60–90 menit) sebelum klien pertama tanda tangan |
| Kapasitas: owner jadi satu-satunya reviewer | Klien ke-3–4 sudah melebihi waktu owner; SLA meleset | Batas kapasitas di SOP § 5 (≤ 85% jam reviewer); mulai 1 klien pilot; TASK-059 SOP tim sebelum klien ke-3 |
| Kontrak/DPA dipakai tanpa cek hukum | Klausul batal, risiko UU PDP (transfer data ke provider AI di luar negeri, Pasal 56) | K6c: konsultan hukum cek kontrak + DPA bersama L1–L6; sampai itu, jangan tanda tangan |
| Harga di repo public | Kompetitor melihat; sulit negosiasi | Harga hanya di price sheet privat + kartu ClickUp (K2) |
| Paket menjanjikan TikTok/Reels tapi CLAU tidak produksi video | Klien kecewa bila tak punya footage | Katalog jelas: naskah + shot list, rekaman oleh klien atau add-on mitra; ditanya di discovery |
| Platform CLAU AI belum dipakai (server mati, provider AI tiruan) | Delivery manual memakan jam lebih banyak | SOP level 1 sudah lengkap; ukur jam aktual 2 bulan pertama lalu koreksi harga/kapasitas |
| Kalender 2027 dari media, bukan dokumen SKB | Salah satu tanggal cuti bersama keliru | Tanggal dicocokkan ≥ 2 media; NEXT ACTION buka SKB di setneg.go.id sebelum lock kampanye Lebaran |
| Spec platform berubah lagi (seperti hashtag 30 → 5) | Konten gagal tayang atau reach turun | Cek ulang spec tiap kuartal (masuk TASK-014 quarterly review) |

**RISK** tersisa: tidak ada bukti hasil (TASK-062) untuk meyakinkan prospek. Mitigasi: harga pilot dengan izin case study tertulis (K5).

## 4. Keputusan owner

Rekomendasi AI: setujui semua. Balas "setuju semua", atau sebut nomornya.

| # | Keputusan | Rekomendasi AI | Jawaban owner |
|---|---|---|---|
| K1 | Isi 3 paket, add-on, dan daftar "tidak termasuk" sesuai `commercial/service-catalog.md` § 2–5 | Setuju | — |
| K2 | Harga **tidak** di repo; angka final di price sheet privat owner. Rekomendasi angka AI ada di kartu ClickUp TASK-067 | Setuju (angka boleh Kakak ubah di kartu) | — |
| K3 | Kontrak minimum 3 bulan lalu bulanan, bayar di muka, setup fee sekali | Setuju | — |
| K4 | Publikasi default oleh klien; penjadwalan oleh tim CLAU (manusia, akses partner) sebagai add-on; AI tidak pernah publish | Setuju | — |
| K5 | Klien pilot pertama: 1 klien, 1 vertical, 1–2 kanal (TASK-055), harga pilot dengan izin case study tertulis | Setuju | — |
| K6 | Syarat sebelum klien pertama **tanda tangan**: (a) owner menilai 1 pilot dengan rubrik (TASK-028); (b) owner membaca knowledge vertical klien pilot; (c) konsultan hukum cek kontrak + DPA + L1–L6 (TASK-053); (d) badan usaha & pajak penyedia ditetapkan. **Prospek, discovery, dan proposal boleh mulai sekarang** | Setuju | — |
| K7 | SLA (katalog § 7) dan batas kapasitas (SOP § 5) dipakai sebagai target awal, diukur ulang setelah 2 bulan | Setuju | — |
| K8 | Positioning: "Konten hospitality yang jujur, legal, dan siap tayang: ditulis dengan AI, diperiksa manusia, disetujui Anda" | Setuju | — |
| K9 | Pilar 2–5 ditunda; kartu TASK-035–039, 060 (bagian Admin), 066 tetap Open tanpa dikerjakan sampai owner membuka lagi | Setuju (sesuai arahan owner 2026-10-22) | Setuju (owner, 2026-10-22: "pilar 2-5 skip ini untuk kedepannya") |

## 5. Setelah disetujui

| Langkah | Siapa |
|---|---|
| Catat jawaban di § 4; ubah status `commercial/` dari Draft ke Approved v1.0.0 lewat PR | AI |
| Isi price sheet privat (Drive) dari rekomendasi di kartu | Owner |
| Nilai pilot 2 v3 dengan rubrik (TASK-028), ±60–90 menit; AI menyiapkan lembar kerjanya bila diminta | Owner |
| Kirim kontrak + DPA + daftar L1–L6 ke konsultan hukum (TASK-053) | Owner |
| Daftar 10 prospek pertama (villa/resto/wedding/travel), discovery call, audit 3 post, proposal | Owner + AI |
| Buka dokumen SKB 2027 dan cocokkan kalender | Owner, atau AI bila setneg.go.id dibuka di network policy |

Kartu TASK-067 **Closed** setelah PR market + paket ini merged dengan CI hijau dan jawaban owner tercatat.

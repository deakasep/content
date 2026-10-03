# 02 — Hospitality Claim Standard

## Purpose

Mengatur klaim spesifik industri hospitality Indonesia yang paling sering bermasalah: rating bintang, sertifikasi, halal, harga & promo, lokasi & jarak, view, fasilitas, F&B, dan treatment spa/wellness.

## Scope

Berlaku untuk konten accommodation, restaurant/cafe/beach club, spa/wellness/retreat, dan tourism experience di semua channel, termasuk OTA listing dan Google Business Profile.

Klasifikasi wajib: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**.

## Mandatory Rules

### Rating, klasifikasi & sertifikasi

- "Bintang 3/4/5" hanya bila properti punya sertifikat klasifikasi/usaha yang masih berlaku. Rating tamu di OTA ≠ klasifikasi bintang — tulis sebagai "rating 9,1 di <platform> per <bulan/tahun>" bila dipakai.
- Rating platform wajib menyebut platform dan tanggal pengambilan; rating berubah, jadi konten evergreen sebaiknya tidak memuat angka rating.
- Sertifikasi (CHSE, eco-label, green building, sertifikat keamanan pangan, dsb.) hanya bila sertifikat ada, atas nama entitas yang benar, dan masih berlaku. Program pemerintah bisa berubah — cek status program saat ini (**ASSUMPTION** sampai diverifikasi).
- Award hanya dengan nama penyelenggara, kategori, dan tahun yang benar.

### Halal & dietary

- "Halal" / logo halal hanya bila ada sertifikat halal yang berlaku untuk outlet/produk tersebut.
- Tanpa sertifikat, jangan pakai "halal", "100% halal", "halal-friendly", atau "muslim-friendly" sebagai klaim status. Boleh menyebut fakta spesifik yang terverifikasi, mis. "menu tanpa babi" — hanya bila **DATA FINAL** dari client dan tetap disarankan legal review.
- Klaim vegan/vegetarian/gluten-free/allergen wajib dikonfirmasi per menu; sebutkan risiko cross-contamination bila client tidak bisa menjamin.

### Harga & promo

- Setiap harga wajib: mata uang, unit (per kamar per malam / per orang / per pax / per treatment), periode berlaku, dan syarat utama.
- Status pajak & service wajib jelas: "net" vs "++" (belum termasuk pajak daerah dan service charge). Besaran persentase mengikuti client & peraturan daerah setempat → **CLIENT CONFIRMATION**.
- "Diskon X%" wajib punya harga acuan yang benar-benar pernah berlaku.
- "Terbatas" / "last 3 rooms" hanya bila benar; dilarang fake scarcity dan fake countdown.
- Harga di konten harus konsisten dengan harga di OTA/website pada periode yang sama.

### Lokasi, jarak & view

- Jarak ditulis dengan moda dan estimasi realistis: "±10 menit berkendara ke Pantai X (kondisi lalu lintas normal)". Jarak jalan kaki wajib **FIELD VERIFICATION** atau diukur dari peta dengan catatan metode.
- "Beachfront" hanya bila properti langsung berbatasan dengan pantai. "Ocean view" sebutkan tipe kamar yang mendapat view.
- "Private pool" vs "shared pool", "private beach" (di Indonesia pantai umumnya akses publik — jangan klaim private beach tanpa dasar hukum yang jelas → **RISK**).

### Fasilitas & layanan

- Fasilitas yang berbayar tambahan wajib disebut berbayar (airport transfer, breakfast, spa).
- Jam operasional & musiman wajib ditulis (beach club, kids club, rooftop).
- Kapasitas (jumlah kamar, kursi, max guest) wajib **DATA FINAL**.

### Spa & wellness

- Dilarang klaim medis: "menyembuhkan", "mengobati", "detoks racun", "menurunkan berat badan", "anti-kanker", "menyembuhkan insomnia".
- Pakai bahasa pengalaman: "membantu merasa rileks", "sensasi hangat", "terinspirasi tradisi pijat Bali".
- Klaim "tradisional", "warisan leluhur", "jamu asli" wajib dasar yang jelas dari client.
- Kualifikasi terapis (sertifikat/lisensi) hanya bila **DATA FINAL**.
- Kontraindikasi (kehamilan, kondisi medis) disarankan disebut pada konten treatment tertentu.

### Experience & aktivitas

- Satwa/alam (lumba-lumba, manta, penyu, sunrise di gunung) ditulis sebagai kemungkinan, bukan jaminan.
- Aktivitas berisiko (surf, dive, trekking) wajib menyebut level/syarat dan tidak meremehkan keselamatan.

## Required Inputs

- Fact sheet properti/outlet terbaru.
- Sertifikat (bintang, halal, CHSE/eco, keamanan pangan) — nomor/masa berlaku dicatat di workspace client, bukan di repo.
- Price list + periode + status pajak/service.
- Menu & allergen info; treatment list.
- Hasil field check untuk jarak/view (bila diklaim).

## Workflow

1. Identifikasi kategori klaim di draft (rating, sertifikasi, halal, harga, lokasi, fasilitas, spa, experience).
2. Terapkan mandatory rules per kategori.
3. Minta bukti untuk setiap klaim sensitif; tandai **CLIENT CONFIRMATION** bila belum ada.
4. Jadwalkan **FIELD VERIFICATION** untuk klaim fisik yang meragukan.
5. Rewrite klaim yang tidak lolos menjadi deskripsi faktual atau hapus.
6. Catat hasil di tabel klaim.

## Deliverables

- Draft yang lolos claim rule.
- Tabel klaim dengan kategori, label, dan bukti.
- Daftar pertanyaan **CLIENT CONFIRMATION** untuk owner.

## Validation/QC Checklist

- [ ] Rating bintang/sertifikasi/award punya bukti berlaku.
- [ ] Tidak ada klaim halal tanpa sertifikat.
- [ ] Harga lengkap: mata uang, unit, periode, syarat, net/++.
- [ ] Tidak ada fake scarcity atau diskon dari harga acuan palsu.
- [ ] Jarak menyebut moda & estimasi; "beachfront"/"private" sesuai fakta.
- [ ] Fasilitas berbayar & jam operasional jelas.
- [ ] Tidak ada klaim medis spa/wellness.
- [ ] Aktivitas alam/satwa tidak dijamin.

## Risks & Mitigation

| RISK | Mitigation |
|---|---|
| Klaim halal tanpa sertifikat → masalah hukum & kepercayaan | Hard block; wajib sertifikat |
| Klaim bintang dari rating OTA → misleading | Bedakan klasifikasi resmi vs rating tamu |
| Harga "++" tidak dijelaskan → komplain tamu saat checkout | Tulis status pajak/service di setiap harga |
| Klaim medis spa → pelanggaran iklan kesehatan | Daftar kata terlarang di QA |
| "Private beach" di pantai publik → konflik warga/hukum | Gunakan "akses langsung ke pantai" bila faktual |

## Escalation Conditions

- Client bersikeras memakai klaim bintang/halal/sertifikasi tanpa bukti.
- Harga di brief berbeda dengan harga di OTA/website.
- Client meminta klaim kesehatan untuk treatment.
- Klaim lokasi bertentangan dengan peta atau hasil field check.

## References

- [01 Content Integrity](./01-CONTENT-INTEGRITY-STANDARD.md)
- [05 Platform](./05-PLATFORM-STANDARD.md)
- [qa/claim-verification.md](../qa/claim-verification.md)
- [knowledge/segments/](../knowledge/segments/hotel.md)
- UU No. 33 Tahun 2014 tentang Jaminan Produk Halal beserta perubahannya (rujukan umum; penerapan wajib dicek legal)
- UU No. 1 Tahun 2022 tentang Hubungan Keuangan Pusat dan Daerah (rujukan pajak daerah atas hotel/restoran; tarif per daerah → **CLIENT CONFIRMATION**)

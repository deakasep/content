# Adversarial Review — Pilot 2 v2 (SIMULASI)

> **Status: self-review (adversarial), BUKAN review independen.** Ditulis oleh AI agent yang sama (Claude Code, sesi yang sama) yang membuat sistem, draft, dan skor 88. Menurut [rule 08](../../rules/08-APPROVAL-PUBLICATION-STANDARD.md), review ini **tidak** memenuhi syarat review independen; TASK-028 tetap terbuka. Pendekatannya: membaca ulang dengan sengaja mencari kesalahan, dan setiap temuan dicek langsung ke file (kutipan baris di bawah).
>
> Tanggal: 2026-10-04 · Objek: [v2.md](./v2.md), [drafts.md](./drafts.md) (C-B dipakai ulang di v2), [brief.json](./brief.json), [fact-sheet.md](./fact-sheet.md), [REPORT.md](./REPORT.md)

## 1. Kesimpulan

**Skor 88 terlalu tinggi.** Skor hasil review ulang: **80/100**, dan kesiapan untuk client nyata **60/100** (sebelumnya diklaim 75).

Alasan utamanya: QA v2 menyatakan semua konten "Pass", padahal ada **6 pelanggaran rule** yang lolos, termasuk **3 klaim tersirat**, jenis masalah yang justru diklaim sudah diperbaiki di TASK-018/024. Artinya gate yang dijalankan oleh pembuatnya sendiri belum bisa diandalkan, dan kenaikan skor v1 → v2 lebih banyak mencerminkan file baru (rule, tool, schema) daripada kualitas output.

## 2. Temuan

| # | Temuan | Bukti (file) | Rule yang dilanggar | Severity |
|---|---|---|---|---|
| R-01 | **C-B punya 2 CTA**: "Simpan untuk nanti, atau kirim ke partner trip kamu." Self-check v1 menandai ✅, dan v2 menyatakan C-B "lolos semua gate" | drafts.md:47; v2.md "C-B tidak berubah dari v1 (lolos semua gate)" | Rule 05: satu konten, satu CTA | High (gate salah lapor) |
| R-02 | **Story frame 1 "Pagi seperti ini di Ubud"** memakai VCSU-MEDIA-001, yang alt text-nya sendiri menyebut foto itu **siang hari** | v2.md:38 vs v2.md:98 | Rule 01: deskripsi sesuai fakta; klaim tersirat (waktu) | Medium |
| R-03 | **"sawah langsung di depan kasur"** (ID) dan **"open onto the rice fields"** (EN): fact sheet hanya menyebut *View: Sawah*, bukan jarak atau akses langsung. "Open onto" menyiratkan pintu langsung ke sawah | v2.md:23, v2.md:29; fact-sheet.md:30 | Klaim tersirat non-DATA FINAL = Fail (TASK-024) | Medium |
| R-04 | **"the 4 × 12 m pool is yours alone"**: villa dijual untuk "beberapa pasangan", jadi kolam dipakai bersama rombongan. Untuk satu pasangan dalam rombongan, kalimat ini menyesatkan | v2.md:29; brief.json `audience.segments` | Klaim tersirat (privasi) | Low–Medium |
| R-05 | **Hashtag #honeymoonbali** (C-A, reel) mengunci segmen honeymoon, padahal target masih **CLIENT CONFIRMATION** di sanity check | v2.md (2×); v2.md §Step 1 | Sanity check: drafting dengan angle sementara tidak boleh dikunci di konten publish | Low |
| R-06 | **CTA C-C = "comment"**, padahal brief menetapkan CTA carousel = `save` | v2.md:55; brief.json:27 | Brief v1.3 `channels[].cta` (baru dibuat, langsung tidak dipatuhi) | Low |
| R-07 | **Voice "elegan-tertata" + sapaan "kamu"**: voice guide memetakan "kamu" ke voice santai/cafe dan "Anda" ke hotel premium. Tidak ada aturan yang mengecek kecocokan arketipe ↔ sapaan | brief.json:23; voice guide baris 34–35 | Rule 03 (konsistensi Voice Card) | Low |
| R-08 | **Metric "story replies"**, padahal story memakai poll + link sticker (tidak mengundang reply) | brief.json:11 | Sanity check objective ↔ format | Low |

### Temuan sistemik (di balik R-01 sampai R-08)

| # | Masalah sistem | Dampak |
|---|---|---|
| S-01 | Deteksi klaim tersirat masih bergantung pada "baca ulang" oleh pembuat draft. Tidak ada langkah wajib yang **mengekstrak setiap kalimat** ke tabel klaim | R-02, R-03, R-04 lolos dua kali (v1 dan v2) |
| S-02 | `check_caption.py` hanya mekanis (panjang, hashtag, emoji, kata terlarang). PASS-nya mudah terbaca sebagai "caption lolos", padahal CTA, klaim, dan voice tidak dicek | R-01 dan R-06 tidak tertangkap; "PASS" memberi rasa aman palsu |
| S-03 | Field brief baru (CTA per channel, voice) tidak dicek ke draft oleh skill maupun QA | R-06, R-07 |
| S-04 | Skor tidak punya rubrik. Angka 74/82/88/92 tidak berasal dari kriteria terukur, jadi naik-turunnya tidak bisa diverifikasi pihak lain | Skor 88 tidak bisa diaudit |
| S-05 | QA v2 hanya menguji ulang item yang gagal di v1, bukan seluruh konten. C-B tidak diperiksa ulang | R-01 terbawa dari v1 ke v2 |

## 3. Skor Baru vs Skor 88

| Dimensi | Skor v2 (self, REPORT) | Skor review ulang | Alasan penurunan |
|---|---|---|---|
| Kualitas output | 82 | **70** | 2 CTA (R-01), waktu di story salah (R-02), 2 klaim tersirat (R-03, R-04), segmen terkunci (R-05). Belum ada penilaian manusia/audiens |
| Konsistensi dengan rules | 90 | **78** | Rule 1-CTA, aturan klaim tersirat (3×), CTA brief, dan sapaan voice dilanggar di output yang dinyatakan Pass |
| Kepatuhan Constitution | 90 | **80** | Prinsip "tidak mengklaim selesai tanpa bukti": QA dan REPORT menyatakan Pass/"lolos semua gate" untuk konten yang melanggar. Self-review dipakai sebagai dasar skor |
| Kepatuhan Boundary | 92 | **92** | Tidak ada temuan: data fiktif, tanpa data client/tamu/credential |
| Kelengkapan deliverable | 88 | **80** | C-B tidak dicek ulang; approval v2 hanya di dalam v2.md; PASS tool hanya mekanis |
| **Rata-rata** | **88** | **80** | |
| **Kesiapan untuk client nyata** | 75 | **60** | Gate yang dijalankan pembuatnya terbukti meloloskan pelanggaran; review manusia (TASK-028), spec platform (TASK-011), dan review knowledge (TASK-001–009) belum ada |

Catatan: skor review ulang juga tanpa rubrik terukur (S-04), dan ditulis oleh pihak yang sama. Anggap skor ini **lebih jujur**, bukan **lebih valid**. Validitas baru ada setelah review manusia.

## 4. Apa yang Tetap Benar dari REPORT

- Klaim berisiko tingkat atas memang tertahan: "mewah", sunset, jarak ke Ubud, dan klip tanpa consent tidak muncul di konten.
- Perbaikan di repo (rule 02 positioning, prompt reel/stories, schema v1.3, aturan self-review) nyata dan tervalidasi oleh CI.
- Klaim bathtub/view dari v1 memang sudah diperbaiki di v2.

## 5. Rekomendasi

| Prioritas | Rekomendasi | Mengatasi |
|---|---|---|
| 1 | **Review manusia (TASK-028)**: kamu atau content lead menjalankan claim verification atas v2. Bandingkan dengan temuan di dokumen ini, karena itu cara menguji apakah review adversarial ini sendiri melewatkan sesuatu | Validitas skor |
| 2 | **Claim extraction per kalimat**: di claim gate, setiap kalimat konten wajib masuk tabel (kalimat → klaim eksplisit/tersirat → label). Bukan "baca ulang" bebas | S-01, R-02–R-04 |
| 3 | **Re-check penuh di setiap versi**: setiap versi baru menjalankan semua gate untuk semua konten, bukan hanya item yang gagal sebelumnya | S-05, R-01 |
| 4 | **Cek field brief di QA**: CTA per channel, sapaan ↔ arketipe, dan segmen yang masih CLIENT CONFIRMATION (tidak boleh dikunci lewat hashtag atau kalimat) | S-03, R-05–R-07 |
| 5 | **Perjelas output `check_caption.py`**: ganti label menjadi "PASS (mekanis)", dan tambah heuristik jumlah CTA (kata kerja ajakan: simpan, kirim, komentar, klik, DM) | S-02, R-01 |
| 6 | **Rubrik skor**: setiap dimensi diturunkan dari hitungan item checklist (mis. % klaim yang lolos gate independen, jumlah pelanggaran rule per konten), bukan angka bebas | S-04 |
| 7 | **Perbaiki draft v2 → v3** setelah poin 2–5 ada, lalu minta review manusia atas v3 | R-01–R-08 |

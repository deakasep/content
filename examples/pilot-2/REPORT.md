# REPORT — Pilot 2: Test End-to-End "Otak" CLAU-AI-CONTENT

> **SIMULASI / FIKTIF.** Tanggal: 2026-10-04. Dijalankan oleh AI agent (Claude Code) di repo `main` setelah commit `2867170`.

## 1. Ringkasan

| | |
|---|---|
| Skenario | Klien baru fiktif **Villa Contoh Sunset Ubud**: villa 5 kamar, view sawah, target pasangan |
| Deliverable diminta | 1 IG post (3 varian caption), 1 reel script, 1 story, fact sheet, brief, QA, approval record |
| Deliverable dihasilkan | Semua: [fact-sheet.md](./fact-sheet.md), [brief.md](./brief.md) + [brief.json](./brief.json), [drafts.md](./drafts.md), [qa.md](./qa.md), [approval-record.md](./approval-record.md) |
| Skor keseluruhan | **82/100** untuk sistem saat dipakai; **65/100** untuk kesiapan dipakai ke client nyata |
| Verdict | Sistem berhasil mencegah klaim bermasalah ("mewah", sunset, foto tanpa consent). Yang belum siap: format video/story, aturan "luxury" di rules, dan beberapa pengecekan yang masih manual |

## 2. Yang Berjalan Baik (bukti)

| Kontrol | Bukti di pilot |
|---|---|
| Fact sheet + label memisahkan fakta dari klaim owner | "Mewah", sunset, dan jarak ke Ubud tertahan sebagai **ASSUMPTION**/**FIELD VERIFICATION** di [fact-sheet.md](./fact-sheet.md) §1, §3, dan tidak muncul di konten |
| Schema v1.2 | [brief.json](./brief.json) valid; field `voice` dan `source_date` wajib bekerja; validator CI mengecek otomatis |
| Rule 02 + knowledge regulasi | "Mewah/luxury" ditangkap sebagai **RISK** karena tidak ada sertifikat LSU |
| Rule 04 privacy | Klip VCSU-VIDEO-001 (pasangan tanpa consent) ditahan; reel diganti shot tanpa wajah |
| Rule 07 visual | Tidak ada AI visual; ada peringatan agar lensa ultra-wide tidak membuat kolam tampak lebih besar |
| Self-check klaim tersirat (TASK-018) | Menandai ⚠️ "bathtub with a rice-field view" |
| Claim gate | Memutuskan "Ubah" untuk C-C dan R1 |
| Mode SIMULASI (TASK-017) | Approval record bertanda SIMULASI; publication checklist **Fail sesuai desain** |
| Aturan nama fiktif | Nama dari brief "Sunset Ubud" diubah menjadi "Villa Contoh Sunset Ubud" |

## 3. Scoring

Skala 0–100. Skor diberikan oleh AI yang sama yang menulis sistem dan output, jadi **berisiko bias ke atas** (lihat §6).

| Dimensi | Skor | Alasan |
|---|---|---|
| **Kualitas output** | **74** | (+) Caption konkret, sensory, tanpa klise; reel script punya shot list, on-screen text, dan catatan risiko. (−) Hook caption reel 133 karakter melanggar aturan ±125; C-C memuat klaim tersirat yang belum terbukti; alt text hanya untuk slide 1; emoji di hook story. Kualitas tulisan belum dinilai manusia atau audiens |
| **Konsistensi dengan rules** | **82** | (+) Semua kata terlarang dihindari; label konsisten di fact sheet, brief, drafts, dan QA; harga tidak dipakai karena tidak ada promo. (−) Rules **tidak bicara** soal "mewah/luxury" dan nama brand yang menyiratkan klaim; aturan itu hanya ada di file riset `knowledge/regulasi` |
| **Kepatuhan Constitution** | **88** | (+) Tidak ada fakta karangan di konten; AI tidak publish/approve; eskalasi ditulis (positioning, target, consent). (−) QA dijalankan oleh pembuat yang sama, sehingga prinsip review independen belum terpenuhi |
| **Kepatuhan Boundary** | **92** | (+) Semua data fiktif; tidak ada data client, tamu, harga kontrak, atau credential; nama memakai "Contoh". (−) Folder `pilot-2/` tidak mengikuti pola penamaan `pilot-<nama>` di `examples/` (mengikuti instruksi task) |
| **Kelengkapan deliverable** | **75** | (+) Ke-6 deliverable ada dan saling terhubung. (−) Reel dan story disusun tanpa prompt/skill khusus (improvisasi); jam publish, URL link sticker, dan alt text per slide belum ada |
| **Rata-rata** | **82** | |
| **Kesiapan untuk client nyata** | **65** | Butuh perbaikan G-02, G-03, G-05, verifikasi spec platform (TASK-011, blocked), dan review owner atas knowledge (9 task di kolom Review) |

## 4. Temuan & Catatan Perbaikan

| ID | Temuan | Dampak | Prioritas | Rekomendasi |
|---|---|---|---|---|
| G-01 | Tidak ada pengecekan **kecocokan strategi** di brief (villa 5 kamar ↔ target pasangan). Hanya tertangkap karena agent kebetulan menyadarinya | Konten bisa menarik audiens yang tidak akan membeli | High | Tambah item "brief sanity check" di [WORKFLOW Step 1](../../WORKFLOW.md): kapasitas ↔ segmen, harga ↔ segmen, objective ↔ channel |
| G-02 | Tidak ada prompt/skill **reel/video script** | Format paling penting untuk discovery (menurut riset tren) dikerjakan improvisasi | High | Buat `prompts/video/reel-script.md` + skill `draft-reel-script` (hook 1–3 detik, shot list, on-screen text, audio, consent per shot) |
| G-03 | Tidak ada prompt/skill **Stories**; aturan emoji/hook/safe area untuk story belum ada | Inkonsistensi format story | Normal | Tambah prompt stories (frame, sticker, link) + aturan di rule 05 |
| G-04 | Batas hook ±125 karakter hanya ada di prompt, tidak di **self-check skill**; output melanggar | Hook terpotong di feed | Normal | Masukkan panjang hook ke self-check `draft-caption`; pertimbangkan script `scripts/check_caption.py` |
| G-05 | "Mewah/luxury/7-star" dan **nama brand yang menyiratkan klaim** ("Sunset", "Beachfront", "Ocean") tidak diatur di rule 02 atau voice guide | Agent bergantung pada file riset yang tidak wajib dibaca skill | High | Tambahkan ke rule 02 (claim hotspots) + daftar kata di voice guide; jadikan context wajib di skill drafting |
| G-06 | Self-check klaim tersirat **mendeteksi** tapi tidak **memaksa** perbaikan sebelum diserahkan | Draft bermasalah tetap sampai ke gate | Normal | Exit criteria skill: klaim tersirat non-DATA FINAL = **Fail**, bukan ⚠️ |
| G-07 | Alt text hanya 1 per post, belum per slide carousel | Aksesibilitas & social search kurang optimal | Low | Self-check: alt text per slide/aset |
| G-08 | Schema hanya punya tanggal publish, tanpa **jam**; link sticker tidak punya field | Publication checklist gagal di item jadwal & link | Low | Tambah `deadlines.publish_time` dan field CTA URL (opaque) |
| G-09 | Spec platform (batas caption, durasi reel, safe area story) masih **ASSUMPTION** | Tidak bisa jadi gate otomatis | High | TASK-011, butuh akses help center (blocked di sesi agent) |
| G-10 | QA dijalankan oleh pembuat yang sama | Bias; review independen tidak terpenuhi | High | Owner/reviewer manusia menjalankan claim gate pada pilot ini; atau sesi agent terpisah yang hanya me-review |
| G-11 | Inventaris di instruksi task berbeda dari repo: **schemas 1 file** (bukan 3); templates sekarang **7** (ada fact sheet) | Hanya catatan; tidak ada fungsi yang hilang | Info | Schema tambahan (mis. fact sheet JSON) bisa dibuat bila dibutuhkan validasi otomatis |

## 5. Rekomendasi Urutan Kerja

1. **G-05** (rule "luxury" & nama brand): murah, langsung mencegah klaim paling berisiko.
2. **G-02** (reel script): format prioritas untuk hospitality di 2026 (**ASSUMPTION** dari riset tren global).
3. **G-01** (brief sanity check) dan **G-06** (implied claim = Fail).
4. **G-10**: review manusia atas pilot ini, supaya skor punya pembanding independen.
5. G-03, G-04, G-07, G-08 sebagai perbaikan kecil.
6. G-09/TASK-011 begitu akses help center tersedia.

## 6. Keterbatasan Test

- **Self-grading:** pembuat sistem, pembuat output, dan penilai adalah agent yang sama. Skor sebaiknya dianggap batas atas sampai ada review manusia.
- **Aset fiktif:** visual QA, panjang video, dan alt text tidak diuji pada file nyata.
- **Tanpa data audiens:** kualitas "menarik/tidak" belum diuji ke audiens atau insight platform.
- **Spec platform belum terverifikasi** (TASK-011).
- Pengecekan otomatis yang dijalankan: validasi schema, panjang caption/hook, jumlah hashtag/emoji, dan kata terlarang (script Python ad-hoc, belum ada di `scripts/`).

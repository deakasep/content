# Paket Review — TASK-041 (vertical fokus siap enterprise)

> Untuk manusia. Bagian AI sudah selesai (fact sheet, schema v1.4, pilot SIMULASI, eval, riset sumber sekunder). Paket ini berisi **semua langkah manusia** yang tersisa, siap dikerjakan tanpa membaca ulang seluruh repo. Isi kolom kosong, lalu minta agent memindahkan hasilnya ke repo. Disiapkan 2026-10-09 oleh AI agent (Claude Code). AI tidak mengisi hasil review atau keputusan di dokumen ini.

## Ringkasan

| # | Pekerjaan | Siapa | Estimasi | Hasil yang dicatat |
|---|---|---|---|---|
| 1 | Review independen 3 pilot | Content lead / owner — **bukan** pembuat draft (rule 08) | ± 30 menit per pilot | Tabel § 1 per pilot |
| 2 | Legal review | Konsultan hukum / notaris | 1 sesi | Tabel § 2 |
| 3 | Verifikasi sumber primer | Owner, atau agent setelah domain dibuka | ± 1 jam | Tabel § 3 |
| 4 | Keputusan owner | Pak Indra / Dea Karisna | 5 menit | Kalimat keputusan § 4 |

## 1. Review Independen Pilot (rule 08, qa/scoring-rubric)

Pilot ada di `clau-ai-marketing/examples/`. Untuk tiap pilot: buka `brief.json`, `fact-sheet.md`, `drafts.md`, `qa.md`, lalu hitung ulang **sendiri**. Jangan hanya menyetujui tabel QA agent.

| Langkah | Cara |
|---|---|
| A. Integritas klaim | Pecah caption per kalimat; tiap kalimat yang berisi klaim harus cocok dengan baris **DATA FINAL** di fact sheet. Skor = % kalimat OK tanpa perubahan |
| B. Kepatuhan rule | Cari pelanggaran rule 01–09 (klaim, consent, harga, AI visual). Penalti High 15 / Medium 8 / Low 3 |
| C. Kecocokan brief | Voice, sapaan, emoji, CTA, kata wajib/terlarang sesuai `brief.json` |
| D. Kelengkapan | Item publication checklist yang berlaku (approval nyata = N/A di SIMULASI) |

| Pilot | Reviewer (peran) | Tanggal | A | B | C | D | Total | Temuan (selisih dengan self-review agent) | Lulus? |
|---|---|---|---|---|---|---|---|---|---|
| Kafe Contoh Canggu (`pilot-kafe-contoh-canggu`) | Dea Karisna (owner) | 2026-10-09 | 60 | 89 | 100 | — | 83 | Klaim lokasi tersirat ("ombak pagi", "sebelum surf") dan "arabika" tanpa sumber lolos self-check (K-03, K-04) | v1 ☒ → **v2 ✅ lulus** (2026-10-09) |
| Villa Contoh Uluwatu wedding (`pilot-wedding-contoh-uluwatu`) | Dea Karisna (owner) | 2026-10-09 | 67 | 86 | 100 | — | 84 | Klaim view laut & "meja panjang" tanpa fakta; "kapasitas yang sama" hanya benar untuk seated (W-04, W-05) | v1 ☒ → **v2 ✅ lulus** (2026-10-09) |
| Trip Contoh Labuan Bajo (`pilot-trip-contoh-labuan-bajo`) | Dea Karisna (owner) | 2026-10-09 | 63 | 86 | 100 | — | 83 | Syarat berenang tidak ditulis; kesan pasti berangkat; spot ditulis pasti; TikTok "tanpa harga tersembunyi" (T-04, T-05) | v1 ☒ → **v2 ✅ lulus** (2026-10-09; tetap tertahan gate izin sebelum tayang) |

Metode (dicatat apa adanya): AI agent menyusun pre-review kritis atas draft-nya sendiri; reviewer membaca dan menyatakan "setuju" di sesi Claude Code 2026-10-09. D tidak dihitung (publication checklist belum dijalankan di SIMULASI); Total = rata-rata A–C. Kesiapan ketiganya **0**. Detail per kalimat ada di `qa.md` § Review Independen masing-masing pilot, lewat [clau-ai-marketing#22](https://github.com/d34faiza-commits/clau-ai-marketing/pull/22).

**Temuan lintas pilot:** ketiga self-check agent "lulus", padahal review menemukan klaim tersirat atau syarat yang hilang. Self-check `skills/draft-caption` #7 sudah diperluas. Cek ulang v2 (2026-10-09): reviewer menyatakan **"lulus semua"** (v2 = 100/100/100; dapat di-upgrade kapan saja). Saat cek ulang, AI menemukan 2 sisa temuan di kanal yang tidak dinilai (GBP kafe "arabika", terjemahan nama area wedding EN) — diperbaiki di clau-ai-marketing#23.

Pertanyaan yang sengaja diuji pilot (cek reviewer setuju):

| Pilot | Pertanyaan |
|---|---|
| Kafe | Apakah "menu tanpa daging" cukup jelas dan tidak terbaca sebagai "halal"? Apakah "++" tanpa persentase PB1 boleh tayang? → Tidak terbaca halal (perjelas telur/seafood di menu); "++" boleh, lebih baik "(belum termasuk pajak & service)" |
| Wedding | Apakah kalimat "Foto: acara nyata… dengan izin pasangan" perlu di caption, atau cukup di consent register? Apakah daftar "tidak termasuk" harus di caption IG? → Pertahankan kalimat izin (singkat); daftar "tidak termasuk" tidak wajib di IG bila ada di website/WA + "belum termasuk pajak & service" |
| Travel | Apakah izin usaha & sertifikat kapten wajib jadi **syarat tayang** (bukan hanya syarat booking)? → **Ya**, syarat tayang (reviewer, 2026-10-09) |

## 2. Legal Review

| # | Pertanyaan | Konteks di repo | Jawaban legal | Tanggal | Dampak ke rules/knowledge |
|---|---|---|---|---|---|
| L1 | Bolehkah venue/WO menulis "kami bantu urus dokumen pernikahan WNA" di konten? Syarat apa yang wajib menyertainya? | `knowledge/segments/wedding.md` § Temuan Riset | | | |
| L2 | Izin acara/banjar/keramaian untuk wedding di villa: siapa yang wajib mengurus, dan perlu disebut di paket? | `templates/wedding-fact-sheet.md` § 3 | | | |
| L3 | Dokumen legalitas minimum operator open trip/kapal yang harus ada sebelum dipromosikan (izin usaha, kelaikan kapal, sertifikat kapten/pemandu)? | `templates/travel-fact-sheet.md` § 1, pilot travel `qa.md` T-03 | | | |
| L4 | Klaim asuransi peserta: apa yang boleh ditulis tanpa melanggar aturan pemasaran asuransi? | `templates/travel-fact-sheet.md` § 1 | | | |
| L5 | Promosi alkohol (beach club, corkage wedding) di IG/TikTok: batasan regulasi & platform? | `knowledge/segments/restaurant.md` claim hotspots | | | |
| L6 | Kata "no pork no lard" tanpa sertifikat halal: boleh dipakai atau berisiko? | `knowledge/segments/restaurant.md`, `templates/fnb-fact-sheet.md` § 5 | | | |

## 3. Verifikasi Sumber Primer

Agent sudah menemukan angka dari sumber sekunder (berita/operator). Konfirmasi ke sumber resmi lalu isi kolom. Bila domain sumber dibuka di environment Claude Code (**Allowed domains**), agent bisa mengerjakan bagian ini.

| # | Fakta | Nilai sekunder (2026-10-09) | Sumber primer yang dicek | Nilai primer + tanggal akses | Status |
|---|---|---|---|---|---|
| S1 | Kuota pengunjung TN Komodo | ± 1.000/hari sejak 1 Apr 2026 | Pernyataan Balai TN Komodo (Koordinator Kehumasan Maria Rosdalima Panggur) via [ANTARA 14 Apr 2026](https://www.antaranews.com/berita/5525623/btnk-tetapkan-kuota-1000-wisatawan-per-hari-di-tn-komodo); teks dikonfirmasi owner | **1.000 wisatawan/hari sejak 1 Apr 2026** — dicek 2026-10-09 | ✅ Terkonfirmasi (cek ulang sebelum musim ramai) |
| S2 | Cara beli tiket TN Komodo | Aplikasi SiOra | Balai TN Komodo / SiOra | | ☐ |
| S3 | Tarif masuk WNI | Rp50.000 hari kerja / Rp75.000 hari libur (PP 36/2024) | Teks PP 36/2024 / SiOra | | ☐ |
| S4 | Tarif masuk WNA | Belum ditemukan | PP 36/2024 / SiOra | | ☐ |
| S5 | Aturan drone di TN Komodo | Belum ditemukan | Balai TN Komodo | | ☐ |
| S6 | Musim manta | Ada sepanjang tahun; puncak bertentangan | Data operator client (per client) | | ☐ CLIENT CONFIRMATION |
| S7 | Spec platform IG/TikTok/GBP (TASK-011) | ASSUMPTION | Help center resmi | | ☐ |

## 4. Keputusan Owner

| Issue | Pilihan | Rekomendasi agent | Kalimat keputusan (salin & kirim ke agent) |
|---|---|---|---|
| [#46](https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/46) Nama produk | A: tetap "CLAU AI Content Studio" · B: payung "CLAU AI", "Content Studio" = modul AI Marketing | B (lebih cocok untuk 5 pilar; hanya ganti string i18n & brand guideline) | ✅ **Diputuskan: B** — Dea Karisna (d34faiza), 2026-10-09 |
| [#47](https://github.com/d34faiza-commits/CLAU-AI-CONTENT/issues/47) WORKFLOW.md | Ubah "1 Marketing & Content" → "1 AI Marketing" (PATCH) atau biarkan | Ubah (konsistensi dengan v3.0.0) | ✅ **Diputuskan: ubah** — Dea Karisna (d34faiza), 2026-10-09 (WORKFLOW.md v1.0.1) |

> Catatan: dokumen Approved hanya diubah atas perintah **Pak Indra** atau **Dea Karisna (d34faiza)**. Kalau mengedit lewat GitHub web, tempel isi file `.md` mentah, bukan tampilan preview.

## Setelah Paket Diisi

1. § 1 lulus → agent mengisi Record di `qa/scoring-rubric` per pilot + status Independent score.
2. § 2 → agent memperbarui rules/knowledge sesuai jawaban legal (perubahan rules mengikuti otoritas owner).
3. § 3 → baris jadi **DATA FINAL** dengan sumber + tanggal akses.
4. Semua selesai → TASK-041 ke Done; status wedding & travel di `clau-ai-core/docs/verticals.md` → **Fokus — Aktif**.

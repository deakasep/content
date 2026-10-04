# QA Gates — Villa Contoh Sunset Ubud (SIMULASI)

> **SIMULASI / FIKTIF.** Draft: [drafts.md](./drafts.md). Reviewer: AI agent (Claude Code), yang juga menulis draft dan sistemnya. Hasil gate ini **bukan** review independen; lihat [REPORT.md](./REPORT.md) §Keterbatasan.

## 1. [Claim Verification](../../qa/claim-verification.md)

| # | Klaim (persis di konten) | Konten | Kategori | Label | Sumber | Hasil |
|---|---|---|---|---|---|---|
| 1 | Tiga dari lima kamar menghadap sawah | C-A, C-C, R1 | facility | **DATA FINAL** | Fact sheet §2 + foto A | OK |
| 2 | Lima kamar, hingga 10 dewasa | C-A, C-B, C-C, R1, S1 | facility | **DATA FINAL** | Fact sheet §2 | OK |
| 3 | Bathtub di kamar sawah | C-B, R1 | facility | **DATA FINAL** | Fact sheet §2 | OK |
| 4 | "Bathtub with a rice-field view" (tersirat: sawah terlihat dari bathtub) | C-C | location | **FIELD VERIFICATION** | Fact sheet hanya menyebut kamar sawah punya bathtub, bukan bahwa bathtub menghadap sawah | **Ubah**: ganti jadi "a bathtub in the rice-field rooms" atau tunggu foto |
| 5 | Shot bathtub "sawah di jendela" | R1 | location | **FIELD VERIFICATION** | Sama dengan #4 | **Ubah shot** bila jendela kamar mandi tidak menghadap sawah |
| 6 | Kolam privat 4 × 12 m | semua | facility | **DATA FINAL** | Fact sheet §3 + foto A | OK |
| 7 | Sarapan di bale tepi sawah | C-A, C-B, R1, S1 | F&B | **DATA FINAL** | Fact sheet §3 | OK |
| 8 | Private chef, berbayar, pesan H-1 | C-A (ID & EN), C-B | F&B | **DATA FINAL** | Fact sheet §3 | OK; status berbayar disebut ✔ |
| 9 | Sunset | — | location | **FIELD VERIFICATION** | — | Tidak dipakai ✔ |
| 10 | Mewah / luxury | — | other | **ASSUMPTION** → **RISK** | — | Tidak dipakai ✔ |
| 11 | Jarak ke pusat Ubud | — | location | **FIELD VERIFICATION** | — | Tidak dipakai ✔ |
| 12 | Nama brand mengandung "Sunset" | semua | other | **RISK** | — | Nama bukan klaim, tapi memicu ekspektasi; lihat REPORT temuan G-05 |

**Hasil: Conditional.** C-A, C-B, dan S1 lolos. C-C dan R1 butuh perbaikan klaim bathtub/view (#4, #5).

> Catatan: klaim #4 lolos self-check skill di [drafts.md](./drafts.md) (ditandai ⚠️ tapi tidak dihapus) dan baru diputuskan "Ubah" di gate ini. Self-check TASK-018 berhasil **mendeteksi**, tapi skill belum mewajibkan **menghapus atau mengubah** sebelum diserahkan (temuan G-06).

## 2. [Content Review](../../qa/content-review.md)

| Area | Hasil | Catatan |
|---|---|---|
| Objective & struktur | **Conditional** | 1 CTA per konten ✔. Hook caption reel 133 karakter, melebihi aturan prompt ±125 (temuan G-04) |
| Brand voice | **Conditional** | Elegan-tertata, tanpa klise & kata terlarang. Voice Card client belum ada (**CLIENT CONFIRMATION**) |
| Bahasa & budaya | Pass | Paritas klaim ID/EN di C-A cocok; topik pura subak tidak disentuh; reel menghindari drone di atas rumah warga |
| Platform | **Conditional** | Panjang caption 226–726 karakter, di bawah batas kerja 2.200 yang masih **ASSUMPTION** (TASK-011). Spec durasi reel & safe area story belum terverifikasi |
| Kelengkapan | Pass | Tabel klaim, alt text, open items ada |

## 3. [Visual & AI Review](../../qa/visual-ai-review.md)

| Item | Hasil |
|---|---|
| Kategori visual | Foto A untuk carousel & story ✔; video B (light edit) untuk reel ✔ |
| Visual AI | Tidak dipakai ✔ |
| Distorsi ukuran kolam | Reel memberi catatan "hindari ultra-wide" ✔. Belum bisa dicek pada file nyata (aset fiktif) |
| Golden hour / sunset footage | Sengaja tidak dipakai ✔ |

**Hasil:** Pass (dengan catatan: aset fiktif, jadi visual sebenarnya belum diperiksa).

## 4. [Privacy & Rights Review](../../qa/privacy-rights-review.md)

| Item | Hasil |
|---|---|
| VCSU-VIDEO-001: pasangan dapat dikenali, consent belum ada | **Ditahan**: reel memakai shot tanpa wajah. Bila klip ini ingin dipakai → **NEXT ACTION** consent |
| Tangan staf di shot sarapan | OK (tidak dapat dikenali); bila wajah terlihat → consent staf |
| Musik reel | Library komersial akun bisnis, wajib dicek saat edit (**CLIENT CONFIRMATION** ketersediaan di akun) |
| Data tamu | Tidak ada ✔ |
| Konten berbayar | Tidak (`paid: false`) ✔ |

**Hasil:** Pass dengan syarat (VCSU-VIDEO-001 tidak dipakai tanpa consent).

## 5. [Publication Checklist](../../qa/publication-checklist.md) (pre-check, Mode SIMULASI)

| Item | C-A | C-B | C-C | R1 | S1 |
|---|---|---|---|---|---|
| Approval record **Approved** & versi sama | ❌ SIMULASI | ❌ | ❌ | ❌ | ❌ |
| Gate QA lulus | ✅ | ✅ | ❌ klaim #4 | ❌ klaim #5, hook | ✅ |
| Akun & channel benar | n/a (fiktif) | n/a | n/a | n/a | n/a |
| Tanggal, jam, zona waktu | ✅ 2026-10-17 WITA (jam belum ditetapkan ⚠️) | ✅ | ✅ | ✅ | ✅ |
| Tanpa placeholder / komentar internal | ✅ | ✅ | ✅ | ✅ | ✅ |
| Link berfungsi | n/a | n/a | n/a | n/a | ⚠️ link sticker belum ada URL |
| Harga/promo masih berlaku | n/a (tanpa promo) | n/a | n/a | n/a | n/a |
| Disclosure berbayar/AI | n/a | n/a | n/a | n/a | n/a |
| Alt text / subtitle | ✅ alt text | ⚠️ alt text belum per varian | ⚠️ | ✅ on-screen text | — |
| Tag & mention | ✅ tidak ada | ✅ | ✅ | ✅ | ✅ |
| Musik berlisensi | n/a | n/a | n/a | ⚠️ cek saat edit | n/a |

**Hasil: Fail, sesuai desain.** Mode SIMULASI tidak pernah boleh publish. Di luar blocker approval, blocker nyata yang ditemukan adalah klaim bathtub/view (C-C, R1), jam publish yang belum ditetapkan, dan URL link sticker story.

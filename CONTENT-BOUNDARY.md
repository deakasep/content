---
document_title: "CLAU Content Repository Boundary"
document_owner: "Dea Karisna / AI Marketing"
version: "0.1.4"
status: "Draft"
classification: "Internal"
---

# CLAU Content Repository Boundary

## Purpose

Menetapkan batas apa yang boleh dan tidak boleh disimpan di repository CLAU-AI-CONTENT. Repo ini adalah **playbook reusable** (rules, prompt, skill, knowledge umum, template, QA) — bukan arsip client, bukan media library, dan bukan tempat credential.

## Authority

Tunduk pada [CONTENT-CONSTITUTION.md](./CONTENT-CONSTITUTION.md). Klasifikasi data mengikuti [rules/09-DATA-CLASSIFICATION.md](./rules/09-DATA-CLASSIFICATION.md).

## Peran Repository

Repo ini **adalah**:

- sumber utama rules, prompt, skill, knowledge reusable, template, dan QA gate;
- tempat contoh konten yang **sudah dianonimkan** (fictional property, tanpa identitas client nyata);
- review surface lewat diff commit (dan pull request bila dipakai).

Repo ini **bukan**:

- arsip brief, draft, atau konten final per client;
- media library foto/video properti atau tamu;
- arsip review mentah, DM, chat WhatsApp, atau komentar;
- tempat credential akun social media, OTA extranet, ads account;
- database tamu, booking, atau CRM.

## Konten yang Diizinkan

Boleh masuk repo bila **semua** syarat terpenuhi:

1. scope `Reusable` — berlaku lintas client;
2. sensitivity `Public` atau `Internal`;
3. lifecycle `Approved`, atau `Draft`/`For Review` dengan status tertulis jelas di frontmatter/header dokumen;
4. tidak mengandung identitas client nyata, data tamu, harga kontrak, atau credential;
5. contoh konten memakai properti fiktif (mis. "Villa Contoh Ubud", "Kafe Contoh Canggu");
6. lolos `python scripts/validate.py` dan self-review diff sebelum push (atau review PR bila memakai PR).

## Konten yang Dilarang

Jangan commit:

- nama, foto, nomor HP, email, nomor booking, nomor kamar, atau tanggal menginap tamu;
- review/komentar mentah yang bisa mengidentifikasi tamu;
- foto/video asli properti client (simpan di media storage client);
- brief, kontrak, rate card, revenue, occupancy, atau data komersial client;
- password, token, OTP, cookie, API key, recovery code akun apa pun;
- export data dari Meta Business Suite, TikTok, GBP, atau OTA yang memuat data pengguna;
- output AI yang belum direview dan mengandung data client.

## Storage Zones

| Zone | Lokasi | Boleh di Git? | Isi |
|---|---|---:|---|
| Playbook | Repo ini | Ya | Rules, prompt, skill, knowledge umum, template, QA |
| Client Workspace | Folder/drive per client di luar repo | Tidak | Brief, draft, konten final, approval record terisi |
| Media Library | Storage media client (cloud drive / DAM) | Tidak | Foto, video, logo client, release form |
| Consent Register | Sistem client atau spreadsheet terproteksi | Tidak | Consent tamu, staf, talent, UGC |
| Credential Store | Password manager / secret manager | Tidak | Akses akun social media, OTA, ads |
| Analytics | Platform insight / report per client | Tidak | Data performa yang memuat data pengguna |

## Client-Specific Boundary

Pelajaran dari project client boleh dijadikan knowledge reusable hanya bila:

- nama client, lokasi spesifik, dan detail yang bisa mengidentifikasi sudah dihapus;
- menghapus nama saja tidak cukup bila kombinasi detail (lokasi + jumlah kamar + fitur unik) masih mengenali properti;
- owner repo me-review risiko re-identifikasi.

## Exceptions

Exception butuh persetujuan tertulis owner repo, berisi scope, alasan, data owner, sensitivity, akses, retensi, dan tanggal kedaluwarsa. Exception tidak pernah mengizinkan penyimpanan credential atau data pribadi tamu.

## Enforcement

- Branch + PR = **DISIPLIN MANUAL** (bukan enforcement otomatis). Direct push ke `main` = **DIIZINKAN** untuk solo dev di GitHub Free, TAPI WAJIB: commit message jelas, validator lokal lulus, backup rutin. Kalau tim 2+ orang, upgrade ke GitHub Team untuk branch protection.
- CI menjalankan `scripts/validate.py` (termasuk pola secret sederhana) dan gagal bila ada pelanggaran yang terdeteksi.
- Validator tidak menangkap semua pelanggaran; self-review diff (atau reviewer PR) tetap wajib cek manual.
- Bila data terlarang terlanjur ter-commit: hapus dari konten aktif, nilai apakah perlu pembersihan history (butuh otorisasi owner), rotasi credential bila relevan, dan catat insiden.

**Status:** **ASSUMPTION** — sesuai realita solo dev, GitHub Free tier. Akan di-review kalau: tim bertambah, upgrade GitHub Team, atau repo jadi public.

## Branch Protection & Disiplin Manual

GitHub Free tier tidak support branch protection di private repo. Di halaman pricing, "Repository rules" pada plan Free hanya untuk *public repositories*; untuk private repo fitur ini ada di Team dan Enterprise.

**Status:** **DATA FINAL** — sumber: <https://github.com/pricing>, diakses 2026-10-03.

### Mitigasi:

1. Commit message format — pakai `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`
2. Branch per fitur — `feat/nama-fitur`, `fix/nama-bug` (disarankan untuk perubahan besar; wajib bila tim 2+ orang)
3. Pull Request — review sendiri sebelum merge (disarankan untuk perubahan besar; wajib bila tim 2+ orang)
4. Validator lokal — test sebelum push
5. Backup rutin — push tiap selesai file

### Upgrade Path:

Kalau tim udah 2+ orang, upgrade ke GitHub Team untuk branch protection aktif.

| Item | Nilai | Sumber | Status |
|---|---|---|---|
| Harga GitHub Team | USD 4 per user/bulan **untuk 12 bulan pertama** (harga promo, bertanda `*` di halaman) | <https://github.com/pricing>, diakses 2026-10-03 | **DATA FINAL** |
| Harga GitHub Team setelah 12 bulan pertama | Tidak tercantum di halaman pricing | <https://github.com/pricing>, diakses 2026-10-03 | **ASSUMPTION** — cek ulang saat akan upgrade |
| Billing bulanan vs tahunan | Tidak tercantum di halaman pricing | — | **ASSUMPTION** — cek ulang saat akan upgrade |

Harga berubah sewaktu-waktu; verifikasi ulang ke halaman pricing sebelum upgrade.

## Revision History

| Version | Date | Status | Summary |
|---|---|---|---|
| 0.1.0 | 2026-10-03 | Draft | Initial repository boundary |
| 0.1.1 | 2026-10-03 | Draft | Tambah mitigasi branch protection (disiplin manual) untuk GitHub Free |
| 0.1.2 | 2026-10-03 | Draft | Sesuaikan enforcement dengan realita solo dev |
| 0.1.3 | 2026-10-03 | Draft | Verifikasi harga GitHub Team & batas fitur Free ke github.com/pricing |
| 0.1.4 | 2026-10-03 | Draft | Seragamkan metadata (owner) |

# Status & Handoff CLAU AI

> **Untuk sesi AI baru (Claude atau agent lain): baca halaman ini dulu.** Satu halaman untuk melanjutkan kerja tanpa riwayat chat. Diperbarui setiap ada perubahan status material. Last updated: 2026-10-27 (H1 merged; otorisasi merge ChatGPT/Codex setara Claude; runtime belum aktif).
>
> Peta semua pondasi otak (link ke file sumber): [peta-otak.md](./peta-otak.md). Board task: **ClickUp** → workspace Jerco Holding Company → Space **Clau AI** → folder **CLAU AI** (board utama sejak 2026-10-21); [tasks/](../tasks/README.md) = riwayat.

## 1. Siapa & Otoritas

| Item | Isi |
|---|---|
| Owner CLAU | **Dea Karisna (d34faiza)** |
| Otoritas perubahan dokumen Approved | Pak Indra atau Dea Karisna (d34faiza) |
| Repo Jerco (`indra-boop/*`, `d34faiza-commits/jerco-*`) | **Milik Pak Indra — jangan disentuh tanpa persetujuan beliau** |
| Repo CLAU | AI boleh langsung kerja (feature branch → PR → CI hijau → AI merge dalam scope yang diizinkan). Push langsung ke `main` dilarang (core, marketing, agents; dijaga `main-guard`) |
| AI tidak boleh | Publish, kirim ke pihak luar, self-approve, mengarang review manusia, commit data client nyata / `.env` / credential |

## 2. Repo CLAU

| Repo | Peran | Command validasi |
|---|---|---|
| `clau-core` | Otak induk: AI-CONSTITUTION **v3.1.0 Approved**, AI-BOUNDARY **1.7.0 Approved**, AGENTS **1.1.0 Approved**, router, WORKFLOW v1.0.1; API/database aktif 0.10.0, runtime contracts H1 v1.0.0 terpisah | `python scripts/validate_core.py` |
| `clau-market` | Pilar 1 AI Marketing (aktif): rules, skills, knowledge, templates, QA, pilot | `git submodule update --init --recursive && python scripts/validate.py --require-submodules` |
| `clau-agent` | Platform: registry (pillars + `autonomy_max`), backend FastAPI + PostgreSQL, frontend, deploy VPS 1 | `cd backend && pytest` · `python agents/evals/run_evals.py --check` |
| `clau-content` | Arsip + markas kerja: board task, paket review, design, halaman ini | `python scripts/validate.py` |

Submodule: `core/` di agents & marketing, `agents/` di marketing. Alur otomatis: core di-merge → bot PR bump core di agents → CI hijau → merge → bot PR bump agents + core di marketing (core marketing = pin agents/core, wajib sama). Edit selalu di repo sumber. Detail: `SUBMODULE.md` (agents/marketing), `clau-core/docs/getting-started.md` § 2.

## 3. Keputusan yang Sudah Diambil (jangan dibahas ulang)

| Tanggal | Keputusan | Sumber |
|---|---|---|
| 2026-10-09 | AI-CONSTITUTION v3.0.0: 5 pilar v2 (AI Marketing, AI Sales, AI Admin, AI Business Intelligence, AI Automation), otonomi A/B/C default **B**, vertical fokus villa, restoran/cafe, wedding, travel | `clau-core/AI-CONSTITUTION.md` |
| 2026-10-09 | Struktur repo tetap; core = otak; clau-content = markas kerja (opsi 1) | [peta-otak.md](./peta-otak.md) |
| 2026-10-09 | Brand produk "CLAU AI" (opsi B); WORKFLOW.md diubah ke v1.0.1 | [review-packet-task-041.md § 4](./review-packet-task-041.md) |
| 2026-10-09 | Data sensitif (database, auth, enkripsi) = rencana ke depan, belum dibangun (dilampaui 2026-10-12: lihat baris berikut) | TASK-041 |
| 2026-10-12 | AI-CONSTITUTION 3.1.0 / AI-BOUNDARY 1.2.0: semua push ke `main` (core, marketing, agents) wajib lewat PR dengan CI hijau; ditegakkan `main-guard` karena tetap GitHub Free | `clau-core/AI-BOUNDARY.md` § Disiplin Push |
| 2026-10-12 | Database PostgreSQL 16 sesuai kontrak core; aturan approval ditegakkan di database (CHECK + trigger); role aplikasi tanpa DDL | `clau-core/shared/database-schema.md` |
| 2026-10-12 | Login: Argon2id, sesi di server (cookie aman + CSRF), 2FA wajib owner, tanpa pendaftaran publik; owner membuat akun | `clau-agent/backend/README.md` |
| 2026-10-13 | AI-BOUNDARY 1.3.0: clau-content = arsip + markas kerja; job `docker` jadi check wajib clau-agent; VPS 1 hanya menayangkan `release/vps1` (commit `main` yang CI-nya hijau) | `clau-core/AI-BOUNDARY.md` |
| 2026-10-13 | Belum beli domain: VPS 1 tetap pratinjau tanpa login; VPS 2 menunggu VPS 1 maksimal. PR 3 (workflow) boleh jalan tanpa VPS 2 | owner, sesi 2026-10-13 |
| 2026-10-16 | AI-BOUNDARY v1.4.0 § Data ke Provider AI: hanya fakta yang dikonfirmasi klien + request disamarkan ke model AI; panggilan dicatat tanpa isi; API key hanya di worker VPS 2; hasil AI selalu draft (owner: "setuju gas") | `clau-core/AI-BOUNDARY.md` |
| 2026-10-16 | Repo di-rename: clau-core, clau-agent, clau-market, clau-content (isi tetap) dan dijadikan **public, hanya untuk dilihat**: LICENSE source-available di keempat repo, AI-BOUNDARY v1.5.0 (semua yang di-commit termasuk riwayat dianggap publik, tanpa IP/host server). Download/clone/screenshot tidak bisa dicegah secara teknis; perlindungannya hukum (owner: "Gass B kak") | `LICENSE`, `clau-core/AI-BOUNDARY.md` |
| 2026-10-15 | Pemulihan database selalu **manual** (satu perintah `clau-vps2-restore` yang dijalankan manusia); server yang mati boleh hidup lagi otomatis, isi database tidak pernah diganti otomatis. Backup tiap 6 jam + salinan Backblaze B2 | owner, sesi 2026-10-15; `clau-agent/docs/deploy/vps-2-setup.md` § 2, § 5 |
| 2026-10-15 | VPS 2 jalan **tanpa domain** dulu: backend + database + frontend login di VPS 2, dibuka hanya lewat HTTPS Tailscale (tim internal). Setelah domain ada, frontend kembali ke VPS 1 (keputusan VPS #1) | owner, sesi 2026-10-15; `clau-agent/docs/deploy/vps-2-setup.md` § 2 |
| 2026-10-21 | Board kerja CLAU pindah ke **ClickUp** (Space **Clau AI**, terpisah dari Jerco; alur Open → in progress → review → Closed seperti board Rekan AI). Satu list per pilar + Platform + Release & Deploy; judul kartu memuat `TASK-xxx`. Board Markdown `tasks/` dibekukan sebagai riwayat; task baru mulai TASK-064 di ClickUp (arahan Pak Indra lewat telepon dengan owner) | [tasks/README.md § Board ClickUp](../tasks/README.md#board-clickup) |
| 2026-10-22 | **Fokus Pilar 1 AI Marketing hospitality sampai siap jual; Pilar 2–5 ditunda** (kartu TASK-035–039 & TASK-066 tidak dikerjakan sampai owner membuka lagi). Owner: "pilar 2-5 skip ini untuk kedepannya.. saat ini kita fokus ke pilar 1 hospitalty" | [review-packet-task-067.md](./review-packet-task-067.md) |
| 2026-10-09 | Dependabot tidak membuka update versi mayor otomatis; versi mayor dikerjakan sebagai PR tersendiri setelah diuji | `clau-agent/docs/security.md` § 5 |
| 2026-10-09 | Review independen 3 pilot SIMULASI (kafe, wedding, travel): v1 belum lulus → **v2 lulus**, "dapat di-upgrade kapan saja" | [review-packet-task-041.md § 1](./review-packet-task-041.md) |

**Keputusan coding 2026-10-27:** Pak Indra mengizinkan ChatGPT/OpenAI Codex otomatis merge seperti Claude untuk scope pekerjaan yang sudah diizinkan. Berlaku setelah seluruh CI wajib hijau pada head terakhir; gunakan expected head SHA dan jangan bypass review/ruleset. Sumber: [core#22](https://github.com/d34faiza-commits/clau-core/pull/22), AI-BOUNDARY 1.7.0 dan AGENTS 1.1.0. Ini bukan approval konten client.

Cara review via chat yang disepakati: AI menyusun **pre-review kritis** (dicatat jujur sebagai buatan AI), owner menjawab "setuju"/"ubah". Jangan pernah menulis review seolah-olah dibuat manusia.

## 4. Status Sekarang

| Area | Status |
|---|---|
| Pilar 1 AI Marketing | Aktif. 4 vertical fokus punya fact sheet, voice guide, pilot SIMULASI lulus |
| Pilar 2–5 | Planned, **ditunda owner 2026-10-22** (fokus Pilar 1); blueprint di `clau-core/docs/blueprints/` |
| Platform (agents) | Backend **v0.10.0** (2026-10-22: 2FA wajib content lead TASK-054; penanda isi konten & level approval otomatis TASK-032, migrasi 0007) (PR 2b merged 2026-10-13, PR 3 & 3b merged 2026-10-14, antrean AI agents#54 + UI PR 4d): PostgreSQL 16 (22 tabel, migrasi 0001–0007, Constraint Wajib), login + CSRF + 2FA wajib owner (QR + kode cadangan), `/users` (owner), keluar semua perangkat, backup terenkripsi + uji restore; kontrak `core/shared` 0.8.0. Dites lokal & CI; **live di VPS 2 2026-10-15 s.d. 2026-10-22** (server dimatikan; lihat baris VPS 2). Workflow ([agents#46](https://github.com/d34faiza-commits/clau-agent/pull/46)): request → draft → QA → approval, Rule 08 ditegakkan server + database (migrasi 0004), isolasi klien, 14 temuan audit adversarial diperbaiki. Fact sheet ([agents#48](https://github.com/d34faiza-commits/clau-agent/pull/48)): klien, fact sheet & Konfirmasi Fakta oleh klien (migrasi 0005, 18 tabel), UI `/requests` & `/fact-sheets`, 10 temuan audit adversarial diperbaiki. Antrean AI (migrasi 0006): job, worker terpisah, AI fact-check, batas biaya, provider tiruan. Belum: provider AI nyata (PR 4c) |
| Backend VPS 2 | **Dimatikan owner 2026-10-22** (biaya); dibuat lagi setelah ada dana (TASK-065). Sebelumnya live tanpa domain lewat HTTPS Tailscale, backend 0.9.0, backup tiap 6 jam + salinan Backblaze B2. **Data:** backup terenkripsi di B2 (isi SIMULASI + akun owner; belum ada klien nyata), terhapus otomatis 60 hari setelah diupload (lifecycle `vps2/`). Kunci pemulihan (`CLAU_BACKUP_PASSPHRASE`, `CLAU_SECRET_KEY`, key B2) di password manager owner. Membuat ulang: `clau-agent/docs/deploy/vps-2-setup.md` § 5 (server pengganti) |
| Dashboard VPS 1 | **Dimatikan owner 2026-10-22** (biaya); dibuat lagi dengan `vps1-setup.sh` satu perintah (`clau-agent/docs/deploy/vps-1-setup.md` § 0). Job CI `release-vps1` tetap memajukan `release/vps1` ke commit `main` yang hijau, jadi server baru langsung mendapat versi terbaru |
| Keamanan | Header + CSP, Nginx dikeraskan, sandbox systemd, audit dependency + scan secret di CI, Actions dipin SHA, Dependabot. 2026-10-13: audit login/database (22 temuan ditutup) dan audit CI lintas repo (urutan sync core→agents→marketing, pin core wajib sama, token tidak terbaca kode PR, `main-guard` hanya menghitung run GitHub Actions dan semua run harus hijau). Detail: `clau-agent/docs/security.md` |
| Client nyata | Belum ada. Konten SIMULASI tidak bisa dinaikkan jadi konten client; mulai dari Step 1 CONTENT-WORKFLOW dengan fact sheet nyata |

## 4a. Hospitality Runtime — Golden Path Tara (2026-10-27)

**Status: implementasi contracts H1 sudah merged; belum aktif di runtime production.** Arahan sesi
2026-10-27: jalankan Hospitality Agent Runtime Master Blueprint v1.0, mulai Tara,
Pilar 1 hospitality. [PR core#21](https://github.com/d34faiza-commits/clau-core/pull/21)
menambahkan contracts v1.0.0, strict JSON Schema, 10 synthetic fixtures, error registry,
reference checks dan 43 conformance tests. Hasil lokal: validator core PASS, fixture
PASS, 43 tests PASS, diff check PASS. Ini **self-review AI**, bukan independent review
manusia, security audit runtime, atau real-model evaluation.

Sumber implementasi: [H1 contracts dan migration gates](https://github.com/d34faiza-commits/clau-core/blob/main/shared/runtime/README.md).
CI/mergeability wajib dicek langsung pada commit terakhir PR sebelum AI/owner merge;
status CI pada halaman ini tidak menjadi bukti terbaru. Backend/API tetap 0.10.0,
fake provider; H1 belum mengubah runtime, database atau deployment. Pin core di agent
dan market sudah mencapai `21bebc7` (core#22); CI main agent `7878d62` hijau saat
pemeriksaan. Ini bukti saat pemeriksaan, bukan jaminan status CI di masa depan.

Urutan berikutnya:

1. H1 [core#21](https://github.com/d34faiza-commits/clau-core/pull/21) dan handoff [content#74](https://github.com/d34faiza-commits/clau-content/pull/74) sudah merged. Policy [core#22](https://github.com/d34faiza-commits/clau-core/pull/22) juga merged dan tersinkron. Entry point Codex platform: [agent#71](https://github.com/d34faiza-commits/clau-agent/pull/71); cek merge/CI dan sync market sebelum lanjut H2.
2. H2: bundle Tara hospitality, pinned knowledge/schema/tool contracts, eval matrix.
3. H3–H4: loader/context assembler, migration non-draft outcomes/memory/evidence,
   deterministic validators dan review UI/approval gates.
4. H5–H6: real provider + budget/retention gates, real-output eval dan human rubric.
5. H7: SIMULASI end-to-end dan pilot client nyata dengan independent review.

H1 tidak membuktikan production readiness. Provider nyata, quality threshold dan pilot
client belum terpenuhi. Task ID ClickUp baru tidak dikarang; kaitkan pekerjaan H1–H7
ke board utama saat akses ClickUp tersedia. TASK-052 tetap terbuka (belum complete).

## 5. Pekerjaan Terbuka (urut prioritas)

| # | Item | Siapa | Lokasi |
|---|---|---|---|
| 1 | Legal review L1–L6 (WNA, izin acara, legalitas operator, asuransi, alkohol, "no pork no lard") | Konsultan hukum / notaris | [review-packet § 2](./review-packet-task-041.md) |
| 2 | Sumber primer S2–S7 (tiket & tarif TN Komodo, drone, manta, spec platform) | Owner, atau AI setelah domain resmi dibuka di network policy | [review-packet § 3](./review-packet-task-041.md) |
| 3 | Domain + HTTPS publik (blocker login klien; tim internal sudah login lewat HTTPS Tailscale di VPS 2) + CSP nonce; lalu kembali ke keputusan VPS #1 (frontend di VPS 1) | Owner (beli domain) → AI | `clau-agent/docs/security.md` § 2, § 6 |
| 4 | Tahap 2 (AI menulis draft, TASK-052): AI-BOUNDARY v1.4.0 disetujui owner 2026-10-16; kontrak 0.9.0 (core#16) + antrean, worker, AI fact-check, batas biaya, provider tiruan (agents#54) dibangun. UI PR 4d selesai (`/requests/[id]` *Buat draft dengan AI*, `/ai-usage`). Sisa: provider Claude PR 4c (butuh akun API, batas biaya, retensi data dari owner) | AI → Owner | TASK-052 |
| 5 | Token CI: `SUBMODULE_READ_TOKEN` read-only sudah disimpan (owner, 2026-10-13). Sisa: pengingat kalender sebelum token `SUBMODULE_READ_TOKEN` & `SUBMODULE_TOKEN` kedaluwarsa | Owner | `SUBMODULE.md` § Setup GitHub Actions |
| 5a | **Server dimatikan 2026-10-22** (TASK-065): amankan kunci pemulihan, putuskan backup B2 (hilang otomatis 60 hari), hapus mesin di Tailscale dan deploy key di GitHub; hidupkan lagi saat ada dana | Owner | Kartu ClickUp TASK-065 |
| 6 | VPS 2 selesai: setup A–I, backup 6 jam + B2 aktif (2026-10-19; TASK-049 Done). VPS 1 pengganti satu perintah: `vps1-setup.sh` (agents#57). Sisa: uji coba "VPS 2 hilang total" di VPS sementara (±30 menit, sekali) | Owner + AI | `clau-agent/docs/deploy/vps-2-setup.md` § 5, `vps-1-setup.md` § 0 |
| 7 | Onboarding client nyata pertama (1 client, 1 vertical, 1 kanal) | Owner + AI (paket onboarding) | `clau-market/templates/client-onboarding.md` |
| 8 | Aktivasi pilar 2–5 setelah VPS | Owner + AI | `tasks/backlog.md` TASK-035–039 |
| 8e | ~~Audit `clau-core` untuk 5 pilar~~ **selesai 2026-10-22** (core#19 merged): nama repo pilar usulan diseragamkan (`clau-sales`, `clau-admin`, `clau-insight`, `clau-automation`), blueprint `ad-brief` L3, cabang Pilar 5 di decision tree, § Data Lintas Pilar, AI-BOUNDARY 1.6.1 | — | clau-core `docs/5-pillar-architecture.md` |
| 8a | ~~AI-BOUNDARY 1.6.0~~ **selesai 2026-10-22**: [core#17](https://github.com/d34faiza-commits/clau-core/pull/17) merged, sudah sampai ke clau-agent (#59) dan clau-market (#62); TASK-064 Closed | — | clau-core `AI-BOUNDARY.md` § Disiplin Push |
| 8b | ~~TASK-050 CI hemat menit~~ **ditutup owner 2026-10-22**: Actions gratis karena repo public. Bila repo kembali private, buka task baru | — | Kartu ClickUp TASK-050 |
| 8c | ~~TASK-054 keamanan sebelum klien login~~ **selesai 2026-10-22**: [agents#60](https://github.com/d34faiza-commits/clau-agent/pull/60) + [core#19](https://github.com/d34faiza-commits/clau-core/pull/19) merged (backend 0.9.1: 2FA wajib content lead, timer pembersihan sesi VPS 2, prosedur rotasi secret); kartu Closed | — | `clau-agent/docs/deploy/vps-2-setup.md` § 4a |
| 8d | ~~TASK-032 level approval otomatis~~ **selesai 2026-10-22**: [core#19](https://github.com/d34faiza-commits/clau-core/pull/19), [agents#61](https://github.com/d34faiza-commits/clau-agent/pull/61), [market#64](https://github.com/d34faiza-commits/clau-market/pull/64) merged, CI main hijau. Backend **0.10.0** (migrasi 0007): review negatif & terjemahannya → L3, harga di teks → L2, orang → L2, iklan/influencer/agama-adat/krisis → L3; kartu Closed | — | [review-packet-task-032.md](./review-packet-task-032.md) |
| 8h | **Pilar 1 siap jual (TASK-067):** commercial kit (paket, discovery, proposal, FAQ, SOP delivery, kontrak + DPA draft), kalender 2027, perbaikan batas 5 hashtag Instagram, verifikasi sebagian spec platform ([market#67](https://github.com/d34faiza-commits/clau-market/pull/67)). **K1–K8 disetujui owner 2026-10-23**; commercial kit Approved v1.0.0 + Facebook + realita lapangan ([market#68](https://github.com/d34faiza-commits/clau-market/pull/68)). Syarat sebelum klien pertama tanda tangan: TASK-028 (owner menilai 1 pilot), TASK-053 (cek hukum kontrak + DPA + L1–L6), badan usaha & pajak | Owner → AI | [review-packet-task-067.md](./review-packet-task-067.md) |
| 8f | *(Ditunda owner 2026-10-22)* **Paket keputusan aktivasi Pilar 2 AI Sales** (TASK-066): tahap 1 = `inquiry-reply`, `guest-message`, `complaint-escalation` (baru), tanpa Level A & tanpa integrasi WhatsApp; menunggu jawaban owner K1–K9. Persiapan boleh jalan sebelum server hidup; dipakai client nyata setelah TASK-052 PR 4c, TASK-065, TASK-053 | Owner → AI | [review-packet-task-066.md](./review-packet-task-066.md) · kartu ClickUp TASK-066 |
| 8g | Sync submodule 2026-10-22 selesai: [agents#62](https://github.com/d34faiza-commits/clau-agent/pull/62) & [market#66](https://github.com/d34faiza-commits/clau-market/pull/66) merged, pin `core/` di agents & marketing = core `a07f0c3` (main), CI `main` hijau di ketiga repo. Branch sisa di clau-core untuk dihapus owner: `claude/task-054-2fa-content-lead` (PR #18 ditutup) | Owner (hapus branch) | GitHub |
| 9 | Backlog lain | — | ClickUp Space **Clau AI** (riwayat: [tasks/backlog.md](../tasks/backlog.md)) |

## 5a. Roadmap ke "maksimal" (urutan disepakati owner 2026-10-15)

Board: ClickUp Space **Clau AI** (riwayat: [tasks/](../tasks/README.md)). Urutan kerja; tahap berikutnya dipicu beban/jumlah klien, bukan tanggal.

| Tahap | Isi | Task |
|---|---|---|
| A. Segera | Backup 6 jam + B2 + pemulihan manual (agents#54, selesai), CI hemat menit (tidak diperlukan selama repo public: GitHub Actions gratis, dicek 2026-10-22), uji "VPS 2 hilang total" | TASK-049, 050, 051 |
| B. Sebelum klien nyata pertama | Domain + HTTPS, **Tahap 2 AI menulis draft** → **AI Content Agent "Paket Konten Bulanan"** (produk pertama yang menghasilkan uang), legal & UU PDP, keamanan tambahan, onboarding klien pertama | TASK-047, **052 (sedang dirancang)**, **063**, 053, 054, 055 |
| C. Menuju ±30 klien | Monitoring & alarm, staging, dashboard biaya & kualitas AI, SOP tim, penagihan | TASK-056–060 |
| D. 200+ klien | Worker terpisah, database terkelola, 2+ server aplikasi, pentest | TASK-061 |
| E. Non-teknis | Tim reviewer (batas kapasitas sebenarnya), bukti hasil, sumber primer S2–S7 | TASK-059, 062, 041 |

Prinsip produk (owner 2026-10-15): tidak ada AI → langsung publish; alur = AI menghasilkan → AI fact-check ke data klien → owner review → approve (+ klien) → final. Urutan agent: Content → Sales → Customer Service → SEO → Advertising → Business (peta ke pilar: usulan Tahap 2 § 1a).

Prinsip skala (owner 2026-10-15): 12 agent = satu aplikasi di VPS 2, bukan satu server per agent; server ditambah bertahap sesuai beban tanpa membangun ulang.

## 6. Cara Kerja untuk AI (ringkas)

1. Baca halaman ini → `CLAUDE.md` repo yang dikerjakan → `core/AGENTS.md`.
2. `git fetch`; bila PR branch sebelumnya sudah merge, mulai ulang branch dari `origin/main`.
3. Kerja di feature branch → validator lulus → commit (`feat:`/`fix:`/`docs:`/`refactor:`/`chore:`/`test:`) → PR → CI hijau → AI merge tanpa meminta izin ulang untuk task yang sudah diizinkan (perintah Pak Indra 2026-10-27; core AI-BOUNDARY § Merge oleh AI Coding Agent). Gunakan expected head SHA; jangan bypass ruleset/review. Perubahan `core/shared` (kontrak) di-merge dulu, lalu pin `core/` di agents dipindah ke commit merge.
4. Label evidence persis: `DATA FINAL`, `ASSUMPTION`, `CLIENT CONFIRMATION`, `FIELD VERIFICATION`, `RISK`, `NEXT ACTION`.
5. Setelah perubahan status material, perbarui halaman ini dan **kartu ClickUp** yang terkait (lewat konektor ClickUp bila ada; bila tidak, sebutkan ke owner kartu mana yang perlu dipindah). Kartu **Closed** hanya bila PR merge dan CI hijau, dicek langsung di GitHub.
6. Status platform cukup ditulis di sini dan di `clau-agent/CLAUDE.md`; dokumen lain me-link ke sini.
7. **Setelah merge oleh AI/owner (otomatis, tanpa menunggu diminta; otorisasi 2026-10-27):** cek langsung di GitHub bahwa CI `main` hijau di repo yang di-merge dan bot sync submodule (core → agents → market) selesai; bila PR bot konflik atau gagal, jalankan ulang workflow `sync-submodules` atau perbaiki lewat PR baru (AI-BOUNDARY § Kapan PR Boleh Disebut Selesai); pindahkan kartu ClickUp yang kriteria *Selesai bila*-nya terpenuhi ke **Closed** dengan komentar bukti; perbarui halaman ini; lalu lanjut ke kartu berikutnya dengan prioritas tertinggi yang tidak butuh keputusan owner, dan sebutkan kartu yang butuh keputusan owner.

Saat sesi aktif, agent terus memantau CI sampai dapat merge atau ada blocker nyata.
Jika sesi terputus/limit, catat PR/head/status pending; jangan mengklaim sudah merged
atau terus berjalan di background. Sesi berikutnya baca ulang GitHub sebelum melanjutkan.

## 7. Pindah Akun Claude

Semua kerja tersimpan di GitHub, bukan di akun claude.ai. Akun Claude lain tetap bisa melanjutkan kerja selama:

1. Akun Claude baru disambungkan ke akun GitHub yang sama (`d34faiza-commits`) lewat claude.ai/connect-github. Kalau akun GitHub-nya berbeda, akun itu harus ditambahkan sebagai collaborator di repo CLAU (dan oleh Pak Indra untuk repo Jerco).
2. Semua kerja penting sudah di-commit, di-push, dan masuk `main` lewat PR. Yang hanya ada di chat tidak ikut pindah.
3. Halaman ini sudah mencerminkan status terakhir.

Tidak ikut pindah: riwayat chat/sesi, memory & Projects claude.ai, pengaturan environment Claude Code (network policy, secret, setup script), scheduled task, dan connector (mis. **ClickUp**, Google Drive; sambungkan ulang di claude.ai/customize/connectors lalu mulai sesi baru). Saat membuat sesi baru, pilih repo dengan nama baru (`clau-core`, `clau-agent`, `clau-market`, `clau-content`) supaya pemantauan PR berjalan. Siapkan ulang di akun baru; secret diambil dari password manager owner, tidak pernah dari repo.

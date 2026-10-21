# Done

Arsip task yang sudah lolos acceptance criteria. Jangan dihapus — ini jejak traceability. Tambahkan `- Completed: YYYY-MM-DD` dan `- Commit: <hash>` saat memindahkan task ke sini. Format: [task-template](./templates/task-template.md).

## TASK-049: Backup VPS 2 tiap 6 jam + Backblaze B2 + pemulihan manual (pasang di server)

- ID: TASK-049
- Status: Done
- Priority: High
- Assignee: Dea Karisna + AI
- Created: 2026-10-15
- Due: —
- Description: Kode siap di agents#54 (backup tiap 6 jam, salinan B2 dengan Object Lock, `clau-vps2-restore`, mode server pengganti). Menunggu CI (kuota GitHub Actions habis s.d. awal bulan) lalu merge. Owner: simpan `CLAU_SECRET_KEY` di password manager (bisa sekarang), buat akun B2 (langkah I nomor 1–5).
- Acceptance Criteria: agents#54 merged dengan CI hijau; langkah E diulang di VPS 2; `clau-vps2-offsite setup` menampilkan `OK Object Lock aktif`; `clau-vps2-check` menunjukkan salinan B2 ≤ 13 jam; `CLAU_SECRET_KEY` tersimpan di password manager.
- Related: https://github.com/d34faiza-commits/clau-agent/pull/54, [vps-2-setup § 3 H–I, § 5](https://github.com/d34faiza-commits/clau-agent/blob/main/docs/deploy/vps-2-setup.md)
- Note 2026-10-19: agents#54 merged; backup terenkripsi tiap 6 jam + salinan Backblaze B2 (Object Lock 30 hari) aktif di VPS 2; `sudo clau-vps2-check` = 0 gagal, 0 perlu dicek; passphrase backup, `CLAU_SECRET_KEY`, dan key B2 di password manager owner (lihat docs/status.md § 4).
- Completed: 2026-10-19
- Commit: clau-agent `c6999db` (docs status VPS 2), merge [agents#58](https://github.com/d34faiza-commits/clau-agent/pull/58)

## TASK-048: Tahap 1 PR 3b — fact sheet, konfirmasi fakta, dan UI workflow

- ID: TASK-048
- Status: Done
- Priority: High
- Assignee: AI (Claude Code), review owner
- Created: 2026-10-14
- Due: —
- Description: Endpoint kelola klien, fact sheet (versi, approve oleh approver klien), dan konfirmasi fakta (`fact_confirmations`, append-only) sesuai kontrak core; lalu halaman workflow di frontend (daftar request, editor draft + klaim, QA, tombol keputusan dengan bukti tertulis). Sampai ini selesai, approval draft yang memuat klaim fakta tetap ditolak (`facts_unconfirmed`, fail closed).
- Acceptance Criteria: Kontrak core diperbarui & di-merge dulu; konfirmasi fakta hanya oleh approver klien/owner dengan jejak; UI tidak menampilkan tombol publish; test PostgreSQL + E2E lewat frontend; CI hijau.
- Related: TASK-046, <https://github.com/d34faiza-commits/clau-core/blob/main/shared/api-contracts.md>
- Note 2026-10-14: PR [core#15](https://github.com/d34faiza-commits/clau-core/pull/15) (kontrak 0.8.0) dan [agents#48](https://github.com/d34faiza-commits/clau-agent/pull/48) (backend 0.8.0 + UI). 295 test, uji mutasi 34/35, E2E Docker + uji browser lulus; 10 temuan audit adversarial diperbaiki. Kedua PR merge dengan CI hijau.
- Completed: 2026-10-14
- Commit: clau-core `0f392b0` (merge #15), clau-agent `93b43ae` (merge #48)

## TASK-046: Tahap 1 PR 3 — workflow request → draft → QA → approval di API

- ID: TASK-046
- Status: Done
- Priority: High
- Assignee: AI (Claude Code), review owner
- Created: 2026-10-13
- Due: —
- Description: Endpoint requests/drafts/qa-records/approvals sesuai kontrak core; aturan Rule 08 dicek di server (kode di `api-contracts.md` § Kode Aturan Approval, termasuk `facts_unconfirmed` lewat `claims.fact_key` + `drafts.fact_sheet_id`); isolasi data per klien di setiap query. Tidak butuh VPS 2.
- Acceptance Criteria: Kontrak core di-merge dulu; test ke PostgreSQL sungguhan untuk setiap kode aturan; tidak ada endpoint publish; CI hijau.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/shared/api-contracts.md>, TASK-032
- Note 2026-10-14: PR [core#14](https://github.com/d34faiza-commits/clau-core/pull/14) (kontrak 0.7.0) dan [agents#46](https://github.com/d34faiza-commits/clau-agent/pull/46) (backend 0.7.0). 242 test lulus, mutation test 28/28, E2E Docker lulus; 14 temuan audit adversarial diperbaiki. Kedua PR merge dengan CI hijau.
- Completed: 2026-10-14
- Commit: clau-core `a56dd37` (merge #14), clau-agent `36547d4` (merge #46)

## TASK-045: Pasang paket VPS 1 tahap 2 (user khusus, cek & backup rutin)

- ID: TASK-045
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-13
- Due: —
- Description: Jalankan `sudo bash /srv/clau/clau-ai-agents/scripts/deploy/vps1-harden.sh` di VPS 1 (rollback otomatis bila gagal), lalu di admin Tailscale hapus entri `clau-vps1-aja` dan matikan key expiry `clau-vps1`.
- Acceptance Criteria: `sudo clau-vps1-check` tanpa GAGAL (screenshot dikirim ke agent); status VPS 1 di `clau-agent/docs/deploy/vps-1-setup.md` § 1 diperbarui ke DATA FINAL.
- Related: <https://github.com/d34faiza-commits/clau-agent/blob/main/docs/deploy/vps-1-setup.md>
- Completed: 2026-10-13
- Commit: clau-agent `6b79fc8` (paket), dipasang di VPS 1 oleh owner
- Note 2026-10-13: `sudo clau-vps1-check` = 0 gagal, 0 perlu dicek (UFW, SSH, fail2ban, Tailscale key expiry mati, frontend sebagai `clau-web`, exposure 1.3, backup config pertama 17 file).

## TASK-012: Pilot workflow dengan brief fiktif end-to-end

- ID: TASK-012
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Uji WORKFLOW.md (9 langkah) memakai properti fiktif ("Villa Contoh Ubud") dari brief sampai approval record, untuk menemukan celah di rules/skills/QA sebelum dipakai untuk client nyata.
- Acceptance Criteria: Satu brief valid terhadap schema, draft dari minimal 2 skill, semua QA gate terisi, daftar temuan/perbaikan dibuat sebagai task baru.
- Related: [pilot](../examples/pilot-villa-contoh-ubud/README.md), [WORKFLOW.md](../WORKFLOW.md), [content-brief schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/clau-content/issues/12>
- Completed: 2026-10-04
- Commit: 12c1eaa

## TASK-015: Tambah Voice Card ke schema & template brief

- ID: TASK-015
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-01 pilot TASK-012: brief tidak membawa Voice Card, sehingga brand voice tidak bisa diverifikasi dan skill jatuh ke voice default.
- Acceptance Criteria: Schema brief punya field voice (arketipe, 3 kata sifat, 3 "bukan", sapaan, emoji, kata wajib/terlarang) atau referensi Voice Card; `templates/content-brief.md` selaras; brief pilot diperbarui; validator lulus.
- Related: [pilot F-01](../examples/pilot-villa-contoh-ubud/README.md), [rule 03](../rules/03-CLIENT-BRAND-VOICE-STANDARD.md), issue <https://github.com/d34faiza-commits/clau-content/issues/15>
- Completed: 2026-10-04
- Commit: d05bda3

## TASK-016: Bikin template fact sheet properti

- ID: TASK-016
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-02 pilot TASK-012: tidak ada template fact sheet properti (bed type, ukuran kamar, kamar mandi, kebijakan, check-in/out, aksesibilitas), sehingga listing OTA tertahan placeholder.
- Acceptance Criteria: `templates/property-fact-sheet.md` ada (minimal vertical accommodation), setiap field punya kolom label evidence; skill `write-ota-listing` merujuk template ini; validator lulus.
- Related: [pilot F-02](../examples/pilot-villa-contoh-ubud/README.md), [write-ota-listing](../skills/write-ota-listing/SKILL.md), issue <https://github.com/d34faiza-commits/clau-content/issues/16>
- Completed: 2026-10-04
- Commit: ccb0145

## TASK-017: Mode simulasi/pilot di WORKFLOW & approval record

- ID: TASK-017
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-05 pilot TASK-012: WORKFLOW dan approval record tidak punya mode simulasi, sehingga record pilot berisiko terbaca sebagai approval nyata.
- Acceptance Criteria: `WORKFLOW.md` dan `templates/approval-record.md` punya aturan eksplisit mode SIMULASI (penanda wajib, langkah yang boleh dilewati, larangan publish); versi & Revision History naik; validator lulus.
- Related: [pilot F-05](../examples/pilot-villa-contoh-ubud/README.md), [WORKFLOW.md](../WORKFLOW.md), issue <https://github.com/d34faiza-commits/clau-content/issues/17>
- Completed: 2026-10-04
- Commit: 3dd6aee

## TASK-018: Self-check klaim tersirat di skill draft-caption

- ID: TASK-018
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-06 pilot TASK-012: klaim tersirat di Varian C lolos self-check skill dan baru tertangkap di claim gate.
- Acceptance Criteria: Self-check `draft-caption` (dan skill drafting lain yang relevan) menambah langkah ekstrak klaim tersirat (view, jarak, suasana, kapasitas) lalu cocokkan ke tabel klaim; validator lulus.
- Related: [pilot QA klaim #7](../examples/pilot-villa-contoh-ubud/qa-and-approval.md), [draft-caption](../skills/draft-caption/SKILL.md), issue <https://github.com/d34faiza-commits/clau-content/issues/18>
- Completed: 2026-10-04
- Commit: 32a6b47

## TASK-019: Wajibkan source_date untuk klaim DATA FINAL di schema

- ID: TASK-019
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan F-07 pilot TASK-012: schema hanya mewajibkan `source` untuk klaim DATA FINAL, padahal rule 01 dan Constitution meminta versi/tanggal sumber.
- Acceptance Criteria: Schema brief mewajibkan `source` + `source_date` untuk klaim DATA FINAL; brief contoh tetap valid; validator lulus.
- Related: [pilot F-07](../examples/pilot-villa-contoh-ubud/README.md), [schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/clau-content/issues/19>
- Completed: 2026-10-04
- Commit: 139718e

## TASK-010: Bikin automations/level-1-manual/README.md

- ID: TASK-010
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Dokumentasikan automation level 1 (manual/semi-manual) untuk workflow konten: checklist harian, copy-paste skill/prompt ke AI tool, scheduling manual oleh manusia. Folder `automations/` belum ada.
- Acceptance Criteria: Folder `automations/level-1-manual/` ada dengan README berisi scope, langkah, tools yang dipakai, dan batas (AI tidak publish/approve sendiri sesuai CONTENT-CONSTITUTION); validator lulus; README root mencantumkan folder baru.
- Related: [automations level 1](../automations/level-1-manual/README.md), [WORKFLOW.md](../WORKFLOW.md), [rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md), issue <https://github.com/d34faiza-commits/clau-content/issues/11>
- Completed: 2026-10-04
- Commit: 99ed168

## TASK-020: Atur kata positioning (luxury/mewah) & nama brand yang menyiratkan klaim

- ID: TASK-020
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-05 pilot 2: "mewah/luxury" dan nama brand seperti "Sunset" tidak diatur di rules, hanya di file riset regulasi.
- Acceptance Criteria: Rule 02 punya bagian kata positioning & nama brand (checklist, risk, eskalasi); voice guide punya daftar kata positioning + pengganti; validator lulus.
- Related: [rule 02](../rules/02-HOSPITALITY-CLAIM-STANDARD.md), [pilot-2 G-05](../examples/pilot-2/REPORT.md), issue <https://github.com/d34faiza-commits/clau-content/issues/20>
- Completed: 2026-10-04
- Commit: ae3d6c4

## TASK-021: Prompt & skill reel/video script

- ID: TASK-021
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-02 pilot 2: tidak ada prompt/skill reel script; script dibuat improvisasi.
- Acceptance Criteria: `prompts/video/reel-script.md` + skill `draft-reel-script` (SKILL.md + agents/openai.yaml) dengan shot list, klaim & consent per shot; README index; validator lulus.
- Related: [reel-script](../prompts/video/reel-script.md), [skill](../skills/draft-reel-script/SKILL.md), issue <https://github.com/d34faiza-commits/clau-content/issues/21>
- Completed: 2026-10-04
- Commit: 03cf564

## TASK-022: Prompt Stories + aturan Reels/Stories/alt text di rule 05

- ID: TASK-022
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-03 & G-07 pilot 2: tidak ada prompt Stories; aturan emoji/hook/sticker/link dan alt text per slide belum ada.
- Acceptance Criteria: `prompts/stories/stories-sequence.md`; rule 05 punya aturan Reels, Stories, alt text per gambar + checklist; validator lulus.
- Related: [stories-sequence](../prompts/stories/stories-sequence.md), [rule 05](../rules/05-PLATFORM-STANDARD.md), issue <https://github.com/d34faiza-commits/clau-content/issues/22>
- Completed: 2026-10-04
- Commit: 090d678

## TASK-023: Brief sanity check di WORKFLOW Step 1

- ID: TASK-023
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-01 pilot 2: ketidakcocokan strategi (villa 5 kamar vs target pasangan) tidak dicek sistem.
- Acceptance Criteria: WORKFLOW Step 1 punya tabel sanity check (kapasitas, harga, objective, positioning, nama brand, consent); template brief §9b; versi WORKFLOW naik; validator lulus.
- Related: [WORKFLOW](../WORKFLOW.md), [content-brief](../templates/content-brief.md), issue <https://github.com/d34faiza-commits/clau-content/issues/23>
- Completed: 2026-10-04
- Commit: 8a6c1f9

## TASK-024: check_caption tool + pengetatan self-check skill drafting

- ID: TASK-024
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-04, G-06, G-07 pilot 2: hook >125 lolos, klaim tersirat hanya ditandai, alt text 1 per post.
- Acceptance Criteria: `scripts/check_caption.py` (hook, panjang, hashtag, emoji, kata terlarang); exit criteria skill: klaim tersirat non-DATA FINAL = Fail; alt text per slide; validator lulus.
- Related: [check_caption.py](../scripts/check_caption.py), [draft-caption](../skills/draft-caption/SKILL.md), issue <https://github.com/d34faiza-commits/clau-content/issues/24>
- Completed: 2026-10-04
- Commit: 80098d3

## TASK-025: Schema v1.3: jam publish & CTA per channel

- ID: TASK-025
- Status: Done
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-08 pilot 2: schema tidak punya jam publish dan target CTA.
- Acceptance Criteria: Schema v1.3 punya `deadlines.publish_time` dan `channels[].cta` (target wajib untuk link/nomor); brief contoh valid; template & publication checklist selaras; validator lulus.
- Related: [schema](../schemas/content-brief.schema.json), issue <https://github.com/d34faiza-commits/clau-content/issues/25>
- Completed: 2026-10-04
- Commit: 34ce0c4, 43ef8c2

## TASK-026: Aturan review independen & self-review agent

- ID: TASK-026
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Temuan G-10 pilot 2: QA dijalankan oleh pembuat output yang sama.
- Acceptance Criteria: Rule 08 mewajibkan claim review independen untuk L2/L3; record QA punya kolom Independen?; AGENTS.md mengatur QA agent = self-review; validator lulus.
- Related: [rule 08](../rules/08-APPROVAL-PUBLICATION-STANDARD.md), [AGENTS.md](../AGENTS.md), issue <https://github.com/d34faiza-commits/clau-content/issues/26>
- Completed: 2026-10-04
- Commit: 2110c66

## TASK-027: Re-run pilot 2 setelah perbaikan

- ID: TASK-027
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Membuktikan perbaikan TASK-020–026 dengan menjalankan ulang pilot 2.
- Acceptance Criteria: `examples/pilot-2/v2.md` dengan sanity check, drafts v2, check_caption PASS, QA v2, approval SIMULASI; REPORT diperbarui dengan status temuan & skor v2.
- Related: [v2](../examples/pilot-2/v2.md), [REPORT](../examples/pilot-2/REPORT.md), issue <https://github.com/d34faiza-commits/clau-content/issues/27>
- Completed: 2026-10-04
- Commit: 1c377b9

## TASK-029: Split repo jadi clau-core, clau-market, clau-agent

- ID: TASK-029
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Memisahkan fondasi, Pilar 1, dan platform ke tiga repo private; repo ini jadi arsip.
- Acceptance Criteria: Tiga repo ter-push dan CI hijau; core sebagai submodule di marketing & agents; `scripts/split_repo.py` reproducible; README arsip menunjuk ke repo baru.
- Related: [split_repo.py](../scripts/split_repo.py), <https://github.com/d34faiza-commits/clau-core>, <https://github.com/d34faiza-commits/clau-market>, <https://github.com/d34faiza-commits/clau-agent>
- Completed: 2026-10-04
- Commit: c46c0b9, 4d1ae12 (arsip); core c23ec00, marketing f347e0a, agents e66a17a

## TASK-030: Rekomendasi review adversarial 2–6: proses QA

- ID: TASK-030
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Ekstraksi klaim per kalimat, re-check penuh per versi, cek field brief di QA, CTA check di check_caption.py, rubrik skor.
- Acceptance Criteria: check_caption menangkap R-01 (2 CTA) dan R-06 (CTA beda dari brief) pada draft lama; QA docs dan rubrik ada; CI hijau.
- Related: [scoring-rubric](https://github.com/d34faiza-commits/clau-market/blob/main/qa/scoring-rubric.md), [claim-verification](https://github.com/d34faiza-commits/clau-market/blob/main/qa/claim-verification.md), [check_caption.py](https://github.com/d34faiza-commits/clau-market/blob/main/scripts/check_caption.py)
- Completed: 2026-10-04
- Commit: clau-market f4bcdfd

## TASK-031: Pilot 2 v3 dengan proses QA baru (rekomendasi 7)

- ID: TASK-031
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Perbaiki R-01–R-08, jalankan QA baru penuh, skor dengan rubrik.
- Acceptance Criteria: v3.md berisi tabel ekstraksi kalimat semua konten, kecocokan brief, output check_caption aktual, self-score berbasis rubrik; temuan baru dicatat.
- Related: [v3](https://github.com/d34faiza-commits/clau-market/blob/main/examples/pilot-2/v3.md), [v3 brief](https://github.com/d34faiza-commits/clau-market/blob/main/examples/pilot-2/v3/brief.json)
- Completed: 2026-10-04
- Commit: clau-market e7e06e7

## TASK-001: Riset statistik pariwisata Indonesia

- ID: TASK-001
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Kumpulkan statistik pariwisata Indonesia (wisman, wisnus, okupansi, kontribusi ekonomi) sebagai context campaign. Draft sudah ada di research pack commit `0a43975`.
- Acceptance Criteria: Setiap angka punya label evidence, sumber, dan tanggal akses; angka yang dikutip dari media dicek ulang ke publikasi primer (BPS/Kemenpar) sebelum dipakai di konten; validator lulus.
- Related: [indonesia-tourism-stats-2025-2026.md](../knowledge/market/indonesia-tourism-stats-2025-2026.md), issue <https://github.com/d34faiza-commits/clau-content/issues/2>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-002: Bikin knowledge/segments/hotel.md

- ID: TASK-002
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Segment knowledge hotel & resort: audience, content pillars, claim hotspots, shot list, KPI, kesalahan umum. Dibuat di commit `622037c`.
- Acceptance Criteria: Owner setuju isi relevan untuk vertical Hotel/Resort; tidak ada klaim tanpa label; validator lulus.
- Related: [hotel.md](../knowledge/segments/hotel.md), issue <https://github.com/d34faiza-commits/clau-content/issues/3>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-003: Bikin knowledge/segments/villa.md

- ID: TASK-003
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Segment knowledge villa, guesthouse & homestay. Dibuat di commit `9d7b8f7`.
- Acceptance Criteria: Owner setuju isi relevan untuk vertical Villa/Guesthouse/Homestay; good-to-know & claim hotspots sesuai pengalaman lapangan; validator lulus.
- Related: [villa.md](../knowledge/segments/villa.md), issue <https://github.com/d34faiza-commits/clau-content/issues/4>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-004: Bikin knowledge/segments/restaurant.md

- ID: TASK-004
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Segment knowledge restaurant, cafe & beach club. Dibuat di commit `3c7e17c`.
- Acceptance Criteria: Owner setuju isi relevan; aturan halal/dietary & alkohol selaras dengan [regulasi 2026](../knowledge/regulasi/hospitality-content-2026.md); validator lulus.
- Related: [restaurant.md](../knowledge/segments/restaurant.md), issue <https://github.com/d34faiza-commits/clau-content/issues/5>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-005: Bikin knowledge/segments/spa.md

- ID: TASK-005
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Segment knowledge spa, wellness & retreat, termasuk daftar kata klaim medis yang dilarang. Dibuat di commit `3d6980f`.
- Acceptance Criteria: Owner setuju daftar kata terlarang/pengganti; tidak ada klaim medis; validator lulus.
- Related: [spa.md](../knowledge/segments/spa.md), issue <https://github.com/d34faiza-commits/clau-content/issues/6>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-006: Bikin knowledge/platforms/instagram.md

- ID: TASK-006
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Referensi platform Instagram. Dibuat di commit `da4635d`. Nilai spec masih ASSUMPTION — verifikasi dilacak di TASK-011.
- Acceptance Criteria: Owner setuju struktur & praktik konten; spec diverifikasi lewat TASK-011 atau tetap berlabel ASSUMPTION; validator lulus.
- Related: [instagram.md](../knowledge/platforms/instagram.md), issue <https://github.com/d34faiza-commits/clau-content/issues/7>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-007: Bikin knowledge/platforms/tiktok.md

- ID: TASK-007
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Referensi platform TikTok. Dibuat di commit `34aea21`. Spec durasi & panjang caption masih CLIENT CONFIRMATION — dilacak di TASK-011.
- Acceptance Criteria: Owner setuju angle konten & aturan musik akun bisnis; validator lulus.
- Related: [tiktok.md](../knowledge/platforms/tiktok.md), issue <https://github.com/d34faiza-commits/clau-content/issues/8>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-008: Bikin knowledge/calendar-id/national-holidays.md

- ID: TASK-008
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Pola kalender momen Indonesia (commit `bc9ea06`) plus tanggal SKB 2026 dari research pack (commit `0a43975`).
- Acceptance Criteria: Tanggal 2026 cocok dengan dokumen SKB resmi (nomor SKB + tanggal akses tercatat); pola umum tidak bertentangan dengan file 2026; validator lulus.
- Related: [national-holidays.md](../knowledge/calendar-id/national-holidays.md), [national-holidays-2026.md](../knowledge/calendar-id/national-holidays-2026.md), issue <https://github.com/d34faiza-commits/clau-content/issues/9>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-009: Bikin knowledge/voice-guides/hospitality-voice.md

- ID: TASK-009
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Default hospitality voice + 5 arketipe voice. Dibuat di commit `fa2c8f9`.
- Acceptance Criteria: Owner setuju arketipe & daftar klise; dipakai di minimal satu Voice Card saat pilot (TASK-012); validator lulus.
- Related: [hospitality-voice.md](../knowledge/voice-guides/hospitality-voice.md), issue <https://github.com/d34faiza-commits/clau-content/issues/10>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-013: Review knowledge/platforms/google-business.md & destinations

- ID: TASK-013
- Status: Done
- Priority: Normal
- Assignee: Dea Karisna
- Created: 2026-10-04
- Due: —
- Description: Dua file knowledge yang belum masuk daftar review TASK-002–009. Cek akurasi, relevansi untuk 3 vertical awal, dan selaraskan dengan research pack 2026.
- Acceptance Criteria: Tidak ada klaim tanpa label; fakta volatile punya sumber + tanggal akses atau ditandai cek ulang; validator lulus.
- Related: [google-business.md](../knowledge/platforms/google-business.md), [indonesia-overview.md](../knowledge/destinations/indonesia-overview.md), issue <https://github.com/d34faiza-commits/clau-content/issues/13>
- Completed: 2026-10-04
- Approval: owner (Dea Karisna / d34faiza) 2026-10-04, "untuk saat ini semua approve dulu"; tanpa revisi. Perubahan berikutnya hanya atas perintah Pak Indra atau Dea Karisna (d34faiza)

## TASK-033: Kartu persona + contoh + eval per agent

- ID: TASK-033
- Status: Done
- Priority: High
- Assignee: Dea Karisna
- Created: 2026-10-07
- Due: —
- Description: Agent harus menulis seperti staf ahli yang hangat sesuai keahliannya (bahasa, etika, gaya balasan), dengan suara brand client, tanpa mengaku manusia.
- Acceptance Criteria: 12 kartu persona (termasuk 3 agent planned); kasus uji per agent dengan contoh bagus & buruk; runner yang membuktikan contoh buruk tertangkap; rubrik penilaian manusia; registry terhubung; test CI lulus; skill yang lemah soal voice terhubung ke voice guide & persona.
- Related: <https://github.com/d34faiza-commits/clau-agent/tree/main/agents/personas>, <https://github.com/d34faiza-commits/clau-agent/tree/main/agents/evals>, issue <https://github.com/d34faiza-commits/clau-content/issues/30>
- Completed: 2026-10-07
- Commit: clau-agent 0eafa3a, clau-market bddf9f4

## TASK-034: Keputusan owner — scope, nama, urutan pilar 2–5 & nama produk

- ID: TASK-034
- Status: Done
- Priority: High
- Assignee: Pak Indra / Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: `5-pillar-architecture.md` di core masih Draft: pilar 2–5 berstatus ASSUMPTION menunggu CLIENT CONFIRMATION soal nama, urutan, scope, dan nama repo (`clau-ai-sales`, `clau-ai-guest`, `clau-ai-operations`, `clau-ai-analytics` = usulan). Sekalian putuskan nama produk: tetap "CLAU AI Content Studio" untuk semua pilar (opsi A) atau merek payung "CLAU AI" dengan "Content Studio" sebagai modul Pilar 1 (opsi B). Sertakan keputusan **konsep v2** (AI Marketing, AI Sales, AI Admin, AI Business Intelligence, AI Automation; cetak biru di `clau-core/docs/blueprints/`): dipakai sebagai nama 5 pilar atau tidak. Langkah ini membuka TASK-035–042.
- Acceptance Criteria: Keputusan tercatat di Revision History AI-CONSTITUTION; `5-pillar-architecture.md` tidak lagi bertanda ASSUMPTION untuk item yang diputuskan; tabel pilar di core README, `registry.json` → `pillars`, dan `design/pillars.md` § Nama Produk sudah sama; test registry clau-agent dan validator core lulus.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/5-pillar-architecture.md>, [design/pillars.md](../design/pillars.md), <https://github.com/d34faiza-commits/clau-agent/blob/main/agents/registry.json>, issue <https://github.com/d34faiza-commits/clau-content/issues/35>
- Note 2026-10-09: **Diputuskan owner** (Dea Karisna / d34faiza): AI-CONSTITUTION v3.0.0 Approved — 5 pilar v2, otonomi A/B/C default B, vertical fokus villa, restoran/cafe, wedding, travel. Diterapkan di core (tabel pilar, router, 5-pillar-architecture) dan registry agents; menunggu merge core#5 + agents#16 + marketing#15 (d34faiza-commits). Nama produk belum diputuskan → dipisah ke TASK-043.
- Completed: 2026-10-09
- Commit: clau-core 25e59ea (merge #5), clau-agent 9ca8d3d (merge #16)

## TASK-040: Keputusan amandemen otonomi bertingkat & perluasan scope vertical

- ID: TASK-040
- Status: Done
- Priority: Normal
- Assignee: Pak Indra / Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: AI Sales (WhatsApp assistant) dan AI Automation butuh AI mengirim ke customer, sedangkan AI-CONSTITUTION §4.7 (Approved) melarangnya; §2 juga membatasi scope ke hospitality. Draf amandemen (Level A otomatis / B draft / C eskalasi + perluasan vertical) sudah disiapkan di `clau-core/docs/proposals/autonomy-levels.md` dan **belum berlaku**.
- Acceptance Criteria: Owner memutuskan terima/ubah/tolak; bila diterima: AI-CONSTITUTION naik versi dengan Revision History, kolom Otonomi di `router.md`, `autonomy_max` di `registry.json` + test, validator core & test agents lulus.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/docs/proposals/autonomy-levels.md>, <https://github.com/d34faiza-commits/clau-core/blob/main/AI-CONSTITUTION.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/42>
- Note 2026-10-09: Usulan 1 (otonomi bertingkat) **Approved** di AI-CONSTITUTION v3.0.0 §4.7 + §4a; kolom Otonomi router + `autonomy_max` registry + test sudah dibuat, menunggu merge core#5 + agents#16 + marketing#15 (d34faiza-commits). Usulan 2 (scope di luar hospitality) **tidak** diputuskan; tetap usulan, dilacak di TASK-041.
- Completed: 2026-10-09
- Commit: clau-core 25e59ea (merge #5), clau-agent 9ca8d3d (merge #16)

## TASK-043: Keputusan nama produk untuk 5 pilar

- ID: TASK-043
- Status: Done
- Priority: Low
- Assignee: Pak Indra / Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: Dipisah dari TASK-034. AI-CONSTITUTION v3.0.0 menetapkan 5 pilar v2 tetapi tidak memutuskan nama produk. Opsi A: tetap "CLAU AI Content Studio" untuk semua pilar. Opsi B: merek payung "CLAU AI", "Content Studio" = modul AI Marketing. Detail: [design/pillars.md § Nama Produk](../design/pillars.md#nama-produk).
- Acceptance Criteria: Keputusan tercatat; bila B: string i18n `app.name` + brand guideline diperbarui; validator lulus.
- Related: [design/pillars.md](../design/pillars.md), [design/brand/brand-guideline.md](../design/brand/brand-guideline.md), issue <https://github.com/d34faiza-commits/clau-content/issues/46>
- Note 2026-10-09: **Diputuskan opsi B** oleh owner Dea Karisna (d34faiza) atas rekomendasi agent ("gas kak.. kasih aku yg terbaik. aku percaya kaka"): merek payung **CLAU AI**, "Content Studio" = modul AI Marketing. Diterapkan di design/ (brand guideline, README, pillars.md, Figma/prototype guide, wireframe, tokens) dan frontend clau-agent (logo, judul, Pengaturan); menunggu merge PR.
- Completed: 2026-10-09
- Commit: clau-content #51, clau-agent #17 (merge 2026-10-09)

## TASK-044: Selaraskan WORKFLOW.md core dengan 5 pilar v2

- ID: TASK-044
- Status: Done
- Priority: Low
- Assignee: Dea Karisna
- Created: 2026-10-09
- Due: —
- Description: `clau-core/WORKFLOW.md` (Approved v1.0.0) masih menyebut "1 Marketing & Content" di tabel workflow pilar. Persetujuan v3.0.0 hanya mencakup AI-CONSTITUTION, jadi WORKFLOW.md tidak diubah tanpa perintah owner.
- Acceptance Criteria: Owner memerintahkan perubahan; WORKFLOW.md naik versi PATCH dengan Revision History; README core Versi Dokumen sama; validator core lulus.
- Related: <https://github.com/d34faiza-commits/clau-core/blob/main/WORKFLOW.md>, issue <https://github.com/d34faiza-commits/clau-content/issues/47>
- Note 2026-10-09: Diperintahkan owner Dea Karisna (d34faiza) atas rekomendasi agent. WORKFLOW.md v1.0.1 (PATCH) di clau-core#6; menunggu merge.
- Completed: 2026-10-09
- Commit: clau-core #6 (merge 2026-10-09)

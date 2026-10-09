# ROADMAP — UI/UX CLAU AI

> **ID:** Roadmap dari spesifikasi sampai handoff ke development. Total ± **4 minggu kalender** (± 18 hari kerja) bila satu desainer bekerja penuh. Tanggal di bawah adalah **usulan**, mulai Senin 12 Okt 2026; geser bila mulai lebih lambat.
> **EN:** Roadmap from spec to developer handoff, ~4 calendar weeks for one full-time designer. Dates are proposals.

```text
 Okt 2026          Minggu 1        Minggu 2        Minggu 3        Minggu 4
                   12–16           19–23           26–30           2–6 Nov
 F1 Spec        ✅ (selesai)
 F2 Figma          █████
 F3 Prototype                     ███
 F4 User test           ░░(rekrut)   ░░█████ (wawancara paralel sejak minggu 1)
 F5 Iterate                                        ███
 F6 Handoff                                           █
```

## Fase 1 — Spec ✅ Selesai

| Deliverable | Lokasi |
|---|---|
| Wireframe, mockup spec, user flow (Portal & Studio) | `wireframes/`, `mockups/`, `user-flow/` |
| Design system (warna, tipografi, spacing, ikon, 22 komponen) | `design-system/` |
| Design tokens + generator + cek contrast | `tokens/` |
| Brand guideline + 3 konsep logo | `brand/` |
| Rencana riset (wawancara, survey, rekrutmen) | `research/` |
| Panduan Figma, daftar komponen, panduan developer, QA checklist | `figma/`, `handoff/` |

**Exit criteria:** ✅ semua dokumen ada di `main`; ✅ token lulus contrast AA (46 pasangan).

## Fase 2 — Figma (1 minggu · 12–16 Okt)

| Hari | Kerja | Output |
|---|---|---|
| 1 | Setup file, import token (Variables Light/Dark), text & effect styles | Foundations page |
| 2–3 | Component library: 22 + 5 komponen CLAU | Components page |
| 4 | Portal mobile (8 layar) + desktop (7) | Layar Portal |
| 5 | Studio desktop (8) + mobile (5); state kosong/loading/error; 3 layar EN & 3 Dark | Layar Studio |

Paralel: **mulai rekrutmen** responden (lihat [recruitment.md](./research/recruitment.md)) dan sebar survey.

**Exit criteria:** checklist di [figma-guide](./figma/figma-guide.md) terpenuhi · review Pak Indra (link + 3 pertanyaan keputusan) · link dicatat di [prototype-link.md](./figma/prototype-link.md).

## Fase 3 — Prototype (3 hari · 19–21 Okt)

| Hari | Kerja |
|---|---|
| 1 | Flow F1 Approve (prioritas): Notifikasi → Detail → Konfirmasi fakta → Setujui → Sukses, termasuk error |
| 2 | F2–F5 Portal + S1 Pipeline Studio |
| 3 | Tes internal di HP Android 360 px; perbaiki link rusak; siapkan task Maze |

**Exit criteria:** semua flow bisa diselesaikan tanpa jalan buntu; dites di HP sungguhan.

## Fase 4 — User Test (1 minggu · 22–28 Okt, termasuk akhir pekan bila responden hanya bisa saat itu)

| Kerja | Detail |
|---|---|
| Wawancara | 5 responden ([interview-guide](./research/interview-guide.md)); bisa dimulai sejak Fase 2 |
| Usability test | 5 responden (kuota di [recruitment.md](./research/recruitment.md)), task T1–T5 di [prototype-guide](./prototype/prototype-guide.md) |
| Survey | ≥ 30 respons, ≥ 3 wilayah di luar Bali ([survey](./research/survey.md)) |
| Sintesis | Affinity map; asumsi R1–R6: terbukti/dibantah; update persona & journey |

**Exit criteria:** laporan temuan dengan severity; persona & journey diperbarui dari ASSUMPTION menjadi temuan.

## Fase 5 — Iterate (3 hari · 29 Okt – 2 Nov)

| Hari | Kerja |
|---|---|
| 1 | Prioritaskan temuan (severity × frekuensi); putuskan bersama owner |
| 2 | Revisi komponen di library + layar; update dokumen spec |
| 3 | Tes ulang singkat (3–5 orang baru, task sama) untuk temuan *Tinggi* |

**Exit criteria:** T1–T5 ≥ 80% berhasil, SEQ ≥ 4/5; tidak ada temuan severity Tinggi yang terbuka.

## Fase 6 — Handoff (1 hari · 3 Nov)

| Kerja | Detail |
|---|---|
| Finalisasi | Frame ditandai *Ready for dev*; token final di repo; versi Figma diberi nama `v1.0 — Handoff` |
| Walkthrough | Sesi 60 menit dengan developer: token, komponen, flow, aturan server ([developer-guide](./handoff/developer-guide.md)) |
| Backlog | Pecah per halaman → issue/task dengan link frame + spec + item [qa-checklist](./handoff/qa-checklist.md) |

**Exit criteria:** developer bisa mulai tanpa pertanyaan blocker; semua link Figma aktif.

## Setelah Handoff (di luar roadmap ini)

| Tahap | Perkiraan | Catatan |
|---|---|---|
| Implementasi Portal (MVP: login, beranda, konten + approval, konfirmasi fakta, notifikasi) | 3–4 minggu | Prioritas tertinggi |
| Implementasi Studio (MVP: klien, pipeline, tandai tayang) | 3–4 minggu | |
| Laporan + PDF, kalender, AI agent monitor | 2–3 minggu | |
| Pilot dengan 1–2 client | 2 minggu | Data nyata hanya di environment produksi, tidak di repo |

## Risiko / Risks

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Rekrut responden lambat | Fase 4 mundur | Mulai rekrut di Fase 2; siapkan cadangan |
| Desainer paruh waktu | Semua fase ×2 | Prioritaskan Portal mobile + F1; Studio bisa menyusul |
| Keputusan nama/logo belum ada | Brand di Figma memakai placeholder | Pakai logotype teks "CLAU" sementara; logo final tidak memblokir prototype |
| Hasil test bertentangan dengan spec | Revisi besar | Wajar; itu tujuan testing. Jadwalkan Fase 5 tanpa dipangkas |

## Status

| Fase | Status | Update terakhir |
|---|---|---|
| 1 Spec | ✅ Selesai | 2026-10-06 |
| 2 Figma | ⬜ Belum mulai | — |
| 3 Prototype | ⬜ | — |
| 4 User test | ⬜ | — |
| 5 Iterate | ⬜ | — |
| 6 Handoff | ⬜ | — |

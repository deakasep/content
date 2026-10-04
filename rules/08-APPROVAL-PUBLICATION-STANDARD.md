# 08 — Approval & Publication Standard

## Purpose

Memastikan tidak ada konten yang dipublish, dijadwalkan, atau di-boost tanpa approval tertulis dari pihak berwenang, dan setiap publikasi tercatat.

## Scope

Berlaku untuk semua konten dan semua channel, termasuk balasan review publik, iklan berbayar, update listing OTA, GBP post, dan WhatsApp broadcast.

Klasifikasi wajib: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**.

## Mandatory Rules

- Setiap client menetapkan **approver** (nama peran + kontak di workspace client) saat onboarding. Tanpa approver, tidak ada publish.
- Approval harus **tertulis** dan dapat ditelusuri (email, komentar di tools approval, pesan yang diarsipkan di sistem client).
- Approval mencakup versi spesifik: teks, visual, channel, tanggal/jam publish, budget ads (bila ada).
- Perubahan setelah approval → approval ulang untuk bagian yang berubah.
- AI/automation tidak boleh: publish, schedule, boost, atau membalas publik tanpa approval.
- Creator tidak boleh self-approve konten yang memuat: klaim sensitif, harga/promo, data/foto orang, konten berbayar, atau topik sensitif.
- **Review independen:** untuk konten L2/L3, [claim verification](../qa/claim-verification.md) dijalankan oleh pihak yang **bukan** pembuat draft. Kalau draft dibuat AI, review oleh manusia (content lead/owner) dihitung independen. AI yang me-review output AI-nya sendiri, atau creator yang me-review drafnya sendiri, dicatat sebagai **self-review** dan tidak memenuhi syarat ini.
- Setiap record QA mencatat kolom **Independen? (Ya / Tidak — self-review)**. Self-review boleh dipakai sebagai pre-check, tapi tidak cukup untuk approval L2/L3.
- Level approval:

| Level | Jenis konten | Approver minimum |
|---|---|---|
| L1 | Konten rutin tanpa klaim baru (mood, behind-the-scenes tanpa orang) | Content lead + client approver (boleh batch per minggu) |
| L2 | Promo, harga, klaim fasilitas, konten dengan orang, listing OTA | Client approver per konten |
| L3 | Ads berbayar, kolaborasi influencer, balasan review negatif, konten krisis, topik agama/budaya | Owner/GM client per konten |

- Balasan review positif rutin boleh memakai template yang sudah di-approve (L1); review negatif = L3.
- Publikasi dicatat: URL, waktu, versi, publisher.

## Required Inputs

- Approval matrix dari onboarding.
- Draft final + tabel klaim + hasil QA.
- Approval record ([templates/approval-record.md](../templates/approval-record.md)).

## Workflow

1. Tentukan level approval konten.
2. Kirim paket approval: draft final, visual, channel, jadwal, tabel klaim, open items.
3. Terima approval tertulis atau revisi.
4. Revisi → kembali ke QA terkait → approval ulang.
5. Jalankan [qa/publication-checklist.md](../qa/publication-checklist.md).
6. Publish oleh publisher berwenang.
7. Catat publikasi dan simpan bukti di workspace client.

## Deliverables

- Approval record terisi (di workspace client).
- Log publikasi.

## Validation/QC Checklist

- [ ] Level approval benar.
- [ ] Approval tertulis untuk versi final.
- [ ] Tidak ada perubahan setelah approval tanpa approval ulang.
- [ ] Publication checklist lulus.
- [ ] Log publikasi tercatat.

## Risks & Mitigation

| RISK | Mitigation |
|---|---|
| Konten salah publish | Checklist + approval versi spesifik |
| Approval lisan dibantah client | Approval tertulis wajib |
| Scheduler publish draft lama | Cek versi di scheduler sebelum jadwal |
| Balasan review emosional | Review negatif = L3 |

## Escalation Conditions

- Approver tidak responsif mendekati deadline → jangan publish; laporkan.
- Client meminta publish langsung tanpa paket approval untuk konten L2/L3.
- Konten sudah publish ternyata salah → koreksi/unpublish sesuai otoritas dan catat insiden.

## References

- [WORKFLOW.md](../WORKFLOW.md)
- [templates/approval-record.md](../templates/approval-record.md)
- [qa/publication-checklist.md](../qa/publication-checklist.md)

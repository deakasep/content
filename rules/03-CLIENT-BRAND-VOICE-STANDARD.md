# 03 — Client Brand Voice Standard

## Purpose

Memastikan konten yang ditulis AI terdengar seperti **brand client**, bukan seperti AI generik atau seperti brand lain. Brand voice dan brand asset adalah milik client.

## Scope

Berlaku untuk semua konten yang dipublikasikan atas nama client: caption, bio, listing, balasan review, email, WhatsApp broadcast, script video, dan materi cetak.

Klasifikasi wajib: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**.

## Mandatory Rules

- Setiap client wajib punya **Voice Card** (diisi saat onboarding) sebelum produksi rutin. Tanpa Voice Card, voice berstatus **CLIENT CONFIRMATION** dan pakai default di [hospitality-voice.md](../knowledge/voice-guides/hospitality-voice.md).
- Voice Card minimum: 3 kata sifat brand, 3 "kami bukan…", sapaan ke tamu, bahasa utama, aturan emoji, kata wajib/terlarang, contoh konten yang disukai.
- Ringkasan Voice Card wajib dibawa ke setiap brief lewat field `voice` ([schema](../schemas/content-brief.schema.json) v1.1) supaya skill dan reviewer memakai voice yang sama.
- Logo, warna, font, dan template visual client tidak boleh diubah, di-recolor, di-stretch, atau dibuat ulang oleh AI.
- Nama properti/outlet ditulis persis sesuai brand guide (kapitalisasi, spasi, aksen).
- Jangan meniru voice brand lain atau kompetitor.
- Konsistensi lintas channel: voice sama, format menyesuaikan platform.
- Balasan review tetap memakai voice brand, tapi lebih formal bila review negatif.
- AI generik smell dihapus: hindari frasa klise ("nestled in", "a hidden gem", "unforgettable experience", "surga tersembunyi", "pengalaman tak terlupakan") kecuali Voice Card mengizinkan.

## Required Inputs

- Brand guide client (bila ada) — disimpan di workspace client.
- Voice Card dari [templates/client-onboarding.md](../templates/client-onboarding.md).
- 3–5 contoh konten lama yang disetujui client sebagai acuan.
- Daftar kata wajib/terlarang.

## Workflow

1. Cek apakah Voice Card ada dan disetujui.
2. Bila belum, pakai default voice + tandai **CLIENT CONFIRMATION**.
3. Draft dengan Voice Card sebagai constraint.
4. Self-check: bandingkan draft dengan contoh konten acuan.
5. Hapus klise AI dan kata terlarang.
6. Cek nama brand, hashtag brand, dan handle akun.

## Deliverables

- Draft sesuai voice.
- Catatan deviasi bila ada (mis. konten krisis memakai tone lebih formal).

## Validation/QC Checklist

- [ ] Voice Card ada atau status **CLIENT CONFIRMATION** dicatat.
- [ ] Kata sifat brand tercermin di draft.
- [ ] Tidak ada kata terlarang dan klise AI.
- [ ] Nama brand/outlet ditulis benar.
- [ ] Logo/asset visual tidak diubah.
- [ ] Sapaan & emoji sesuai Voice Card.

## Risks & Mitigation

| RISK | Mitigation |
|---|---|
| Konten terdengar generik/AI → engagement rendah | Voice Card + contoh acuan + daftar klise |
| Logo diubah AI → brand rusak | Asset visual hanya dari media library client |
| Voice tidak konsisten antar admin/agent | Voice Card sebagai single source; review berkala |

## Escalation Conditions

- Client belum punya brand guide dan menolak mengisi Voice Card.
- Permintaan meniru brand lain.
- Permintaan mengubah logo/identitas visual.

## References

- [knowledge/voice-guides/hospitality-voice.md](../knowledge/voice-guides/hospitality-voice.md)
- [templates/client-onboarding.md](../templates/client-onboarding.md)
- [qa/content-review.md](../qa/content-review.md)

# Reel / Short Video Script

## Purpose

Menyusun script video pendek vertikal (Instagram Reels, TikTok) untuk bisnis hospitality: hook, shot list per detik, on-screen text, audio, caption, dan status consent per shot, tanpa klaim yang belum terbukti.

## When to Use

- Room/villa reveal, "a morning at…", proses (masak, treatment, persiapan), arrival, neighbourhood.
- Vertical: villa, hotel, restaurant/cafe/beach club, spa/wellness.

**Jangan dipakai untuk:** iklan berbayar dengan talent (butuh brief kolaborasi & approval L3), atau video yang menampilkan upacara/tempat suci tanpa izin.

## Required Inputs

| Input | Contoh fiktif | Status minimum |
|---|---|---|
| Brief (`voice`, `claims`, `assets`, `restrictions`) | [pilot-2 brief](../../examples/pilot-2/brief.json) | Valid schema |
| Fact sheet properti | [template](../../templates/property-fact-sheet.md) | **DATA FINAL** per baris yang dipakai |
| Daftar aset video + status orang/consent | VCSU-VIDEO-001: pasangan, consent belum ada | Per aset |
| Durasi target & platform | ±20–30 detik, IG Reels | **CLIENT CONFIRMATION** bila spec platform belum terverifikasi |
| Bahasa on-screen text | ID / EN / bilingual | **DATA FINAL** |

## Optional Inputs

- Referensi gaya (link konten client sebelumnya yang disetujui).
- Musik/audio yang sudah dipilih client (status lisensi).

## Prompt

```text
Kamu adalah short-form video scriptwriter untuk hospitality di Indonesia.

KONTEKS
- Brand: [NAMA_BRAND] ([VERTICAL], [LOKASI_UMUM])
- Voice: [ARKETIPE] | sapaan: [SAPAAN] | emoji: [ATURAN]
- Objective: [OBJECTIVE] | CTA: [SATU CTA]
- Platform & durasi: [IG Reels/TikTok], ±[N] detik, 9:16
- Bahasa on-screen: [ID/EN/bilingual]

FAKTA YANG BOLEH DITAMPILKAN (DATA FINAL saja)
- [FAKTA + SUMBER]

ASET
- [ASSET_REF] — [isi] — orang: [none / identifiable-with-consent / identifiable-pending-consent]

TERLARANG
- Kata: [restrictions.forbidden_terms]
- Klaim yang ditahan: [klaim FIELD VERIFICATION / ASSUMPTION]

ATURAN
- Ikuti rules 01, 02 (termasuk kata positioning & nama brand), 04, 05, 07.
- Hook 0–3 detik: visual spesifik + on-screen text ≤ 6 kata.
- Setiap shot yang menampilkan fakta = klaim; harus ada di daftar DATA FINAL.
- Shot tidak boleh memperkuat klaim tersirat (mis. footage sunset untuk nama "Sunset" tanpa bukti; lensa ultra-wide yang membesarkan ruang/kolam).
- Orang yang dapat dikenali tanpa consent → jangan dipakai; tulis shot pengganti.
- Tanpa voice-over AI yang meniru orang nyata. Musik: library komersial akun bisnis atau berlisensi.
- On-screen text wajib (ditonton tanpa suara). Satu CTA di akhir.

TUGAS
1. Tulis 2 opsi hook (visual + teks).
2. Tabel shot: detik | shot | aset | on-screen text | klaim (label) | orang/consent | catatan teknis.
3. Caption reel (hook ≤125 karakter, 1 CTA, 3–8 hashtag).
4. Daftar "yang sengaja tidak ditampilkan" + alasan.

OUTPUT
- Opsi hook, tabel shot, caption (code block), daftar dikecualikan, tabel klaim, data gap & NEXT ACTION.
```

## Expected Output

- 2 opsi hook + 1 shot list lengkap.
- Caption reel siap copy-paste.
- Tabel klaim per shot dan status consent per aset.

## Related Standards

- [02 Hospitality Claim](../../rules/02-HOSPITALITY-CLAIM-STANDARD.md)
- [04 Privacy, Consent & UGC](../../rules/04-PRIVACY-CONSENT-UGC-STANDARD.md)
- [05 Platform](../../rules/05-PLATFORM-STANDARD.md)
- [07 AI Visual & Disclosure](../../rules/07-AI-VISUAL-DISCLOSURE-STANDARD.md)
- [content-trends-hospitality-2026](../../knowledge/platforms/content-trends-hospitality-2026.md)
- Skill: [draft-reel-script](../../skills/draft-reel-script/SKILL.md)

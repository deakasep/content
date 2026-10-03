# 07 — AI Visual & Disclosure Standard

## Purpose

Mengatur penggunaan gambar, video, dan audio hasil AI (atau editing berat) supaya tidak menyesatkan calon tamu tentang kondisi nyata properti, makanan, treatment, atau pengalaman.

## Scope

Berlaku untuk: text-to-image, image-to-image, AI video, AI voice-over, AI avatar, background replacement, sky replacement, object removal/addition, dan retouch berat pada foto properti/makanan/orang.

Klasifikasi wajib: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**.

## Mandatory Rules

### Kategori visual

| Kategori | Contoh | Boleh di konten? | Syarat |
|---|---|---|---|
| **A — Foto asli** | Foto properti/makanan asli, koreksi warna & exposure ringan | Ya | Hak foto jelas |
| **B — Edit ringan** | Crop, straighten, hapus debu/kabel kecil, color grading | Ya | Tidak mengubah fakta fisik |
| **C — Edit material** | Ganti langit, tambah/hapus objek, perluas kolam, hapus bangunan tetangga | Terbatas | Tidak boleh untuk listing/OTA; wajib disclosure bila dipakai di konten mood |
| **D — AI generated / ilustratif** | Moodboard, ilustrasi konsep, background abstrak, ilustrasi menu baru | Terbatas | Wajib label; tidak boleh menggambarkan properti/menu nyata seolah foto asli |

### Aturan inti

- Foto untuk **OTA listing, GBP, website room page, dan menu** wajib kategori A atau B.
- Visual kategori D tidak boleh menampilkan: kamar, kolam, view, pantai, restoran, makanan, atau treatment room milik client seolah nyata.
- Visual kategori C/D di konten sosial wajib disclosure (label platform "AI info"/"AI-generated" bila tersedia, dan/atau teks "Ilustrasi AI").
- Dilarang membuat AI image orang nyata (tamu, staf, influencer, tokoh publik) tanpa consent tertulis.
- Dilarang AI voice-over yang meniru suara orang nyata tanpa consent.
- AI avatar/presenter wajib diungkapkan sebagai AI.
- Dilarang membuat visual budaya/agama yang salah atau merendahkan (pakaian adat keliru, pura fiktif dengan atribut sakral).
- Logo client di visual AI wajib ditempel dari file master, bukan digenerate AI.
- Simpan metadata internal: tool, prompt ringkas, tanggal, kategori — di workspace client.

## Required Inputs

- Tujuan visual (listing / sosial / iklan / moodboard internal).
- Asset asli dari media library client.
- Logo master client.
- Consent untuk orang yang muncul (bila ada).

## Workflow

1. Tentukan tujuan & channel visual.
2. Tentukan kategori (A–D) yang diizinkan untuk channel tersebut.
3. Produksi/edit visual.
4. Review dengan [qa/visual-ai-review.md](../qa/visual-ai-review.md): artefak AI, teks rusak, tangan/wajah aneh, logo terdistorsi, detail budaya keliru.
5. Pasang label/disclosure untuk kategori C/D.
6. Catat metadata internal.

## Deliverables

- File visual dengan nama yang menyertakan kategori, mis. `villa-contoh_ig-feed_D-ai-illustration_v1.png`.
- Catatan disclosure dan metadata internal.

## Validation/QC Checklist

- [ ] Kategori visual sesuai channel.
- [ ] Listing/menu/website hanya kategori A/B.
- [ ] Tidak ada fasilitas/makanan fiktif yang tampil seolah nyata.
- [ ] Label AI terpasang untuk kategori C/D.
- [ ] Tidak ada orang nyata yang digenerate tanpa consent.
- [ ] Logo dari file master, tidak terdistorsi.
- [ ] Tidak ada artefak AI (teks rusak, jari aneh, objek melayang).
- [ ] Detail budaya/agama benar.

## Risks & Mitigation

| RISK | Mitigation |
|---|---|
| Tamu merasa ditipu karena properti berbeda dari foto | Listing hanya A/B; C/D diberi label |
| Deepfake orang nyata → masalah hukum | Larangan tanpa consent |
| Artefak AI → brand terlihat murahan | Visual QA wajib |
| Kebijakan platform tentang label AI berubah | Cek kebijakan berkala; default selalu label |

## Escalation Conditions

- Client meminta visual AI untuk listing/OTA.
- Client meminta foto "dipercantik" sampai mengubah fakta (kolam diperluas, bangunan tetangga dihapus untuk klaim view).
- Permintaan meniru wajah/suara orang nyata.

## References

- [01 Content Integrity](./01-CONTENT-INTEGRITY-STANDARD.md)
- [04 Privacy, Consent & UGC](./04-PRIVACY-CONSENT-UGC-STANDARD.md)
- [qa/visual-ai-review.md](../qa/visual-ai-review.md)
- Kebijakan label konten AI masing-masing platform (wajib dicek tanggal akses)

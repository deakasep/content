# 04 — Privacy, Consent & UGC Standard

## Purpose

Melindungi privacy tamu, staf, talent, dan pemilik konten UGC (user-generated content) saat konten hospitality diproduksi dengan AI.

## Scope

Berlaku bila konten memuat atau memakai: wajah/tubuh orang yang dapat dikenali, nama, review, testimoni, foto/video tamu, repost dari akun lain, data dari DM/WhatsApp, atau data booking.

Klasifikasi wajib: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**.

## Mandatory Rules

### Consent

- Orang yang dapat dikenali (tamu, staf, talent, anak) hanya boleh tampil bila ada consent tercatat di consent register client.
- Consent minimum mencatat: siapa, untuk konten/asset apa, channel apa, periode, tanggal, cara consent diberikan, dan cara menarik consent.
- **Anak-anak:** wajib consent orang tua/wali; default hindari wajah anak yang jelas.
- Consent bisa ditarik — konten terkait wajib diturunkan atau diedit dalam waktu wajar.
- Staf juga butuh consent; hubungan kerja tidak otomatis berarti consent untuk marketing.

### UGC & repost

- Repost/regram hanya dengan izin pemilik akun (komentar/DM persetujuan yang diarsipkan di sistem client).
- Credit sesuai permintaan pemilik (handle, nama).
- Tidak boleh crop watermark atau mengubah makna konten UGC.
- Tag/mention tamu hanya bila tamu sendiri menandai properti atau setuju.

### Review & testimoni

- Kutipan review boleh dipakai bila review publik, makna tidak diubah, dan identitas disamarkan (inisial / "tamu dari Jakarta") kecuali tamu setuju disebut.
- Jangan memakai review privat, email, atau chat sebagai testimoni tanpa izin eksplisit.
- Jangan memberi insentif untuk review positif tanpa mengikuti kebijakan platform.

### Data pribadi

- AI tidak boleh menerima atau memproses data pribadi lebih dari yang diperlukan. Samarkan sebelum input ke AI tool: `<NAMA_TAMU>`, `<NO_BOOKING>`.
- Jangan mengungkap di konten/balasan publik: nomor kamar, tanggal menginap, nomor booking, nomor HP, email, kebangsaan spesifik bila tidak relevan, kondisi kesehatan.
- Balasan review tidak boleh mengonfirmasi detail menginap tamu ("terima kasih sudah menginap 3 malam di kamar 204").
- Data dari DM/WhatsApp tidak dipakai untuk konten tanpa izin.

## Required Inputs

- Consent register client (akses baca untuk approver; tidak disalin ke repo).
- Bukti izin repost UGC.
- Asset media dari media library client.

## Workflow

1. Identifikasi semua orang yang dapat dikenali dan semua data pribadi di asset/draft.
2. Cek consent register untuk setiap orang.
3. Tidak ada consent → ganti asset, blur, crop, atau minta consent (**NEXT ACTION**).
4. UGC → cek bukti izin + format credit.
5. Samarkan data pribadi di draft dan di input ke AI.
6. Catat hasil di [qa/privacy-rights-review.md](../qa/privacy-rights-review.md).

## Deliverables

- Asset & draft yang bebas data pribadi tanpa consent.
- Catatan consent reference (ID register, bukan isi data pribadi).

## Validation/QC Checklist

- [ ] Semua orang yang dapat dikenali punya consent tercatat.
- [ ] Anak-anak: consent wali ada atau wajah tidak terlihat jelas.
- [ ] UGC: izin & credit tercatat.
- [ ] Kutipan review tidak mengubah makna dan identitas disamarkan.
- [ ] Tidak ada nomor kamar/booking/tanggal menginap/kontak di konten publik.
- [ ] Input ke AI tool sudah disamarkan.

## Risks & Mitigation

| RISK | Mitigation |
|---|---|
| Pelanggaran perlindungan data pribadi | Minimum data, samarkan, consent register |
| Tamu keberatan wajahnya dipakai → komplain publik | Consent tertulis sebelum publish |
| Repost UGC tanpa izin → klaim hak cipta | Izin tercatat + credit |
| Balasan review membuka detail menginap | Template balasan tanpa detail booking |

## Escalation Conditions

- Asset penting tidak punya consent dan deadline mepet.
- Tamu meminta konten diturunkan.
- Review berisi data pribadi pihak ketiga atau tuduhan serius.
- Permintaan memakai data tamu untuk targeting/ads.

## References

- UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (rujukan umum; kewajiban spesifik wajib legal review)
- [01 Content Integrity](./01-CONTENT-INTEGRITY-STANDARD.md)
- [CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md)
- [qa/privacy-rights-review.md](../qa/privacy-rights-review.md)

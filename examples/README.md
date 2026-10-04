# Examples

Contoh dan pilot memakai **properti fiktif**, sesuai [CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md) (konten yang diizinkan, poin 5).

## Aturan

- Nama properti selalu mengandung kata **"Contoh"** (mis. "Villa Contoh Ubud", "Kafe Contoh Canggu").
- Tidak ada data client nyata, foto asli, nama tamu, harga kontrak, atau credential.
- Approval di contoh selalu ditandai **SIMULASI**.
- Setiap `brief.json` di folder ini divalidasi terhadap [schema](../schemas/content-brief.schema.json) oleh `python scripts/validate.py`.

## Index

| Folder | Isi | Task |
|---|---|---|
| [pilot-villa-contoh-ubud/](./pilot-villa-contoh-ubud/README.md) | Pilot WORKFLOW end-to-end: villa, IG carousel + Booking.com | TASK-012 |

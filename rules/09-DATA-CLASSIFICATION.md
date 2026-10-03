# 09 — Data Classification

## Purpose

Menetapkan klasifikasi data empat axis untuk semua data client, konten, dan asset di CLAU-AI-CONTENT, sehingga jelas apa yang boleh dipakai, disimpan di mana, dan boleh dipublish atau tidak.

## Scope

Berlaku untuk seluruh data yang diterima dari client, dihasilkan AI, atau dipublikasikan: brief, fact sheet, harga, asset media, review, consent, analytics, dan konten draft/final.

Klasifikasi wajib: **DATA FINAL**, **ASSUMPTION**, **CLIENT CONFIRMATION**, **FIELD VERIFICATION**, **RISK**, **NEXT ACTION**.

## Mandatory Rules

Setiap item data diklasifikasikan di **4 axis**. Bila beberapa kontrol berlaku, pakai yang **paling ketat**.

### Axis 1 — Sensitivity

| Nilai | Definisi | Contoh hospitality | Boleh di repo? |
|---|---|---|---|
| `Public` | Sudah/boleh dipublikasikan | Caption publish, info di website client | Ya (bila Reusable) |
| `Internal` | Non-publik, dampak kecil | Template, voice guide generik, prompt | Ya |
| `Confidential` | Client/komersial/personal, dampak material | Rate contract OTA, occupancy, revenue, brief client, consent register | Tidak |
| `Restricted` | Credential, data pribadi sensitif | Password akun IG/OTA, data paspor/KTP tamu, data kesehatan tamu | Dilarang total |

### Axis 2 — Lifecycle

| Nilai | Arti |
|---|---|
| `Raw` | Data mentah dari client/tamu, belum diproses |
| `Draft` | Draft konten/dokumen dalam pengerjaan |
| `For Review` | Menunggu QA/approval |
| `Approved` | Disetujui tertulis oleh pihak berwenang |
| `Published` | Sudah tayang di channel |
| `Superseded` | Digantikan versi baru |
| `Archived` | Tidak aktif, disimpan untuk rekam jejak |
| `Rejected` | Ditolak; tidak dipakai |

AI tidak boleh mengubah lifecycle menjadi `Approved` atau `Published`.

### Axis 3 — Scope

| Nilai | Arti | Lokasi |
|---|---|---|
| `Reusable` | Berlaku lintas client tanpa identitas client | Repo ini |
| `Client Specific` | Terkait satu client | Workspace client |
| `Campaign Specific` | Terkait satu campaign client | Workspace client |

### Axis 4 — Evidence

| Label | Arti |
|---|---|
| **DATA FINAL** | Terverifikasi, ada sumber & approval |
| **ASSUMPTION** | Dugaan kerja; tidak boleh tampil di konten publish |
| **CLIENT CONFIRMATION** | Butuh konfirmasi client |
| **FIELD VERIFICATION** | Butuh pengecekan lokasi |
| **RISK** | Potensi masalah dengan likelihood/impact/owner/mitigasi |
| **NEXT ACTION** | Tindakan + owner + target |

### Contoh klasifikasi

| Item | Sensitivity | Lifecycle | Scope | Evidence |
|---|---|---|---|---|
| "Villa punya 3 kamar tidur" dari fact sheet bertanda tangan owner | Public | Approved | Client Specific | **DATA FINAL** |
| "Kira-kira 5 menit ke pantai" dari chat staf | Internal | Raw | Client Specific | **FIELD VERIFICATION** |
| Harga promo Ramadan belum dikonfirmasi | Confidential | Draft | Campaign Specific | **CLIENT CONFIRMATION** |
| Prompt template caption | Internal | Approved | Reusable | **DATA FINAL** |
| Password akun Instagram client | Restricted | — | Client Specific | — (tidak diproses) |

### Aturan penyimpanan

- Hanya `Public`/`Internal` + `Reusable` yang masuk repo.
- `Confidential` → workspace client terproteksi.
- `Restricted` → password manager/secret manager; tidak pernah diinput ke AI tool.

## Required Inputs

- Data/asset yang akan dipakai + sumbernya.
- Informasi pemilik data dan tujuan penggunaan.

## Workflow

1. Identifikasi pemilik, sumber, dan tujuan data.
2. Tentukan Sensitivity.
3. Tentukan Lifecycle.
4. Tentukan Scope.
5. Beri label Evidence pada setiap klaim.
6. Simpan di zona yang sesuai ([CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md)).

## Deliverables

- Klasifikasi tercatat di brief (field `classification`) dan di tabel klaim.

## Validation/QC Checklist

- [ ] Keempat axis terisi untuk data utama brief.
- [ ] Tidak ada data `Confidential`/`Restricted` di repo.
- [ ] Tidak ada credential di input AI.
- [ ] Hanya **DATA FINAL** di konten publish.
- [ ] Lifecycle `Approved` hanya dengan approval manusia.

## Risks & Mitigation

| RISK | Mitigation |
|---|---|
| Data client bocor lewat repo | Boundary + validator + self-review diff / review PR |
| Credential diinput ke AI | Larangan + placeholder |
| Klaim Draft dianggap final | Label evidence wajib di tabel klaim |

## Escalation Conditions

- Sensitivity atau pemilik data tidak jelas.
- Data `Restricted` ditemukan di chat, brief, atau repo.
- Permintaan memindahkan data `Confidential` ke tool/pihak lain tanpa izin.

## References

- [CONTENT-CONSTITUTION.md](../CONTENT-CONSTITUTION.md)
- [CONTENT-BOUNDARY.md](../CONTENT-BOUNDARY.md)
- [schemas/content-brief.schema.json](../schemas/content-brief.schema.json)

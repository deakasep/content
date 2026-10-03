---
name: localize-content
description: Localize hospitality marketing content between Bahasa Indonesia and English (and bilingual formats) for Indonesian villas, hotels, restaurants, and spas — natural tone, claim parity across languages, correct local terms, and cultural/religious sensitivity. Use when the user asks to translate, localize, or create a bilingual version of hospitality content.
---

# Localize Content

## Load Required Context

- `../../CONTENT-CONSTITUTION.md`
- `../../rules/03-CLIENT-BRAND-VOICE-STANDARD.md`
- `../../rules/06-LOCALIZATION-BAHASA-STANDARD.md`
- `../../knowledge/voice-guides/hospitality-voice.md`
- `../../knowledge/destinations/indonesia-overview.md`

## Workflow

1. Konfirmasi: bahasa sumber, bahasa target, varian English (US/UK), audiens target, channel, Voice Card.
2. Ekstrak semua klaim dari teks sumber ke tabel paritas.
3. Lokalisasi makna, bukan kata per kata; sesuaikan idiom, contoh, dan CTA dengan audiens.
4. Pertahankan istilah lokal penting (mis. *joglo*, *lulur*, *jamu*) + penjelasan singkat untuk audiens asing.
5. Sesuaikan format: mata uang (Rp/IDR), angka, tanggal, satuan.
6. Cek sensitivitas budaya/agama di bahasa target.
7. Cek paritas: setiap klaim muncul di kedua bahasa, tidak ada klaim tambahan.
8. Rekomendasikan review fluent/native speaker untuk konten penting (listing, website, press).

## Output

- Teks target dalam code block (atau format bilingual sesuai channel).
- Tabel paritas klaim: Klaim | ID | EN | Status.
- Glosarium istilah lokal.
- Catatan perubahan lokalisasi (bagian yang sengaja tidak diterjemahkan literal).

## Self-Check

1. Klaim identik di semua versi bahasa.
2. Tone sesuai Voice Card di bahasa target.
3. Istilah lokal benar dan dijelaskan.
4. Format mata uang/angka/tanggal sesuai bahasa.
5. Tidak ada frasa yang bisa menyinggung secara budaya/agama.

## Safety Boundary

- Tidak menambah klaim yang tidak ada di sumber.
- Tidak menerjemahkan dokumen legal/kontrak sebagai terjemahan resmi.
- Tidak menghapus disclosure (iklan/AI) saat lokalisasi.

## Exit Criteria

**Pass** bila paritas klaim lengkap dan self-check lulus. Konten listing/website tanpa review fluent speaker = **Conditional**.

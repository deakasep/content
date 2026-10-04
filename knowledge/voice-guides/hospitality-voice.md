# Hospitality Voice Guide

## Scope

Default voice untuk konten hospitality Indonesia bila client belum punya Voice Card (status **CLIENT CONFIRMATION**), plus arketipe voice yang bisa dipilih saat onboarding.

## Prinsip Default: "Host yang Baik"

Tulis seperti host yang menyambut tamu di depan pintu:

| Prinsip | Lakukan | Hindari |
|---|---|---|
| Hangat | Sapaan ramah, kalimat mengundang | Kaku, birokratis |
| Spesifik | "Kopi Kintamani diseduh pelan saat kabut turun" | "Kopi enak dengan view indah" |
| Sensory | Lihat, dengar, cium, rasa, sentuh | Daftar fasilitas tanpa rasa |
| Jujur | Deskripsi yang akan benar-benar dialami | Superlatif kosong |
| Ringkas | Satu ide per konten | Paragraf panjang tanpa jeda |
| Hormat | Budaya & warga lokal sebagai tuan rumah | Eksotisasi, stereotip |

## Arketipe Voice (pilih 1 saat onboarding)

| Arketipe | Kode (`voice.archetype` di brief) | Cocok untuk | Ciri | Contoh kalimat (fiktif) |
|---|---|---|---|---|
| **Tenang & Membumi** | `tenang-membumi` | Villa sawah, wellness retreat, spa | Kalimat pendek, ritme pelan, alam | "Pagi di sini dimulai dengan suara air di parit sawah." |
| **Hangat & Kekeluargaan** | `hangat-kekeluargaan` | Homestay, guesthouse, resto keluarga | Sapaan akrab, cerita host | "Bu Made sudah siapkan pisang goreng hangat buat kamu." |
| **Elegan & Tertata** | `elegan-tertata` | Resort, fine dining, hotel premium | Diksi rapi, tidak berlebihan | "Makan malam lima hidangan, disajikan saat matahari turun di Selat Lombok." |
| **Santai & Playful** | `santai-playful` | Cafe, beach club, surf camp | Energi, humor ringan, emoji relevan | "Ombak pagi oke, kopi kedua juga oke 🌊" |
| **Informatif & Praktis** | `informatif-praktis` | Business hotel, transit, budget | Poin, jelas, efisien | "5 menit ke stasiun. Check-in mulai 14.00. Wi-Fi di semua area." |

## Sapaan

| Pilihan | Kapan |
|---|---|
| "kamu" | Audiens muda, cafe, beach club, voice santai |
| "Anda" | Hotel premium, korporat, fine dining |
| "Kak" | Sangat kasual, layanan chat/DM (bila Voice Card mengizinkan) |
| "you" (EN) | Konten English — natural, tidak formal berlebihan |

Satu sapaan per client, konsisten.

## Daftar Klise yang Dihindari

| ID | EN |
|---|---|
| surga tersembunyi | hidden gem |
| pengalaman tak terlupakan | unforgettable experience |
| tempat terbaik untuk... | the best place to... |
| nikmati liburan impian | your dream getaway awaits |
| kemewahan tiada tara | unparalleled luxury |
| terletak di jantung... (dipakai berulang) | nestled in the heart of... |

Klise boleh hanya bila Voice Card client secara eksplisit mengizinkan.

## Emoji

- Default: 0–3 per caption, relevan dengan isi (🌿 🌊 ☕ 🌅).
- Hindari emoji di balasan review negatif.
- Hindari emoji yang bisa bermakna lain atau sensitif secara religius.

## Contoh Transformasi (fiktif)

**Sebelum (generik):**
"Nikmati pengalaman tak terlupakan di villa mewah kami yang terletak di surga tersembunyi Ubud! Fasilitas terbaik untuk liburan impian Anda!!!"

**Sesudah (Tenang & Membumi):**
"Bangun, buka pintu kaca, dan sawah sudah di depan kaki. Dua kamar, satu kolam privat, dan sarapan Indonesia yang diantar ke teras setiap pagi."

Perubahan: superlatif & klise dihapus, diganti fakta spesifik (**DATA FINAL** dari fact sheet), tanda seru dikurangi.

## References

- [03 Client Brand Voice](../../rules/03-CLIENT-BRAND-VOICE-STANDARD.md)
- [templates/client-onboarding.md](../../templates/client-onboarding.md)

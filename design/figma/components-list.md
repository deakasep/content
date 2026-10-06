# Components List — untuk Figma / for Figma

> **ID:** Daftar build untuk component library di Figma: **22 komponen inti + 5 komponen khusus CLAU**. Nama Figma, variant property, ukuran, state, dan sketsa ASCII. Detail perilaku & do/don't ada di [components.md](../design-system/components.md); nilai token di [tokens.md](../tokens/tokens.md).
> **EN:** Build list for the Figma library: 22 core + 5 CLAU-specific components with Figma names, variant properties, sizes, states, and ASCII sketches.

**State standar** (`State=`): `Default` · `Hover` · `Focus` · `Pressed` · `Disabled` · (`Loading` / `Error` bila relevan).

## Ringkasan / Summary

| # | Nama Figma | Variant properties | Size | Jumlah varian* |
|---|---|---|---|---|
| 1 | `Button` | Type: Primary/Secondary/Ghost/Danger · State · Icon left/right (bool) | sm 40 · md 44 · lg 52 | 4 × 3 × 6 = 72 |
| 2 | `Form/Input` | Type: Text/Email/Password/Number · State + Error/Success | md 44 | 4 × 7 = 28 |
| 3 | `Form/Textarea` | State · Counter (bool) | auto 3–10 baris | 7 |
| 4 | `Form/Select` | Type: Native/Combobox/Multi · State · Open (bool) | md 44 | 3 × 6 × 2 |
| 5 | `Form/Checkbox`, `Form/Radio` | Checked: Off/On/Indeterminate (checkbox) · State | 20 (area 44) | 3 × 5 |
| 6 | `Form/Toggle` | On (bool) · State | 44 × 24 | 2 × 5 |
| 7 | `Card` | Type: Default/Interactive/Elevated/Media · State | fleksibel | 4 × 3 |
| 8 | `Table` (+ `Table/Header cell`, `Table/Row`) | Sort: None/Asc/Desc · Row state: Default/Hover/Selected | baris 52 (Studio 44) | — |
| 9 | `Modal` | Type: Dialog/Form/Bottom sheet · Breakpoint: Mobile/Desktop | 440 / 560–640 / full | 3 × 2 |
| 10 | `Toast` | Type: Success/Error/Warning/Info · Action (bool) | 360 | 4 × 2 |
| 11 | `Badge` | Tone: Neutral/Primary/Secondary/Success/Warning/Error/Info · Removable (bool) | 24 | 7 × 2 |
| 12 | `Avatar` (+ `Avatar/Group`) | Type: Photo/Initials · Status dot (bool) | 24 · 32 · 40 · 56 | 2 × 2 × 4 |
| 13 | `Tooltip` | Position: Top/Bottom/Left/Right | maks 240 | 4 |
| 14 | `Breadcrumb` | Levels: 2/3/4 | — | 3 |
| 15 | `Tabs` | Count 2–5 · Item state: Default/Active/Hover/Focus · Counter (bool) | 44 | — |
| 16 | `Pagination` | Type: Numbered (desktop)/Load more (mobile) | — | 2 |
| 17 | `Nav/Bottom nav`, `Nav/Rail`, `Nav/Sidebar` | Active item 1–5 · Collapsed (sidebar) | 64 / 80 / 256 · 72 | — |
| 18 | `Nav/Top bar` | Surface: Portal/Studio · Breakpoint | 56 / 64 | 2 × 2 |
| 19 | `Footer` | Breakpoint | — | 2 |
| 20 | `State/Empty` | Size: Section/Page · Action (bool) | — | 2 × 2 |
| 21 | `State/Skeleton` | Shape: Card/List row/Table row/Stat/Text | — | 5 |
| 22 | `State/Error` | Type: Inline/Section/Page/Offline banner | — | 4 |
| C1 | `CLAU/Evidence Badge` | Label: DATA FINAL/CLIENT CONFIRMATION/FIELD VERIFICATION/ASSUMPTION/RISK/NEXT ACTION | 24 | 6 |
| C2 | `CLAU/Fact Confirm Row` | Status: Pending/Confirmed/Corrected | — | 3 |
| C3 | `CLAU/Content Preview` | Format: Feed 4:5/Feed 1:1/Story 9:16/Reel 9:16 · Slides 1–10 | lebar kartu | 4 |
| C4 | `CLAU/Approval Bar` | Approve enabled (bool) · Level: L1/L2/L3 · Breakpoint | sticky | 2 × 3 × 2 |
| C5 | `CLAU/Agent Status Pill` | Status: Ready/Working/Waiting human/Error | 24 | 4 |

\*Jumlah varian untuk perencanaan. Gunakan *component properties* (boolean, instance swap, text) supaya tidak meledak menjadi ratusan varian.

---

## Sketsa ASCII / ASCII Sketches

### 1. Button

```text
 Primary          Secondary         Ghost           Danger          Disabled
┌──────────────┐ ┌──────────────┐                  ┌────────────┐  ┌──────────────┐
│ ✓  Setujui   │ │ ✎  Minta rev │    Lihat semua › │ Hapus      │  │   Simpan     │ (50%)
└──────────────┘ └──────────────┘                  └────────────┘  └──────────────┘
 fill primary     outline input     teks primary    fill error     opacity 0.5
 Loading: [ ◌ Menyimpan… ]  (lebar tetap)          Focus: ring 2px + offset 2px
```

### 2–3. Input & Textarea

```text
 Email                                   Caption
┌──────────────────────────────┐        ┌──────────────────────────────┐
│ nama@villa.com               │        │ Sarapan di bale, lalu …      │
└──────────────────────────────┘        │                              │
 Error:                                  │                1.240 / 2.200 │
┌──────────────────────────────┐        └──────────────────────────────┘
│ nama@villa                   │ (border error)
└──────────────────────────────┘
 x Format email belum benar.
```

### 4–6. Select, Checkbox/Radio, Toggle

```text
┌────────────────────────── ▾ ┐   [x] Konten baru via email    (o) Bahasa Indonesia
│ WITA                        │   [ ] Laporan bulanan          ( ) English
└─────────────────────────────┘   [-] Pilih sebagian (tabel)
 Toggle off: (●━━━)   on: (━━━●)   label kiri, toggle kanan
```

### 7. Card (Media / konten)

```text
┌──────────────────────────────┐
│ ┌──────┐ Carousel sarapan    │
│ │ 4:5  │ IG feed · 11 Okt    │
│ └──────┘ [Ditinjau] [L2]     │
│          ? 2 fakta perlu     │
│            konfirmasi        │
└──────────────────────────────┘
```

### 8. Table (desktop) → list kartu (mobile)

```text
┌─────────────────────┬──────────┬─────────┬────┐      ┌──────────────────────────┐
│ Nama ↕              │ Industri │ Status  │    │      │ Villa Contoh Ubud        │
├─────────────────────┼──────────┼─────────┼────┤ ───► │ Villa · Bali   [Onboard] │
│ Villa Contoh Ubud   │ Villa    │ Onboard │ ⋮  │      └──────────────────────────┘
└─────────────────────┴──────────┴─────────┴────┘
```

### 9. Modal: Dialog (desktop) & Bottom sheet (mobile)

```text
┌────────────────────────────────┐        ┌──────────────────────────────┐
│ Tolak konten ini?          [x] │        │            ────              │
│ Konten akan kembali ke tim.    │        │ Minta revisi                 │
│                                │        │ ┌──────────────────────────┐ │
│          [Batal] [Tolak konten]│        │ │ Apa yang perlu diubah?   │ │
└────────────────────────────────┘        │ └──────────────────────────┘ │
 fokus awal: Batal                        │ [Ganti foto] [Ubah jadwal]   │
                                          │ [         Kirim          ]   │
                                          └──────────────────────────────┘
```

### 10–13. Toast, Badge, Avatar, Tooltip

```text
┌──────────────────────────────────────────────┐
│ ✓ Konten disetujui.               [Urungkan] │   [Ditinjau] [L2] [Baru x]
└──────────────────────────────────────────────┘   (SW) (DK) (+3)   ┌────────────┐
                                                                    │ Salin (⌘C) │
                                                                    └─────┬──────┘
```

### 14–16. Breadcrumb, Tabs, Pagination

```text
 Klien › Villa Contoh Ubud › Konten › Carousel sarapan

 Semua   Perlu Anda (3)   Disetujui   Tayang
 ─────   ══════════════
          (aktif: garis bawah primary 2px)

 ‹ Sebelumnya   1  [2]  3  …  8   Berikutnya ›     Menampilkan 26–50 dari 184
 Mobile: [ Muat lebih banyak ]
```

### 17–19. Navigation, Top bar, Footer

```text
 Bottom nav (mobile)                      Sidebar (desktop)
┌──────────────────────────────────┐     ┌────────────────┐
│  ⌂      ▦      ▣      ▤      ◯   │     │ ◯ CLAU         │
│ Beranda Konten Kalender …        │     │ ▌⌂ Beranda     │ ← aktif: bg primary-subtle
└──────────────────────────────────┘     │  ▦ Konten   3  │
                                         │  ▣ Kalender    │
                                         └────────────────┘
 Top bar: [Villa Contoh Ubud ▾]   ID|EN   (!)   (S)
 Footer:  © 2026 CLAU · Privasi · Syarat · ID|EN
```

### 20–22. Empty, Skeleton, Error

```text
 Empty                         Skeleton                       Error (section)
        [ ikon 48 ]           ┌──────────────────────────┐   ┌──────────────────────────┐
  Belum ada konten bulan ini  │ ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒    │   │ ! Kalender belum bisa    │
  Tim sedang menyiapkan       │ ▒▒▒▒▒▒  ▒▒▒▒▒▒▒          │   │   dimuat.  [Coba lagi]   │
  konten pertama Anda.        └──────────────────────────┘   └──────────────────────────┘
```

### C1–C5. Komponen CLAU

```text
 C1 Evidence Badge
 [✓ DATA FINAL] [? CLIENT CONFIRMATION] [⌖ FIELD VERIFICATION] [◌ ASSUMPTION] [! RISK] [→ NEXT ACTION]

 C2 Fact Confirm Row
┌──────────────────────────────────────────────────────┐
│ AC di semua kamar         [? CLIENT CONFIRMATION]    │  Pending   (bg warning-subtle)
│                           [✓ Benar]  [✎ Perbaiki]    │
├──────────────────────────────────────────────────────┤
│ 3 kamar tidur             [✓ DATA FINAL]  Bu Sari ✓  │  Confirmed
└──────────────────────────────────────────────────────┘

 C3 Content Preview (Feed 4:5)        C4 Approval Bar (mobile, sticky)
┌────────────────────┐               ┌──────────────────────────────────┐
│ (o) villacontoh    │               │ [✎ Minta revisi] [✓ Setujui]     │
│ ┌────────────────┐ │               │ Setujui aktif setelah semua      │
│ │     media      │ │               │ fakta dikonfirmasi.              │
│ └────────────────┘ │               └──────────────────────────────────┘
│      ● ○ ○ ○       │
│ caption…           │               C5 Agent Status Pill
└────────────────────┘               [● Siap] [● Bekerja (3)] [● Menunggu manusia] [x Error]
```

## Urutan Build & Estimasi / Build Order

| Hari | Komponen |
|---|---|
| 1 | Button, Badge, Avatar, Icon wrapper, Form (Input, Textarea, Select, Checkbox, Radio, Toggle) |
| 2 | Card, Tabs, Breadcrumb, Pagination, Toast, Tooltip, Modal, Navigation, Top bar, Footer, Table, States, komponen CLAU (C1–C5) |

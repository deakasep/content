# Benchmark Sintra.ai → CLAU AI (web + agent)

> Catatan semua sistem yang terlihat di situs publik sintra.ai, dibandingkan dengan yang sudah ada di `deakasep/web` dan `deakasep/agent`. Dicek AI 2026-11-02 dari halaman publik (beranda, pricing, Brain AI, integrations, summer edition, help center kredit, money-back, fair use, affiliate). Label: `DATA FINAL` = tertulis di situs Sintra saat dicek · `ASSUMPTION` = dugaan AI · `NEXT ACTION` = usulan, belum keputusan owner.
>
> ⚠️ `RISK`: Fair Use Policy Sintra melarang memakai layanan mereka untuk membuat produk pesaing atau menyalin logika/prompt asisten mereka. Catatan ini hanya dari halaman publik (tanpa login/akun Sintra). Kita meniru **alur bisnis**, bukan teks, gambar, nama karakter, atau prompt mereka.

## 1. Peta situs Sintra (menu & footer)

| Grup | Isi |
|---|---|
| Product | Pricing · Log in (`app.sintra.ai`) · Book a demo |
| AI employees | Halaman "What is an AI employee?" + 12 halaman per karyawan |
| Features | Brain AI · Integrations |
| Resources | Blog · Case studies · Help & guides (Intercom, `help.sintra.ai`) · **Summer edition 2026** (halaman changelog musiman) · 3 tools gratis: Aesthetic bio maker, Comment generator, Discord bio maker |
| Solutions | 12 landing page SEO: AI agents, AI assistants, AI copilots, AI operators, AI workforce, AI orchestration, AI chatbots, AI bots, AI team, Conversational AI, Generative AI, Agentic AI |
| Company | Careers · Affiliate program |
| Legal | Terms & conditions · Privacy policy · Refund policy · Money-back guarantee · Fair use policy · Other policies · Consent Preferences (banner cookie) |
| Lain | Aplikasi iOS & Android (QR "Get Sintra app"), sosmed (IG, LinkedIn, FB, TikTok, X, YouTube, Reddit, grup FB komunitas), pop-up "welcome gift" pengumpul email, perusahaan PlayOS, Inc. |

## 2. 12 AI employee Sintra

| Nama | Peran | Use case bawaan ("Included with") |
|---|---|---|
| Buddy | Business strategist / BD | Newsletter strategy, brand generator, investor update, marketing strategy, product launcher, target audience, business idea, meeting notes, competitor analyzer |
| Cassie | Customer support | Comment responder, product manual, FAQ, customer chat, support report, email responder |
| Commet | eCommerce / website builder | Winning product finder, product page optimizer, margin calculator, Shopify analyzer, product description, testimonial, landing page, website translator; **bangun website** |
| Dexter | Data analyst | P&L, balance sheet, sales forecaster, ROI calculator; Google Analytics, QuickBooks, Xero |
| Emmie | Email marketer | Abandoned cart, campaign, post-purchase, welcome flow, email calendar, pop-up text, win-back, content email |
| Gigi | Personal growth coach | Meal plan, workout, schedule, study helper (Strava) |
| Milli | Sales manager | Cold email, discovery & closing call script, follow-up, incentive plan, negotiation, sales contract, email list, proposal, cold calling; Meta Ads, HubSpot, Salesforce |
| Penn | Copywriter | Blog, email, video ad script, tone changer, VSL, newsletter, advertorial, FB ads, FB post |
| Scouty | Recruiter | Resume screener, job description, onboarding, outreach, interview planner, LinkedIn outreach |
| Seomi | SEO | SEO blog writer, SEO auditor, keyword, backlink, site structure |
| Soshie | Social media | Strategy, reels script, viral trend finder, TikTok, X, YouTube script, LinkedIn; **posting & jadwal otomatis** |
| Vizzy | Executive assistant | Image generation, upscale, remove background, trip planner, birthday, financial reporter; kalender, email, Slack, Notion, Trello, Todoist, Linear, GitHub |

Pola halaman per karyawan: nama + peran + kartu "What I can do" (3 kemampuan) + daftar use case + integrasi yang dipakai. Tiap karyawan dulu juga dijual satuan ($39/bulan) selain paket semua karyawan "Sintra X".

## 3. Sistem produk (yang terlihat)

| Sistem | Cara kerja di Sintra (`DATA FINAL`) |
|---|---|
| Onboarding 4 langkah | Isi konteks bisnis → sambungkan tools → atur aturan & level approval → karyawan AI bekerja |
| **Brain AI** | Basis pengetahuan bersama semua karyawan: teks, URL website (scrape), PDF/TXT/CSV + ±20 format lain; **quick-save** dari chat ke Brain; ringkasan otomatis jadi "quick facts"; **pertanyaan harian** dari karyawan untuk melengkapi Brain; sampai 5 profil brand, ganti profil instan |
| Workspace | Profil bisnis tak terbatas; workspace bisa dibagi ke tim (undang anggota); kredit & paket **per workspace**; workspace baru (setelah berlangganan) dapat 20 kredit gratis/bulan |
| Chat | Tiap karyawan = chatbot; **@mention** karyawan lain di chat; level berpikir **Spark / Smart / Pro** (makin dalam makin mahal kredit); editor teks bawaan untuk hasil tulisan; bikin slide/presentasi siap ekspor; video iklan pendek dengan audio + **storyboard pratinjau sebelum kredit terpakai** |
| Browser agent | Karyawan bisa login ke aplikasi pihak ketiga lewat browser bawaan, sebagai alternatif bila tidak ada integrasi |
| Custom AI employee | Buat karyawan sendiri (deskripsikan pekerjaan → Sintra menyiapkan); 5–10 kredit, tugas berat sampai 100 kredit |
| Marketplace helper | Publikasikan helper buatan sendiri, rak & kategori kurasi, **creator dibayar otomatis** saat helper dipakai orang, link publik |
| Penemuan helper | Favorit (bintang), pencarian semantik, rekomendasi helper di beranda & tempat kerja |
| Automations | Beranda gabungan tugas + otomasi terjadwal; Sintra menyarankan apa yang layak diotomasi; contoh: posting sosmed mingguan, cek komentar FB, ringkasan rapat harian dari email + kalender |
| Daily Ideas | Karyawan proaktif mengirim ide (model "pull") — tidak memakan kredit sampai dibalas |
| Notifikasi | Bell inbox: semua balasan, hasil, dan **approval** dari helper & otomasi |
| Integrasi | ±29 integrasi resmi 1 klik (OAuth) + klaim "1.000+": Gmail, Outlook/Microsoft, Google Calendar/Drive/Tasks/Analytics/Workspace Admin, LinkedIn, Facebook, Instagram, Meta Ads, TikTok, YouTube, Notion, Slack, Trello, Todoist, Linear, GitHub, Dropbox, QuickBooks, Xero, Salesforce, HubSpot, WordPress, Webflow, Shopify, Strava. Tiap integrasi dipasang ke karyawan yang memakainya; integrasi bisa **privat atau publik untuk tim**; minta integrasi baru dari dashboard |
| Bahasa | 100+ bahasa |
| Platform | Web (`app.sintra.ai`) + aplikasi iOS & Android |
| Model AI | Halaman pricing menyebut berbasis Claude Sonnet 4.5 |
| Keamanan & data | Enkripsi transit & at rest, tidak melatih model dengan data user, tidak menyimpan credential integrasi, export/hapus data kapan saja, klaim GDPR |

## 4. Kredit & harga Sintra

| Item | Sintra (`DATA FINAL`, 2026-11-02) |
|---|---|
| Paket | Satu paket semua karyawan; durasi 1 / 3 / 12 bulan; harga coret + diskon 50–70% ($48,50 · $70,80/3 bln · $187,20/12 bln saat dicek); VAT bisa berlaku; checkout Stripe |
| Isi paket | 12 helper, 250 kredit/bulan, 15+ integrasi, support 24/7 |
| Paket besar | Tier 7.000 dan 10.000 kredit (baru) |
| Kredit | Reset tiap bulan pada tanggal mulai langganan, **tidak menumpuk**; habis = karyawan berhenti; pop-up saat menipis |
| Top up | Dijual sebagai **langganan tambahan** (bukan beli sekali), bisa naik/turun/hapus; **tidak bisa direfund** |
| Extra credits | Bonus/goodwill dari support, dipakai setelah kredit bulanan, tidak reset, hangus ±1 tahun; daftar per grant |
| Trial | Freemium 3 hari, 50 kredit sekali per akun |
| Log pemakaian | Riwayat rinci biaya tiap aksi di Usage & Billing |
| Contoh tarif | Pesan chat 0,1–1 (makin panjang thread makin mahal → saran pisah chat per tugas) · balasan agen 0,1 · gambar 0,5–1,8 · post sosmed di chat 1 · ambil email seminggu 1 · scrape website 0,5 · simpan ke Brain oleh agen 0,1 · tugas terjadwal 1–5 (basic) / 3–10 (riset) / 5–20+ (kompleks) · video UGC 15 detik ±40 · website 15–20 (1 halaman) / 25–40 (multi) · custom employee 5–10 |
| Gratis (tanpa kredit) | Jawab pertanyaan panduan, Daily Ideas dibuat, isi Brain manual, posting terjadwal yang sudah dibuat, setup otomasi, agen tidak membalas |
| Refund | Garansi uang kembali 14 hari untuk paket berbayar (bukan trial), diproses 3–5 hari kerja, top up tidak termasuk |

## 5. Pemasaran & pertumbuhan Sintra

- **Affiliate** (lewat Impact.com): komisi 30% → 35% (10+ sale/bulan) → 40% (25+) → 50% (30+), plus 15% recurring sampai 12 bulan; cookie 30 hari; payout bulanan, sale payable 30 hari setelah transaksi, minimum $10; larang bidding keyword merek & klaim menyesatkan; dashboard, kupon, landing page khusus, materi promosi.
- Social proof: angka (100M+ prompt 2025, 600K+ akun, 50+ negara, 40–50 ribu pengusaha), logo media, testimoni bertanggal & negara.
- Tabel pembanding vs ChatGPT, Claude, Lindy, Marblism.
- Tools gratis untuk SEO (bio maker, comment generator), 12 landing page "Solutions" untuk kata kunci, blog, case study.
- Book a demo, pop-up hadiah email, changelog musiman yang dikemas seperti event.

## 6. Gap: Sintra vs CLAU sekarang

Status CLAU dibaca dari `content/docs/status.md` (2026-10-30), `agent/CLAUDE.md` (backend 0.14.0), dan `web/src/data/*`.

| Sistem Sintra | CLAU sekarang | Gap |
|---|---|---|
| 12 karyawan + halaman per karyawan | 15 agen (registry + `/agen/:slug` di web), 10 aktif | ✅ Setara; CLAU belum punya daftar "use case 1 klik" per agen di web |
| Brain AI | Fact sheet + Konfirmasi Fakta (`/fact-sheets` = Brain bisnis), halaman web `/brain-ai` | Belum: upload file (PDF/CSV), scrape URL, quick-save dari chat, pertanyaan harian, multi profil brand |
| Chat dengan karyawan | "Segera hadir" (web), backend pakai request → draft | Belum: chat, @mention, level Spark/Smart/Pro, editor bawaan |
| Approval sebelum posting | ✅ Lebih ketat (Rule 08, review independen, klien klik Setujui) | Keunggulan CLAU; pertahankan |
| Automations / tugas terjadwal | Belum | Belum ada |
| Daily Ideas & notifikasi bell | Notifikasi kredit menipis/habis saja | Belum: inbox notifikasi, ide proaktif |
| Integrasi | Web menjanjikan IG/FB/TikTok/GBP; implementasi = TASK-006 | Belum ada integrasi jalan; tidak ada Gmail/Calendar/Drive |
| Custom employee + marketplace + creator dibayar | Belum | Fitur besar, belum direncanakan |
| Workspace & tim | Klien, membership, peran, 2FA (lebih aman) | Belum: banyak workspace per akun, kredit per workspace |
| Kredit & top up | 500 kredit/bln, top up 250/550/1.500, hangus 12 bln, riwayat pemakaian | Sintra: top up = langganan & non-refund; trial 50 kredit 3 hari; extra credits; tier besar |
| Trial | Belum | Belum ada freemium/trial |
| Garansi 14 hari | Belum tertulis di web | `NEXT ACTION` owner putuskan |
| Video, gambar, website, slide | Nova, Aruna, Teguh = Planned | Belum |
| Mobile app | Belum (web responsif) | — |
| Affiliate | Belum | — |
| Legal | Privasi, Syarat, Penghapusan Data | Belum: kebijakan refund, fair use, banner consent cookie |
| Konten pemasaran | Home, agen, harga, Brain, integrasi | Belum: blog, case study, help center, changelog, tools gratis, halaman solusi SEO, book a demo |

## 7. Usulan prioritas (`NEXT ACTION`, perlu persetujuan owner)

**Web (bisa dikerjakan tanpa server):**
1. Daftar use case per agen di `/agen/:slug` (meniru pola "Included with").
2. Halaman legal tambahan: Kebijakan Refund + Penggunaan Wajar (setelah owner memutuskan aturan garansi).
3. Halaman "Yang baru" (changelog) + FAQ "apa itu karyawan AI".
4. Bagian langkah onboarding 4 tahap di beranda (sudah ada HowItWorks — cek kesesuaian).

**Agent/platform (sebagian butuh provider AI nyata, TASK-004):**
1. Brain: upload file & scrape URL → fakta *belum dikonfirmasi* sampai klien setuju (sesuai AI-BOUNDARY).
2. Chat per agen + quick-save ke Brain (menunggu provider AI nyata).
3. Automations terjadwal + inbox notifikasi (hasil tetap draft, approval tetap manusia).
4. Trial kredit sekali per akun + log biaya per aksi yang lebih rinci.

Fitur yang **tidak** diusulkan ditiru tanpa keputusan owner: posting otomatis tanpa approval, browser agent yang login dengan password klien (bertentangan dengan aturan tidak menyimpan credential), marketplace helper berbayar.

Sumber: sintra.ai (beranda, /pricing, /features/brain-ai, /integrations, /summer-edition, /affiliate, /legal/money-back-guarantee, /legal/fair-use-policy) dan help.sintra.ai artikel *Workspace credits* — dibaca 2026-11-02.

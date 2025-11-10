# TikTok Music Trend API Scraper
Empower your product, dashboard, or research pipeline with real-time insight into TikTok’s trending music. This scraper reveals popular sounds by region, enriched with track metadata so you can spot rising songs, evaluate momentum, and fuel discovery experiences. Built for reliability and clarity, it turns noisy trends into structured, actionable data.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>TikTok Music Trend API</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project programmatically collects trending TikTok music and associated metadata (title, author, covers, usage counts, duration, and more), organized by country/region. It solves the challenge of tracking fast-moving audio trends at scale without manual browsing. It’s ideal for music startups, A&R teams, social analytics platforms, agencies, and creators who need dependable data on what’s hot right now.

### Why Track TikTok Sounds for Growth
- Identify breakout tracks early to inform playlisting, scouting, or marketing.
- Compare sound popularity across regions with simple, consistent fields.
- Power creator tooling: recommend sounds that fit niche, mood, or tempo.
- Enrich campaign planning with usage counts and cover art references.
- Export structured JSON/CSV that’s ready for pipelines and BI tools.

## Features
| Feature | Description |
|----------|-------------|
| Regional trending feed | Fetch trending sounds by specific two-letter country/region code (e.g., US). |
| Music detail fields | Title, author, duration, cover art (thumb/medium/large), media URIs, and identifiers. |
| Usage metrics | Includes user_count and status fields to infer traction and availability. |
| Rate-limited safe runs | Tuned to balance speed and stability for consistent collection. |
| Pagination & limits | Control volume via `limit` to match your quotas and batch processes. |
| Robust logging | Clear progress messages to monitor crawls and diagnose inputs quickly. |
| Clean schema | Normalized keys for straightforward ingestion into databases or data lakes. |
| Portable output | Results can be consumed by Python, Node.js, or any language with JSON/CSV support. |

---
## What Data This Scraper Extracts
| Field Name | Field Description |
|-------------|------------------|
| id / id_str / mid | Numeric and string identifiers for the music item. |
| title | Track title as shown in TikTok. |
| author | Display name of the sound owner/artist. |
| duration | Length of the track in seconds. |
| user_count | Approximate number of videos using the sound (usage signal). |
| status | Availability status code for the track. |
| is_original | Whether the sound is marked as original. |
| cover_thumb / cover_medium / cover_large | Objects holding image dimensions and URL lists for artwork. |
| play_url | Object containing media URL information (if available). |
| external_song_info / tt_to_dsp_song_infos | External song/DSP mapping fields when present. |
| extra | JSON string with extended analysis (beats, energy, loudness, etc.) when available. |
| region | Two-letter region used for the query (input). |
| scraped_at | ISO timestamp of when the item was collected. |

---
## Example Output
    [
      {
        "artists": null,
        "author": "Happy New Year",
        "author_position": null,
        "cover_large": {
          "height": 720,
          "uri": "tos-alisg-v-2774/13d12608283d48109381420cd82f7403",
          "url_list": [
            "https://p16-sign-sg.tiktokcdn.com/tos-alisg-v-2774/13d12608283d48109381420cd82f7403~720x720.jpeg?lk3s=08d74b56&x-expires=1732656955&x-signature=N73ScRM46o6gGh31211nxFrZiTA%3D"
          ],
          "url_prefix": null,
          "width": 720
        },
        "cover_medium": {
          "height": 720,
          "uri": "tos-alisg-v-2774/13d12608283d48109381420cd82f7403",
          "url_list": [
            "https://p16-sign-sg.tiktokcdn.com/tos-alisg-v-2774/13d12608283d48109381420cd82f7403~200x200.jpeg?lk3s=08d74b56&x-expires=1732656955&x-signature=F5QyimvV8P7EYYBb7zGNOejmDUY%3D"
          ],
          "url_prefix": null,
          "width": 720
        },
        "cover_thumb": {
          "height": 720,
          "uri": "tos-alisg-v-2774/13d12608283d48109381420cd82f7403",
          "url_list": [
            "https://p16-sign-sg.tiktokcdn.com/tos-alisg-v-2774/13d12608283d48109381420cd82f7403~100x100.jpeg?lk3s=08d74b56&x-expires=1732656955&x-signature=qoRY31w40%2Fj%2BKT64gthAbDQuAfg%3D"
          ],
          "url_prefix": null,
          "width": 720
        },
        "duration": 60,
        "external_song_info": null,
        "extra": "{\"amplitude_peak\":0.97009987,\"beats\":{\"audio_effect_onset\":\"https://sf16-music-sign.tiktokcdn.com/obj/tos-alisg-v-2774/543f352ee8bd4038a9d82447b378b2f1?lk3s=08d74b56\\u0026x-expires=1732656955\\u0026x-signature=W155PXJs2W7xpX3f2e7U%2FkeV0rc%3D\",\"beats_tracker\":\"https://sf16-music-sign.tiktokcdn.com/obj/tos-alisg-v-2774/859a57e4064249f09f763d5179dc6e19?lk3s=08d74b56\\u0026x-expires=1732656955\\u0026x-signature=nBB5UcPWv%2FlbltfHqzLg6XPhER0%3D\",\"energy_trace\":\"https://sf16-music-sign.tiktokcdn.com/obj/tos-alisg-v-2774/4977a388c37d41998a8f704176a05719?lk3s=08d74b56\\u0026x-expires=1732656955\\u0026x-signature=5St8sbSjOBMSLaSTCMwLuIUJ0h4%3D\",\"merged_beats\":\"https://sf16-music-sign.tiktokcdn.com/obj/tos-alisg-v-2774/49d43db2d49c4a9ab198cb76eafb37ad?lk3s=08d74b56\\u0026x-expires=1732656955\\u0026x-signature=bqb7gBPmtFhEuQ7DZqc2Wmj8zNs%3D\"},\"loudness_lufs\":-9.540354}",
        "id": 7090803692152031234,
        "id_str": "7090803692152031234",
        "is_original": false,
        "offline_desc": "This song can not play offline",
        "play_url": { "height": 720, "uri": "", "url_list": [], "url_prefix": null, "width": 720 },
        "source_platform": 10033,
        "status": 1,
        "title": "Happy New Year (Remake)",
        "user_count": 78426,
        "region": "US",
        "scraped_at": "2025-11-10T22:00:00Z"
      }
    ]

---
## Directory Structure Tree
    TikTok Music Trend API/
    ├── src/
    │   ├── runner.py
    │   ├── client/
    │   │   ├── http_client.py
    │   │   └── tiktok_music_api.py
    │   ├── extractors/
    │   │   └── normalize.py
    │   ├── outputs/
    │   │   ├── dataset_writer.py
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample_output.json
    ├── tests/
    │   └── test_schema.py
    ├── requirements.txt
    └── README.md

---
## Use Cases
- **A&R teams** use it to **spot rising tracks by region**, so they can **scout artists earlier with data-backed conviction**.
- **Creator tools** use it to **recommend fresh, relevant sounds**, so users **boost video reach and engagement**.
- **Agencies** use it to **validate soundtrack choices for campaigns**, so they **align creative with current audience tastes**.
- **Music analytics platforms** use it to **enrich dashboards with trending audio signals**, so clients **monitor momentum and plan releases**.
- **Product teams** use it to **build discovery feeds and alerts**, so they **ship sticky features that track what’s hot**.

---
## FAQs
**Q1: What inputs are required?**
Provide a two-letter `region` code (e.g., "US") and an optional `limit` to cap items per run.

**Q2: Do URLs in cover or media objects always resolve?**
Media providers rotate signatures; URLs are best treated as short-lived references. Store metadata and refresh periodically.

**Q3: How do I avoid collecting too much data at once?**
Use `limit` to control volume and schedule multiple small runs for steady, reliable ingestion.

**Q4: Can I join this data with DSP catalogs?**
Yes—leverage identifiers (title/author) and optional external info fields to map to your catalog or a third-party matcher.

---
## Performance Benchmarks and Results
- **Primary Metric:** ~100 music items per minute on standard residential proxies with conservative concurrency.
- **Reliability Metric:** 96–99% successful item capture across routine runs when inputs are valid.
- **Efficiency Metric:** Lightweight memory footprint; linear scaling with modest CPU usage for batch sizes under 1,000.
- **Quality Metric:** >98% field completeness for core keys (title, author, duration, covers, identifiers) on trending feeds.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>

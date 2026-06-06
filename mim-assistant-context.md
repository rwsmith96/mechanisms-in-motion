# Mechanisms in Motion: Assistant Context Spec

**This is the canonical brief for any AI assistant helping run the Mechanisms in Motion (MiM) podcast.** Every calendar event in `mim-recording-schedule.ics` carries a paste-ready prompt that points here. Load this file, find the step you are on, and execute. The calendar is the spine; this file is the source of truth behind it.

Repo home: `~/thetis-docs/projects/mechanisms-in-motion/`
Files: `mim-podcast-roadmap.pdf` (human six-pager) · `mim-recording-schedule.ics` (the calendar) · `generate_ics.py` (regenerates the calendar) · `mim-assistant-context.md` (this file) · `research/` (raw research + critic findings).

---

## 1. What the show is

Mechanisms in Motion is the AES podcast: Amazon's internal operating mechanisms translated into playbooks any company can use. Tagline: **"Day 1 Energy for Every Stage of Growth."** The podcast feeds the book ("Mechanisms: The Scaling Playbook") and brings in consulting leads: guests become relationships, relationships move the book, consulting closes from both. Format: remote video interview, two hosts plus one guest, ~60 minutes of conversation.

**Roles.** Rich owns logistics: the tools, billing, hardware, publishing, QA, and the booking system. Carla Anderson Skogland owns the guest slate: who comes on, in what order, the outreach, and the question arc (with Rich). **Editing is owned by Kenzie (Carla's daughter, sound-mixing degree), with a backup editor in Carla's network behind her** — Rich does QA/oversight on the cut, not the cut itself (decided on the 2026-06-05 call). Both Rich and Carla co-host every recording. Neither host has run a podcast before, so the whole system is built for the fewest moving parts that still produce clean separate tracks, broadcast-compliant audio, and video that looks like it was shot in a studio.

## 2. The locked stack (do not re-litigate)

| Layer | Tool | Plan / cost | One-line job |
|---|---|---|---|
| Record | Riverside.fm | Pro, ~$24/mo annual | Local-first remote recording at 1080p/30fps; guests join in Chrome, no install |
| Edit | Descript | Creator, ~$24/mo annual ($35 monthly) | Edit by text; Studio Sound, filler removal, Automatic Multicam, AI clips |
| Host/distribute | Transistor.fm | Professional, $49/mo | One upload → audio RSS to Apple+Spotify + auto-post full video to YouTube |
| Schedule | Calendly | **Carla's existing subscription, renamed (no new cost)** | Guests self-book; auto-timezone; sends Riverside link + prep doc |

Run-rate ≈ **$97/mo** on annual billing (Calendly runs off Carla's existing account, so no new $15/mo line). One-time hardware ≈ **$1,600** for two matched host kits (Rich already owns his headphones, so only one headphone set is bought). Riverside can pause after the recording sprint.

**Decisions already set (treat as fixed):** fully remote cloud-studio recording · prosumer hardware (~$850/host) · Descript post · 6–8 episodes recorded in an Aug/Sept 2026 block · recording starts late August · **recordings on Tuesday/Friday mornings** (Thursdays are hard for Carla; Fridays also open more exec calendars) · **editing owned by Kenzie, not Rich** · **Calendly reuses Carla's account** · **Keith (Carla's husband, a sound engineer) is vetting the gear list before the kit order.**

**Distribution truth:** the guaranteed path is audio via RSS (Apple + Spotify) plus auto-posted full video to YouTube. Native video on Apple/Spotify (HLS via Transistor) is a 2026 rollout; treat it as a bonus only if it is live on the account at setup. Never promise it.

## 3. The two matched host kits (~$850 each)

| Item | Buy | Price | Note |
|---|---|---|---|
| Mic | Shure MV7+ (black, USB-C) | $279 | The highest-impact dollar. Run over USB-C, no interface. |
| Webcam | Logitech MX Brio 4K | $199 | One USB-C cable, no capture card, no dummy battery. |
| Key light | Elgato Key Light Neo | $99 | USB-powered, no Wi-Fi/app to fail on record day. |
| Headphones | Sony MDR-7506 | $100 | Closed-back, kills echo. Plug into the mic. **Rich already owns his; buy one set (Carla's).** |
| Boom arm | RODE PSA1+ | $126 | Silent, rated to hold the heavy MV7+. |
| Room | Reflection filter / foam | ~$50 | Plus rug/curtains/bookshelf, free. |

Buy two matched kits (Rich in San Diego, Carla near Seattle) and change components together so both feeds stay matched; only one headphone set is bought since Rich already owns his. **Keith (Carla's husband, a sound engineer/musician who has researched the build) is vetting this list and the setup; incorporate his write-up before ordering on Jul 1, and confirm whether he is coming to San Diego to set up Rich's kit.** Optional guest-uplift kit for marquee guests: a clip light + USB mic/lav (~$25–60) shipped ahead.

## 4. Production spec (the numbers that never change)

- **Loudness:** −14 LUFS integrated, **True Peak −1.0 dBTP**, stereo. Same audio bed in the video render and the podcast MP3.
- **Video:** 1080p, **30fps locked** across both host kits and every guest. Transcode any variable-rate guest track to constant frame rate before editing. H.264 MP4 to YouTube.
- **Audio:** stereo MP3/AAC, 48kHz, to Transistor.
- **Studio Sound at 60–80%** per track (not 100%, which sounds robotic). MV7+ in Auto Level, light denoise, **reverb off**.
- **Two record-day non-negotiables:** (1) confirm the MV7+ is the selected mic in Riverside, not the laptop default; (2) stay on the page until every track shows 100% uploaded before anyone closes the tab. Both hosts also run a QuickTime audio backup every session (local-first is not a guarantee).
- **Pre-publish QA gate (every episode):** export reads −14 LUFS / −1.0 dBTP; lip-sync spot-checked at start, middle, and final minute of the video; captions track the audio at the end of the file.

## 5. Conventions

- **Regenerate the calendar from the script,** never hand-edit the `.ics`. Edit the `SESSIONS` / `MILESTONES` / `STEPS` data in `generate_ics.py` and re-run `python3 generate_ics.py`.
- **Re-render the six-pager** by editing `mim-podcast-roadmap.html` and running headless Chrome `--print-to-pdf`, then reading every page. No em dashes anywhere (commas, colons, semicolons, periods, parens). No Saturday work blocks.
- **Dates are defaults.** They flex around Carla's real guest slate; regenerate when they move.
- **Voice:** direct, professional, pyramid-first. Guest-facing copy is warm and plain.

## 6. The step plan (definitions of done)

Each step matches a calendar event. "Right looks like" is the acceptance test.

1. **Lock the stack + dates with Carla (due Jun 5).** Right: stack confirmed, eight Tue/Fri slots on both calendars, guest-slate ownership confirmed with Carla. *(Done on the 2026-06-05 call.)*
2. **Keith's gear review incorporated (due Jun 19).** Right: Keith's written notes captured; kit list reconciled to any swaps he flags; San Diego setup visit confirmed or declined.
3. **First 4 guests identified + invites out (Carla, due Jun 19).** Right: four names, four warm invites sent with the Calendly link; a 6–8 slate forming.
4. **Order both hardware kits (Rich, due Jul 1).** Right: two matched kits ordered (one headphone set), arriving before late July, Keith's review folded in.
5. **Kits assembled + bench-tested (due Jul 27).** Right: both kits built; mic on the arm; Shure Motiv app set (Auto Level, light denoise, reverb off); mic/cam/light/headphones confirmed working on each machine.
6. **Editor (Kenzie) learns Descript on scrap footage (due Jul 31).** Right: editor confirmed (Kenzie, else Lauren, else a pro); one full mock edit done end to end (import multitrack → Studio Sound → filler removal → multicam → captions → one clip → export to spec).
7. **Day-1 software setup (Aug 3).** Right: three accounts live on annual billing (Calendly reuses Carla's existing account, renamed); Riverside "Export to Descript" enabled; YouTube channel connected in Transistor; RSS submitted once to Apple Podcasts Connect and Spotify for Creators; Calendly "Recording" event built; prep one-pager written; editor lanes confirmed (Kenzie cuts, Rich QA, Carla clips/caption-QA).
8. **Full test run (Fri Aug 14).** Right: 5–10 min recorded with a stand-in; all tracks uploaded to 100%; Descript export lands separate tracks; lip-sync clean at the END of the take; export reads −14 LUFS / −1.0 dBTP at 30fps.
9. **Record Ep01–Ep08 (Aug 25 – Sep 18, Tue/Fri).** Right per session: clean separate local tracks captured, slate + 3-sec sync pause recorded, uploads confirmed 100%, QuickTime backup saved.
10. **Edit each episode (rolling, Kenzie).** Right: episode cut to the production spec, 2–4 vertical clips made, passes the pre-publish QA gate (Rich runs the gate).
11. **Launch + weekly publish (Tue Sep 22 →).** Right: first episode live; 1–2 episode buffer held; season queued in Transistor scheduled-publish; each guest sent their clips.

## 7. Guest ops (one Calendly event, one prep doc)

Calendly event "Mechanisms in Motion: Recording", 75 min, 15-min buffers, Riverside link as the location, one shared booking calendar, intake questions (headline/title, LinkedIn/bio, one Amazon-mechanism story). Set availability so a slot requires BOTH hosts free, and after each booking confirm the invite actually carries the Riverside link and the prep doc resolves view-only. Tech check is the first 5 minutes of the recording. The reusable prep one-pager carries: the premise + tagline, the 5–6 question arc, format (conversational, ~60 min, video on), the 4-line tech checklist (laptop + Chrome, headphones on, wired internet or near the router, close Slack/email), a one-line audio+video reuse consent, and "we record locally so a dropped connection won't ruin audio; keep talking; stay until your upload hits 100%."

## 8. Release cadence

Record the 8 in the Aug/Sept block plus one hosts-only evergreen, then publish weekly on a fixed day ("new episodes every Tuesday"). Queue the season with Transistor scheduled-publish. **Launch gate:** do not launch Sep 22 unless 4 episodes are fully edited and QA-passed (plus the evergreen). **Buffer rule:** never publish below a 1-episode buffer; if it hits zero, pause the streak by design with a pre-written note rather than shipping unedited. Track status in a simple running doc (Ep#, guest, recorded, edited, publish date).

## 9. Risks, gates, and recovery (program discipline)

The recording design is sound; the two structural risks are **edit throughput concentrated on one person** and **no redundancy for the irreplaceable asset (the guest track) and operator (Rich)**. The plan handles them with gates and runbooks, not hope.

**Edit throughput is the real constraint, not recording.** Budget 5–8 hrs/episode for the first three, 3–5 after (active edit + clips + two exports + QA, plus any CFR transcode). It is a protected weekly block on the calendar. Split the work: **Kenzie owns the cut, multicam, and export** (with a backup editor in Carla's network); Rich runs the QA gate and tracks throughput; Carla owns clip selection, caption QA, and the guest-clip send. Handing editing to a dedicated editor materially de-risks this constraint versus the original Rich-edits-everything plan, but it adds a person to confirm and onboard (the Jul 31 Descript step). 48-hour SLA: no recording sits un-started for more than two days. If editing falls more than one episode behind, publish from buffer and add a second freelance Descript editor behind Kenzie (a shared project link makes this trivial; it is the single highest-leverage spend).

**Gates and decision ownership.** Rich is the accountable launch-readiness owner (go/no-go on sprint start and on each publish); Carla is consulted. Pre-committed thresholds, so no live debate: start the sprint only with **3+ guests booked** (the Jul 24 gate); **never publish below a 1-episode buffer.**

**Critical path is the guest slate.** It runs through Carla, who is load-constrained. Carla curates names and warm intros; Rich executes outreach, chasing, and booking off a shared list. A weekly 15-min slate check-in (on the calendar) keeps it from drifting. Bank one hosts-only evergreen as a no-show release valve and launch buffer; keep a standby-guest name per week and a 48-hour reconfirm.

**Data-loss runbook (the guest's local track is irreplaceable).** Every session has an "upload marshal": one host's only end-of-session job is to confirm EVERY track, including the guest's, to 100% in the Riverside dashboard before the guest is released. If a track is missing or stalls, do not end the call: keep the guest on while it re-uploads; if it can't, rebook on the spot. Immediately archive both QuickTime backups + the Riverside download to a shared cloud folder, one per episode (`MiM-EpNN-Guest-YYYY-MM-DD/`), which is the system of record, not laptop-local files.

**Single-point-of-failure coverage.** Both Rich and Carla are admins on each account (logins in a credentials note); Carla (or Kenzie / the freelance editor) is the backup publisher and can run the QA gate and hit publish if Rich is out. Editing already has a backup chain (Kenzie, then a backup editor). The publish runbook is written so a second person can execute it.

**Integration and directory latency.** Apple/Spotify directory review is not instant. Publish a 60-second trailer at Day-1 setup to start the review clock weeks early, and run one private end-to-end test episode (Transistor → Apple/Spotify ingest + YouTube auto-post) before launch. Document the manual-YouTube-upload fallback if Transistor's auto-post won't connect.

**No Season-2 cliff.** The Season 1 backlog runs out in November. A mid-October trigger (on the calendar) starts booking and recording the next batch before the buffer is exhausted.

---

*To publish this project to a URL later (so the calendar prompts can point at a link instead of a local path), the whole folder is plain markdown plus one HTML/PDF and can drop onto any static host or a GitHub Pages site with no changes.*

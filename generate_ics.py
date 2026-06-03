#!/usr/bin/env python3
"""
Generate mim-recording-schedule.ics: the SPINE of the Mechanisms in Motion launch.

The calendar is the project's backbone. Every event description is self-contained:
what to DO, what to BUY / HAVE READY, what RIGHT LOOKS LIKE (definition of done), and
a paste-ready ASSISTANT PROMPT that points at the canonical spec (mim-assistant-context.md)
so an AI assistant loaded with that prompt knows exactly how to execute the step.

All times America/Los_Angeles. Dates are sensible defaults; edit the data below and
re-run to regenerate if the real guest slate shifts the schedule. Never hand-edit the .ics.
"""

import datetime as dt

CAL_NAME = "Mechanisms in Motion: Launch"
TZID = "America/Los_Angeles"
RIVERSIDE = "Riverside studio link (paste the persistent studio URL here once created)"
DTSTAMP = "20260603T160000Z"  # fixed so re-runs are reproducible

# Optional deep-context pointer. Each prompt is SELF-CONTAINED and does not require this;
# it is for whoever wants the full spec. Update this one line once the project is published
# to a shared URL (so Carla's web assistant can fetch it too), then re-run to refresh every prompt.
SPEC_REF = "https://raw.githubusercontent.com/rwsmith96/mechanisms-in-motion/main/mim-assistant-context.md"
HOWTO = "https://github.com/rwsmith96/mechanisms-in-motion/blob/main/how-to/"  # plain-language guides

# Self-contained preamble: works pasted into ANY assistant (Claude.ai, ChatGPT, Claude Code),
# with no repo or file access required. The event's own DO and RIGHT LOOKS LIKE are the brief.
PROMPT_HEAD = (
    "You are helping run Mechanisms in Motion, the AES podcast: a remote, two-host video interview "
    "show that turns Amazon's internal operating mechanisms into playbooks any company can use "
    "(tagline 'Day 1 Energy for Every Stage of Growth'). Rich owns logistics; Carla owns the guest "
    "slate. The DO list and RIGHT LOOKS LIKE in this calendar event (above) are your brief for this "
    "step. Use them. Then do this: "
)


# ---------- ICS plumbing ----------
def fold(line: str) -> str:
    out, cur = [], ""
    for ch in line:
        if len((cur + ch).encode("utf-8")) > 73:
            out.append(cur)
            cur = " " + ch
        else:
            cur += ch
    out.append(cur)
    return "\r\n".join(out)


def esc(text: str) -> str:
    return (text.replace("\\", "\\\\").replace(";", "\\;")
            .replace(",", "\\,").replace("\n", "\\n"))


def local(date: str, hm: str) -> str:
    y, mo, d = date.split("-"); h, mi = hm.split(":")
    return f"{y}{mo}{d}T{h}{mi}00"


def build_desc(lead, do, buy, done, prompt, guides=None):
    parts = [lead, ""]
    parts.append("DO")
    parts += [f"- {x}" for x in do]
    parts.append("")
    if buy:
        parts.append("BUY / HAVE READY")
        parts += [f"- {x}" for x in buy]
        parts.append("")
    parts.append("RIGHT LOOKS LIKE")
    parts += [f"- {x}" for x in done]
    parts.append("")
    parts.append("HOW-TO GUIDES (plain language, jargon decoded, each with a chatbot prompt)")
    for g in (guides or []):
        parts.append(f"- {g}")
    parts.append(f"- All guides: {HOWTO}README.md")
    parts.append("")
    parts.append("ASSISTANT PROMPT (paste into Claude or ChatGPT for step-by-step help)")
    parts.append(PROMPT_HEAD + prompt)
    parts.append("")
    parts.append(f"FULL PROJECT SPEC (optional, for deep context): {SPEC_REF}")
    return "\n".join(parts)


def event(uid, summary, *, date=None, start=None, end=None, all_day_end=None,
          desc="", location="", alarms=None, rrule=None):
    lines = ["BEGIN:VEVENT", f"UID:{uid}@mechanismsinmotion.aes", f"DTSTAMP:{DTSTAMP}"]
    if all_day_end is not None:
        lines.append(f"DTSTART;VALUE=DATE:{date.replace('-', '')}")
        lines.append(f"DTEND;VALUE=DATE:{all_day_end.replace('-', '')}")
    else:
        lines.append(f"DTSTART;TZID={TZID}:{local(date, start)}")
        lines.append(f"DTEND;TZID={TZID}:{local(date, end)}")
    if rrule:
        lines.append(f"RRULE:{rrule}")
    lines.append(f"SUMMARY:{esc(summary)}")
    if location:
        lines.append(f"LOCATION:{esc(location)}")
    if desc:
        lines.append(f"DESCRIPTION:{esc(desc)}")
    lines += ["STATUS:CONFIRMED", "TRANSP:OPAQUE"]
    for trig in (alarms or []):
        lines += ["BEGIN:VALARM", "ACTION:DISPLAY",
                  f"DESCRIPTION:{esc(summary)}", f"TRIGGER:{trig}", "END:VALARM"]
    lines.append("END:VEVENT")
    return "\r\n".join(fold(l) for l in lines)


# ---------- The steps (the spine) ----------
KIT_ITEMS = [
    "Shure MV7+ (black, USB-C) $279 - shure.com or B&H",
    "Logitech MX Brio 4K $199 - logitech.com",
    "Elgato Key Light Neo $99 - elgato.com",
    "Sony MDR-7506 headphones $100 - any pro-audio retailer",
    "RODE PSA1+ boom arm $126 - rode.com",
    "Reflection filter / acoustic foam ~$50 - Amazon (TONOR / TroyStudio)",
]

events = []

# --- Preliminary milestones (all-day due dates) ---
events.append(event(
    "mim-lock-plan",
    "MiM DUE: Lock the stack + Aug/Sept recording dates with Carla",
    date="2026-06-05", all_day_end="2026-06-06", alarms=["-P2D"],
    desc=build_desc(
        "The gate that starts everything. Confirm the build with Carla and lock the dates.",
        ["Walk Carla through the six-pager (mim-podcast-roadmap.pdf).",
         "Confirm the four-tool stack and the ~$1,700 two-kit hardware spend.",
         "Lock the eight Tue/Thu recording slots on both calendars.",
         "Confirm the split: Rich = logistics, Carla = guest slate."],
        None,
        ["Stack approved; 8 slots on both calendars; guest-slate ownership confirmed with Carla."],
        "We are at STEP 1: lock the stack and dates. Draft a 5-line confirmation message to Carla "
        "in Rich's voice summarizing the stack, the cost, the Aug/Sept recording dates, and the "
        "logistics/guest-slate split.",
        guides=[f"Import this calendar into your own: {HOWTO}import-calendar.md"])))

events.append(event(
    "mim-guest-slate",
    "MiM DUE: First 4 guests identified + invites out (Carla)",
    date="2026-06-19", all_day_end="2026-06-20", alarms=["-P2D"],
    desc=build_desc(
        "Carla's first deliverable: seed the guest slate.",
        ["Name the first 4 guests for the launch block and their order.",
         "Send warm invites with the Calendly booking link for the Aug 25+ slots.",
         "Aim for a full 6-8 slate by early July."],
        None,
        ["4 names chosen; 4 warm invites sent; a 6-8 guest slate forming."],
        "We are at STEP 2: guest-slate kickoff (Carla owns). Draft a warm, peer-to-peer guest-invite "
        "template (subject + 6-8 lines): the show in one line, the ask (75-min remote video), and a "
        "placeholder for the Calendly link.")))

events.append(event(
    "mim-order-kits",
    "MiM DUE: Order both hardware kits (Rich)",
    date="2026-07-01", all_day_end="2026-07-02", alarms=["-P2D"],
    desc=build_desc(
        "Order two identical kits (~$850 each) so they arrive together and stay matched. Pulled to Jul 1 "
        "from Jul 10 to absorb back-order risk on the long-lead items.",
        ["Order both kits in one pass; add a spare XLR cable.",
         "Ship one to Rich (San Diego), one to Carla (Seattle area).",
         "Target arrival before late July; if any item is back-ordered, sub the nearest equivalent now."],
        KIT_ITEMS,
        ["Two identical kits ordered; arriving before late July; no item silently back-ordered past Jul 25."],
        "We are at STEP 3: order hardware. Confirm the kit list and current prices/links, flag any "
        "out-of-stock item with the nearest equivalent, and produce one ordered shopping list with "
        "direct buy links for both kits.",
        guides=[f"Set up the kit once it arrives: {HOWTO}hardware-setup.md"])))

# Booked-guest gate (PM-critic fix: critical path runs through the guest slate)
events.append(event(
    "mim-guest-gate",
    "MiM GATE: 3+ guests confirmed and BOOKED before the spend",
    date="2026-07-24", all_day_end="2026-07-25", alarms=["-P2D"],
    desc=build_desc(
        "Hard go/no-go gate. The slate is the critical path, so it gets a gate of its own.",
        ["Confirm at least 3 guests are BOOKED in Calendly (not just invited) for the sprint.",
         "Carla curates names + warm intros; Rich executes the outreach, chasing, and booking off the shared list.",
         "If short of 3, hold the sprint start or plan to open with hosts-only evergreens."],
        None,
        ["3+ guests booked into real Aug/Sept slots; Rich has made the go/no-go call on the sprint."],
        "We are at the GUEST GATE. Help me check we have 3+ guests booked, draft chase notes to any "
        "invited-but-unbooked guests, and decide go / no-go on starting the Aug 25 sprint.")))

events.append(event(
    "mim-assemble-kits",
    "MiM DUE: Both kits assembled + bench-tested",
    date="2026-07-27", all_day_end="2026-07-28", alarms=["-P2D"],
    desc=build_desc(
        "Build and bench-test both kits before the test run.",
        ["Assemble both kits; mount the MV7+ on the PSA1+ arm.",
         "Install the Shure Motiv app; set Auto Level on, light denoise, reverb OFF.",
         "Confirm mic, webcam, light, and headphones work on each machine."],
        None,
        ["Both kits built and bench-tested; Motiv settings applied on each machine."],
        "We are at STEP 4: assemble + bench-test the kits. Give me a 10-minute setup checklist for "
        "the MV7+ (USB-C mode + Motiv settings), the MX Brio, Key Light Neo placement (45 degrees, "
        "slightly above eye level), and a 30-second test-recording to confirm each kit.",
        guides=[f"Assemble + settings, step by step: {HOWTO}hardware-setup.md"])))

events.append(event(
    "mim-learn-descript",
    "MiM DUE: Learn Descript on scrap footage (Rich)",
    date="2026-07-31", all_day_end="2026-08-01", alarms=["-P2D"],
    desc=build_desc(
        "Build Descript muscle memory before the test run.",
        ["Run one full mock edit end to end on throwaway footage.",
         "Import multitrack, Studio Sound 60-80%, filler removal, Automatic Multicam, captions, one vertical clip, export to spec."],
        None,
        ["One full mock edit done; export reads -14 LUFS / -1.0 dBTP at 1080p/30fps."],
        "We are at STEP 5: learn Descript. Walk me, in order, through one full mock edit of a 5-minute "
        "multitrack remote interview with the exact spec settings (Studio Sound 60-80%, filler removal, "
        "Automatic Multicam, captions, one 9:16 clip, export -14 LUFS / -1.0 dBTP at 1080p/30fps). Flag "
        "the top 3 beginner mistakes as we go.",
        guides=[f"The edit, step by step: {HOWTO}descript-edit.md",
                f"What the export numbers mean: {HOWTO}export-settings.md"])))

# --- Day-1 setup (timed) ---
events.append(event(
    "mim-day1-setup",
    "MiM: Day-1 software setup (one time)",
    date="2026-08-03", start="09:00", end="11:00", alarms=["-P1D"],
    desc=build_desc(
        "One-time account setup. Do it once, never touch again.",
        ["Create the 4 accounts on annual billing (Riverside Pro, Descript Creator, Transistor Pro, Calendly Standard).",
         "In Riverside, enable 'Export to Descript' (email Riverside support now if the button is missing).",
         "Connect the YouTube channel inside Transistor (document the manual-upload fallback if it won't connect).",
         "Publish a 60-second TRAILER now and submit the RSS feed to Apple Podcasts Connect + Spotify for Creators, so directory review (days, sometimes weeks) clears well before launch.",
         "Run one private/unlisted end-to-end test episode: Transistor -> confirm Apple/Spotify ingest + YouTube auto-post actually fire.",
         "Build the Calendly 'Recording' event (75 min, 15-min buffers, Riverside link as location, 3 intake questions); confirm the invite carries the link and the prep doc resolves view-only.",
         "Write the guest prep one-pager (Google Doc, view-only).",
         "Set up the shared master-asset cloud folder (Drive/Dropbox), one folder per episode.",
         "Add both Rich and Carla as admins on each account where allowed; record logins in a credentials note.",
         "Confirm editor lanes: Rich owns the cut/multicam/export; Carla owns clip selection + caption QA + guest-clip send."],
        None,
        ["Accounts live + both admins; trailer published and feeds submitted for early review; private end-to-end publish proven; YouTube connected; Calendly + prep doc verified; shared asset folder ready."],
        "We are at STEP 6: Day-1 software setup. Give me an ordered runbook with the exact click-path for "
        "each task, the trailer + private-test-episode procedure, the precise Calendly 'Recording' fields, "
        "and the full text of the guest prep one-pager (include a one-line audio+video reuse consent).",
        guides=[f"Day-1 setup, step by step: {HOWTO}day1-setup.md"])))

# --- Test run (timed) ---
events.append(event(
    "mim-test-run",
    "MiM: Full test run (Rich + Carla + stand-in guest)",
    date="2026-08-13", start="09:00", end="09:45", location=RIVERSIDE, alarms=["-P1D", "-PT1H"],
    desc=build_desc(
        "Prove the whole chain AND rehearse the real failure modes before the first marquee guest. Costs nothing to break here.",
        ["Rich + Carla + a stand-in on a RANDOM laptop with a default webcam (rehearse the degraded guest, not the happy path).",
         "Mid-record, have the stand-in close the tab and rejoin; confirm their local track survived.",
         "Confirm every participant's tracks upload to 100%; rehearse the transcode-to-CFR step on the guest track.",
         "Export to Descript; confirm each person lands as a SEPARATE track; verify lip-sync at the END of the take.",
         "Confirm 30fps everywhere; export reads -14 LUFS / -1.0 dBTP."],
        None,
        ["Chain proven AND a disconnect/rejoin + degraded-guest + CFR-transcode rehearsed. Lip-sync clean at the end."],
        "We are at STEP 7: full test run. Give me a 10-minute test-run script that deliberately rehearses a "
        "degraded guest, a mid-record disconnect/rejoin, and the transcode-to-CFR fix, plus a pass/fail "
        "checklist for the chain (100% upload, separate-track export, end-of-take lip-sync, -14 LUFS / "
        "-1.0 dBTP, 30fps), and exactly what to do if any check fails.",
        guides=[f"Recording in Riverside: {HOWTO}riverside-record.md",
                f"Editing + export numbers: {HOWTO}descript-edit.md"])))

# --- Recording sessions ---
SESSIONS = [("2026-08-25", 1), ("2026-08-27", 2), ("2026-09-01", 3), ("2026-09-03", 4),
            ("2026-09-08", 5), ("2026-09-10", 6), ("2026-09-15", 7), ("2026-09-17", 8)]
REC_DO = [
    "T-minus 5 min, BEFORE the guest joins: both hosts confirm MV7+ selected, 'separate tracks / local recording' ON, and QuickTime backup rolling. If any is unconfirmed, fix it before admitting the guest.",
    "Headphones on for everyone (kills echo).",
    "Hit Record; say the slate ('Episode N, take 1'); pause 3 seconds silent for sync.",
    "Record ~60 min of conversation. If a guest's audio is rough, ask them live to move closer, turn off fans/AC, and put on headphones.",
    "UPLOAD MARSHAL: one host's only end-of-session job is to watch EVERY track (including the GUEST's) to 100% in the Riverside dashboard. The other host handles the goodbye. The guest is NOT released until the marshal calls 'clear.'",
    "If a track is missing or stalls, do NOT end the call: keep the guest on while it re-uploads; if it can't, rebook on the spot while you have them.",
    "Archive immediately: both QuickTime backups + the Riverside download go to the shared cloud folder 'MiM-EpNN-Guest-YYYY-MM-DD/' before any editing.",
]
for date, ep in SESSIONS:
    events.append(event(
        f"mim-record-ep{ep:02d}",
        f"MiM: Record Ep{ep:02d} (guest TBD)",
        date=date, start="09:00", end="10:45", location=RIVERSIDE, alarms=["-P1D", "-PT1H"],
        desc=build_desc(
            f"Mechanisms in Motion, Episode {ep:02d}. 105-min block: 15 setup + 75 record + 15 buffer. "
            "The guest's local track is the one irreplaceable asset; protect it (upload marshal + archive below).",
            REC_DO, None,
            [f"Clean separate local tracks captured; slate + 3-sec sync pause; GUEST track confirmed 100% before release; "
             f"Ep{ep:02d} archived to the shared cloud folder; edit started within 48 hours."],
            f"We are recording Episode {ep:02d} today. Before we start, quiz me on the record-day "
            "non-negotiables (T-minus mic/local-recording/QuickTime check, headphones, slate + sync pause, "
            "upload marshal confirms the GUEST track to 100% before release, archive to the shared folder). "
            "After the session, remind me to archive and to start the edit within 48 hours.",
            guides=[f"Recording run-of-show: {HOWTO}riverside-record.md",
                    f"Your free local backup: {HOWTO}quicktime-audio-backup.md",
                    f"Editing afterward: {HOWTO}descript-edit.md"])))

# --- Launch + weekly publish (recurring) ---
events.append(event(
    "mim-publish-weekly",
    "MiM: Publish episode (weekly)",
    date="2026-09-22", start="08:00", end="08:30", rrule="FREQ=WEEKLY;BYDAY=TU;COUNT=8", alarms=["-P1D"],
    desc=build_desc(
        "New episode goes live today. The first occurrence is launch day. LAUNCH GATE: do not launch Sep 22 "
        "unless 4 episodes are fully edited and QA-passed (plus the evergreen). If not, move launch right.",
        ["Confirm the episode passed the pre-publish QA gate.",
         "Publish, or confirm the Transistor scheduled-publish fired.",
         "Send the guest their clips.",
         "Buffer rule: never publish below a 1-episode buffer. If the buffer hits zero, pause the streak by design with a pre-written note; do not ship unedited."],
        None,
        ["Episode live; QA gate passed; guest sent their clips; buffer >= 1 maintained (or streak paused on purpose)."],
        "We are at the weekly PUBLISH step. First confirm we still hold a 1-episode buffer (if not, help me "
        "decide pause-vs-ship). Then run the 3-check pre-publish QA gate (-14 LUFS / -1.0 dBTP, lip-sync at "
        "start/mid/end, captions tracking), the Transistor publish steps, and a short note to the guest with clips.",
        guides=[f"Publish + the QA check: {HOWTO}publish-and-qa.md",
                f"What the loudness numbers mean: {HOWTO}export-settings.md"])))

# --- Recurring program cadence + contingency events (PM/Ops-critic fixes) ---
events.append(event(
    "mim-slate-sync",
    "MiM: Weekly slate + program check-in (Rich + Carla, 15 min)",
    date="2026-06-22", start="08:30", end="08:45", rrule="FREQ=WEEKLY;BYDAY=MO;COUNT=13", alarms=["-PT30M"],
    desc=build_desc(
        "Short standing check so the slate and the schedule never drift silently. Runs Jun 22 through the sprint.",
        ["Review the guest pipeline: named, invited, booked counts against the gate (3+ booked by Jul 24).",
         "Surface any slip in gear, setup, or editing against the calendar.",
         "Make any go/no-go or date-shift calls now, not on a record morning."],
        None,
        ["Slate and schedule status known; any slip named and owned; decisions made by Rich as launch-readiness owner."],
        "This is our weekly MiM check-in. Ask me the 4 numbers that matter (guests named / invited / booked, "
        "episodes edited) and flag anything off-track against the calendar with a recommended fix.")))

events.append(event(
    "mim-edit-block",
    "MiM: Edit + QA block (protect editing throughput)",
    date="2026-08-26", start="13:00", end="16:00", rrule="FREQ=WEEKLY;BYDAY=WE;COUNT=9", alarms=["-PT30M"],
    desc=build_desc(
        "A protected 3-hr editing block so the edit backlog can't collapse the buffer. Edit throughput, not "
        "recording, is the real constraint: budget 5-8 hrs/episode for the first three, 3-5 after.",
        ["Edit the most recent recording toward the spec (Studio Sound, multicam, captions, clips, export).",
         "Honor the 48-hour SLA: no recording sits un-started for more than two days.",
         "If editing falls more than one episode behind, publish from buffer and outsource the next first-pass to a freelance Descript editor."],
        None,
        ["Backlog held to <= 1 episode; every recording edit-started within 48h; buffer protected."],
        "This is my weekly edit block. Help me pick which episode to edit, run the Descript steps in order to "
        "the spec, and tell me honestly if I'm falling behind the publish cadence and should outsource a cut.")))

events.append(event(
    "mim-evergreen",
    "MiM: Record evergreen buffer episode (hosts-only, no guest)",
    date="2026-08-20", start="09:00", end="10:15", location=RIVERSIDE, alarms=["-P1D"],
    desc=build_desc(
        "Bank one publishable hosts-only episode as launch insurance and a no-show release valve. Same kit and "
        "checklist as a real session; no guest to coordinate.",
        ["Rich + Carla record a real, publishable hosts-only episode (a mechanism deep-dive works well).",
         "Run the full record-day discipline (mic select, local recording, upload marshal, archive).",
         "Edit it like any episode; keep it ready to drop into any week the pipeline gaps."],
        None,
        ["One evergreen episode recorded, edited, archived, and held in reserve before launch."],
        "We are recording the evergreen buffer episode (hosts-only). Suggest a strong standalone topic from "
        "the Amazon-mechanisms catalog that needs no guest, and run me through the same record-day checklist.",
        guides=[f"Recording run-of-show: {HOWTO}riverside-record.md"])))

events.append(event(
    "mim-season2-trigger",
    "MiM TRIGGER: Start booking + recording Season 2 (avoid the runway cliff)",
    date="2026-10-13", all_day_end="2026-10-14", alarms=["-P2D"],
    desc=build_desc(
        "The Season 1 backlog runs out in November. Start the next batch now so the show does not cliff.",
        ["Carla seeds the Season 2 guest slate; Rich opens Calendly slots for late Oct / Nov.",
         "Book and record the next 4-6 before the Season 1 buffer is exhausted.",
         "Keep one evergreen in reserve at all times."],
        None,
        ["Season 2 slate started and first sessions booked while Season 1 is still publishing."],
        "We are at the Season 2 trigger. Help me plan the next recording batch so the weekly streak never "
        "breaks: how many to book, by when, given the Season 1 buffer.")))

# ---------- VTIMEZONE + assembly ----------
VTIMEZONE = "\r\n".join([
    "BEGIN:VTIMEZONE", "TZID:America/Los_Angeles",
    "BEGIN:DAYLIGHT", "TZOFFSETFROM:-0800", "TZOFFSETTO:-0700", "TZNAME:PDT",
    "DTSTART:19700308T020000", "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU", "END:DAYLIGHT",
    "BEGIN:STANDARD", "TZOFFSETFROM:-0700", "TZOFFSETTO:-0800", "TZNAME:PST",
    "DTSTART:19701101T020000", "RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU", "END:STANDARD",
    "END:VTIMEZONE",
])

calendar = "\r\n".join([
    "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//AES//Mechanisms in Motion//EN",
    "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
    f"X-WR-CALNAME:{CAL_NAME}", f"X-WR-TIMEZONE:{TZID}",
    VTIMEZONE, *events, "END:VCALENDAR",
]) + "\r\n"

with open("mim-recording-schedule.ics", "w", newline="") as f:
    f.write(calendar)

print(f"Wrote mim-recording-schedule.ics with {len(events)} base VEVENTs "
      f"({len(SESSIONS)} recordings + milestones/gates + Day-1 + test + evergreen + recurring publish/slate/edit + Season 2 trigger). "
      "Every description carries DO / RIGHT LOOKS LIKE / ASSISTANT PROMPT.")

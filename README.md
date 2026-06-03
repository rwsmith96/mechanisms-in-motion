# Mechanisms in Motion: Launch Project

The launch plan for **Mechanisms in Motion**, the AES podcast that turns Amazon's internal operating mechanisms into playbooks any company can use. Tagline: *Day 1 Energy for Every Stage of Growth.*

**New here? Carla, start with [CARLA-START-HERE.md](CARLA-START-HERE.md).**

## What's in this repo

| File | What it is |
|---|---|
| [mim-podcast-roadmap.pdf](mim-podcast-roadmap.pdf) | The six-page roadmap: stack, hardware, workflow, scheduling, and the working-backwards timeline. Start here for the whole picture. |
| [mim-recording-schedule.ics](mim-recording-schedule.ics) | The project calendar. Import it into your calendar and it becomes the spine of the whole launch. |
| [mim-assistant-context.md](mim-assistant-context.md) | The canonical spec for any AI assistant helping run the show. Every calendar prompt points here. |
| [generate_ics.py](generate_ics.py) | Regenerates the calendar. Edit the dates/steps here and re-run; never hand-edit the `.ics`. |
| [CARLA-START-HERE.md](CARLA-START-HERE.md) | Plain-language onboarding for Carla: how to access everything and use the calendar. |

## How this project runs: the calendar is the spine

Import `mim-recording-schedule.ics` into your calendar. Every event, from "order the kits" to "record Episode 03" to "publish," carries three things in its notes:

1. **DO** the steps for that day.
2. **RIGHT LOOKS LIKE** the definition of done.
3. An **ASSISTANT PROMPT** you can paste straight into Claude or ChatGPT to get walked through the step.

To run any step, open its calendar event and either follow the checklist or paste the prompt. The roadmap PDF is the map; the calendar is how you drive it.

## Roles

- **Rich** owns logistics: tools, billing, hardware, editing, publishing, the booking system.
- **Carla** owns the guest slate: who comes on, in what order, the outreach, the question arc.

Both co-host every recording. Recording sprint: 8 episodes, Tue/Thu mornings, Aug 25 to Sep 17, 2026. Launch: weekly on Tuesdays from Sep 22.

## Updating dates

Dates are sensible defaults that flex around the real guest slate. To change them: edit the `SESSIONS` / `MILESTONES` lists in `generate_ics.py`, run `python3 generate_ics.py`, and re-import the new `.ics`.

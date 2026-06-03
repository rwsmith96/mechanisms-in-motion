# Export settings, in plain English

When you finish editing an episode in Descript, you "export" it: Descript bakes your edit into two finished files, one video for YouTube and one audio for the podcast apps. The roadmap lists exact numbers to use every time. Here is what each one actually means. You do not have to memorize them; this page exists so the words aren't scary, and the [Descript edit guide](descript-edit.md) tells you exactly where to click.

## The short version

Make every episode the **same loudness** as other professional shows, with **sharp video**, and make sure the **YouTube version and the podcast version sound identical**. Descript does almost all of this for you on export. That's the whole idea.

## Each setting, decoded

- **Loudness: −14 LUFS.** LUFS is just a way to measure how loud something feels to a human ear. Streaming platforms (Spotify, YouTube, Apple) automatically turn everything toward −14, so if you target −14 your show sits at the same volume as every other show. Get this wrong and your episode sounds noticeably quieter or louder than what the listener just played. (The minus sign is normal here; louder is closer to 0.)

- **True peak: −1.0 dBTP.** This is a tiny safety gap so the loudest moment (a laugh, a raised voice) never "clips," the harsh crackle you hear when audio is pushed too hard. −1.0 leaves a sliver of headroom so it always sounds clean.

- **Video: 1080p, 30fps, H.264 MP4.** "1080p" is the resolution (crisp HD, the standard for talking-head video; 4K is overkill and just makes files huge). "30fps" is 30 frames per second, how smooth the motion looks. "H.264 MP4" is simply the most universal video file type; YouTube and everything else accept it. Translation: a normal, high-quality HD video file.

- **Audio: stereo MP3/AAC, 48kHz.** MP3 and AAC are the standard small audio file types every podcast app plays. "48kHz" is the audio quality setting (fine for voice). "Stereo" just means two channels. Translation: a normal, high-quality podcast audio file.

- **Frame rate: 30fps locked across both kits + guests.** Everyone records at the same 30 frames per second. If one person is at a different rate, the audio and the lips slowly drift out of sync over an hour. Keeping everyone at 30 prevents that. (If a guest's camera records at an odd rate, Descript or a free tool called HandBrake can convert it first; the [Descript guide](descript-edit.md) covers it.)

- **Same audio bed in the video and the podcast file.** The "audio bed" is the cleaned-up sound from your edit. This rule just means the YouTube viewer and the podcast listener hear the *exact same* polished audio, not two different mixes. In practice: you clean the audio once, and both exports use it. Descript does this automatically as long as you export both from the same project.

## Do I have to set all this manually?

Mostly no. Descript's Creator plan has these as export presets, and Studio Sound plus the loudness normalization handle the loudness and peak for you. You pick "1080p" and "MP3," confirm loudness normalization is on, and export. The [Descript edit guide](descript-edit.md) walks the clicks. The [publish + QA guide](publish-and-qa.md) shows the 30-second check that confirms the numbers came out right.

## Paste this into a chatbot if you get stuck

```
I'm exporting a podcast episode from Descript and want it to match professional
streaming standards. Explain, in plain language for a non-technical person, how to
export TWO files from my Descript project: (1) a YouTube video at 1080p, 30fps, H.264
MP4, and (2) a podcast audio file as stereo MP3 at 48kHz, both normalized to about
−14 LUFS integrated with a −1.0 dBTP true-peak ceiling, using the same cleaned audio
in both. Tell me exactly which buttons/menus to click in current Descript, and a quick
way to confirm the loudness came out right.
```

---
type: project
title: Game Engine with Realistic Body Destruction Physics
date: 2026
status: prototype, playable in the browser since 2026-10-05
stack: [Macroquad, WebAssembly, GitHub Pages]
ai_written_code: [Rust, C++] # built by directing coding agents; C++ until the port to Rust on 2026-06-28
tags: [personal-project, game-engine, physics, simulation, agentic-coding, telemetry]
repo: https://github.com/AzizjonKasimov/realistic-human-body-deformation-physics
website: https://azizjonkasimov.github.io/realistic-human-body-deformation-physics/
case_study: https://azizjonkasimov.github.io/work/body-physics/ # on the portfolio site since 2026-10-11
demo_video: https://www.youtube.com/watch?v=YSuN8D9t4ZI # the October 2026 update; the June video is in the Proof Note
sources: ["LinkedIn Activity section visible on profile, viewed 2026-06-23", "YouTube demo video description, viewed 2026-09-26", "Repository history and GitHub language stats, checked 2026-09-26", "Update video transcript and the project's strike scenarios, 2026-10-06", "Repository, its verify run, and its project notes, checked 2026-10-11"]
---

# Game Engine with Realistic Body Destruction Physics

**Personal prototype, visible in LinkedIn Activity on 2026-06-23**

Prototype game-engine project built from scratch after experimenting with coding agents: in C++
at first, and in Rust (with Macroquad) since a port on 2026-06-28.
The LinkedIn activity post describes a 2D pixelated character with layered body-destruction
simulation: skin tears first, then muscles and bleeding, then bones. Fractured bones can damage
other tissue on impact, and joints simulate a realistic range of motion.

## Development Notes From LinkedIn Activity

- Started with a smaller 2D scope because Azizjon had no prior game-development experience.
- Used coding agents heavily, then improved agent effectiveness by adding telemetry and testing
  infrastructure so agents could debug behavior from clearer signals.
- Current limitations noted in the post: skin, muscles, and bones still interact imperfectly;
  the body does not yet feel sturdy enough under weapon impact; bone fracture behavior still
  uses primitive pre-made fracture patterns.
- Future direction noted in the post: try stronger models and a goal/loop workflow where agents
  continue experimenting until a target is reached.

## October 2026 Update

From the update video (published 2026-10-06) and the repository:

- Azizjon built the update with Claude Opus 5.5 by saying what looked wrong; every commit of the
  2026-10-05 and 2026-10-06 work names Claude Opus 5.5 as co-author.
- Damage follows the speed of a blow: a slow push does no harm, a medium hit mostly bruises, and
  only a hard hit breaks bones. Skin, muscle, and bone work together better than in June.
- The figure is a neutral mannequin, and the tools are a sledgehammer, a bat, and a knife.
- The same Rust app runs in the browser on GitHub Pages, phones included, so anyone can try it
  from a link.
- Feedback became automatic tests: 20 test scenarios check every change (the count that
  `strike_scenarios --list` printed on 2026-10-06).
- Limitation stated in the video: the injuries are still not close to real life. Next step named
  there: build on an existing open-source physics engine.

## Injuries Checked Against Research (2026-10-09)

From the repository, checked on 2026-10-11 (50 commits; all 35 October commits name Claude Opus
5.5 as co-author):

- Injuries follow published research: each strike scenario lists the real-life outcome, how often
  it happens, and its source (biomechanics, forensic, or medical studies, in the repo's
  `docs/INJURY_REFERENCE.md`). The figure stands for a 1.75 m adult, with a 4.5 kg sledgehammer
  head and a 0.8 kg bat. A rule for every play is that a knife never breaks a long bone, and the
  slow-push scenario checks that a slow push never breaks bone.
- 27 strike scenarios (`strike_scenarios --list` on 2026-10-11) run after every change, and a
  sweep plays each one 45 times (the swing moved along and across it, and bones at 0.8, 1.0, and
  1.25 of their strength), so outcomes that vary in real life are judged by how often they happen.
  All 27 were in band on 2026-10-11. Two checks are known gaps: a bat brought down on the
  shoulder never breaks the collarbone (in real life it usually does), and a hard bat always
  breaks the shin (it should only sometimes).
- The browser build simulates bit for bit like the Windows build. A one-bruise difference in one
  scenario was traced to the platform `atan2` function, which rounded differently in each build,
  and fixed by using the `libm` crate; a script compares both builds on every scenario.
- Techniques are studied and rebuilt from open source and papers, with the source credited in the
  code: knife cuts that open (Rapier's soft-body cuts), blood that runs down the skin
  (Overgrowth's surface blood), and bones that break where they bend most (NVIDIA Blast's stress
  solver). Moving the whole simulation onto Rapier was tried on a branch: it ran about 40% faster
  but met 15 of 20 scenarios against the engine's 20, so Azizjon turned it down.
- Sound is synthesized from what the simulation does; nothing is a recording.
- The app saves screenshots and film strips itself (capture mode), so Azizjon judges visual
  changes from pictures rather than numbers he cannot judge.
- The simulation steps 60 times a second on the visitor's device; the site has no server.
- 2026-10-11: the game's start screen gained an About section and an in-game About button
  (`I`) that link to the case study, the update video, and the source code.
- 2026-10-11 (commit 58301c7): injuries are drawn as they really look, shown fully but never
  exaggerated. Blood comes only out of wounds and is drawn at its real size; a blow reddens the
  skin at once and its bruise develops over about 17 minutes, as real bruises do (Scafide et al.
  2020; Randeberg et al. 2007); broken bone stays in the body, a fourth rule for every play.
  Still 27 strike scenarios.

## Proof Note

Confirmed on 2026-09-26 from the YouTube demo's description:

- Demo video: "Game Engine with Realistic Body Destruction Physics"
  (<https://www.youtube.com/watch?v=hCXVPSU6etE>, 6 minutes 28 seconds, published 2026-06-20 on
  the channel `@azizjon_kasimov`).
- Repository: <https://github.com/AzizjonKasimov/realistic-human-body-deformation-physics>
  (public, created 2026-05-02).
- The description says Azizjon wrote the engine from scratch in C++, with no prior
  game-development experience, after seeing how much coding agents had improved. The video shows
  that C++ version. On 2026-06-28 the repository was ported to Rust (commit "Port sandbox to Rust
  and polish body physics"), so the public code is Rust now.
- Because it was built with coding agents, list neither C++ nor Rust as a skill on the strength
  of it (the same rule as for the AI-built Android apps).
- Update video: "I Made My Body Physics Engine More Realistic With Claude Opus 5.5"
  (<https://www.youtube.com/watch?v=YSuN8D9t4ZI>, 4 minutes 4 seconds, published 2026-10-06),
  with the YouTube Short "My Body Physics Engine Got a Big Update"
  (<https://youtube.com/shorts/L87wyjLrdNE>, 20 seconds, published 2026-10-06), which links to it.
  The update video's materials are in the private `video_tools` repo
  (`videos/2026-10-06-physics-update/`).

Since 2026-10-11 the portfolio website features this project, at the user's request: a case
study at `/work/body-physics/` ("A body physics engine, checked against injury research", in all
six languages) and a third card in How I build. It describes the project as a realistic injury
simulation built by directing AI coding agents, names no programming language, and puts a content
note on the Play button. Its pictures show the body before any blow and one bruise, added at the
user's request once bruises developed like real ones: a moderate sledgehammer swing on the upper
arm (the `hammer_moderate_swing` scenario's blow, with the hand moved away afterwards; no bone
breaks), with the red mark right after the blow beside the bruise 17 simulated minutes later.

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
demo_video: https://www.youtube.com/watch?v=YSuN8D9t4ZI # the October 2026 update; the June video is in the Proof Note
sources: ["LinkedIn Activity section visible on profile, viewed 2026-06-23", "YouTube demo video description, viewed 2026-09-26", "Repository history and GitHub language stats, checked 2026-09-26", "Update video transcript and the project's strike scenarios, 2026-10-06"]
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

The portfolio website links the channel but does not feature this project.

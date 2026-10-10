---
name: motion-storyboard
description: "Turn a motion design brief into an actionable storyboard and frame-accurate timing plan. Use for animated explainers, product teasers, logo reveals, and animation preproduction; not for static layouts."
---

# Motion Storyboard

Create a motion plan another designer or coding agent can implement without inventing the sequence.

## Establish the brief

Extract the message, audience, visual identity, exact copy, destination, aspect ratio, duration, frame rate, and asset constraints. Reuse supplied choices. If a missing detail blocks implementation, ask about that detail; otherwise state a reasonable provisional choice. Preserve exact brand names, claims, and supplied text. Do not introduce an unsupported product feature or slogan.

Inspect actual assets before assigning them a role. Distinguish a provided logo, a temporary placeholder, and an asset still to be created. Identify whether the user wants a plan, an animatic, or a finished render; a storyboard request does not automatically authorize the full production.

## Design the sequence

Build the sequence around changes in meaning: establish, reveal, explain, resolve. Use only the beats the message needs. Give each scene one dominant focal point and connect transitions through a visual relationship such as shared position, shape, color, or direction.

For each scene, specify its frame range, visible content, hierarchy, motion, easing intent, transition, and any audio cue. Make reading holds explicit; entrance and exit animation are not reading time. A supplied soundtrack can guide timing, but do not invent a beat grid without inspecting it.

Read [the timing guide](references/timing.md) when converting duration to frames or planning beat boundaries. The bundled `scripts/frame_plan.py` can report exact frame count and preview sample positions; run it from this skill's actual installed directory.

## Deliver

Return the brief assumptions, scene table, asset list, and implementation notes needed for the chosen tool. Name unresolved inputs. If producing an animatic, inspect the actual playback and label unfinished visuals; do not present a written shot list as rendered animation.

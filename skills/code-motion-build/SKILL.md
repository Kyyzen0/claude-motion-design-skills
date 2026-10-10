---
name: code-motion-build
description: "Implement motion graphics as editable code using the available project stack and render a verifiable preview. Use for programmatic animations in web, SVG, canvas, Python, or an existing video-rendering framework."
---

# Code Motion Build

Turn the approved concept or supplied brief into editable animation source and a viewable result.

## Choose the execution path

Inspect the project stack, installed versions, existing render command, and available assets. Honor a requested tool. For an existing project, extend its animation approach before proposing another library. For a new project, choose the simplest available stack that can produce the requested deliverable and explain the choice briefly.

Do not claim an After Effects, Blender, or browser integration exists without verifying it. If the requested application is unavailable, make useful tool-independent planning progress and ask before substituting a different deliverable. Consult official documentation for unfamiliar or version-sensitive APIs.

## Structure the animation

Separate composition dimensions, palette, typography, timing, and asset paths from scene logic where this makes iteration easier. Keep parameters few and meaningful. Derive state from explicit time or frame indices so seeking and rendering reproduce the same frame. Seed randomness and avoid dependency on network requests or wall-clock time during frame generation.

Load fonts and assets before capture. Choose one time authority: do not combine a renderer's frame clock with independently advancing CSS animation or timers unless synchronization is intentional and verified. Clean up listeners, timers, GPU resources, and temporary DOM on lifecycle changes.

Read [the implementation guide](references/implementation.md) for preview and capture pitfalls.

## Produce and verify

Run the project's actual preview or render path. Inspect start, reveal, peak, settled, and final states plus playback at normal speed. Check destination size and frame rate. Inspect the output file itself rather than assuming that an exit code establishes successful visual output.

Deliver editable source, the requested preview or export, and concise run instructions. If rendering is blocked, preserve the runnable source and identify the exact missing capability. Do not call source code a finished video.

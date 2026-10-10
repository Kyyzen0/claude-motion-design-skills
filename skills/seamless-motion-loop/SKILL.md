---
name: seamless-motion-loop
description: "Create or repair seamless animation loops with consistent state and velocity at the wrap point. Use for looping backgrounds, logo loops, loading visuals, and procedural motion; not one-shot transitions."
---

# Seamless Motion Loop

Make the repeated playback feel continuous, not merely similar at its first and last frame.

## Define the loop

Record the period, frame rate, output dimensions, moving elements, and intended visual rhythm. Determine whether the loop is decorative, communicates progress, or must synchronize to audio. A looping loader must not imply a measured percentage without real progress data.

## Build periodic motion

Express state from an absolute phase when possible: phase = (time modulo period) / period. Use periodic position, rotation, opacity, and other animated properties. Match the wrap-point state and, for smooth continuous movement, the velocity. Matching endpoints alone can still create a visible acceleration jump.

Use seeded randomness or a construction that is periodic; unseeded per-frame noise cannot reliably replay. Include particle birth/death, trails, shadows, texture movement, and camera state in the seam check. A periodic source can still produce a discontinuity if temporal effects retain mismatched history.

Read [the loop guide](references/looping.md) for frame sampling and seam diagnostics. Keep fixed-step animation independent of wall-clock timing when rendering frames. Do not append a duplicate endpoint frame: one period is sampled over [0, period), not over an inclusive range ending at the same pose.

## Inspect the seam

Play at least three repetitions, including the last-to-first transition. Inspect the frames around the seam, not just the first and last stills. A nonzero pixel difference is normal for a moving object; compare it with ordinary neighboring-frame motion. Distinguish compression artifacts from source discontinuity.

For interface loops, respect reduced-motion preferences and avoid distracting indefinite movement when a static state serves the task.

## Deliver

Provide the source and requested rendered loop when tools permit. Report period, frame count, sampling convention, format, and seam checks actually performed. If only source was created, say the loop has not yet been visually verified.

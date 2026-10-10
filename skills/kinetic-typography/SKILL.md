---
name: kinetic-typography
description: "Create animated typography sequences with readable pacing, purposeful word emphasis, and stable layout. Use for title sequences, captions, typographic promos, and text-led motion graphics."
---

# Kinetic Typography

Animate text so its movement supports the meaning and its reading order stays clear.

## Lock the content

Use the exact supplied words, punctuation, language, and brand spelling. Confirm whether captions must match a provided recording. Do not replace the copy with a stronger marketing claim. Inspect available fonts and their usage rights; if the font is unavailable, name the substitute and do not present it as a faithful match.

## Compose before animating

Set type scale, line breaks, alignment, margins, contrast, and the mobile viewing size. Reserve enough space for the largest word and accents. Preview the longest line before building entrances. Use actual font metrics or browser measurement where available rather than guessing character widths.

Choose emphasis by sentence meaning: reveal a claim, separate a contrast, or land a key noun. Avoid equal animation on every word. Group phrases when word-by-word motion harms comprehension. Give each phrase a settled reading hold; validate it by reading at playback speed instead of imposing an arbitrary words-per-second rule.

## Build the sequence

Use a small coherent motion vocabulary. Specify reveal direction, overshoot if justified, settling, and exit. Avoid multiple overlapping focal points. Keep typographic weight and baseline relationships stable unless their change serves the concept.

In browser-based implementations, preserve semantic text and reading order. Keep split-letter decorative layers out of the accessibility tree, expose the full text once, and do not split inside a Unicode grapheme cluster. Provide a reduced-motion state that still conveys the full message.

## Verify and deliver

Check exact copy, clipping, line breaks, font loading, and pacing in actual playback at the destination dimensions. For a video, inspect sampled frames and the complete sequence. Report whether timing was reviewed against real audio, a provisional guide, or no soundtrack.

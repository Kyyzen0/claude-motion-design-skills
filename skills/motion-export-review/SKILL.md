---
name: motion-export-review
description: "Review rendered animation quality and export settings against a delivery brief. Use for final video, GIF, alpha, or web-animation handoff checks; not for authoring a new storyboard."
---

# Motion Export Review

Verify that the actual deliverable matches the brief and survives its target playback environment.

## Establish delivery requirements

Identify destination, aspect ratio, pixel dimensions, duration, frame rate, codec or container, transparency, audio, loop behavior, and any file-size limit. Use the user's explicit requirements; do not invent current platform limits. Verify official specifications when a platform-specific rule matters.

## Inspect the artifact

Read metadata with available tools and inspect actual playback. Check beginning, major transitions, reading holds, seam when looping, and the final frame. Look for clipped text, missing fonts, incorrect assets, accidental blank frames, stutter, banding, flicker, and unintended background changes. Inspect the smallest intended display size.

Read [the export guide](references/export.md) only for the relevant delivery mode. Do not infer alpha from the extension; verify the pixel format and transparent content. Distinguish intended transparent pixels from black compositing in the preview tool. Check audio presence, synchronization, and endpoint behavior when audio is requested.

## Optimize without changing the design

If a size limit is exceeded, try encoding settings before shrinking dimensions or shortening content. Preserve the master and create a separate export. Measure the resulting file size in bytes and compare it with the stated limit, clarifying decimal MB versus MiB when the boundary matters.

After re-encoding, inspect the result again. A smaller file can introduce banding, unreadable text, palette artifacts, or altered timing. Do not silently drop transparency or audio to meet a limit.

## Report

Give the artifact path, measured properties, checks performed, and issues with a timestamp or frame reference. Clearly separate metadata validation from visual playback review. If the task is review-only, report findings without replacing the source or export.

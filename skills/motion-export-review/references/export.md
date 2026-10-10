# Export checks by delivery mode

Use the current brief and verified target specifications for exact encoding settings. This guide describes checks rather than fixed platform presets.

## Video

When FFmpeg utilities are available, inspect metadata without modifying the file:

```sh
ffprobe -v error -show_streams -show_format -of json "output.mp4"
```

Compare stream dimensions, duration, codec, pixel format, nominal and average frame rates, and audio streams with the brief. Variable frame rate or timebase details may explain differences; do not infer a constant frame grid from a single field. Container duration can differ from individual stream duration.

Play the file and inspect representative frames. Confirm that an intended still hold remains still, transitions occur at the planned time, and the final frame is deliberate. Check sound against visual cues when synchronization matters.

## Transparency

Container extension does not establish alpha support. Verify an alpha-capable pixel format and actual transparent pixels. Preview over both light and dark backgrounds to reveal halos, premultiplication problems, and accidental matte colors. Preserve an alpha master before making an opaque delivery version.

## GIF or animated image

Inspect repeat behavior, frame delays, color palette, dithering, and transparency where supported. Fine gradients and small text can degrade despite acceptable file size. Compare playback duration with the planned duration; per-frame delay quantization may alter it.

## Web animation

Check the actual embed at intended dimensions, load behavior, interruption, resource weight, reduced motion, and keyboard interaction where applicable. A screen recording does not establish that the interactive source behaves correctly.

## Size limits

Measure file bytes. A decimal 1 MB limit is 1,000,000 bytes; 1 MiB is 1,048,576 bytes. If the requirement says “less than,” equality fails. Keep some margin when upload rules are uncertain, or verify the exact rule.

After each encoding change, recheck transparency, audio, dimensions, timing, and visual quality. Do not overwrite the only master or silently alter the delivery contract.

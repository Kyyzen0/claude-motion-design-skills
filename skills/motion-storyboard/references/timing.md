# Timing and frame boundaries

Use one frame rate for the plan and render. A frame index is zero-based. For a composition with N frames, valid indices are 0 through N−1. Express scene spans as half-open ranges: [start, end). Their length is end−start; adjacent scenes share a boundary without double-counting a frame.

For constant frame rate f, frame i represents time i/f. The intended duration is N/f. The last frame's timestamp is (N−1)/f, not the duration. An encoder displays that last frame for another frame interval.

Represent fractional frame rates explicitly, such as 30000/1001, when the deliverable uses them. Decimal 29.97 and 30000/1001 are not identical. Duration × frame rate must be an integer for an exact full-frame plan. If it is not, choose a frame count deliberately and report the realized duration; do not silently round a locked duration.

Run the bundled helper from this installed skill's directory:

```sh
python3 scripts/frame_plan.py --seconds 6 --fps 30 --samples 5
python3 scripts/frame_plan.py --frames 180 --fps 30 --samples 5
```

For six seconds at 30 fps:

| Scene | Frame range | Duration | Purpose |
| --- | --- | --- | --- |
| Establish | [0, 30) | 1 second | Introduce the existing logo |
| Explain | [30, 135) | 3.5 seconds | Reveal the supplied message and hold it |
| Resolve | [135, 180) | 1.5 seconds | Settle on the final brand lockup |

Those durations are an example, not a template for every brief. Reading speed depends on language, copy length, visual complexity, and audience. Test the hold by reading the actual copy at normal playback speed.

Distinguish scene timing from animated subevents. A 90-frame scene might use 12 frames for entry, 66 frames settled, and 12 frames for exit. Do not describe the full three seconds as a reading hold.

When audio is present, inspect the track or supplied cue timings. Snap selected cues to the frame grid, record the quantization error if it matters, and preserve the soundtrack's intended endpoint. A filename such as “120bpm” is not proof of its tempo or first-beat offset.

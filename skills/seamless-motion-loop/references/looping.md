# Loop construction and diagnostics

For a period T, let phase = (t mod T)/T. A position such as x = center + amplitude × sin(2π × phase) is periodic in state and velocity. Use integer cycles per period when multiple oscillations need to repeat together. Noninteger cycles generally break the wrap point.

Rotation by a full turn is visually periodic for an appropriately rendered object, although its raw angle changes. Compare rendered state rather than requiring every numerical parameter to be identical. Noise and particles need their own periodic construction; a random seed alone makes playback reproducible but does not guarantee a seamless loop.

Render N frames at times i/f for i in [0, N), with T = N/f. Do not add frame N as an extra duplicate first pose. That extra frame can create a perceptible pause and changes the cycle duration.

## Seam diagnosis

1. View several complete repetitions at playback speed.
2. Inspect frames N−2, N−1, 0, and 1 in sequence.
3. Compare the last-to-first movement with ordinary nearby movements. A moving edge naturally produces a pixel difference.
4. If the seam has a jump, trace all animated properties and temporal effects. Check position, orientation, opacity, particle age, trail accumulation, lighting, and camera.
5. If the seam pauses, look for a duplicated endpoint, asymmetric hold, variable frame timing, or export quantization.

Endpoint position continuity does not guarantee velocity continuity. A ping-pong movement can reverse abruptly at the endpoint. If the design needs a smooth reversal, settle speed at the turnaround; if it needs continuous circulation, use a periodic path instead.

Animated image formats and players can quantize frame delays or handle repeat metadata differently. Inspect the actual exported file in the intended player; source timing alone is insufficient.

# Implementation and preview checks

## Existing web project

Use the installed animation system. Inspect package versions and existing cleanup patterns. Keep interaction state authoritative; animation should visualize it. Use semantic elements and a reduced-motion variant for interactive output.

Before capture, wait for fonts and image assets to finish loading. Record the viewport and scale. Capturing a responsive layout at a different viewport can change line breaks and timing assumptions.

## Frame-based video project

Follow the project's frame-clock and render APIs. Derive every animated value from the supplied frame or time. Avoid independent timers and CSS animations that keep advancing while the renderer seeks a frame. Render a frame out of order to verify that its content does not depend on previous playback state.

Some procedural effects genuinely require simulation history. In that case, use a deterministic fixed-step precomputation or replay from a known state, and document the cost. Do not call a stateful simulation seek-safe without checking it.

## SVG, canvas, and procedural graphics

Keep logical composition dimensions separate from display dimensions. Check clipping, stroke width, pixel density, and text metrics. Ensure random placement has a stable seed and that assets resolve from the project rather than a developer's absolute path.

Prefer a small number of coherent shapes to dense decoration that becomes noise at the intended viewing size. Choose an actual visual hierarchy before adding movement.

## Native application or external renderer

Verify executable availability, version, and actual scripting access. Generate project-native source only when you know the required file format or API. Do not rename a text file with a project extension and call it an editable project.

## Handoff

Provide the actual entry point, command, relevant version constraints, asset locations, and output path. Distinguish interactive browser preview, rendered video, still-frame inspection, and compiled source. Identify audio provenance and license status when supplied assets have known restrictions; do not invent licensing clearance.

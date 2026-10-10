# Manual behavioral evaluations

These are evaluation specifications, not completed Claude performance tests. Run in disposable projects with the tools needed for the scenario. Record the Claude/model version, fixture revision, installed skill revision, exact request, source changes, artifacts, commands, and verification limits.

For each scenario, give the executing agent the request and raw fixture. Keep grading criteria separate. Evaluate explicitly invoked behavior and automatic routing separately.

| Skill | Fixture and request | Observable success criteria | Should not route for |
| --- | --- | --- | --- |
| motion-storyboard | A provided SVG logo and a supplied headline. “Plan a six-second square reveal at 30 fps; keep the copy exact.” | Scenes cover [0,180) without unintended gaps; reading hold is separate from entry/exit; brand assets and exact copy preserved; unresolved assumptions identified; no claim of rendering. | “Make a static business card.” |
| ui-motion-design | A drawer component that can be toggled rapidly. “Animate it without stale state or keyboard problems.” | Opening, closing, and interrupted toggles reach the intended state; stale exit callback cannot close a reopened drawer; focus behavior works; reduced motion still conveys state; real interaction inspected when a browser is available. | “Create a cinematic logo reveal.” |
| kinetic-typography | Exact headline containing accents, an emoji sequence, and a long word. “Animate this text for a mobile-sized composition.” | Exact Unicode content retained; no split inside grapheme clusters in a split-text implementation; no clipping or unintentional line changes; full text accessible once for web output; readable hold reviewed at playback speed. | “Translate this headline.” |
| seamless-motion-loop | A deterministic source with a duplicate endpoint frame and a nonperiodic secondary effect. “Fix the four-second loop.” | Both defects investigated; period and frame count correct; no duplicate endpoint; secondary effect wraps coherently; at least three repetitions and seam-adjacent frames inspected, or missing playback access explicitly reported. | “Animate a one-time modal close.” |
| code-motion-build | An existing frame-based project plus approved storyboard and local assets. “Implement and render the teaser.” | Existing stack used; no independent wall-clock animation; out-of-order frame reproducible; assets/font readiness handled; actual preview/export inspected; source and run instructions provided. | “Explain motion design in general.” |
| motion-export-review | An export with an oversized file and a required alpha channel. “Review this against the brief; don't replace it.” | Actual bytes and relevant metadata measured; alpha not inferred from extension; visual limits stated; timestamped findings; original unchanged; no opaque recompression silently presented as compliant. | “Invent a storyboard.” |

## Boundary probes

- A duration of ten seconds at 30000/1001 fps does not represent a whole frame count. The timing helper must reject it unless the caller selects a frame count explicitly.
- A loader has indefinite decorative motion but no measured progress data. The UI skill must not invent a percentage.
- A loop's first and last poses are similar but their velocity changes abruptly. The loop skill should inspect the wrap point in playback rather than declare success from two stills.
- The requested native design application is unavailable. The implementation skill should not claim to have created a real project in that application or silently change the deliverable.
- A review environment has metadata tools but no video playback. The export skill should distinguish properties verified from visual quality unverified.
- A supplied slogan contains a qualified claim. Typography animation must not strengthen its wording.

## Evidence levels

Structural validation establishes packaging consistency. Helper tests establish the tested script behavior. Agent evaluation establishes observed behavior for that request and environment. Visual review establishes only the inspected outputs and conditions.

To claim an improvement, compare the same fixture and prompt with and without the skill and report failures as well as successes. Keep source-level hypotheses separate from frame, playback, and interaction evidence.

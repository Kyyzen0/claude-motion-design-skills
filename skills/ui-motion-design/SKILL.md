---
name: ui-motion-design
description: "Design and implement purposeful interface motion for state changes, navigation, feedback, and transitions. Use for microinteractions and animated UI behavior, not standalone promotional videos."
---

# UI Motion Design

Use movement to explain an interface change while preserving control and readability.

## Understand the state transition

Inspect the component, its state model, and existing motion conventions. Identify what the user did, what changed, and which element needs attention. Separate entry, exit, progress, and error feedback. Do not make essential feedback depend on completing a decorative animation.

Choose the smallest motion that communicates the relationship. Shared-element motion can preserve spatial context; a brief opacity change may be enough for a status label. Avoid animating every child when it obscures the active task.

## Specify and implement

Use the current stack and version. Define the start state, end state, duration, easing, interruption behavior, and reduced-motion alternative. Treat timing ranges as hypotheses to test in context rather than universal rules.

For layout motion, compare transform-based animation with actual layout changes. Prefer transforms and opacity when they preserve the intended result, but do not claim they guarantee smoothness. Measure expensive paint, layout, or large surfaces when there is an observed performance problem.

Handle rapid repeated clicks, reversing a transition, component unmount, and asynchronous completion. Cancel or replace obsolete work; a delayed callback must not restore stale UI. Exit effects must not leave hidden controls focusable or block keyboard input. Read [the UI motion checklist](references/ui-motion.md) for lifecycle and accessibility checks.

## Verify

Exercise the real interaction at normal speed, under interruption, and with reduced motion enabled. Check keyboard focus and final state. Inspect narrow and wide layouts when both are supported. Automated state assertions complement playback inspection; they do not prove the visual rhythm is right.

Deliver the implemented interaction, checked cases, and any unavailable runtime evidence. If asked only for design advice, return a concrete motion specification without modifying the app.

# UI motion lifecycle checklist

Use the sections relevant to the component.

## Interrupted transitions

- Define what happens when the target changes before completion: continue from the current visual state, restart, reverse, or snap. Test the chosen behavior.
- Keep the logical final state independent of a callback that may never fire. An animation can be canceled, a node can unmount, or reduced motion can remove its duration.
- Remove stale asynchronous work. An exit completion must not close a newly reopened panel.
- Verify that hidden elements are not keyboard reachable. Manage focus according to the component's semantics rather than according to decorative movement alone.

## Reduced motion

For web interfaces, inspect `prefers-reduced-motion` support in the existing styling or animation system. Reduce large translation, parallax, repeated oscillation, and zoom while preserving state information. The fallback may be a static state or a brief non-spatial change; choose it for the actual interaction.

Check both a preference present at launch and a changed preference when the project supports live updates. Avoid globally setting every duration to a tiny value without testing event-dependent logic.

## Loading and feedback

A looping animation indicates activity; measured progress requires real progress data. Keep the label available when motion is disabled. Give success and failure different semantic states rather than relying only on color or a bounce.

## Performance evidence

Use the browser or target runtime's profiler when motion visibly stutters or involves expensive work. Check layout, paint, compositor work, and resource size. Report the device and test conditions. `transform`, `opacity`, and `will-change` are not a substitute for measurement; persistent unnecessary layers can increase memory use.

# Contributing

Keep each skill focused on one production stage. Instructions should improve a motion-specific decision: timing, hierarchy, continuity, rendering, interaction, or delivery. Avoid generic creativity advice and mandatory software when the workflow does not need it.

Shared frontmatter uses only `name` and a single JSON-quoted `description`; JSON strings are valid YAML scalars. Match the directory name to `name`. References and helpers must remain within the installed skill folder. Do not add dependencies on another skill's filesystem location.

For a change:

1. Explain the motion problem and the behavior the skill should improve.
2. Update the relevant manual evaluation scenario, including a routing counterexample.
3. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
4. Add executable tests when changing helper behavior.
5. If claiming visual or behavioral success, provide the actual playback or agent-evaluation evidence and its limits.

Use official documentation for version-dependent APIs. Include only original instructions and assets you have permission to distribute. Do not commit private briefs, client media, licensed font files, credentials, or machine-specific paths.

Repository content is in English. When a skill runs, preserve the user's requested language and the exact language of supplied typography.

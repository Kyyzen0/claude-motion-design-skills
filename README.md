# Claude Motion Design Skills

Six practical skills for planning, implementing, and reviewing motion design with Claude Code.

Build clearer storyboards, purposeful UI transitions, readable kinetic typography, seamless loops, and editable animations. Each skill focuses on a distinct production stage and includes checks that separate written plans, working source, and visually verified exports.

These are workflow skills, not a video-generation model or an After Effects integration. They use the tools available in your environment. Rendering may require a browser, FFmpeg, a project renderer, or the application you choose; the pack itself does not install those tools or provide assets, fonts, or music.

## The skills

| Skill | What it helps produce | Example invocation |
| --- | --- | --- |
| [motion-storyboard](skills/motion-storyboard/SKILL.md) | Brief, scene sequence, frame ranges, reading holds, asset list | `/motion-storyboard Plan a 6-second logo reveal at 30 fps using the supplied logo.` |
| [ui-motion-design](skills/ui-motion-design/SKILL.md) | UI motion with interruption handling and reduced-motion behavior | `/ui-motion-design Animate this settings drawer; handle rapid toggles and keyboard focus.` |
| [kinetic-typography](skills/kinetic-typography/SKILL.md) | Text-led animation with meaningful emphasis and readable pacing | `/kinetic-typography Animate the supplied headline; keep the exact words and accent marks.` |
| [seamless-motion-loop](skills/seamless-motion-loop/SKILL.md) | Repeatable motion with a checked wrap point | `/seamless-motion-loop Create a 4-second looping logo animation with no pause at the seam.` |
| [code-motion-build](skills/code-motion-build/SKILL.md) | Editable animation source and a verified preview when rendering is available | `/code-motion-build Implement this approved storyboard in the existing animation project.` |
| [motion-export-review](skills/motion-export-review/SKILL.md) | Export review with measured properties and frame or timestamp findings | `/motion-export-review Check this loop, transparency, timing, and the 5 MB delivery limit.` |

## Install for Claude Code

Clone this repository:

```sh
git clone https://github.com/Kyyzen0/claude-motion-design-skills.git
cd claude-motion-design-skills
```

Use Python 3.10 or newer. The installer has no third-party dependencies. On Windows, `py -3` can replace `python3`.

Install into an existing project:

```sh
python3 scripts/install.py --project /path/to/your/project
```

Or install for your user account:

```sh
python3 scripts/install.py --user
```

Preview a selected installation first:

```sh
python3 scripts/install.py --project /path/to/your/project --skill kinetic-typography --dry-run
```

Use multiple `--skill` arguments to select several skills. With none specified, all six are installed. The installer copies full folders into `.claude/skills/` inside the chosen project or user home. It does not overwrite existing skills or modify Claude settings. To update, inspect and move the previous folder before installing the replacement. A failed copy may leave a partial destination; inspect it before retrying.

Manual installation: copy the desired directories from `skills/` into your project's `.claude/skills/` or `~/.claude/skills/`. Keep references and scripts inside each copied skill folder.

Start a new Claude Code session and invoke a skill with `/skill-name`, or describe a task matching its description. Local discovery can be restricted by your organization's settings. Local user-directory installation does not install skills into Claude.ai, Cowork, or cloud sessions. See the [official Claude Code skill documentation](https://code.claude.com/docs/en/skills) for those environments. Installation paths and invocation syntax were checked on October 10, 2026.

## Example production brief

```text
/code-motion-build
Create a 6-second, 1080×1080, 30 fps logo reveal using assets/logo.svg.
Use the existing project renderer. Preserve the logo geometry and brand colors.
Reveal the logo, hold it, then settle on the final lockup.
No extra copy, soundtrack, or generated assets.
Deliver editable source and an MP4 preview, and report which playback checks ran.
```

If you do not have an approved concept yet, start with `/motion-storyboard`. If you only need a critique or export review, request that scope explicitly. Skills do not authorize paid services, publishing, unrelated redesigns, or replacing your chosen production tool.

## Exact timing helper

`motion-storyboard` includes a dependency-free timing helper:

```sh
python3 skills/motion-storyboard/scripts/frame_plan.py --seconds 6 --fps 30 --samples 5
python3 skills/motion-storyboard/scripts/frame_plan.py --frames 300 --fps 30000/1001
```

The helper reports exact rational duration, frame count, an exclusive end boundary, and preview sample frames. It rejects durations that cannot span an integer number of frames at the chosen rate, so you choose any rounding deliberately. It does not render animation, determine reading speed, or verify a loop seam.

## Validate the pack

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validation checks the pack's restricted YAML frontmatter, skill names, local links, and Python syntax. Helper tests check rational timing, frame boundaries, sample indices, installation, conflict preservation, and execution from the installed directory. GitHub Actions runs these checks on Linux, macOS, and Windows.

These checks do not prove that Claude follows the skills or that an animation is visually successful. The skills have not yet been benchmarked in real Claude sessions. See [behavioral evaluation scenarios](evals/SCENARIOS.md) for fixture-based tasks and grading criteria.

## Repository layout

```text
skills/
  motion-storyboard/          # Storyboard + timing guide + frame helper
  ui-motion-design/           # UI lifecycle and accessibility checks
  kinetic-typography/         # Text composition and animation
  seamless-motion-loop/       # Periodic motion and seam diagnostics
  code-motion-build/          # Implementation and preview workflow
  motion-export-review/       # Delivery and encoding checks
scripts/                     # Installer and repository validator
tests/                       # Executable-helper tests
evals/                       # Manual agent evaluation specifications
```

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). [MIT licensed](LICENSE). This is an independent project and is not affiliated with Anthropic or any animation software vendor.

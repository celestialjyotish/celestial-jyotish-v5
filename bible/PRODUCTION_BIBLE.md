Celestial Jyotish V5 --- Production Bible
Status: V5 foundation  
Document role: Master operating specification for the automated
content-production system.
---
1. Purpose
Celestial Jyotish V5 converts an astrology topic into a complete,
production-ready video package through a staged, quality-gated pipeline.
The system must preserve two goals simultaneously:
Teach real Jyotish accurately.
Present it with cinematic storytelling strong enough to hold
attention.
A beautiful scene that teaches nothing fails. An accurate scene
presented as a static talking head also fails the creative direction.
---
2. Source-of-Truth Hierarchy
When instructions conflict, use this order:
Current Character Bible --- identity and continuity of Dev/Asha.
Current Voice Bible --- voice and narration/lip-sync behavior.
Current Production Bible --- pipeline, QC, asset and publishing
rules.
Creative Brief --- brand philosophy and storytelling direction.
Topic-specific research and classical sources --- factual
Jyotish content.
Previous production examples --- examples only; never override
current bibles.
Model-generated suggestions --- never treated as authoritative
facts.
A previous prompt, script, or generated scene must not silently override
a current bible.
---
3. Creative North Star
SHOW > EXPLAIN
Astrological concepts should be expressed through visible human behavior
whenever possible.
Example:
> A line about anger versus conscious decision-making should show a real
> flash of anger followed by the character catching himself and choosing
> to repair the moment.
The viewer should be able to understand the broad idea from the action
even with the audio muted.
Motion is mandatory
Characters should not simply stand, sit, or recite information to
camera.
Every scene should contain a meaningful physical task, interaction,
movement, or environmental action.
Friction and repair
Dev and Asha should not exist in permanent harmony. Appropriate stories
can contain:
friction → consequence → awareness → conscious repair
The repair should normally be demonstrated through action rather than a
lecture.
Common-man grounding
Cosmic or technical Jyotish concepts should be translated into
recognizable human situations: relationships, work, money, family
pressure, decisions, responsibility, trust, deadlines, uncertainty, and
ordinary choices.
Dev and Asha are characters inside grounded reality, not supernatural
gods.
Glamour is a branding layer
Premium glamour can help establish the Celestial Jyotish visual
identity, but it must remain in service of story, trust, and dignity. It
should never become explicit or vulgar.
---
4. Story Architecture
For a 12--15 scene episode, use a three-act structure:
Act I --- Friction of brilliance
Establish the placement's useful strength while showing the raw or
unrefined side creating a visible problem.
Act II --- The catalyst
Another character, event, or consequence challenges or grounds the first
character.
The unresolved issue should affect something tangible such as money,
trust, work, family, or another meaningful stake.
Act III --- Depth and resolution
The astrological energy is channelled constructively through a concrete
common-person action.
The ending should demonstrate what an ordinary person could actually do.
---
5. Script Standards
Language
Target:
70% Hindi / 30% English
Hindi should be conversational, respectable, simple, and easy to follow
aloud.
Avoid unnecessarily academic vocabulary.
Technical accuracy
Technical Jyotish terminology is allowed when it materially helps the
explanation.
Do not remove technical content merely because it is technical.
Instead:
explain the term through context,
connect it to a visible consequence,
avoid stacking unexplained terminology,
adapt depth to the audience and platform.
For example, a technically useful statement such as:
> सप्तम भाव में मंगल अपनी विशेष दृष्टि से लग्न और द्वितीय भाव को प्रभावित करता है।
can remain technical when the surrounding narration makes its practical
meaning understandable.
Research bar
Topic scripts should be checked against:
classical Jyotish texts,
established Jyotish literature,
reputable modern sources where relevant.
Every substantive astrological claim should have a traceable research
basis before it reaches the final script.
No repeated information
Each scene should advance the explanation rather than restating an
earlier point.
---
6. Attention Architecture
The V5 attention system is not a claim about literally manipulating
dopamine. It is a structured storytelling system using:
pattern interruption,
self-relevance,
curiosity gaps,
emotional salience,
anticipation,
progressive disclosure,
micro-payoffs,
visual salience,
object memory anchors,
narrative tension,
meaningful resolution.
Opening principle
The opening should establish a human problem or surprising consequence
before delivering heavy technical explanation.
Retention principle
Every scene should provide at least one of:
new information,
new consequence,
emotional change,
visual transformation,
unanswered tension,
meaningful payoff.
---
7. Production Pipeline
``` text
TOPIC
  ↓
RESEARCH
  ↓
ASTROLOGY VERIFICATION
  ↓
FACT PACK
  ↓
STORY ARCHITECTURE
  ↓
SCRIPT
  ↓
SCRIPT EVALUATION
  ↓
REVISION
  ↓
SCENE PLAN
  ↓
IMAGE SEEDS
  ↓
MASTER IMAGES
  ↓
VIDEO GENERATION
  ↓
VOICE
  ↓
SFX / MUSIC
  ↓
LIP-SYNC WHEN REQUIRED
  ↓
SUBTITLES / GRAPHICS
  ↓
FFMPEG ASSEMBLY
  ↓
TECHNICAL QC
  ↓
CREATIVE QC
  ↓
FINAL MASTER
  ↓
PLATFORM PACKAGING
  ↓
APPROVAL GATE
  ↓
PUBLISH / SCHEDULE
  ↓
ANALYTICS
```
---
8. Machine-Readable Stage Contracts
The pipeline should not treat the entire production as one giant
generation request.
Recommended intermediate artifacts:
``` text
facts.json
astrology_verification.json
story_architecture.json
script.json
evaluation.json
revised_script.json
scenes.json
image_prompts.json
video_prompts.json
voice_plan.json
audio_plan.json
subtitle_plan.json
edit_plan.json
qc_report.json
publishing_package.json
```
Each stage consumes a validated artifact and produces the next artifact.
---
9. Quality Gates
Gate 1 --- Research
Required:
claims identified,
source attached to each substantive claim,
contradictions flagged,
uncertain claims marked `UNCERTAIN`,
no unsupported deterministic prediction inserted.
Gate 2 --- Astrology verification
Required:
planetary/house/sign relationships checked,
technical terminology checked,
interpretation separated from textual rule,
source traceability preserved.
Gate 3 --- Story
Required:
human problem,
visible action,
meaningful stakes,
escalation,
resolution,
no scene that exists only to recite information.
Gate 4 --- Script
Required:
understandable Hindi,
controlled English usage,
no unnecessary jargon,
no repetitive points,
timing-compatible dialogue,
factual claims traceable to the fact pack.
Gate 5 --- Scene
Required:
character continuity,
action matches narration,
props already exist in the image seed,
no talking-head-only scene,
camera movement is purposeful.
Gate 6 --- Generation
Required:
correct aspect ratio,
correct character identity,
no unintended text/logos,
motion continuity,
acceptable anatomy,
acceptable temporal consistency.
Gate 7 --- Final video
Required:
correct audio,
clean voice,
subtitles synchronized,
no accidental generation artifacts,
no unauthorized watermark/provenance alteration,
correct export dimensions and frame rate.
---
10. Video Prompt Contract
For engines using the Creative Brief's current production format:
approximately 30--60 words per video prompt,
one primary action,
one camera movement,
one audio direction,
one preservation/continuity instruction,
natural flowing sentences rather than bracket-heavy scaffolding,
approximately 5--8 second clips as the stable base unit,
longer sequences chained from an appropriate continuation frame
rather than forcing one oversized generation.
Do not force artificial timestamped micro-beats into fluid physical
actions.
Timestamps may be used for planning and editing, but should not
unnecessarily dictate every internal movement of the generation model.
---
11. Image → Video Continuity
The image is the visual seed.
Therefore:
> Every important prop used by the video action must already exist in
> the image seed.
Do not introduce a new major object halfway through a video prompt
unless the selected generation engine has been explicitly validated for
that behavior.
The scene plan should identify:
subject,
environment,
wardrobe,
key prop,
lighting,
camera,
physical action,
emotional state,
continuity requirement.
---
12. Audio Architecture
Narration
Narration normally runs while characters perform physical actions with
lips closed.
On-screen speech
Only genuine visible character speech should trigger lip-sync.
Voice continuity
Use the current Voice Bible as the authority for:
Dev voice,
Asha voice,
speed,
resonance,
stability,
emotional register,
Hindi/English delivery.
The production system must not allow a generated scene to silently
change the established character voice.
---
13. Generation Stack
The V5 architecture is intentionally model-agnostic.
Current planned roles:
``` text
PydanticAI
    ↓
Model / Agent Pool
    ├── Gemini
    ├── Claude
    ├── Nemotron
    └── Jev
    ↓
Research / Story / Script / Evaluation
    ↓
ComfyUI
    ├── image workflows
    ├── video workflows
    ├── audio workflows
    └── synchronization workflows
    ↓
FFmpeg
    ↓
Final Master
```
Role separation
PydanticAI - typed orchestration, - structured outputs, -
validation, - tool calling.
LiteLLM - provider/model gateway, - model switching, - centralized
model configuration.
Nemotron - research/reasoning worker where appropriate, -
alternative model in the pool, - not the workflow framework.
Jev - structured evaluator/decision layer, - confidence and QC
signals, - not the primary creative writer.
Promptfoo - evaluation and regression testing, - especially suitable
for GitHub Actions CI.
ComfyUI - local generation control layer, - reusable generation
workflows, - image/video/audio model integration.
FFmpeg - deterministic final assembly, - subtitles, - audio
mixing, - transitions, - export.
---
14. Watermark and Provenance Rule
The pipeline must prefer generation paths that produce a clean final
asset under their applicable license and product terms.
Never build a workflow around:
removing a required watermark,
obscuring provenance,
altering a provider's required attribution,
bypassing a licensing restriction.
If a provider requires a watermark or provenance marker, the system
should either:
retain it, or
select a different generation route whose terms permit the intended
output.
---
15. Asset Naming
Use deterministic names.
Example:
``` text
CJ_V5_E001_SC003_IMG_v001.png
CJ_V5_E001_SC003_VID_v001.mp4
CJ_V5_E001_SC003_VO_DEV_v001.wav
CJ_V5_E001_SC003_SFX_v001.wav
CJ_V5_E001_SC003_SUB_v001.srt
```
Recommended episode structure:
``` text
episode/
  research/
  story/
  script/
  scenes/
  images/
  video/
  voice/
  audio/
  subtitles/
  edit/
  qc/
  publish/
```
Never overwrite a production asset without versioning.
---
16. Publishing Safety
Publishing is a separate state machine.
``` text
DRAFT
  ↓
READY_FOR_REVIEW
  ↓
APPROVED_FOR_PUBLISH
  ↓
PUBLISHED
```
The automation must never jump directly from generation to publishing.
A final human approval gate should exist before a production system is
trusted with automatic public publishing.
---
17. Platform Packaging
The master production asset should be separated from platform-specific
packaging.
Create a common master first, then generate:
YouTube package,
Instagram package,
Facebook package,
X package,
Dailymotion package,
Atoplay package.
Each package may have its own:
title,
description,
hashtags,
thumbnail,
caption,
duration/format constraints,
publishing metadata.
Publishing time should eventually be determined from the connected
platform's own audience/engagement data rather than a universal assumed
"best time."
---
18. Cost Control
The system should prefer:
local/open models where quality is sufficient,
API calls only where they materially improve quality,
cached research and reusable outputs,
evaluation before expensive generation,
low-cost drafts before final renders.
Do not generate expensive video before the research, script, and scene
plan pass their quality gates.
---
19. Failure Handling
Every stage should return a machine-readable result.
Minimum status vocabulary:
``` text
PASS
REVISE
BLOCK
ERROR
UNCERTAIN
```
Examples:
unsupported astrology claim → `BLOCK`
weak visual action → `REVISE`
provider unavailable → `ERROR`
ambiguous source interpretation → `UNCERTAIN`
fully validated scene → `PASS`
The system should not silently continue after a `BLOCK`.
---
20. Final Principle
Celestial Jyotish V5 is not a prompt generator.
It is a research → reasoning → storytelling → generation →
verification → publishing system.
The model may change.
The provider may change.
The generation engine may change.
The production contract does not.
The enduring requirements are:
accurate Jyotish + human story + visible action + character
continuity + cinematic presentation + measurable QC + safe publishing.
---
Source Basis
This document incorporates the standing Celestial Jyotish Creative
Brief, particularly its requirements for common-man storytelling, SHOW
> EXPLAIN, mandatory motion, friction and repair, three-act structure,
premium-but-dignified glamour, 70% Hindi / 30% English,
classical/reputable research, scene duration discipline, video-prompt
constraints, image-to-video prop continuity, narration/lip-sync
separation, and thumbnail standards.
Current V5 architecture decisions are explicitly marked as project
decisions and do not claim to be statements from the Creative Brief.

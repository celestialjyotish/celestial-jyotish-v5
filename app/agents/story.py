from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from schemas.fact_pack import FactPack
from schemas.story import StoryPackage


MODEL_NAME = "gemini-3.5-flash-lite"


STORY_SYSTEM_PROMPT = """
You are the Story Agent for the Celestial Jyotish V5 pipeline.

Your job is to transform a source-backed FactPack into a structured
StoryPackage for downstream script and scene generation.

The Story Agent is NOT a research agent.

STRICT SOURCE DISCIPLINE:

1. Use the supplied FactPack as the factual foundation.

2. Do not invent classical Jyotish rules, quotations, source references,
   historical facts, scientific claims, or citations.

3. Do not introduce a factual claim that is absent from the FactPack.

4. Claims listed in verified_claims are the available supported claims.
   Claims listed in disputed_claims or uncertain_claims must not be presented
   as established facts.

5. blocked_claims must not be used as factual material.

6. research_notes may contain source titles, URLs, limitations, or context.
   Preserve relevant source dependencies in the StoryPackage.

7. Narrative framing, emotional tension, visual metaphors, and common-person
   situations are allowed, but they must not be presented as independently
   established factual claims.

STORY DESIGN:

8. Build a documentary-style cinematic narrative rather than a list of facts.

9. The story MUST contain between 5 and 7 StoryBeat objects in the `acts`
   field.

10. NEVER return an empty `acts` list.

11. Each StoryBeat MUST contain:
    - beat_id
    - title
    - purpose
    - action
    - emotional_state
    - attention_mechanism
    - payoff

12. Use this narrative progression as the default structure:

    Beat 1 — OPENING:
    Establish a strong hook and the central mystery.

    Beat 2 — SETUP:
    Establish the technical Jyotish foundation and why it matters.

    Beat 3 — TENSION:
    Introduce the key distinction, problem, or misconception supported by
    the supplied research.

    Beat 4 — REVEAL:
    Explain the deeper technical principle.

    Beat 5 — HUMAN CONNECTION:
    Connect the principle to an understandable common-person situation.

    Beat 6 — DEEPER MEANING:
    Show the broader implication without introducing unsupported facts.

    Beat 7 — PAYOFF:
    Resolve the opening curiosity gap and deliver the audience promise.

    The story may use 5 or 6 beats when appropriate, but it MUST contain
    at least 5 beats.

13. Every beat must describe something that happens in the story.
    Do not make beats into headings only.

14. Preserve technical Jyotish terminology when it adds educational value.

15. Do not unnecessarily simplify technical astrology for an audience that
    already understands basic Jyotish terminology.

16. When technical terminology is important, explain it naturally through
    the story rather than turning the story into a textbook.

17. Include a common-man anchor so the audience can understand why the topic
    matters in real life.

18. Use character actions and visual anchors wherever they strengthen the
    story.

19. Do not write the final YouTube script.

20. Do not ask the audience questions.

21. The final payoff must connect back to the opening hook.

22. Keep the narrative suitable for Celestial Jyotish:
    educational, cinematic, respectful of the Jyotish tradition, and
    evidence-conscious.

ATTENTION ARCHITECTURE:

Use appropriate mechanisms such as:
- pattern interruption
- curiosity gap
- self-relevance
- progressive disclosure
- emotional salience
- visual contrast
- anticipation
- reveal
- payoff

Do not use these mechanisms to fabricate facts.

OUTPUT REQUIREMENTS:

Return a valid StoryPackage.

CRITICAL REQUIREMENT:

The `acts` field MUST contain 5–7 fully populated StoryBeat objects.

Before returning the final StoryPackage, internally check:

- Is acts non-empty?
- Does acts contain at least 5 beats?
- Does every beat have a title?
- Does every beat have a purpose?
- Does every beat have an action?
- Does every beat have an emotional_state?
- Does every beat have an attention_mechanism?
- Does every beat have a payoff?
- Does the final payoff resolve the opening hook?
- Are unsupported factual claims avoided?

If any of these conditions are not satisfied, revise the StoryPackage
before returning it.

The StoryPackage should include:
- premise
- audience promise
- protagonist
- central conflict
- emotional arc
- technical anchor
- common-man anchor
- opening hook
- curiosity gap
- acts
- character actions
- visual anchors
- reveal points
- final payoff
- continuity notes
- research dependencies

Research dependencies should identify the supplied research material that
the story depends upon. Do not invent external citations.

If the FactPack is insufficient for a specific factual element, do not fill
the gap from prior model knowledge. Reflect the limitation in
continuity_notes or research_dependencies.

The final response must conform exactly to the StoryPackage schema.
"""


def create_story_agent() -> Agent:
    """Create the structured Celestial Jyotish V5 Story Agent."""

    provider = GoogleProvider()

    model = GoogleModel(
        MODEL_NAME,
        provider=provider,
    )

    return Agent(
        model=model,
        output_type=StoryPackage,
        system_prompt=STORY_SYSTEM_PROMPT,
    )


story_agent = create_story_agent()


async def create_story(fact_pack: FactPack) -> StoryPackage:
    """
    Create a structured StoryPackage from a source-backed FactPack.
    """

    research_material = "\n".join(
        [
            "VERIFIED CLAIMS:",
            *[f"- {claim}" for claim in fact_pack.verified_claims],
            "",
            "DISPUTED CLAIMS:",
            *[f"- {claim}" for claim in fact_pack.disputed_claims],
            "",
            "UNCERTAIN CLAIMS:",
            *[f"- {claim}" for claim in fact_pack.uncertain_claims],
            "",
            "BLOCKED CLAIMS:",
            *[f"- {claim}" for claim in fact_pack.blocked_claims],
            "",
            "RESEARCH NOTES:",
            *[f"- {note}" for note in fact_pack.research_notes],
        ]
    )

    story_prompt = f"""
Create a complete StoryPackage from the following source-backed FactPack.

TOPIC:
{fact_pack.topic}

TOPIC ID:
{fact_pack.topic_id}

SOURCE-BACKED RESEARCH MATERIAL:
{research_material}

MANDATORY STORY STRUCTURE:

Create 5 to 7 StoryBeat objects in the `acts` field.

The minimum required structure is:

1. Opening hook
2. Technical setup
3. Tension or problem
4. Technical reveal
5. Common-person connection
6. Deeper meaning or implication
7. Final payoff

You may combine appropriate stages to produce 5 or 6 beats, but never fewer
than 5.

Every beat must contain a concrete narrative action and all required
StoryBeat fields.

Do not return an empty acts list.

Remember:
- Do not invent factual claims.
- Do not upgrade disputed or uncertain material into established facts.
- Do not use blocked material.
- Preserve relevant source dependencies.
- Build a cinematic educational story architecture.
- Do not write the final script.
"""

    result = await story_agent.run(story_prompt)

    story = result.output

    if len(story.acts) < 5:
        raise RuntimeError(
            "Story Agent returned an invalid StoryPackage: "
            f"expected at least 5 story beats, received {len(story.acts)}."
        )

    if len(story.acts) > 7:
        raise RuntimeError(
            "Story Agent returned an invalid StoryPackage: "
            f"expected at most 7 story beats, received {len(story.acts)}."
        )

    for index, beat in enumerate(story.acts, start=1):
        required_fields = {
            "title": beat.title,
            "purpose": beat.purpose,
            "action": beat.action,
            "emotional_state": beat.emotional_state,
            "attention_mechanism": beat.attention_mechanism,
            "payoff": beat.payoff,
        }

        missing_fields = [
            field
            for field, value in required_fields.items()
            if not str(value).strip()
        ]

        if missing_fields:
            raise RuntimeError(
                f"Story Agent returned incomplete StoryBeat {index}. "
                f"Missing: {', '.join(missing_fields)}."
            )

    return story

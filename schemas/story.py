from pydantic import BaseModel, Field


class StoryBeat(BaseModel):
    """A structured narrative beat within a Celestial Jyotish story."""

    beat_id: str = Field(
        ...,
        description="Stable identifier for the story beat."
    )

    title: str = Field(
        ...,
        description="Short internal title for the story beat."
    )

    purpose: str = Field(
        ...,
        description="Narrative purpose of the beat."
    )

    action: str = Field(
        ...,
        description="What happens during this beat."
    )

    emotional_state: str = Field(
        ...,
        description="Primary emotional state created or changed by the beat."
    )

    attention_mechanism: str = Field(
        ...,
        description="Primary attention mechanism used by the beat."
    )

    payoff: str = Field(
        ...,
        description="Information, emotional, or narrative payoff delivered by the beat."
    )


class StoryPackage(BaseModel):
    """
    Structured story architecture for one Celestial Jyotish topic.

    This is the controlled handoff between the fact-pack
    and screenplay/script stages.
    """

    story_id: str = Field(
        ...,
        description="Stable identifier for the story."
    )

    topic: str = Field(
        ...,
        description="Astrology topic being developed into a story."
    )

    premise: str = Field(
        ...,
        description="Central narrative premise of the story."
    )

    audience_promise: str = Field(
        ...,
        description="Clear promise describing what the audience will understand, discover, or experience."
    )

    protagonist: str = Field(
        ...,
        description="Primary character through whose experience the story is grounded."
    )

    central_conflict: str = Field(
        ...,
        description="Central tension, problem, mystery, or contradiction driving the story."
    )

    emotional_arc: str = Field(
        ...,
        description="Planned emotional progression from beginning to end."
    )

    technical_anchor: str = Field(
        ...,
        description="Core Jyotish principle or technical concept that must remain accurate in the story."
    )

    common_man_anchor: str = Field(
        ...,
        description="Concrete everyday-life situation used to make the astrology relatable."
    )

    opening_hook: str = Field(
        ...,
        description="Opening narrative hook designed to create immediate attention."
    )

    curiosity_gap: str = Field(
        ...,
        description="Central unanswered question or information gap that sustains attention."
    )

    acts: list[StoryBeat] = Field(
        default_factory=list,
        description="Ordered narrative beats forming the story architecture."
    )

    character_actions: list[str] = Field(
        default_factory=list,
        description="Important character actions that communicate meaning through behavior."
    )

    visual_anchors: list[str] = Field(
        default_factory=list,
        description="Recurring objects, locations, symbols, or visual motifs that reinforce memory and continuity."
    )

    reveal_points: list[str] = Field(
        default_factory=list,
        description="Important discoveries or progressive revelations."
    )

    final_payoff: str = Field(
        ...,
        description="Final narrative and informational payoff delivered to the audience."
    )

    continuity_notes: list[str] = Field(
        default_factory=list,
        description="Important continuity requirements for characters, props, locations, and story logic."
    )

    research_dependencies: list[str] = Field(
        default_factory=list,
        description="Fact-pack claim IDs or research elements that the story depends upon."
    )

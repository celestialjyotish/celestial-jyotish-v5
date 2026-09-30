from pydantic import BaseModel, Field


class ScriptLine(BaseModel):
    """One spoken or narrated line within a Celestial Jyotish script."""

    line_id: str = Field(
        ...,
        description="Stable identifier for the script line."
    )

    beat_id: str = Field(
        ...,
        description="Story beat associated with this script line."
    )

    speaker: str = Field(
        ...,
        description="Speaker identity, such as Narrator, Dev, or Asha."
    )

    text: str = Field(
        ...,
        description="Exact spoken or narrated text."
    )

    language_mix: str = Field(
        ...,
        description="Language composition of the line, such as Hindi, English, or Hindi-English."
    )

    delivery_style: str = Field(
        ...,
        description="Required vocal delivery, tone, pace, and emotional character."
    )

    estimated_duration_seconds: float = Field(
        ...,
        ge=0,
        description="Estimated duration of the spoken line in seconds."
    )

    lip_sync_required: bool = Field(
        default=False,
        description="Whether visible character lip-sync is required for this line."
    )

    technical_claim_ids: list[str] = Field(
        default_factory=list,
        description="Astrology claim IDs directly supported by this line."
    )


class ScriptSection(BaseModel):
    """A structured section connecting story beats to screenplay content."""

    section_id: str = Field(
        ...,
        description="Stable identifier for the script section."
    )

    beat_id: str = Field(
        ...,
        description="Story beat represented by this section."
    )

    purpose: str = Field(
        ...,
        description="Narrative purpose of the section."
    )

    emotional_target: str = Field(
        ...,
        description="Primary emotional response intended for the audience."
    )

    visual_intent: str = Field(
        ...,
        description="What the audience should see while the section plays."
    )

    lines: list[ScriptLine] = Field(
        default_factory=list,
        description="Ordered spoken or narrated lines in this section."
    )

    transition: str = Field(
        ...,
        description="How this section transitions into the next section."
    )


class ScriptPackage(BaseModel):
    """
    Production-ready structured screenplay package.

    This is the controlled handoff between the story stage
    and scene, visual, voice, and video production stages.
    """

    script_id: str = Field(
        ...,
        description="Stable identifier for the script."
    )

    story_id: str = Field(
        ...,
        description="Story package identifier from the story stage."
    )

    topic: str = Field(
        ...,
        description="Astrology topic covered by the script."
    )

    title: str = Field(
        ...,
        description="Working title of the production."
    )

    format: str = Field(
        ...,
        description="Target content format, such as Short, Reel, or Long-form."
    )

    target_duration_seconds: float = Field(
        ...,
        gt=0,
        description="Target total duration of the finished spoken script."
    )

    language_ratio: str = Field(
        default="70% Hindi / 30% English",
        description="Target language balance for the script."
    )

    narration_style: str = Field(
        ...,
        description="Overall narration and storytelling style."
    )

    sections: list[ScriptSection] = Field(
        default_factory=list,
        description="Ordered screenplay sections."
    )

    opening_hook: str = Field(
        ...,
        description="Exact opening hook used to capture attention."
    )

    audience_promise: str = Field(
        ...,
        description="Promise established for the audience at the beginning."
    )

    technical_integrity_notes: list[str] = Field(
        default_factory=list,
        description="Important Jyotish accuracy requirements that must be preserved during production."
    )

    continuity_notes: list[str] = Field(
        default_factory=list,
        description="Character, prop, location, wardrobe, and story continuity requirements."
    )

    visual_requirements: list[str] = Field(
        default_factory=list,
        description="High-level visual requirements that must be respected during scene production."
    )

    audio_requirements: list[str] = Field(
        default_factory=list,
        description="Voice, music, sound-effect, silence, and mixing requirements."
    )

    final_payoff: str = Field(
        ...,
        description="Final informational and emotional payoff of the script."
    )

    total_estimated_duration_seconds: float = Field(
        ...,
        ge=0,
        description="Calculated or validated total estimated spoken duration."
    )

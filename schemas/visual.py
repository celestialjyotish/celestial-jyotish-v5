from pydantic import BaseModel, Field


class VisualReference(BaseModel):
    """A visual reference used to preserve identity, style, or continuity."""

    reference_id: str = Field(
        ...,
        description="Stable identifier for the visual reference."
    )

    reference_type: str = Field(
        ...,
        description="Reference category such as character, wardrobe, location, prop, style, or composition."
    )

    description: str = Field(
        ...,
        description="Description of what the reference must preserve."
    )

    required: bool = Field(
        default=True,
        description="Whether this reference is mandatory for generation."
    )


class VisualContinuity(BaseModel):
    """Continuity requirements that must survive visual generation."""

    character_requirements: list[str] = Field(
        default_factory=list,
        description="Character identity, facial, physical, wardrobe, and styling requirements."
    )

    prop_requirements: list[str] = Field(
        default_factory=list,
        description="Important prop identity, placement, and appearance requirements."
    )

    environment_requirements: list[str] = Field(
        default_factory=list,
        description="Location, architecture, atmosphere, and environmental continuity requirements."
    )

    lighting_requirements: list[str] = Field(
        default_factory=list,
        description="Lighting direction, intensity, color, and continuity requirements."
    )

    composition_requirements: list[str] = Field(
        default_factory=list,
        description="Framing, subject placement, negative space, and composition requirements."
    )


class VisualPackage(BaseModel):
    """
    Production-ready visual-generation specification.

    This is the controlled handoff between scene design
    and master-image generation.
    """

    visual_id: str = Field(
        ...,
        description="Stable identifier for the visual package."
    )

    scene_id: str = Field(
        ...,
        description="Scene package identifier associated with this visual."
    )

    shot_id: str = Field(
        ...,
        description="Stable identifier for the individual visual shot."
    )

    title: str = Field(
        ...,
        description="Short internal title for the visual."
    )

    purpose: str = Field(
        ...,
        description="Narrative and visual purpose of the shot."
    )

    aspect_ratio: str = Field(
        default="16:9",
        description="Required output aspect ratio, such as 16:9, 9:16, or 1:1."
    )

    resolution: str = Field(
        ...,
        description="Target image resolution."
    )

    visual_style: str = Field(
        ...,
        description="Required visual and cinematic style."
    )

    master_image_prompt: str = Field(
        ...,
        description="Complete prompt for generating the master image."
    )

    negative_prompt: str = Field(
        default="",
        description="Elements, artifacts, or visual qualities that must be avoided."
    )

    character_locks: list[str] = Field(
        default_factory=list,
        description="Character-lock requirements that must remain consistent across generations."
    )

    references: list[VisualReference] = Field(
        default_factory=list,
        description="Reference images or visual references required for generation."
    )

    continuity: VisualContinuity = Field(
        ...,
        description="Continuity requirements for the visual."
    )

    composition_notes: str = Field(
        ...,
        description="Detailed composition and subject-placement instructions."
    )

    lighting_notes: str = Field(
        ...,
        description="Detailed lighting and illumination instructions."
    )

    color_grade: str = Field(
        ...,
        description="Required cinematic color treatment and grading direction."
    )

    typography_requirements: list[str] = Field(
        default_factory=list,
        description="Typography or on-image text requirements, when applicable."
    )

    branding_requirements: list[str] = Field(
        default_factory=list,
        description="Celestial Jyotish branding and footer-lock requirements."
    )

    image_generator: str = Field(
        ...,
        description="Generation system intended for the master image."
    )

    generation_status: str = Field(
        default="PENDING",
        description="Generation state such as PENDING, GENERATED, APPROVED, or REJECTED."
    )

    master_image_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the approved master image asset."
    )

    video_motion_prompt: str = Field(
        ...,
        description="Prompt describing how the master image should be animated into video."
    )

    motion_constraints: list[str] = Field(
        default_factory=list,
        description="Movement limitations required to protect image identity and continuity."
    )

    preservation_requirements: list[str] = Field(
        default_factory=list,
        description="Elements that must remain unchanged during image-to-video generation."
    )

    visual_qc_checks: list[str] = Field(
        default_factory=list,
        description="Quality-control checks required before visual approval."
    )

    rejection_reasons: list[str] = Field(
        default_factory=list,
        description="Reasons the visual may be rejected during quality control."
    )

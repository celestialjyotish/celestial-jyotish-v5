from pydantic import BaseModel, Field


class CharacterPresence(BaseModel):
    """A character's presence and continuity requirements within a scene."""

    character_id: str = Field(
        ...,
        description="Stable character identifier from the Character Bible."
    )

    role: str = Field(
        ...,
        description="Narrative role of the character in this scene."
    )

    action: str = Field(
        ...,
        description="Specific physical action performed by the character."
    )

    expression: str = Field(
        ...,
        description="Facial expression and emotional presentation."
    )

    wardrobe: str = Field(
        ...,
        description="Wardrobe requirements for continuity."
    )

    speaking: bool = Field(
        default=False,
        description="Whether the character visibly speaks on screen."
    )

    continuity_notes: list[str] = Field(
        default_factory=list,
        description="Character-specific continuity requirements."
    )


class CameraPlan(BaseModel):
    """Camera and motion specification for one production scene."""

    shot_type: str = Field(
        ...,
        description="Shot composition such as ECU, CU, MCU, MS, or WS."
    )

    camera_angle: str = Field(
        ...,
        description="Camera angle and viewpoint."
    )

    camera_movement: str = Field(
        ...,
        description="Camera movement such as push-in, tracking, pan, tilt, or static."
    )

    lens_language: str = Field(
        ...,
        description="Intended cinematic lens and depth-of-field characteristics."
    )

    framing: str = Field(
        ...,
        description="Subject placement and framing requirements."
    )


class ScenePackage(BaseModel):
    """
    Production-ready scene specification.

    This is the controlled handoff between the script stage
    and image, video, voice, sound, and editing stages.
    """

    scene_id: str = Field(
        ...,
        description="Stable identifier for the scene."
    )

    script_id: str = Field(
        ...,
        description="Script package identifier associated with this scene."
    )

    section_id: str = Field(
        ...,
        description="Script section represented by this scene."
    )

    scene_number: int = Field(
        ...,
        gt=0,
        description="Sequential scene number within the production."
    )

    title: str = Field(
        ...,
        description="Short internal title for the scene."
    )

    purpose: str = Field(
        ...,
        description="Narrative and production purpose of the scene."
    )

    duration_seconds: float = Field(
        ...,
        gt=0,
        description="Target duration of the scene."
    )

    action: str = Field(
        ...,
        description="Primary visible action that occurs during the scene."
    )

    environment: str = Field(
        ...,
        description="Location, setting, atmosphere, and environmental conditions."
    )

    time_of_day: str = Field(
        ...,
        description="Required time-of-day or lighting condition."
    )

    characters: list[CharacterPresence] = Field(
        default_factory=list,
        description="Characters present in the scene."
    )

    camera: CameraPlan = Field(
        ...,
        description="Camera composition and movement plan."
    )

    visual_style: str = Field(
        ...,
        description="Required visual style and cinematic treatment."
    )

    lighting: str = Field(
        ...,
        description="Lighting design and illumination requirements."
    )

    color_language: str = Field(
        ...,
        description="Color palette and visual color-language requirements."
    )

    props: list[str] = Field(
        default_factory=list,
        description="Important physical props appearing in the scene."
    )

    visual_anchors: list[str] = Field(
        default_factory=list,
        description="Recurring visual motifs or memory anchors."
    )

    narration_text: str = Field(
        default="",
        description="Narration or voice-over associated with the scene."
    )

    narration_speaker: str = Field(
        default="Narrator",
        description="Voice responsible for narration."
    )

    lip_sync_required: bool = Field(
        default=False,
        description="Whether visible mouth synchronization is required."
    )

    dialogue_text: str = Field(
        default="",
        description="On-screen character dialogue, if any."
    )

    audio_direction: str = Field(
        ...,
        description="Voice, music, sound-effect, ambience, and silence direction."
    )

    transition_in: str = Field(
        ...,
        description="Transition into the scene."
    )

    transition_out: str = Field(
        ...,
        description="Transition out of the scene."
    )

    image_generation_prompt: str = Field(
        ...,
        description="Prompt used to generate the scene's master image."
    )

    video_generation_prompt: str = Field(
        ...,
        description="Prompt used to animate the master image into video."
    )

    continuity_requirements: list[str] = Field(
        default_factory=list,
        description="Character, wardrobe, prop, location, lighting, and visual continuity requirements."
    )

    preservation_requirements: list[str] = Field(
        default_factory=list,
        description="Elements that must remain unchanged during image-to-video generation."
    )

    technical_claim_ids: list[str] = Field(
        default_factory=list,
        description="Astrology claim IDs represented or supported by this scene."
    )

    qc_requirements: list[str] = Field(
        default_factory=list,
        description="Quality-control checks required before the scene is approved."
    )

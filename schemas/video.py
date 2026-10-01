from pydantic import BaseModel, Field


class VideoMotion(BaseModel):
    """Motion and camera behavior for image-to-video generation."""

    action: str = Field(
        ...,
        description="Primary visible action occurring during the clip."
    )

    camera_movement: str = Field(
        ...,
        description="Camera movement such as push-in, tracking, pan, tilt, orbit, or static."
    )

    subject_movement: str = Field(
        ...,
        description="Required movement of the subject or characters."
    )

    environmental_motion: str = Field(
        default="",
        description="Subtle environmental movement such as fabric, hair, particles, light, smoke, or background activity."
    )

    motion_intensity: str = Field(
        ...,
        description="Overall motion intensity, such as subtle, moderate, or dynamic."
    )

    timing: str = Field(
        ...,
        description="Timing and pacing of the movement across the clip."
    )


class VideoPreservation(BaseModel):
    """Elements that image-to-video generation must preserve."""

    identity_preservation: list[str] = Field(
        default_factory=list,
        description="Character identity and facial features that must remain unchanged."
    )

    wardrobe_preservation: list[str] = Field(
        default_factory=list,
        description="Wardrobe details that must remain unchanged."
    )

    prop_preservation: list[str] = Field(
        default_factory=list,
        description="Props and their important visual details that must remain unchanged."
    )

    environment_preservation: list[str] = Field(
        default_factory=list,
        description="Important environmental and architectural details that must remain stable."
    )

    composition_preservation: list[str] = Field(
        default_factory=list,
        description="Framing, subject placement, and composition elements that must remain stable."
    )

    negative_motion_constraints: list[str] = Field(
        default_factory=list,
        description="Movements or transformations that must not occur."
    )


class VideoAudioSync(BaseModel):
    """Audio synchronization requirements for a generated video clip."""

    audio_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the audio asset."
    )

    audio_start_offset_seconds: float = Field(
        default=0,
        ge=0,
        description="Offset applied before the audio begins relative to the video clip."
    )

    lip_sync_required: bool = Field(
        default=False,
        description="Whether visible speech must be synchronized to the audio."
    )

    lip_sync_system: str = Field(
        default="NONE",
        description="Lip-sync system used when visible speech synchronization is required."
    )

    sync_notes: list[str] = Field(
        default_factory=list,
        description="Additional audio-video synchronization requirements."
    )


class VideoGenerationSettings(BaseModel):
    """Generation parameters for a video model or runtime."""

    provider: str = Field(
        ...,
        description="Video generation provider or runtime."
    )

    model: str = Field(
        ...,
        description="Specific video generation model."
    )

    duration_seconds: float = Field(
        ...,
        gt=0,
        description="Requested video clip duration."
    )

    aspect_ratio: str = Field(
        default="16:9",
        description="Video output aspect ratio."
    )

    resolution: str = Field(
        ...,
        description="Target video resolution."
    )

    frame_rate: int = Field(
        ...,
        gt=0,
        description="Target output frame rate."
    )

    generation_parameters: dict[str, str | int | float | bool] = Field(
        default_factory=dict,
        description="Model-specific generation parameters."
    )


class VideoPackage(BaseModel):
    """
    Production-ready video-generation specification.

    This is the controlled handoff between visual/audio assets
    and the video-generation and final-editing stages.
    """

    video_id: str = Field(
        ...,
        description="Stable identifier for the video clip."
    )

    scene_id: str = Field(
        ...,
        description="Scene package identifier associated with this clip."
    )

    visual_id: str = Field(
        ...,
        description="Visual package identifier providing the master image."
    )

    audio_id: str = Field(
        ...,
        description="Audio package identifier associated with this clip."
    )

    clip_number: int = Field(
        ...,
        gt=0,
        description="Sequential clip number within the production."
    )

    title: str = Field(
        ...,
        description="Short internal title for the video clip."
    )

    purpose: str = Field(
        ...,
        description="Narrative and production purpose of the clip."
    )

    source_image_asset: str = Field(
        ...,
        description="Reference, path, or identifier for the approved master image."
    )

    video_prompt: str = Field(
        ...,
        description="Final prompt sent to the video-generation system."
    )

    motion: VideoMotion = Field(
        ...,
        description="Required movement and camera behavior."
    )

    preservation: VideoPreservation = Field(
        ...,
        description="Elements that must be preserved during generation."
    )

    audio_sync: VideoAudioSync = Field(
        ...,
        description="Audio and lip-sync requirements."
    )

    generation: VideoGenerationSettings = Field(
        ...,
        description="Video-generation runtime and parameter configuration."
    )

    negative_prompt: str = Field(
        default="",
        description="Visual or motion artifacts that must be avoided."
    )

    continuity_requirements: list[str] = Field(
        default_factory=list,
        description="Continuity requirements connecting this clip to adjacent clips."
    )

    transition_in: str = Field(
        ...,
        description="Required transition into this clip."
    )

    transition_out: str = Field(
        ...,
        description="Required transition out of this clip."
    )

    generated_video_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the generated video asset."
    )

    generation_status: str = Field(
        default="PENDING",
        description="Generation state such as PENDING, GENERATED, APPROVED, or REJECTED."
    )

    qc_requirements: list[str] = Field(
        default_factory=list,
        description="Quality-control checks required before the clip is approved."
    )

    qc_status: str = Field(
        default="PENDING",
        description="Quality-control state of the generated clip."
    )

    rejection_reasons: list[str] = Field(
        default_factory=list,
        description="Reasons the generated clip was rejected."
    )

from pydantic import BaseModel, Field


class VoiceProfile(BaseModel):
    """Voice-generation and delivery specification."""

    speaker: str = Field(
        ...,
        description="Voice identity, such as Narrator, Dev, or Asha."
    )

    voice_type: str = Field(
        ...,
        description="Voice category or assigned voice model."
    )

    language_mix: str = Field(
        default="70% Hindi / 30% English",
        description="Target language balance for the spoken content."
    )

    tone: str = Field(
        ...,
        description="Overall vocal tone and emotional character."
    )

    pitch_range: str = Field(
        ...,
        description="Target pitch range or vocal register."
    )

    speaking_rate_wpm: int = Field(
        ...,
        gt=0,
        description="Target speaking rate in words per minute."
    )

    stability: float = Field(
        ...,
        ge=0,
        le=100,
        description="Target voice-generation stability from 0 to 100."
    )

    pronunciation_notes: list[str] = Field(
        default_factory=list,
        description="Pronunciation requirements for names, Sanskrit terms, Hindi words, and technical terminology."
    )

    pause_notes: list[str] = Field(
        default_factory=list,
        description="Required pauses, emphasis gaps, and dramatic timing instructions."
    )


class VoiceSegment(BaseModel):
    """One generated voice segment."""

    segment_id: str = Field(
        ...,
        description="Stable identifier for the voice segment."
    )

    scene_id: str = Field(
        ...,
        description="Scene associated with this voice segment."
    )

    speaker: str = Field(
        ...,
        description="Speaker responsible for the segment."
    )

    text: str = Field(
        ...,
        description="Exact text to be spoken."
    )

    voice_profile: VoiceProfile = Field(
        ...,
        description="Voice-generation profile for this segment."
    )

    lip_sync_required: bool = Field(
        default=False,
        description="Whether visible mouth synchronization is required."
    )

    start_time_seconds: float = Field(
        ...,
        ge=0,
        description="Planned start time of the segment."
    )

    duration_seconds: float = Field(
        ...,
        ge=0,
        description="Expected duration of the generated segment."
    )

    generation_status: str = Field(
        default="PENDING",
        description="Generation state such as PENDING, GENERATED, APPROVED, or REJECTED."
    )

    audio_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the generated voice asset."
    )

    qc_notes: list[str] = Field(
        default_factory=list,
        description="Voice-quality and pronunciation observations."
    )


class MusicCue(BaseModel):
    """Music cue specification for a scene or sequence."""

    cue_id: str = Field(
        ...,
        description="Stable identifier for the music cue."
    )

    scene_id: str = Field(
        ...,
        description="Scene associated with the music cue."
    )

    purpose: str = Field(
        ...,
        description="Narrative or emotional purpose of the music."
    )

    mood: str = Field(
        ...,
        description="Required musical mood."
    )

    style: str = Field(
        ...,
        description="Musical style, genre, or cinematic treatment."
    )

    intensity: str = Field(
        ...,
        description="Required intensity level and progression."
    )

    start_time_seconds: float = Field(
        ...,
        ge=0,
        description="Music cue start time."
    )

    duration_seconds: float = Field(
        ...,
        ge=0,
        description="Target duration of the music cue."
    )

    duck_under_voice: bool = Field(
        default=True,
        description="Whether music should be reduced underneath spoken voice."
    )

    generation_status: str = Field(
        default="PENDING",
        description="Generation state of the music asset."
    )

    audio_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the music asset."
    )


class SoundEffectCue(BaseModel):
    """Sound-effect or ambience cue specification."""

    cue_id: str = Field(
        ...,
        description="Stable identifier for the sound-effect cue."
    )

    scene_id: str = Field(
        ...,
        description="Scene associated with the sound effect."
    )

    effect_type: str = Field(
        ...,
        description="Category of effect such as impact, whoosh, environment, object, transition, or ambience."
    )

    description: str = Field(
        ...,
        description="Description of the required sound."
    )

    purpose: str = Field(
        ...,
        description="Narrative or sensory purpose of the sound."
    )

    start_time_seconds: float = Field(
        ...,
        ge=0,
        description="Sound-effect start time."
    )

    duration_seconds: float = Field(
        ...,
        ge=0,
        description="Target duration of the sound."
    )

    intensity: str = Field(
        ...,
        description="Required sound intensity."
    )

    generation_status: str = Field(
        default="PENDING",
        description="Generation state of the sound asset."
    )

    audio_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the generated sound asset."
    )


class AudioMixSettings(BaseModel):
    """Final audio-mix requirements."""

    voice_priority: str = Field(
        default="PRIMARY",
        description="Priority assigned to dialogue and narration."
    )

    music_priority: str = Field(
        default="SECONDARY",
        description="Priority assigned to background music."
    )

    sfx_priority: str = Field(
        default="SUPPORTING",
        description="Priority assigned to sound effects."
    )

    ambience_priority: str = Field(
        default="SUPPORTING",
        description="Priority assigned to environmental ambience."
    )

    voice_music_ducking: bool = Field(
        default=True,
        description="Whether music should automatically duck underneath speech."
    )

    voice_sfx_ducking: bool = Field(
        default=True,
        description="Whether sound effects should be reduced when they interfere with speech."
    )

    target_loudness_lufs: float | None = Field(
        default=None,
        description="Optional validated final-program loudness target in LUFS."
    )

    peak_limit_db: float | None = Field(
        default=None,
        description="Optional validated final peak ceiling in dBFS."
    )

    silence_requirements: list[str] = Field(
        default_factory=list,
        description="Intentional silence or breathing-space requirements."
    )


class AudioPackage(BaseModel):
    """
    Production-ready audio specification.

    This is the controlled handoff between script/scene planning
    and voice, music, sound-effect, lip-sync, and final-mix stages.
    """

    audio_id: str = Field(
        ...,
        description="Stable identifier for the complete audio package."
    )

    scene_id: str = Field(
        ...,
        description="Scene associated with this audio package."
    )

    script_id: str = Field(
        ...,
        description="Script package identifier."
    )

    target_duration_seconds: float = Field(
        ...,
        gt=0,
        description="Target total duration of the scene audio."
    )

    voice_segments: list[VoiceSegment] = Field(
        default_factory=list,
        description="Ordered voice and dialogue segments."
    )

    music_cues: list[MusicCue] = Field(
        default_factory=list,
        description="Music cues used within the scene."
    )

    sound_effect_cues: list[SoundEffectCue] = Field(
        default_factory=list,
        description="Sound-effect and ambience cues."
    )

    mix_settings: AudioMixSettings = Field(
        ...,
        description="Final scene audio-mix requirements."
    )

    lip_sync_system: str = Field(
        default="NONE",
        description="Lip-sync system required for visible speaking characters."
    )

    audio_style: str = Field(
        ...,
        description="Overall cinematic audio treatment."
    )

    continuity_requirements: list[str] = Field(
        default_factory=list,
        description="Audio continuity requirements across adjacent scenes."
    )

    qc_requirements: list[str] = Field(
        default_factory=list,
        description="Audio quality-control checks required before approval."
    )

    final_mix_asset: str = Field(
        default="",
        description="Reference, path, or identifier for the approved final scene mix."
    )

    generation_status: str = Field(
        default="PENDING",
        description="Overall audio-package state."
    )

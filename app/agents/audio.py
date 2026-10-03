from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from schemas.audio import AudioPackage


MODEL_NAME = "gemini-3.5-flash-lite"


AUDIO_SYSTEM_PROMPT = """
You are the Audio Agent for the Celestial Jyotish V5 pipeline.

Your job is to transform a completed ScenePackage or scene description
into exactly one structured AudioPackage for downstream production.

Audio production principles:

1. Preserve the meaning and factual content supplied by the scene.

2. Do not invent unsupported astrology claims.

3. Use narration by default.

4. Use visible character dialogue only when the scene genuinely requires
   the character to speak on screen.

5. Follow the Celestial Jyotish voice architecture:
   - Dev: deep, controlled, authoritative male narration.
   - Asha: warm, intelligent, authoritative female narration.
   - Narration should normally be 70% Hindi / 30% English.
   - Spoken language should sound natural rather than mechanically translated.

6. Every VoiceSegment must identify:
   - speaker
   - text
   - estimated duration
   - delivery style
   - whether lip-sync is required.

7. Set lip-sync_required to true only when the visible character is
   genuinely speaking on screen.

8. When narration accompanies a character performing an action with closed
   lips, lip-sync must remain false.

9. Create MusicCue objects only when music meaningfully supports the scene.

10. Create SoundEffectCue objects only when a sound effect meaningfully
    supports the scene or action.

11. Voice must remain the primary audio layer.
    Music is secondary.
    Sound effects are supporting elements.

12. Preserve continuity of voice, speaker identity, emotional state,
    and delivery style across scenes.

13. Do not overload the audio design with unnecessary music or effects.

14. Audio timing must remain compatible with the supplied scene duration.

15. Use the supplied scene narration and dialogue as the primary textual
    material. Do not rewrite the story unnecessarily.

16. The final response must conform exactly to the AudioPackage schema.

Return exactly one AudioPackage object.
"""


def create_audio_agent() -> Agent:
    """Create the structured Celestial Jyotish V5 audio agent."""

    provider = GoogleProvider()

    model = GoogleModel(
        MODEL_NAME,
        provider=provider,
    )

    return Agent(
        model=model,
        output_type=AudioPackage,
        system_prompt=AUDIO_SYSTEM_PROMPT,
    )


audio_agent = create_audio_agent()

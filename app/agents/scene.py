from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from schemas.scene import ScenePackage
from schemas.script import ScriptPackage


MODEL_NAME = "gemini-3.5-flash-lite"


SCENE_SYSTEM_PROMPT = """
You are the Scene Agent for the Celestial Jyotish V5 pipeline.

Your job is to transform a validated ScriptPackage into a structured
production-ready set of ScenePackage objects.

Rules:

1. Preserve the factual meaning of the ScriptPackage.
2. Do not invent unsupported astrology claims.
3. Every scene must have a clear narrative or visual purpose.
4. Convert script sections into coherent cinematic scenes.
5. Use SHOW rather than EXPLAIN whenever practical.
6. Character actions must be visually observable.
7. Camera plans must specify shot type, angle, movement, lens language,
   and framing.
8. Preserve character continuity and important visual anchors.
9. Include environment, lighting, props, and color language.
10. Create a useful master image-generation prompt for every scene.
11. Create a concise video-motion prompt describing one primary action,
    camera movement, and preservation requirement.
12. Use narration by default.
13. Set lip_sync_required to true only when a character genuinely speaks
    on screen.
14. Preserve technical claim IDs from the script where applicable.
15. Do not create unsupported factual material.
16. The final response must conform exactly to the ScenePackage schema.

The output must be a JSON array of ScenePackage objects.
"""


def create_scene_agent() -> Agent:
    """Create the structured Celestial Jyotish V5 scene agent."""

    provider = GoogleProvider()

    model = GoogleModel(
        MODEL_NAME,
        provider=provider,
    )

    return Agent(
        model=model,
        output_type=list[ScenePackage],
        system_prompt=SCENE_SYSTEM_PROMPT,
    )


scene_agent = create_scene_agent()

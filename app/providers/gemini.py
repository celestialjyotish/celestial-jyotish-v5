from litellm import acompletion

from .base import ModelProvider, ModelResponse


class GeminiProvider(ModelProvider):
    """Gemini provider implementation using the LiteLLM gateway."""

    def __init__(self, api_key: str | None) -> None:
        self.api_key = api_key

    @property
    def provider_name(self) -> str:
        """Return the provider name."""

        return "gemini"

    async def generate(
        self,
        prompt: str,
        model: str,
        *,
        system_prompt: str | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
    ) -> ModelResponse:
        """
        Generate a response using a Gemini model through LiteLLM.
        """

        if not self.api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        model_name = model
        if not model_name.startswith("gemini/"):
            model_name = f"gemini/{model_name}"

        messages: list[dict[str, str]] = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        request_kwargs: dict[str, object] = {
            "model": model_name,
            "messages": messages,
            "api_key": self.api_key,
            "temperature": temperature,
        }

        if max_tokens is not None:
            request_kwargs["max_tokens"] = max_tokens

        response = await acompletion(**request_kwargs)

        content = response.choices[0].message.content

        if content is None:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return ModelResponse(
            text=str(content),
            model=model_name,
            provider=self.provider_name,
        )

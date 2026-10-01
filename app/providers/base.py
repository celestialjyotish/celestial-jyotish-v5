from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ModelResponse:
    """Standard response returned by an AI model provider."""

    text: str
    model: str
    provider: str


class ModelProvider(ABC):
    """
    Common interface for all Celestial Jyotish V5 model providers.

    Provider-specific implementations such as Gemini, Claude,
    OpenRouter, or local models must follow this interface.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider name."""

        raise NotImplementedError

    @abstractmethod
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
        Generate a model response using the provider.

        Implementations should translate this common interface
        into the provider-specific API call.
        """

        raise NotImplementedError

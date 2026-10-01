import os
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseModel):
    """Application configuration for the Celestial Jyotish V5 pipeline."""

    app_name: str = Field(
        default="Celestial Jyotish V5",
        description="Application name."
    )

    environment: str = Field(
        default_factory=lambda: os.getenv("APP_ENV", "development"),
        description="Runtime environment."
    )

    timezone: str = Field(
        default_factory=lambda: os.getenv("APP_TIMEZONE", "Asia/Kolkata"),
        description="Application timezone."
    )

    log_level: str = Field(
        default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"),
        description="Application logging level."
    )

    project_root: Path = Field(
        default=PROJECT_ROOT,
        description="Root directory of the project."
    )

    data_dir: Path = Field(
        default=PROJECT_ROOT / "data",
        description="Directory for working data."
    )

    assets_dir: Path = Field(
        default=PROJECT_ROOT / "assets",
        description="Directory for generated and source assets."
    )

    output_dir: Path = Field(
        default=PROJECT_ROOT / "output",
        description="Directory for final production outputs."
    )

    anthropic_api_key: str | None = Field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY"),
        description="Anthropic API key loaded from the environment."
    )

    openrouter_api_key: str | None = Field(
        default_factory=lambda: os.getenv("OPENROUTER_API_KEY"),
        description="OpenRouter API key loaded from the environment."
    )

    gemini_api_key: str | None = Field(
        default_factory=lambda: os.getenv("GEMINI_API_KEY"),
        description="Google Gemini API key loaded from the environment."
    )

    def ensure_directories(self) -> None:
        """Create required local working directories when needed."""

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings instance."""

    return Settings()

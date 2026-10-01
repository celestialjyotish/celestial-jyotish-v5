from .config import get_settings


def main() -> None:
    """Start the Celestial Jyotish V5 application."""

    settings = get_settings()
    settings.ensure_directories()

    print(f"{settings.app_name} application initialized.")
    print(f"Environment: {settings.environment}")
    print(f"Timezone: {settings.timezone}")
    print(f"Project root: {settings.project_root}")


if __name__ == "__main__":
    main()

from __future__ import annotations

from typed_settings import option, settings


@settings
class Settings:
    token: str = option(default="token", help="GitHub token")
    trusted_publishing: bool = option(
        default=False, help="Configure trusted publishing"
    )
    dry_run: bool = option(default=False, help="Dry run the CLI")


SETTINGS = Settings()


__all__ = ["SETTINGS", "Settings"]

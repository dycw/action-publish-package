from __future__ import annotations

from subprocess import check_call

from uv_publish.logging import LOGGER


def uv_publish() -> None:
    _log_run("uv", "build", "--wheel")
    _log_run("uv", "publish", "--trusted-publishing", "always")


def _log_run(*cmds: str) -> None:
    LOGGER.info("Running '%s'...", " ".join(cmds))
    _ = check_call(cmds, text=True)


__all__ = ["uv_publish"]

"""Deprecated package name; import :mod:`funbattle` instead."""

from warnings import warn

import funbattle as _funbattle
from funbattle import *  # noqa: F403

warn(
    "notebattle has been renamed to funbattle; update imports to funbattle.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = getattr(_funbattle, "__all__", ())
__path__ = _funbattle.__path__

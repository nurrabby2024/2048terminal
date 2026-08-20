"""2048Terminal: A 2048 clone playable in the terminal with arrow key input."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]
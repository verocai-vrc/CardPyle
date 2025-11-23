"""
cardpyle: lightweight card game engine.

Public API:
- Game loop: Game, Phase
- Domain: Player, Zone, ZoneType, Card, CardDef, CardType
- Data helpers: load_cards_db, instantiate
"""

from __future__ import annotations

# Version (PEP 621 / importlib.metadata)
try:
    from importlib.metadata import PackageNotFoundError, version
    __version__ = version("cardpyle")
except Exception:  # PackageNotFoundError or runtime during editable dev
    __version__ = "0.0.0.dev0"

# Public re-exports (keep this small and curated)
from .game import Game, Phase
from .player import Player
from .zones import Zone, ZoneType
from .cards import (
    Card,
    CardDef,
    CardType,
    load_cards_db,
    instantiate,
)

__all__ = [
    "Game",
    "Phase",
    "Player",
    "Zone",
    "ZoneType",
    "Card",
    "CardDef",
    "CardType",
    "load_cards_db",
    "instantiate",
    "__version__",
]

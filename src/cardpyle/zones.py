from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
import random
from .cards import Card


class ZoneType(str, Enum):
    DECK = "deck"
    HAND = "hand"
    FIELD = "field"
    GRAVEYARD = "graveyard"


@dataclass
class Zone:
    zone_type: ZoneType
    cards: List[Card] = field(default_factory=list)

    def add_top(self, card: Card) -> None:
        self.cards.append(card)

    def remove(self, card: Card) -> None:
        self.cards.remove(card)

    def draw(self, n: int = 1) -> List[Card]:
        drawn: List[Card] = []
        for _ in range(min(n, len(self.cards))):
            drawn.append(self.cards.pop())  # topo do baralho = fim da lista
        return drawn

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def size(self) -> int:
        return len(self.cards)

    def is_empty(self) -> bool:
        return len(self.cards) == 0

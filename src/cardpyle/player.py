from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from .cards import Card, CardType
from .zones import Zone, ZoneType

if TYPE_CHECKING:
    from .game import Game
    
@dataclass
class Player:
    name: str
    deck: Zone
    hand: Zone = field(default_factory=lambda: Zone(ZoneType.HAND))
    field: Zone = field(default_factory=lambda: Zone(ZoneType.FIELD))
    graveyard: Zone = field(default_factory=lambda: Zone(ZoneType.GRAVEYARD))

    # Mana
    max_mana: int = 0
    available_mana: int = 0
    mana_cap: int = 10

    board_limit: int = 5  # limite de criaturas no campo (opcional)

    # game injeta essa referência ao registrar os players
    _game: Optional["Game"] = field(init=False, repr=False, default=None)

    def draw(self, n: int = 1) -> None:
        self.hand.cards.extend(self.deck.draw(n))

    def start_turn(self) -> None:
        self.max_mana = min(self.mana_cap, self.max_mana + 1)
        self.available_mana = self.max_mana

    def end_turn(self) -> None:
        pass

    def can_play_creature(self, card: Card) -> bool:
        if card not in self.hand.cards:
            return False
        if card.type is not CardType.CREATURE:
            return False
        if card.cost > self.available_mana:
            return False
        if len(self.field.cards) >= self.board_limit:
            return False
        return True

    def play_creature(self, card: Card, position: Optional[int] = None) -> bool:
        if not self.can_play_creature(card):
            return False
        self.available_mana -= card.cost
        self.hand.remove(card)
        self.field.add_top(card)
        card.owner = self
        card.board_position = position if position is not None else len(self.field.cards)
        return True

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import List
import random
from .player import Player


class Phase(Enum):
    DRAW = auto()
    MAIN = auto()
    END = auto()


@dataclass
class Game:
    players: List[Player]
    turn_index: int = 0
    phase: Phase = Phase.DRAW
    started: bool = False

    def __post_init__(self) -> None:
        for p in self.players:
            p._game = self

    @property
    def active_player(self) -> Player:
        return self.players[self.turn_index]

    @property
    def opponent(self) -> Player:
        return self.players[1 - self.turn_index]

    def start(self) -> None:
        for p in self.players:
            random.shuffle(p.deck.cards)
            p.draw(5)
        self.started = True
        self.phase = Phase.DRAW

    def next_phase(self) -> None:
        if self.phase is Phase.DRAW:
            self.active_player.start_turn()
            self.active_player.draw(1)
            self.phase = Phase.MAIN
        elif self.phase is Phase.MAIN:
            self.phase = Phase.END
        elif self.phase is Phase.END:
            self.end_turn()

    def end_turn(self) -> None:
        self.active_player.end_turn()
        self.turn_index = 1 - self.turn_index
        self.phase = Phase.DRAW

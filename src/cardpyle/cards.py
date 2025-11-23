from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, TYPE_CHECKING
import uuid
import yaml
from pathlib import Path

if TYPE_CHECKING:
    from .player import Player

class CardType(str, Enum):
    CREATURE = "creature"
    # futuramente: SPELL = "spell", EQUIPMENT = "equipment", etc.


@dataclass(frozen=True)
class CardDef:
    """Definição estática de uma carta (vem do banco YAML)."""
    id: str
    name: str
    type: CardType
    cost: int
    strength: int
    constitution: int
    tags: List[str] = field(default_factory=list)


@dataclass
class Card:
    """Instância de carta no jogo."""
    definition: CardDef
    instance_id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    owner: Optional["Player"] = None  # definido em runtime
    board_position: Optional[int] = None
    health: int = field(init=False)

    def __post_init__(self) -> None:
        self.health = self.definition.constitution

    @property
    def name(self) -> str:
        return self.definition.name

    @property
    def cost(self) -> int:
        return self.definition.cost

    @property
    def type(self) -> CardType:
        return self.definition.type

    @property
    def strength(self) -> int:
        return self.definition.strength

    def receive_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            # remoção do campo é responsabilidade do Game/Player (por enquanto só placeholder)
            self.board_position = None


def load_cards_db(path: str | Path) -> Dict[str, CardDef]:
    """
    Carrega o banco de cartas em YAML.
    Schema por carta:
      id, name, type, cost, strength, constitution, tags[]
    """
    p = Path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    db: Dict[str, CardDef] = {}
    for item in data.get("cards", []):
        cdef = CardDef(
            id=item["id"],
            name=item["name"],
            type=CardType(item["type"]),
            cost=int(item["cost"]),
            strength=int(item["strength"]),
            constitution=int(item["constitution"]),
            tags=list(item.get("tags", [])),
        )
        db[cdef.id] = cdef
    return db


def instantiate(defn: CardDef, count: int = 1) -> List[Card]:
    """Cria N instâncias de uma definição de carta."""
    return [Card(definition=defn) for _ in range(count)]

from __future__ import annotations
from typing import Dict, List
from pathlib import Path
import yaml
from .cards import Card, CardDef, instantiate

def build_deck_from_yaml(path: str | Path, card_db: Dict[str, CardDef]) -> List[Card]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    cards = data.get("cards", {})
    deck: List[Card] = []
    for cid, qty in cards.items():
        if cid not in card_db:
            raise KeyError(f"Carta '{cid}' não existe no banco de cartas.")
        deck.extend(instantiate(card_db[cid], int(qty)))
    return deck

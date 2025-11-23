import random
from pathlib import Path
import pytest
from cardpyle.cards import load_cards_db
from cardpyle.zones import Zone, ZoneType
from cardpyle.player import Player
from cardpyle.game import Game
from cardpyle.decklists import DECK1, build_deck_from_list

ROOT = Path(__file__).resolve().parents[1]
CARDS_YAML = ROOT / "data" / "cards.yaml"

@pytest.fixture
def card_db():
    return load_cards_db(CARDS_YAML)

@pytest.fixture
def game_factory(card_db):
    def _mk():
        random.seed(42)
        p1_deck = Zone(ZoneType.DECK, build_deck_from_list(DECK1, card_db))
        p2_deck = Zone(ZoneType.DECK, build_deck_from_list(DECK1, card_db))
        p1 = Player("P1", deck=p1_deck)
        p2 = Player("P2", deck=p2_deck)
        g = Game([p1, p2])
        g.start()
        return g
    return _mk

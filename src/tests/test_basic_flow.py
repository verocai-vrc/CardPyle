from cardpyle.cards import Card
from cardpyle.game import Phase
from cardpyle.player import Player

def test_start_sets_hands_and_phase(game_factory):
    game = game_factory()
    assert all(len(p.hand.cards) == 5 for p in game.players)
    assert game.phase == Phase.DRAW

def test_draw_phase_increases_mana_and_draws_one(game_factory):
    game = game_factory()
    p = game.active_player
    hand_before = len(p.hand.cards)
    assert p.max_mana == 0 and p.available_mana == 0

    game.next_phase()  # DRAW -> MAIN
    assert game.phase == Phase.MAIN
    assert len(p.hand.cards) == hand_before + 1
    assert p.max_mana == 1 and p.available_mana == 1

def test_play_creature_spends_mana(game_factory):
    game = game_factory()
    p = game.active_player

    # vai para MAIN e ganha 1 de mana
    game.next_phase()
    # garante uma criatura de custo <= mana
    creature = next(c for c in p.hand.cards if c.cost <= p.available_mana)
    ok = p.play_creature(creature)
    assert ok is True
    assert creature in p.field.cards
    assert creature not in p.hand.cards
    assert p.available_mana == 0

def test_cannot_play_without_mana(game_factory):
    game = game_factory()
    p = game.active_player
    # Ainda estamos na fase DRAW antes de start_turn => mana 0
    creature = next((c for c in p.hand.cards if c.cost > p.available_mana), None)
    if creature is None:
        return  # em casos raros não há criatura > mana 0
    assert p.play_creature(creature) is False

def test_turn_rotation(game_factory):
    game = game_factory()
    first = game.active_player
    game.next_phase()  # DRAW->MAIN
    game.next_phase()  # MAIN->END
    game.next_phase()  # END-> troca turno, volta para DRAW
    assert game.active_player is not first
    assert game.phase == Phase.DRAW

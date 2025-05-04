class CreatureCard(Card):
    def __init__(self, name, strength, constitution, cost, card_type, tags, board_position=None):
        super().__init__(name, strength, constitution, cost, card_type, tags, board_position)
        self.card_type = "Creature"
        
        

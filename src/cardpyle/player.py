class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck # Instancia da classe Deck
        self.hand = []
        self.graveyard = []
        self.board = []
    
    def draw_card(self):
        card = self.deck.draw()
        if card:
            self.hand.append(card)
            print(f"{self.name} drew {card.name}.")
        else:
            print("Deck is empty.")

    def play_card(self, card_index, board_position="Frontline"):
        if 0 <= card_index < len(self.hand):
            card = self.hand.pop(card_index)
            card.place_on_board(board_position, self.name)
            self.board.append(card)
            print(f"{self.name} plays {card.name} to the {board_position}.")
        else:
            print(f"Invalid card index: {card_index}")
    
    def show_hand(self):
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand):
            print(f"{i}: {card.name}")

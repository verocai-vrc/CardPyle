import random

class Deck:
    def __init__(self, cards_on_deck = None):
        self.cards_on_deck = cards_on_deck if cards_on_deck else []
        
        #Embaralhar
    def shuffle(self):
        random.shuffle(self.cards_on_deck)
        print("Deck has been shuffled.")
            
        #Puxar
    def draw(self):
        if self.cards_on_deck:
            return self.cards_on_deck.pop()
        else:
            print("Deck is empty. Cant draw a card.")
            return 
            
        #Adicionar carta ao baralho   
    def add_card(self, card):
        self.cards_on_deck.append(card)
        print(f"Card {card.name} has been added to the deck.")
        self.shuffle(self)
        
        #isempty 
    def is_empty(self):
        return len(self.cards_on_deck) == 0
    
        #tamanho
    def size(self):
        return len(self.cards_on_deck)
            
        #descritor
    def __str__(self):
        return f"Deck with {len(self.cards_on_deck)} cards."
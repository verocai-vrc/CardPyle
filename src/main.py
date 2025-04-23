from card import Card
from deck import Deck
from playerFace import playerFace as player

def main(): #teste de main
    print("Jogo começa!")
    
    #Exemlo de cartas
    goblin = Card("Goblin", 1, 3, 1, "Creature", ["Goblin"])
    orc  = Card("Orc", 3, 3, 3, "Creature", ["Orc"])
    dummy = Card("Dummy", 0, 5, 1, "Creature", tags=["Dummy"])
    
    #Exemplo de baralho
    deck = Deck([goblin, orc])
    deck.shuffle()

    #exemplode puxando uma carta do baralho
    card = deck.draw()
    print(f"Puxou {card.name} do baralho.") #printa o nome da carta puxada do baralho
    #joga carta sacada
    card.place_on_board(1, player)
    
    #exemplo de ataque
    card.target_and_hit(dummy)
    

if __name__ == "__main__":
    main()
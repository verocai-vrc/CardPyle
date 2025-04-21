class Card:
    #Construtor da classe carta
    #name: , strength: força de hit, constitution: vida base, cost: custo de ação, type: carta, feitiço, equiṕamento, terreno
    
    def __init__(self, name, strength, constitution, cost, card_type, tags, board_position=None):
        self.name = name
        self.str = strength
        self.con = constitution
        self.cost = cost
        self.type = card_type
        self.tags = tags if tags else []
        self.board_position = board_position
        
        self.board_position = None
        self.health = constitution
        self.owner = None
    
    # jogar no tabuleiro
    def place_on_board(self, board_position, owner):
        self.board_positiom = board_position
        self.owner = owner
    
    
        print(f"{self.name} is placed on {self.board_position}")
        
    # atacar
    def target_and_hit(self, target):
        print(f"{self.name} attacks {target.name} for {self.str} damage.")
        target.receive_damage(self.strength)
        
    # receber dano
    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
        else:
            print(f"{self.name} has {self.health} health left.")
        
    # morrer
    def die(self):
        print(f"{self.name} is destroied and off the board.")
        self.board_position = None
        self.move_to_graveyard(self)
        
    # mover para o cemiterio
    def move_to_graveyard(self):
        print(f"{self.name} is moved to the graveyard.")
class playerFace:
    #Criar construtor da classe playerFace
    #Atributos: MaxHealth, CurrentHealth, Mana

    def __init__(self, MaxHealth, CurrentHealth, Mana, player_attack):
        self.MaxHealth = MaxHealth
        self.CurrentHealth = CurrentHealth
        self.Mana = Mana
        self.player_attack = player_attack

    # Metodo Receber dano
    def player_receive_damage(self, damage):
        self.CurrentHealth -= damage
        if self.CurrentHealth <= 0:
            self.die()
            print(f"{self.name} died... Game Over.")
        else:
            print(f"{self.name} has {self.CurrentHealth} health left.")

    # Metodo atacar com equipamento
    def player_attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.player_attack} damage.")
        target.receive_damage(self.strength)

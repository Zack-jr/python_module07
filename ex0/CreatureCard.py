from .Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Invalid attack or health. Attributes set to 1 by default.")
        self.attack = attack
        self.health = health
    
    def play(self, game_state: dict) -> dict:
        pass
    
    def attack_target(self, target) -> dict:
        pass

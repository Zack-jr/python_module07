from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    """concrete creature card class"""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Invalid attack or health.")
        self.attack = attack
        self.health = health
        self.card_type = "Creature"

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
            }

    def play(self, game_state: Dict) -> Dict:
        if "active" in game_state.values():
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
                }

    def attack_target(self, target: Card) -> Dict:
        """attack target"""

        hit = target.health - self.attack
        if hit <= 0:
            combat_report = True
        else:
            combat_report = False
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": combat_report
            }

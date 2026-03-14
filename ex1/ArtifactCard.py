from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.card_type = "Artifact"

    def play(self, game_state: Dict) -> Dict:
        if "active" in game_state.values():
            return {
                "card_played": self.name, "mana_used": self.cost,
                "effect": self.effect
                }

    def activate_ability(self) -> Dict:
        return {self.effect: "Artifact active until destruction"}

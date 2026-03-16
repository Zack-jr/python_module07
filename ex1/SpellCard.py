from ex0.Card import Card, CardType
from typing import List, Dict


class SpellCard(Card):
    """class for spells"""
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.card_type = CardType.SPELL.value

    def play(self, game_state: Dict) -> Dict:
        """play method"""
        if "active" in game_state.values():
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
                }

    def resolve_effect(self, targets: List) -> Dict:
        """apply spell to targets"""
        self
        return {"Spell applied to": len(targets)}

from . import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.card_type = "Spell"
    
    def play(self, game_state: dict) -> dict:
        if "active" in game_state.values():
            return {"card_played": self.name, "mana_used": self.cost, "effect": self.effect_type}
    
    def resolve_effect(self, targets: list) -> dict:
        self
        return {"Spell applied to": len(targets)}
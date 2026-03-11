from ex0.Card import Card
from . import Combatable
from . import Magical

class   EliteCard(Card, Combatable, Magical):
    
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.card_type = "Elite Card"
        self.mana = 8
        self.health = 10
        self.used_spells = 0
        self.melee_hits = 0

    def play(self, game_state: dict) -> dict:
        if "active" in game_state.values():
            return {"card_played": self.name}
    
    def attack(self, target) -> dict:
        self.melee_hits += 1
        return {"attacker": self.name, "target": target, "damage": 5, "combat_type": "melee"}
    
    def defend(self, incoming_damage: int) -> dict:
        still_alive = False
        self.health -= incoming_damage
        if self.health > 0:
            still_alive = True
        return {"defender": self.name, "damage_taken": incoming_damage, "damage_blocked": 3, "still_alive": still_alive}
    
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.mana -= 4
        self.used_spells += 1
        return {"caster": self.name, "spell": spell_name, "targets": targets, "mana_used": 4}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}
    
    def get_magic_stats(self) -> dict:
        return {"used_spells": self.used_spells, "current_mana": self.mana}

    def get_combat_stats(self) -> dict:
        return {"physical hits": self.melee_hits}
    
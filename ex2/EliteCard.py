from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.card_type = "Elite Card"
        self.mana = 8
        self.health = 10
        self.used_spells = 0
        self.melee_hits = 0

    def play(self, game_state: Dict) -> Dict:
        if "active" in game_state.values():
            return {"card_played": self.name}

    def attack(self, target) -> Dict:
        self.melee_hits += 1
        return {
            "attacker": self.name,
            "target": target,
            "damage": 5,
            "combat_type": "melee"
            }

    def defend(self, incoming_damage: int) -> Dict:
        still_alive = False
        self.health -= incoming_damage
        if self.health > 0:
            still_alive = True
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": 3,
            "still_alive": still_alive
            }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        self.mana -= 4
        self.used_spells += 1
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
            }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> Dict:
        return {"used_spells": self.used_spells, "current_mana": self.mana}

    def get_combat_stats(self) -> Dict:
        return {"physical hits": self.melee_hits}

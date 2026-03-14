from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from typing import List, Dict


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        hand.remove(hand[0])
        mana_used = sum(card.cost for card in hand)
        damage = sum(card.attack for card in hand
                     if isinstance(card, CreatureCard))
        damage += 3
        cards = [card.name for card in hand]
        return {
            "cards_played": cards,
            "mana_used": mana_used,
            "targets_attacked": battlefield,
            "damage_dealt": damage
            }

    def get_strategy_name(self):
        return f"{type(self).__name__}"

    def prioritize_targets(self, available_targets: List) -> List:
        filter = [target for target in available_targets if "Enemy" in target]
        return filter

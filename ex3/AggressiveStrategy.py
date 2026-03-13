from . import GameStrategy
from . import CreatureCard

class   AggressiveStrategy(GameStrategy):
    
    def execute_turn(self, hand: list, battlefield: list) -> dict:
       
       # spell does not have attack attribute
       hand.remove(hand[0])
       mana_used = sum(card.cost for card in hand)
       damage = sum(card.attack for card in hand if isinstance(card, CreatureCard))
       damage += 3
       cards = [card.name for card in hand]
       return {"cards_played": cards, "mana_used": mana_used, "targets_attacked": battlefield, "damage_dealt": damage}

    def get_strategy_name(self):
        return f"{type(self).__name__}"
    
    def prioritize_targets(self, available_targets: list) -> list:
        filtered = [target for target in available_targets if "Enemy" in target]
        return filtered
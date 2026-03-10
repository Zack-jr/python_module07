from . import Card
from . import CreatureCard
from . import SpellCard
from . import ArtifactCard
from random import choice

class Deck():

    def __init__(self):
        self.cards = []
    
    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def remove_card(self, card: Card) -> bool:
        self.cards.remove(card)
    
    def shuffle(self) -> None:
        self.list.shuffle()
    
    def draw_card(self) -> Card:
        return choice(self.cards)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = sum(1 for e in self.cards if isinstance(e, CreatureCard))
        spells = sum(1 for e in self.cards if isinstance(e, SpellCard))
        artifacts = sum(1 for e in self.cards if isinstance(e, ArtifactCard))
        avg_cost = float(sum([e.cost for e in self.cards]) / total_cards)

        return {"total_cards": total_cards, "creatures": creatures, "spells": spells, "artifacts": artifacts, "avg_cost": avg_cost}
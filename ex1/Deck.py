from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import choice, shuffle
from typing import Dict


class Deck():
    """deck of cards class"""

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        """add a card to the deck"""
        self.cards.append(card)

    def remove_card(self, card: Card) -> bool:
        """remove a card from the deck"""
        self.cards.remove(card)

    def shuffle(self) -> None:
        """shuffle the deck"""
        shuffle(self.cards)

    def draw_card(self) -> Card:
        """draw a card from the deck"""
        return choice(self.cards)

    def get_deck_stats(self) -> Dict:
        """get the deck's stats"""
        total_cards = len(self.cards)
        creatures = sum(1 for e in self.cards if isinstance(e, CreatureCard))
        spells = sum(1 for e in self.cards if isinstance(e, SpellCard))
        artifacts = sum(1 for e in self.cards if isinstance(e, ArtifactCard))
        avg_cost = float(sum([e.cost for e in self.cards]) / total_cards)
        avg_cost = round(avg_cost, 2)
        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
            }

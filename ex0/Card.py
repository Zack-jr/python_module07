from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    """category class for rarities"""

    COMMON = "common"
    RARE = "rare"
    LEGENDARY = "legendary"


class CardType(Enum):
    """category class for card types"""

    CREATURE = "creature"
    SPELL = "spell"
    ARTIFACT = "artifact"
    ELITECARD = "Elite Card"


class Card(ABC):
    """abstract card class"""

    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """play a card"""
        pass

    def get_card_info(self) -> dict:
        """get card's info"""
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        """check if card is playable"""
        if available_mana >= self.cost:
            return True
        return False

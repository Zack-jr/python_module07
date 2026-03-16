from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict


class CardFactory(ABC):
    """abstract card factory class"""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """create a creature card"""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """create a spellcard"""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """create an artifact card"""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """create a themed deck"""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """get supported types"""
        pass

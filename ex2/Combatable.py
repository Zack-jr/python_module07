from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    """close combat card archetype"""

    @abstractmethod
    def attack(self, target) -> Dict:
        """abstract attack method"""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """abstract defend method"""
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """abstract get_combat_stats method"""
        pass

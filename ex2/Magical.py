from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """abstract method for cast_spell"""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """abstract method for mana channeling"""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """abstract method for magic stats"""
        pass

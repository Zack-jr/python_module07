from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):
    """game strategy abstract class"""
    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """simulate a turn"""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """get name of strategy"""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """prioritize target"""
        pass

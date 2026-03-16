from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):

    @abstractmethod
    def calculate_rating(self) -> int:
        """calculate card rating"""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """update card wins"""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """update card losses"""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """get card rank info"""
        pass

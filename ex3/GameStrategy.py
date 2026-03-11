from abc import ABC, abstractmethod

class GameStrategy(ABC):
    def execute_turn(self, hand: list, battle)
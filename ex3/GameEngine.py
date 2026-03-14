from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from typing import Dict


class GameEngine():

    def __init__(self):
        self.strategy = None
        self.factory = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.strategy = strategy
        self.factory = factory

    def simulate_turn(self) -> Dict:
        print("Simulating aggressive turn...")

        hand = [
            self.factory.create_creature(),
            self.factory.create_creature("Goblin"),
            self.factory.create_spell()
            ]
        self.cards_created += len(hand)
        print(f"Hand: [{hand[0].name} ({hand[0].cost})"
              f", {hand[1].name} ({hand[1].cost})"
              f", {hand[2].name} ({hand[2].cost})]\n")

        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        battlefield = ["Enemy player"]
        turn_result = self.strategy.execute_turn(hand, battlefield)
        print(f"Actions: {turn_result}")
        self.total_damage = turn_result["damage_dealt"]
        self.turns += 1

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": type(self.strategy).__name__,
            "total_damage": self.total_damage,
            "cards_created": 3
            }

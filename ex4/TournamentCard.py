from . import Card, Combatable, Rankable

class TournamentCard(Card, Combatable, Rankable):

    def __init__(name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

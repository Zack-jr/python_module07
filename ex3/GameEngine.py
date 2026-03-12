from . import GameStrategy, CardFactory

class GameEngine():

    def __init__(self):
        self.strategy = None
        self.status = "active"

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:

        # ????????????///
    def simulate_turn(self) -> dict:
        pass
    def get_engine_status(self) -> dict:
        return {"status": self.status}
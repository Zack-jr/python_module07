from . import Card
from . import CardFactory

class FantasyCardFactory(CardFactory):

    def __init__(self, strategy):
        self.strategy = strategy
        creatures = []
        spells = []
        artifacts = []
    
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        
    
    def create_spell(self, name_or_power: str | int| None = None) -> Card:
        return
    
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass
    
    def create_themed_deck(self, size: int) -> dict:
        pass
    
    def get_supported_types(self) -> dict:
        pass

from . import Card, CreatureCard, SpellCard, ArtifactCard, CardFactory

class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Goblin":
            return (CreatureCard("Goblin Warrior", 2, "Legendary", 5, 8))
        else:
            return CreatureCard("Fire Dragon", 5, "Legendary", 12, 12)
    
    def create_spell(self, name_or_power: str | int| None = None) -> Card:
        if name_or_power:
            return SpellCard(name_or_power, 4, "rare", "hits the enemy")
        return SpellCard("Lightning bolt", 3, "rare", "shocks the enemy")
    
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power:
            return ArtifactCard(name_or_power, 4, "rare", 999, "is now on the field")
    
        return ArtifactCard("Mana Crystal", 4, "rare", 999, "Permanent: +1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:

        deck = {"creatures": [], "spells": [], "artifacts": []}
        while size:
            if size % 2 == 0:
                deck["creatures"].append(self.create_creature())
            elif size % 3 == 0:
                deck["artifacts"].append(self.create_artifact())
            elif size % 5 == 0:
               deck["spells"].append(self.create_spell())
            else:
                deck["creatures"].append(self.create_creature())
            size -= 1
        return deck

    def get_supported_types(self) -> dict:
        return {"creatures": ["dragon", "goblin"], "spells": ["fireball"], "artifacts": ["mana_ring"]}

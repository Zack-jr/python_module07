from . import Card, CreatureCard, Deck, SpellCard, ArtifactCard

def main():
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    creature = CreatureCard("Fire Dragon", 5, "Legedary", 7, 7)
    spell = SpellCard("Lightning Bolt", 5, "rare", "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, "uncommon", float('inf'), "+1 mana per turn")

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print(f"Deck stats: {deck.get_deck_stats()}\n")
    print("Drawing and playing cards:\n")

    for i in range(3):
        drew = deck.draw_card()
        if isinstance(drew, CreatureCard):
            card_type = "Creature"
        elif isinstance(drew, SpellCard):
            card_type = "Spell"
        elif isinstance(drew, ArtifactCard):
            card_type = "Artifact"
            
    print(f"Drew: {drew.name} ({card_type})")

if __name__ == '__main__':
    main()
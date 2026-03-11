from . import Card, CreatureCard, Deck, SpellCard, ArtifactCard

def main():
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    creature = CreatureCard("Fire Dragon", 5, "Legedary", 7, 7)
    spell = SpellCard("Lightning Bolt", 3, "rare", "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, "uncommon", float('inf'), "Permanent: +1 mana per turn")

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)
    deck.shuffle()
    game_state = {"status": "active"}
    print(f"Deck stats: {deck.get_deck_stats()}\n")
    print("Drawing and playing cards:\n")

    for i in range(3):
        drew = deck.draw_card()
        print(f"Drew: {drew.name} ({drew.card_type})")
        print(f"Play result: {drew.play(game_state)}\n")
        deck.remove_card(drew)

    print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == '__main__':
    main()
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main():

    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 7)
    spell = SpellCard("Lightning Bolt", 3, Rarity.RARE.value,
                      "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, Rarity.COMMON.value,
                            float('inf'), "Permanent: +1 mana per turn")

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

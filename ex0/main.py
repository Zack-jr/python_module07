from .CreatureCard import CreatureCard

def main():
    print("=== DataDeck Card Foundation ===\n")

    currency = 8
    print("Testing Abstract Base Class Design:\n")
    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    currency -= 5
    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("Playing  Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state = {"status": "active"}
    print(f"Play result: {dragon.play(game_state)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin_warrior = CreatureCard('Goblin Warrior', 4, 'Rare', 4, 3)
    print(dragon.attack_target(goblin_warrior))

    print(f"\nTesting insufficient mana ({currency} available):")
    elf = CreatureCard('Magic Elf',  7, "Legendary", 8, 3)
    print(f"Playable: {elf.is_playable(currency)}")

    print("\nAbstract pattern successfully demonstrated!")
if __name__ == '__main__':
    main()
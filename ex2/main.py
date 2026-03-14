from ex2.EliteCard import EliteCard


# go into the class's dict, and get the callable values (methods)
def get_methods(cls):
    return [
        name for name, value in cls.__dict__.items()
        if callable(value) and not name.startswith("__")
        ]


def main():
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    interfaces = EliteCard.__bases__
    for interface in interfaces:
        print(f"- {interface.__name__}: {get_methods(interface)}")

    arcane_warrior = EliteCard("Arcane Warrior", 6, "Legendary")
    print(f"\nPlaying {arcane_warrior.name} ({arcane_warrior.card_type}):\n")

    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack("enemy")}")
    print(f"Defense result: {arcane_warrior.defend(2)}\n")

    print("Magic phase:")
    targets = ["Enemy1", "Enemy2"]
    print(f"Spell Cast: {arcane_warrior.cast_spell("Fireball", targets)}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")


if __name__ == '__main__':
    main()

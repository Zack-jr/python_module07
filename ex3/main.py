from . import FantasyCardFactory , AgressiveStrategy, GameEngine

def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    game = GameEngine()
    strategy = AgressiveStrategy()
    factory = FantasyCardFactory(strategy)
    game.configure_engine(factory, strategy)
    print(f"Factory")


    available_cards = {"creatures": ['dragon, goblin'], "spells": ['fireball'], "artifacts": ['mana_ring']}
    print(f"Available types: {available_cards}\n")

    print("Simulating agressive turn...")

if __name__ == '__main__':
    main()

# abstract = GameStrategy, CardFactory,
# concrete = AgressiveStrategy, FantasyCardFactory, GameEngine, 
from . import FantasyCardFactory , AgressiveStrategy, GameEngine

def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    game = GameEngine()
    strategy = AgressiveStrategy()
    print(f"Strategy: {strategy.get_strategy_name()}")
    factory = FantasyCardFactory(strategy)

    game.configure_engine(factory, strategy)


    available_cards = {"creatures": ['dragon, goblin'], "spells": ['fireball'], "artifacts": ['mana_ring']}
    print(f"Available types: {available_cards}\n")

    print("Simulating agressive turn...")

if __name__ == '__main__':
    main()

# abstract = GameStrategy, CardFactory,
# concrete = AgressiveStrategy, FantasyCardFactory, GameEngine, 
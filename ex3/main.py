from . import FantasyCardFactory , AggressiveStrategy, GameEngine

def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    game = GameEngine()
    strategy = AggressiveStrategy()
    factory = FantasyCardFactory()
    game.configure_engine(factory, strategy)
    print(f"Factory: {type(game.factory).__name__}")
    print(f"Strategy: {game.strategy.get_strategy_name()}")
    print(f"Available types: {game.factory.get_supported_types()}\n")

    game.simulate_turn()
    print(f"\nGame Report: {game.get_engine_status()}\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == '__main__':
    main()

# abstract = GameStrategy, CardFactory,
# concrete = AgressiveStrategy, FantasyCardFactory, GameEngine, 
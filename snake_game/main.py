from game.game_engine import GameEngine


def main():
    screen_width, screen_height = 800, 600
    game_engine = GameEngine(screen_width, screen_height)
    game_engine.run()


if __name__ == "__main__":
    main()

import pygame
import sys


class GameEngine:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    screen_width, screen_height = 800, 600
    game_engine = GameEngine(screen_width, screen_height)
    game_engine.run()

import pygame as pg
from game.utilities.vector import Vector as V
from game.scenes.game_scene import GameScene


class MainMenu:
    def __init__(self, screen_width, screen_height):
        pg.init()  # Initialize Pygame
        pg.font.init()  # Initialize the font system

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption("Snake Main Menu")

        self.title_font = pg.font.Font(None, 48)
        self.button_font = pg.font.Font(None, 36)

        self.title_text = self.title_font.render("Snake Game", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(screen_width // 2, 100))

        self.start_button_text = self.button_font.render("Start", True, (255, 255, 255))
        self.start_button_rect = self.start_button_text.get_rect(
            center=(screen_width // 2, 300)
        )

        self.background_image = pg.image.load(
            "game/assets/snake.jpg"
        )  # Replace with your image path
        self.background_image = pg.transform.scale(
            self.background_image, (screen_width, screen_height)
        )

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    return (
                        False,
                        "start_game",
                    )  # Exit the main menu and signal to start the game

        return True

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.title_text, self.title_rect)
        self.screen.blit(self.start_button_text, self.start_button_rect)
        pg.display.flip()

    def run(self):
        running = True
        clock = pg.time.Clock()

        while running:
            running = self.handle_events()
            self.draw()
            clock.tick(30)  # Adjust the frame rate

        pg.quit()


if __name__ == "__main__":
    if __name__ == "__main__":
        screen_width, screen_height = 800, 600
        main_menu = MainMenu(screen_width, screen_height)
        while True:
            result = main_menu.run()
            if result[0]:  # Continue running the main menu
                main_menu = MainMenu(screen_width, screen_height)
            elif result[1] == "start_game":  # Start the game
                game_scene = GameScene(screen_width, screen_height)
                game_scene.run()

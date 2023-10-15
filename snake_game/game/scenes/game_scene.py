import pygame as pg
from game.utilities.vector import Vector as V
from game.entities.snake import Snake
from game.entities.food import Food

class GameScene:
    def __init__(self, screen_width, screen_height):
        # Existing initialization code
        # ...

        self.game_over = False
        self.final_score = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

            # Check for user input when the game is over
            if self.game_over:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        # Restart the game
                        self.initialize_game()
                        self.game_over = False
                    elif high_score_button_rect.collidepoint(event.pos):
                        # Display the high score table
                        self.show_high_scores()
                continue  # Skip handling other events while game over

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.snake.change_direction(V.UP)
                elif event.key == pg.K_DOWN:
                    self.snake.change_direction(V.DOWN)
                elif event.key == pg.K_LEFT:
                    self.snake.change_direction(V.LEFT)
                elif event.key == pg.K_RIGHT:
                    self.snake.change_direction(V.RIGHT)

        return True

    def update(self):
        if not self.game_over:
            self.snake.move()

            if self.snake.check_collision_with_bounds(
                self.screen_width, self.screen_height
            ):
                # Handle collision with the game boundaries
                self.handle_game_over()

            if self.snake.check_collision_with_self():
                # Handle collision with self
                self.handle_game_over()

            if self.snake.head_position == self.food.position:
                # Handle collision with food
                self.food.respawn(self.screen_width, self.screen_height)
                self.snake.grow()
                self.final_score = len(self.snake.body) - 3

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen

        if self.game_over:
            # Draw game over screen
            self.draw_game_over_screen()

        else:
            # Draw the game scene
            self.snake.draw(self.screen)
            self.food.draw(self.screen)

        pg.display.flip()  # Update the display

    def run(self):
        running = True
        clock = pg.time.Clock()

        while running:
            running = self.handle_events()
            self.update()
            self.draw()

            clock.tick(10)  # Adjust the frame rate

        pg.quit()

    def handle_game_over(self):
        self.game_over = True

    def draw_game_over_screen(self):
        # Draw the game over screen with final score and buttons
        # You can use Pygame's drawing functions to create buttons and display the final score
        pass

    def initialize_game(self):
        # Reset the game state when restarting
        self.snake = Snake()
        self.food = Food(self.screen_width, self.screen_height)
        self.final_score = 0

    def show_high_scores(self):
        # Display the high score table
        # You can implement this functionality in a separate method
        pass

if __name__ == "__main__":
    pg.init()
    screen_width, screen_height = 800, 600
    game_scene = GameScene(screen_width, screen_height)
    game_scene.run()

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the width and height of the game window
window_width = 800
window_height = 600

# Set the size of each grid cell
cell_size = 20

# Calculate the number of cells in the window
grid_width = window_width // cell_size
grid_height = window_height // cell_size

# Set the speed of the snake
snake_speed = 10

# Set the direction of the snake
direction = "RIGHT"

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define functions

def draw_snake(snake_body):
    for body_part in snake_body:
        pygame.draw.rect(window, WHITE, (body_part[0], body_part[1], cell_size, cell_size))

def draw_food(food_position):
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], cell_size, cell_size))

def run_game():
    # Set initial positions
    x = window_width / 2
    y = window_height / 2
    x_change = 0
    y_change = 0

    # Create the snake
    snake_body = []
    snake_length = 1

    # Generate the initial food position
    food_position = [random.randrange(1, grid_width) * cell_size,
                     random.randrange(1, grid_height) * cell_size]

    game_over = False
    game_clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -cell_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = cell_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -cell_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = cell_size

        # Update snake position
        x += x_change
        y += y_change

        # Check for collision with the boundaries of the window
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_over = True

        # Create a new head for the snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        # Remove old parts of the snake if it's longer than snake_length
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collision with the snake's body
        for body_part in snake_body[:-1]:
            if body_part == snake_head:
                game_over = True

        # Check for collision with the food
        if x == food_position[0] and y == food_position[1]:
            # Generate a new food position
            food_position = [random.randrange(1, grid_width) * cell_size,
                             random.randrange(1, grid_height) * cell_size]
            snake_length += 1

        # Fill the window with a black background
        window.fill(BLACK)

        # Draw the snake and the food
        draw_snake(snake_body)
        draw_food(food_position)

        # Refresh the game window
        pygame.display.update()

        # Set the frame rate of the game
        game_clock.tick(snake_speed)

    pygame.quit()

# Run the game
run_game()
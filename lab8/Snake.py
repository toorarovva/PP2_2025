import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20  # Grid cell size
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font = pygame.font.SysFont("Verdana", 20)

# Snake initialization
snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
change_to = direction
speed = 10  # Initial speed
score = 0
level = 1

# Function to generate food position
def generate_food():
    while True:
        food_x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        food_y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (food_x, food_y) not in snake:  # Ensure food does not spawn on snake
            return (food_x, food_y)

# First food placement
food = generate_food()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update direction
    direction = change_to

    # Move the snake
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= GRID_SIZE
    elif direction == "DOWN":
        head_y += GRID_SIZE
    elif direction == "LEFT":
        head_x -= GRID_SIZE
    elif direction == "RIGHT":
        head_x += GRID_SIZE

    # Check wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False  # Game over

    # Check self collision
    if (head_x, head_y) in snake:
        running = False  # Game over

    # Update snake's body
    snake.insert(0, (head_x, head_y))

    # Check if food is eaten
    if (head_x, head_y) == food:
        score += 1
        food = generate_food()  # Generate new food
    else:
        snake.pop()  # Remove last part of snake

    # Increase level every 3 points
    if score % 3 == 0 and score > 0:
        level = (score // 3) + 1
        speed = 10 + (level * 2)  # Increase speed

    # Draw snake
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], GRID_SIZE, GRID_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Refresh screen
    pygame.display.update()
    clock.tick(speed)  # Control speed

pygame.quit()

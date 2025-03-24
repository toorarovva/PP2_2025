import pygame
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Create a surface to persist drawings
canvas = pygame.Surface(screen.get_size())
canvas.fill((0, 0, 0))  # Background color

# Default settings
radius = 15
drawing = False
mode = "draw"  # draw, rect, circle, eraser, square, triangle, rhombus
color = (0, 0, 255)  # Default blue
start_pos = None

running = True
while running:
    screen.blit(canvas, (0, 0))  # Keep previous drawings

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key Presses for Color and Mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = (255, 0, 0)  # Red
            elif event.key == pygame.K_2:
                color = (0, 255, 0)  # Green
            elif event.key == pygame.K_3:
                color = (0, 0, 255)  # Blue
            elif event.key == pygame.K_4:
                color = (255, 255, 0)  # Yellow
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_y:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"

        # Mouse Events for Drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                pygame.draw.rect(canvas, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                pygame.draw.circle(canvas, color, center, radius, 2)
            elif mode == "square":
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], side, side), 2)
            elif mode == "right_triangle":
                pygame.draw.polygon(canvas, color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == "equilateral_triangle":
                side = abs(end_pos[0] - start_pos[0])
                height = (math.sqrt(3) / 2) * side
                pygame.draw.polygon(canvas, color, [
                    (start_pos[0], start_pos[1] + height),  # Bottom left
                    (start_pos[0] + side, start_pos[1] + height),  # Bottom right
                    (start_pos[0] + side // 2, start_pos[1])  # Top
                ], 2)
            elif mode == "rhombus":
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(canvas, color, [
                    (start_pos[0], start_pos[1] + height // 2),  # Left
                    (start_pos[0] + width // 2, start_pos[1]),  # Top
                    (start_pos[0] + width, start_pos[1] + height // 2),  # Right
                    (start_pos[0] + width // 2, start_pos[1] + height)  # Bottom
                ], 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(canvas, color, event.pos, radius)
            elif mode == "eraser":
                pygame.draw.circle(canvas, (0, 0, 0), event.pos, radius)  # Erasing with black

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

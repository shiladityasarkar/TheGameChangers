# Import the necessary modules
import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Game')

# Set up the font for the timer
FONT = pygame.font.Font(None, 36)

# Set up the car's properties
CAR_WIDTH = 50
CAR_HEIGHT = 50
CAR_COLOR = RED
CAR_SPEED = 5

# Set up the car's initial position
CAR_X = WIDTH // 2
CAR_Y = HEIGHT // 2

# Set up the lap's properties
LAP_LENGTH = 200
LAP_COUNTER = 0
LAP_START_TIME = 0
LAP_END_TIME = 0

# Game loop variables
game_running = False
game_paused = False

# Set up the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = True
                LAP_START_TIME = time.time()
            elif event.key == pygame.K_r:
                game_running = False
                LAP_COUNTER = 0
                CAR_X = WIDTH // 2
                CAR_Y = HEIGHT // 2
                LAP_START_TIME = 0
                LAP_END_TIME = 0

    keys = pygame.key.get_pressed()
    if game_running and not game_paused:
        if keys[pygame.K_UP]:
            CAR_Y -= CAR_SPEED
        if keys[pygame.K_DOWN]:
            CAR_Y += CAR_SPEED
        if keys[pygame.K_LEFT]:
            CAR_X -= CAR_SPEED
        if keys[pygame.K_RIGHT]:
            CAR_X += CAR_SPEED

        # Check for lap completion
        if CAR_X + CAR_WIDTH > LAP_LENGTH:
            LAP_END_TIME = time.time()
            LAP_COUNTER += 1
            print(f"Lap {LAP_COUNTER} completed in {LAP_END_TIME - LAP_START_TIME} seconds")
            CAR_X = 0
            game_paused = True
        elif CAR_X < 0:
            CAR_X = 0

    # Draw the game screen
    SCREEN.fill(WHITE)
    pygame.draw.rect(SCREEN, CAR_COLOR, (CAR_X, CAR_Y, CAR_WIDTH, CAR_HEIGHT))
    pygame.draw.line(SCREEN, BLACK, (LAP_LENGTH, 0), (LAP_LENGTH, HEIGHT))
    timer_text = FONT.render(f"Lap Time: {time.time() - LAP_START_TIME:.2f} seconds", True, BLACK)
    SCREEN.blit(timer_text, (10, 10))
    lap_text = FONT.render(f"Lap {LAP_COUNTER}", True, BLACK)
    SCREEN.blit(lap_text, (10, 40))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)
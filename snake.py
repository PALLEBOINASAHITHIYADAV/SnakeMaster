import pygame
import random

# Initialize pygame
pygame.init()

# Game Variables
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
BACKGROUND_COLOR = (0, 0, 0)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)    # Normal food
GREEN = (0, 255, 0)  # Bonus food (extra points)
BLUE = (0, 0, 255)   # Slow food (reduces speed)
PURPLE = (128, 0, 128)  # Poisonous food (reduces score & shortens snake)

# Snake Variables
snake_pos = [[300, 300]]  # Initial position
snake_direction = "RIGHT"
speed = 10  # Initial speed

# Food Variables
food_types = [
    {"color": RED, "points": 10, "speed_change": 0, "poison": False, "shrink": False},   # Normal food
    {"color": GREEN, "points": 20, "speed_change": +2, "poison": False, "shrink": False},  # Bonus food
    {"color": BLUE, "points": 10, "speed_change": -2, "poison": False, "shrink": False},  # Slow food
    {"color": PURPLE, "points": -15, "speed_change": 0, "poison": True, "shrink": True}  # Poisonous food
]
food = None


# Function to spawn food
def spawn_food():
    x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    food_type = random.choice(food_types)  # Pick a random food type
    return {"pos": [x, y], "type": food_type}


# Initial food placement
food = spawn_food()

# Game Loop
running = True
score = 0

while running:
    pygame.time.delay(100 - speed * 2)  # Adjust speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != "DOWN":
        snake_direction = "UP"
    if keys[pygame.K_DOWN] and snake_direction != "UP":
        snake_direction = "DOWN"
    if keys[pygame.K_LEFT] and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    if keys[pygame.K_RIGHT] and snake_direction != "LEFT":
        snake_direction = "RIGHT"

    # Update Snake Position
    head = snake_pos[0][:]
    if snake_direction == "UP":
        head[1] -= GRID_SIZE
    elif snake_direction == "DOWN":
        head[1] += GRID_SIZE
    elif snake_direction == "LEFT":
        head[0] -= GRID_SIZE
    elif snake_direction == "RIGHT":
        head[0] += GRID_SIZE

    snake_pos.insert(0, head)  # Move snake forward

    # Check for collision with food
    if snake_pos[0] == food["pos"]:
        food_effect = food["type"]
        score += food_effect["points"]
        speed = max(5, min(20, speed + food_effect["speed_change"]))  # Adjust speed

        # Check if food is poisonous
        if food_effect["poison"]:
            if len(snake_pos) > 3:  # Prevent instant Game Over
                snake_pos.pop()  # Shorten snake
            else:
                running = False  # Game Over if snake gets too short

        food = spawn_food()  # Spawn new food
    else:
        snake_pos.pop()  # Remove tail (move forward)

    # Check for collisions with walls or itself
    if head in snake_pos[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
        running = False  # Game Over

    # Draw everything
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BACKGROUND_COLOR)

    # Draw Snake
    for segment in snake_pos:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw Food
    pygame.draw.rect(screen, food["type"]["color"], (food["pos"][0], food["pos"][1], GRID_SIZE, GRID_SIZE))

    # Display Score
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

# End Game
pygame.quit()
print(f"Game Over! Your final score: {score}")

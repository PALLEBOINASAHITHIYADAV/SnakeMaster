# Ultimate Snake Game

## Game Overview

### Objective
The objective is to control a snake, navigate a grid, and consume food to grow in length. The game continues until the snake collides with itself.

### Setup
- The game runs on a **600x600 pixel** grid.
- The snake starts at the center, moving in a default direction (right).
- Food items appear randomly across the grid.

## Gameplay Mechanics

### Snake Movement:
- The snake moves continuously in the last chosen direction.
- Control the movement using **arrow keys (UP, DOWN, LEFT, RIGHT)**.
- The snake now **wraps around** the screen, reappearing on the opposite side when it moves off the edge.
- Added **pause/resume** functionality (**P to pause, R to resume**).
- Press **Q to quit** the game and **C to play again** after game over.

### Eating Food:
- Food appears randomly as small circles.
- When the snake’s head touches food, it eats it and grows in length.
- Food respawns at a different random location after being consumed.
- **Different Food Types:**
  - **Red (Normal Food)**: +10 points
  - **Green (Bonus Food)**: +20 points, increases speed
  - **Blue (Slow Food)**: +10 points, decreases speed
  - **Purple (Poisonous Food)**: -15 points, shortens snake if long enough

### Growth and Scoring:
- The snake increases in length each time it eats food.
- The player's score rises with each food item consumed.
- **Game speed dynamically adjusts** based on food type (increases with bonus food, decreases with slow food).

### Game Over Conditions:
- The game ends if the snake collides with **its own body**.
- The snake does not die upon hitting the screen boundaries due to the **wrap-around** feature.
- If the snake becomes too short due to consuming **poisonous food**, the game ends.

## Features

- **Color Scheme:**
  - The snake is **light yellow**.
  - Food items appear in **various colors** with different effects.
- **User Interaction:**
  - Real-time movement control using arrow keys.
  - Pause/Resume, Quit, and Restart options for better gameplay experience.

## Future Enhancements
- Progressive difficulty as the game advances.
- Introducing **obstacles** on the grid.
- Adding **various levels** with unique challenges and objectives.

## Installation Guide

### Prerequisites
Before running the game, ensure you have:
- **Python 3.x** installed
- **Pygame Library** (install using `pip install pygame`)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PALLEBOINASAHITHIYADAV/UltimateSnakeGame.git
   ```
2. **Navigate to the Game Directory**:
   ```bash
   cd UltimateSnakeGame
   ```
3. **Run the Game**:
   ```bash
   python snake.py
   ```

Enjoy playing **Ultimate Snake Game**! 🐍


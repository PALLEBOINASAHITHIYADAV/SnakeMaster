# Ultimate Snake Game

## Game Overview

### Objective
The objective is to control a snake, navigate a grid, and consume food to grow in length. The game continues until the snake collides with itself or the player decides to quit.

### Setup
- The game runs on a **600x400 pixel** grid.
- The snake starts at the center, moving in a default direction (right).
- Food items appear randomly across the grid.
- Players can **pause (P) and resume (R)** the game at any time.
- Press **Q** to quit the game or **C** to restart after losing.

## Gameplay Mechanics

### Snake Movement:
- The snake moves continuously in the last chosen direction.
- Control the movement using **arrow keys (UP, DOWN, LEFT, RIGHT)**.
- The snake will **die upon hitting the screen boundaries**.

### Eating Food:
- Food appears randomly as small green squares.
- When the snake’s head touches food, it eats it and grows in length.
- Food respawns at a different random location after being consumed.

### Growth and Scoring:
- The snake increases in length each time it eats food.
- The player's score rises with each food item consumed.
- **Game speed gradually increases** as the snake grows.

### Game Over Conditions:
- The game ends if the snake collides with **its own body**.
- The game also ends if the snake **hits the screen boundaries**.
- Players can restart the game by pressing **C** or quit by pressing **Q**.

## Features

- **Color Scheme:**
  - The snake is **blue**.
  - Food items appear as **green squares**.
- **User Interaction:**
  - Real-time movement control using arrow keys.
  - Pause and resume functionality (**P** to pause, **R** to resume).
  - Restart (**C**) or quit (**Q**) after losing.

## Future Enhancements
- Progressive difficulty as the game advances.
- Introducing **obstacles** on the grid.
- Adding **various levels** with unique challenges and objectives.
- Implementing a leaderboard for high scores.

## Installation Guide

### Prerequisites
Before running the game, ensure you have:
- **Python 3.x** installed
- **Pygame Library** (install using `pip install pygame`)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PALLEBOINASAHITHIYADAV/SnakeMaster.git
   ```
2. **Navigate to the Game Directory**:
   ```bash
   cd SnakeMaster
   ```
3. **Run the Game**:
   ```bash
   python snake.py
   ```

Enjoy playing **Ultimate Snake Game**! 🐍


# Tic-Tac-Toe Minimax Agent

A command-line Tic-Tac-Toe game implemented in Python, where the computer player uses the Minimax algorithm to make optimal decisions.

## Overview

This project demonstrates the use of the Minimax algorithm in a two-player, turn-based game. The AI evaluates possible future game states and selects the move that leads to the best possible outcome, assuming the opponent also plays optimally.

The project was built to explore concepts related to artificial intelligence, adversarial search, recursion, and game trees.

## Features

* Human vs AI gameplay
* AI powered by the Minimax algorithm
* Recursive game-state evaluation
* Win, loss, and draw detection
* Command-line interface
* No external dependencies

## How Minimax Works

Minimax is an adversarial search algorithm commonly used in two-player games.

The AI evaluates each possible move by recursively simulating future turns. Each terminal game state is assigned a value:

| Result     | Score |
| ---------- | ----: |
| AI wins    |     1 |
| Draw       |     0 |
| Human wins |    -1 |

The AI attempts to maximize the score, while assuming the opponent will attempt to minimize it.

For a given board state, the algorithm:

1. Generates all possible moves.
2. Simulates each move.
3. Recursively evaluates the resulting game states.
4. Assigns a score to each outcome.
5. Selects the move with the highest achievable score.

## Board

The board uses positions from 0 to 8:

```text
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

The player enters the position where they want to place their mark.

## Requirements

* Python 3.x

No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/ajib111/tictactoe-minimax-agent.git
```

Navigate to the project directory:

```bash
cd tictactoe-minimax-agent
```

Run the program:

```bash
python tictactoe.py
```

If your system uses `python3`:

```bash
python3 tictactoe.py
```

## Project Structure

```text
tictactoe-minimax-agent/
├── tictactoe.py
└── README.md
```

## Concepts Demonstrated

* Artificial Intelligence
* Minimax algorithm
* Adversarial search
* Recursion
* Game trees
* State-space search
* Decision making

## Future Improvements

* Implement Alpha-Beta pruning
* Add difficulty levels
* Add a graphical user interface
* Add player vs player mode
* Add game statistics
* Add replay functionality

## Author

Ajib Dahal

GitHub: https://github.com/ajib111
Portfolio: https://ajibdahal.vercel.app

# Tic-Tac-Toe Game (Python)

## Overview
This is a Python-based Tic-Tac-Toe game that supports two modes:
- **Player vs. Player (PvP)**: Two players take turns manually.
- **Player vs. AI (PvAI)**: The AI uses the **Minimax algorithm with Alpha-Beta Pruning** to make optimal moves.

## Features
- Supports **two-player mode**.
- AI opponent using **Minimax with Alpha-Beta pruning** for efficiency.
- Simple **command-line interface (CLI)** for easy interaction.
- Detects wins, losses, and draws automatically.

## Project Structure
```
Tic-Tac-Toe/
│── main.py          # Runs the game and manages user interactions
│── TicTacToe.py     # Implements the game logic and AI using Minimax
│── README.md        # Project documentation
```

## Installation & Usage
### Prerequisites
- Python 3.11+ (Ensure Python is installed)

### Running the Game
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:
   ```bash
   python main.py
   ```
4. Choose between **PvP** or **PvAI** mode and start playing!

## How the AI Works
- The AI evaluates the game board using **Minimax with Alpha-Beta Pruning**.
- The algorithm ensures **optimal moves** by minimizing the worst possible loss.
- **Alpha-Beta Pruning** speeds up the decision-making process by ignoring unnecessary calculations.

## Sample Images
![image](https://github.com/user-attachments/assets/917cae90-868e-4a84-8d13-6b691294ee9b)
![image](https://github.com/user-attachments/assets/6984a19d-af80-4d8f-88a2-942984014265)
![image](https://github.com/user-attachments/assets/36c918ab-885b-415e-97e1-a059ce422e55)
![image](https://github.com/user-attachments/assets/e7581392-5e61-43c1-b1b1-a0f51e5442d5)



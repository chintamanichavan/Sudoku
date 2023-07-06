# Sudoku Game

This is a simple Sudoku game implemented in Python using the Pygame library. The game allows you to play Sudoku puzzles and also provides a solver to automatically solve the puzzles.

## Requirements

- Python 3.x
- Pygame library

## How to Run

1. Make sure you have Python installed on your system.
2. Install the Pygame library by running the following command:
   ```
   pip install pygame
   ```
3. Save the code provided in a file named `sudoku_game.py`.
4. Open a terminal or command prompt and navigate to the directory where the `sudoku_game.py` file is saved.
5. Run the following command to start the game:
   ```
   python sudoku_game.py
   ```

## Instructions

- The Sudoku puzzle is displayed on the game window.
- Use the mouse to select a cell by clicking on it.
- Use the number keys (1-9) to enter a number in the selected cell.
- Press the Enter key to deselect a cell.
- Press the Backspace or Delete key to clear the selected cell.
- Press the Space key to solve the Sudoku puzzle automatically.

## Controls

- Mouse Left-Click: Select a cell
- Number Keys (1-9): Enter a number in the selected cell
- Enter Key: Deselect the cell
- Backspace or Delete Key: Clear the selected cell
- Space Key: Solve the Sudoku puzzle automatically

## How it Works

- The game uses the Pygame library to create the game window and handle user input.
- The Sudoku board is represented as a 2D list of numbers.
- The game provides an example Sudoku puzzle that can be modified or replaced with custom puzzles.
- The solver uses a backtracking algorithm to recursively solve the Sudoku puzzle.
- The solver checks the validity of each number entered in a cell by verifying that it doesn't already exist in the same row, column, or 3x3 box.
- The game continuously updates the game window to display the Sudoku board and the selected cell.
- The game loop handles user events and updates the board accordingly.

Feel free to modify and enhance the code as per your requirements. Enjoy playing Sudoku!

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 540
HEIGHT = 600
CELL_SIZE = 60
BOARD_SIZE = CELL_SIZE * 9
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

# Set up fonts
pygame.font.init()
FONT_SIZE = 40
FONT = pygame.font.SysFont("Arial", FONT_SIZE)

# Initialize the Sudoku board
board = [[0 for _ in range(9)] for _ in range(9)]
selected = None

# Load an example Sudoku puzzle
example_puzzle = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]
board = example_puzzle.copy()


def draw_board():
    WIN.fill(WHITE)
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(WIN, BLACK, (0, i * CELL_SIZE), (BOARD_SIZE, i * CELL_SIZE), 3)
            pygame.draw.line(WIN, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_SIZE), 3)
        else:
            pygame.draw.line(WIN, GRAY, (0, i * CELL_SIZE), (BOARD_SIZE, i * CELL_SIZE), 1)
            pygame.draw.line(WIN, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_SIZE), 1)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text_surface = FONT.render(str(board[i][j]), True, BLUE)
                text_rect = text_surface.get_rect(center=((j * CELL_SIZE) + (CELL_SIZE // 2),
                                                          (i * CELL_SIZE) + (CELL_SIZE // 2)))
                WIN.blit(text_surface, text_rect)

    if selected:
        pygame.draw.rect(WIN, BLUE, (selected[1] * CELL_SIZE, selected[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)


def solve_sudoku():
    for row in range(9):
        for colin range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num):
                        board[row][col] = num
                        if solve_sudoku():
                            return True
                        board[row][col] = 0
                return False
    return True


def is_valid(row, col, num):
    # Check if the number already exists in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number already exists in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number already exists in the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def get_cell(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                selected = get_cell(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve_sudoku()
            if event.key == pygame.K_RETURN:
                selected = None
            if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                if selected:
                    board[selected[0]][selected[1]] = 0
            if event.key == pygame.K_1:
                if selected:
                    board[selected[0]][selected[1]] = 1
            if event.key == pygame.K_2:
                if selected:
                    board[selected[0]][selected[1]] = 2
            if event.key == pygame.K_3:
                if selected:
                    board[selected[0]][selected[1]] = 3
            if event.key == pygame.K_4:
                if selected:
                    board[selected[0]][selected[1]] = 4
            if event.key == pygame.K_5:
                if selected:
                    board[selected[0]][selected[1]] = 5
            if event.key == pygame.K_6:
                if selected:
                    board[selected[0]][selected[1]] = 6
            if event.key == pygame.K_7:
                if selected:
                    board[selected[0]][selected[1]] = 7
            if event.key == pygame.K_8:
                if selected:
                    board[selected[0]][selected[1]] = 8
            if event.key == pygame.K_9:
                if selected:
                    board[selected[0]][selected[1]] = 9

    draw_board()
    pygame.display.update()

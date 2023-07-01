import random


def generate_sudoku():
    # Initialize an empty board
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill in the diagonal boxes
    for i in range(0, 9, 3):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                board[i + j][i + k] = nums.pop()

    # Solve the puzzle
    solve_sudoku(board)

    # Remove some numbers from the board to create a puzzle
    empty_cells = 45  # Number of empty cells in the puzzle
    while empty_cells > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            empty_cells -= 1

    return board


def solve_sudoku(board):
    # Find the next empty cell
    row, col = find_empty_cell(board)
    if row == -1:  # If there are no empty cells left, the puzzle is solved
        return True

    # Try each possible value for the empty cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # Place the number in the empty cell
            board[row][col] = num

            # Recursively solve the puzzle
            if solve_sudoku(board):
                return True

            # If the puzzle cannot be solved with this number, remove it
            board[row][col] = 0

    # If none of the possible numbers work, backtrack
    return False


def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return -1, -1  # If there are no empty cells left, return -1


def is_valid_move(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


def print_board(board):
    for row in board:
        print(row)

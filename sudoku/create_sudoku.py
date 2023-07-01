from sudoku import generate_sudoku, print_board, solve_sudoku

# Generate a Sudoku puzzle
board = generate_sudoku()

# Print the puzzle
print("Puzzle:")
print_board(board)

# Solve the puzzle
if solve_sudoku(board):
    print("Solved:")
    print_board(board)
else:
    print("Unsolvable puzzle.")

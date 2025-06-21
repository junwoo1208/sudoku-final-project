from generator import generate_board
from solver import solve, print_board

if __name__ == "__main__":
    print("Generated Sudoku Puzzle:")
    board = generate_board()
    print_board(board)

    print("\nSolving...")
    if solve(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("No solution exists.")

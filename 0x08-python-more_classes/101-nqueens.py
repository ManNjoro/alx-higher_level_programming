#!/usr/bin/python3
"""
    chess class.

"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position
    (row, col) on the board.

    Args:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Args:
        n (int): The size of the board and the number of queens.

    Returns:
        list[list[int]]: List of solutions, each represented as a list
        of queen positions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def solve_nqueens_util(board, row, solutions):
    """
    Recursive utility function to solve the N-Queens problem.

    Args:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The current row to consider.
        solutions (list[list[int]]): List of solutions, each represented
        as a list of queen positions.
    """
    n = len(board)

    # Base case: If all queens are placed, add the solution to the list
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, solutions)
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print the solutions to the N-Queens problem.

    Args:
        solutions (list[list[int]]): List of solutions, each
        represented as a list of queen positions.
    """
    for solution in solutions:
        print(solution)


def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem and print the solutions
    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

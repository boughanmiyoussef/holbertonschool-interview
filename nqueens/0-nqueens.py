#!/usr/bin/python3
"""Solves the N Queens problem using backtracking.

"""

import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_not_number_and_exit():
    """Print number error message and exit with status 1."""
    print("N must be a number")
    sys.exit(1)


def print_too_small_and_exit():
    """Print size error message and exit with status 1."""
    print("N must be at least 4")
    sys.exit(1)


def is_safe(queens, row, col):
    """Check if it's safe to place a queen at (row, col).

    Args:
        queens (list): Current list of queen column positions per row.
        row (int): The row to place a new queen.
        col (int): The column to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(row, n, queens, solutions):
    """Recursive backtracking solver.

    Args:
        row (int): Current row to place a queen.
        n (int): Total number of queens.
        queens (list): Current board state.
        solutions (list): List of all valid solutions.
    """
    if row == n:
        solution = [[r, queens[r]] for r in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve(row + 1, n, queens, solutions)


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_not_number_and_exit()

    if n < 4:
        print_too_small_and_exit()

    queens = [-1] * n
    solutions = []
    solve(0, n, queens, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

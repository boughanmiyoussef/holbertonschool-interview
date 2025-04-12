#!/usr/bin/env python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists of integers representing Pascal's triangle.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []  # Return an empty list if n <= 0

    triangle = [[1]]  # Initialize the triangle with the first row [1]

    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Compute the values in the middle of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        # Append the completed row to the triangle
        triangle.append(row)

    return triangle
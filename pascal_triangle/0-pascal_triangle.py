#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists of integers representing Pascal's triangle.
                       Returns an empty list if n <= 0.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Build the triangle row by row
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Compute the middle values of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        # Append the completed row to the triangle
        triangle.append(row)

    return triangle
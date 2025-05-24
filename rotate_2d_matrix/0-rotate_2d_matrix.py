def rotate_2d_matrix(matrix):
    """
    Rotate the n x n 2D matrix by 90 degrees clockwise in-place.
    
    The matrix will be rotated without using extra space, 
    meaning the rotation is done in-place. This is accomplished by:
    1. Transposing the matrix (swap rows and columns).
    2. Reversing each row to complete the 90-degree clockwise rotation.

    Args:
        matrix (list[list[int]]): A square 2D matrix to rotate.
    
    Returns:
        None: The matrix is modified in-place.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row to complete the 90-degree rotation
    for i in range(n):
        matrix[i].reverse()

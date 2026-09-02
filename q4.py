def multiply_matrices(matrix_a, matrix_b):
    """
    Multiplies two matrices and returns the resulting matrix.
    Prints an error and returns None if multiplication is impossible.
    """
    # STEP 1: Get the dimensions of both matrices
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    # STEP 2: Check if multiplication is mathematically possible
    if cols_a != rows_b:
        print(f"Error: Impossible to multiply a {rows_a}x{cols_a} matrix with a {rows_b}x{cols_b} matrix.")
        print(f"The number of columns in Matrix A ({cols_a}) must equal the number of rows in Matrix B ({rows_b}).")
        return None

    # STEP 3: Create an empty result matrix (The step-by-step way)
    result = [] 
    for i in range(rows_a): 
        new_row = []
        for j in range(cols_b): 
            new_row.append(0)
        result.append(new_row) 
    
    # STEP 4: Perform the multiplication using three nested loops
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a): 
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result

def print_matrix(matrix):
    """Helper function to print matrices in a neat grid."""
    if matrix is None:
        return
    for row in matrix:
        # Formats each number to take up exactly 4 spaces
        formatted_row = [f"{num:4}" for num in row] 
        print("[" + " ".join(formatted_row) + " ]")

# ==========================================
# --- TEST CASES & EXECUTION ---
# ==========================================

if __name__ == "__main__":
    print("--- Test 1: 2x2 Multiplication ---")
    matrix_x = [
        [1, 2],
        [3, 4]
    ]
    matrix_y = [
        [5, 6],
        [7, 8]
    ]
    result_1 = multiply_matrices(matrix_x, matrix_y)
    print_matrix(result_1)
    
    print("\n--- Test 2: Row Vector by Column Vector ---")
    row_vector = [
        [1, 2, 3]
    ] # 1x3
    col_vector = [
        [4],
        [5],
        [6]
    ] # 3x1
    result_2 = multiply_matrices(row_vector, col_vector)
    print_matrix(result_2)
    
    print("\n--- Test 3: Intentional Failure ---")
    matrix_c = [
        [1, 1, 1],
        [2, 2, 2]
    ] # 2x3
    matrix_d = [
        [3, 3],
        [4, 4]
    ] # 2x2
    result_3 = multiply_matrices(matrix_c, matrix_d)
  
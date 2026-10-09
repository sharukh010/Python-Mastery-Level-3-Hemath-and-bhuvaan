def matrix_multiplication(a,b): 
    # a,b are matrixes 
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    c = [[0 for i in range(cols_b)]for i in range(rows_a)]
    # row -> row index of matrix A 
    # col -> col index of matrix c 
    # r -> row index in matrix b and column index in matrix a 
    for row in range(rows_a): 
        for col in range(cols_b): 
            for r in range(rows_b): 
                c[row][col] += a[row][r] * b[r][col]
                
    return c 
    

                
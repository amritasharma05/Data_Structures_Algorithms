"""
Write an algorithm such that if an element in an M*N matrix is 0, entire row and columns are set to 0
Approach
1. Iterate the matrix
2. Determine zero elements and nullify corresponding rows and columns with 0
Time Complexity - O(N^2)
Space Complexity - O(N^2)
"""


def nullify_rows(matrix,row):
    for index in range(len(matrix[0])): # number of columns
        matrix[row][index] = 0


def nullify_cols(matrix,col):
    for index in range(len(matrix)): # number of rows
        matrix[index][col] = 0


def zero_matrix(matrix):
    if matrix is None:
        return None
    rows = []
    cols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    for row in rows:
        nullify_rows(matrix,row)

    for col in cols:
        nullify_cols(matrix,col)
    return matrix


matrix = [[1,0,1],[1,1,1],[1,1,1]]
print("Original Matrix", matrix)
print("Zero Matrix", zero_matrix(matrix))



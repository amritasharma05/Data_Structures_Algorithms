"""
Given an image represented by N*M matrix, where each pixel in the image is 4 bytes, write a method to rotate the image
by 90 degrees. Can you do this in place?
Time Complexity - O(N^2)
Space Complexity - O(N^2)
Approach - Iterate the matrix and rotate layer by layer
"""


matrix = [[1,2,3],
         [4,5,6],
         [7,8,9]]


def rotate_matrix(matrix):
    N = len(matrix[0]) # 3
    for i in range(N//2): # 1
        for j in range(i, N-i-1): # (0,1)
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp

    return matrix

print("Actual Image", matrix)
print("Rotated 90 degrees Clock-wise", rotate_matrix(matrix))
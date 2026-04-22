class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrixCopy = [x[:] for x in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][len(matrix) - 1 - i] = matrixCopy[i][j]
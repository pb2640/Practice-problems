class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix[i])):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
            return matrix

        def reverse(matrix):
            for i in range(len(matrix)):
                j1 = 0
                j2 = len(matrix[i]) - 1
                while j1 < j2:
                    temp = matrix[i][j1]
                    matrix[i][j1] = matrix[i][j2]
                    matrix[i][j2] = temp
                    j1 += 1
                    j2 -= 1
            return matrix

        matrix = transpose(matrix)
        matrix = reverse(matrix)
        return matrix

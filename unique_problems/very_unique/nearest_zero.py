class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat2 = [row.copy() for row in mat]
        # visit all cells of the matrix
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                ele = mat[i][j]
                if ele:
                    top = mat[i - 1][j] if i else float("inf")
                    left = mat[i][j - 1] if j else float("inf")
                    mat[i][j] = min(top + 1, left + 1)

        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[i]) - 1, -1, -1):
                ele = mat[i][j]
                if ele:
                    bottom = mat[i + 1][j] if (i < len(mat) - 1) else float("inf")
                    right = mat[i][j + 1] if (j < len(mat[i]) - 1) else float("inf")
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
        return mat

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_visited = set()
        col_visited = set()
        coords = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    coords.add((i, j))
                    # make row ele 0
        for coord in coords:
            i = coord[0]
            j = coord[1]
            for c in range(len(matrix[i])):
                matrix[i][c] = 0

            for c in range(len(matrix)):
                matrix[c][j] = 0

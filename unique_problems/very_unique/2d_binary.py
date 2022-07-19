class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        unpack 2d array to 1d
        do binary search
        O(n)#bad
        ANother approach:
        treat this 2d array as a 1d array,
        find a mapping between the 2d position to 1d pos
        perform binary search
        """

        def encode(pos, n):
            # i is the row pos, j is the col
            # n is the number of columns
            i = pos[0]
            j = pos[1]
            return (i * n) + j

        def decode(x, n):
            i = x // n
            j = x % n
            return i, j

        l = [0, 0]
        n = len(matrix[0])
        r = [len(matrix) - 1, n - 1]
        lx = encode(l, n)
        rx = encode(r, n)
        while lx <= rx:
            mid = (lx + rx) // 2
            i, j = decode(mid, n)
            mid_ele = matrix[i][j]
            if mid_ele == target:
                return True
            elif mid_ele > target:
                rx = mid - 1
            else:
                lx = mid + 1
        return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def identify_box(row, col):
            if row <= 2 and col <= 2:
                return 0
            if col > 2 and col <= 5 and row <= 2:
                return 1
            if col > 5 and row <= 2:
                return 2
            if row > 2 and row <= 5 and col <= 2:
                return 3
            if row > 2 and row <= 5 and col > 2 and col <= 5:
                return 4
            if row > 2 and row <= 5 and col <= 8:
                return 5
            if row > 5 and row <= 8 and col <= 2:
                return 6
            if row > 5 and row <= 8 and col > 2 and col <= 5:
                return 7
            else:
                return 8

        num_set = [i for i in range(1, 10)]
        num_set = set(num_set)
        row_ref = {}
        col_ref = {}
        box_ref = {}
        for i in range(9):
            row_ref[i] = num_set.copy()
            col_ref[i] = num_set.copy()
            box_ref[i] = num_set.copy()
        for i in range(len(board)):
            for j in range(len(board[i])):
                ele = board[i][j]
                if ele == ".":
                    continue
                ele = int(ele)
                box_num = identify_box(i, j)
                # print(row_ref[i])
                if ele not in row_ref[i]:

                    # print(ele,i,j,"row_ref")
                    return False
                else:
                    row_ref[i].remove(ele)
                if ele not in col_ref[j]:
                    # print(ele,i,j,"col_ref")
                    return False
                else:
                    col_ref[j].remove(ele)
                if ele not in box_ref[box_num]:
                    # print(ele,i,j,"box_ref")
                    return False
                else:
                    box_ref[box_num].remove(ele)
        return True

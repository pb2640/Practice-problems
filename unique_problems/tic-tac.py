class TicTacToe:
    def __init__(self, n: int):
        self.arr = []
        self.n = n
        temp = [0] * n
        for i in range(n):
            self.arr.append(temp.copy())

    def move(self, row: int, col: int, player: int) -> int:
        self.arr[row][col] = player
        n = self.n
        # check row
        ans_row, ans_diag_l, ans_diag_r, ans_col = player, player, player, player
        for i in range(n):
            if self.arr[i][col] != player:
                ans_row = 0
                break
        for i in range(n):
            if self.arr[row][i] != player:
                ans_col = 0
                break
        # left diagnol
        for i in range(n):
            if self.arr[i][i] != player:
                ans_diag_l = 0
                break
        # for right diagnol
        for i in range(n):
            if self.arr[i][n - i - 1] != player:
                ans_diag_r = 0
                break

        # print(self.arr)
        return max(ans_row, ans_col, ans_diag_l, ans_diag_r)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

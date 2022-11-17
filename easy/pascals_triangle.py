class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        if numRows == 1:
            return [ans[0]]
        for i in range(2, numRows):
            prev = ans[i - 1]
            temp = [1]
            for j in range(len(prev) - 1):
                temp.append(prev[j] + prev[j + 1])
            temp.append(1)
            ans.append(temp)
        return ans

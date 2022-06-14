class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dic = {}
        for i in range(len(ref)):
            dic[ref[i]] = i+1
        ans = 0
        for i in range(len(columnTitle)):
            ans+=dic[columnTitle[len(columnTitle)-i-1]]*(26**i)
        return ans
            
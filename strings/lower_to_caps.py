class Solution:
    def toLowerCase(self, s: str) -> str:
        big = "QWERTYUIOPASDFGHJKLZXCVBNM"
        small = "qwertyuiopasdfghjklzxcvbnm"
        big = set(big)
        small = set(small)
        ans = ""
        for letter in s:
            if letter in big:
                ans += letter.lower()
            else:
                ans += letter
        return ans

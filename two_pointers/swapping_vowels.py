class Solution:
    def reverseVowels(self, s: str) -> str:
        ref = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        l = 0
        r = len(s) - 1
        ans = list(s)
        while l < r:
            if s[l] in ref and s[r] in ref:
                temp = ans[l]
                ans[l] = ans[r]
                ans[r] = temp
                l += 1
                r -= 1
                continue
            if s[l] not in ref:
                l += 1
            if s[r] not in ref:
                r -= 1
        return "".join(ans)

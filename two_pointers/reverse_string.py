class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        ref = set(list("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm"))
        while l < r:
            if s[l] in ref and s[r] in ref:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
            if s[l] not in ref:
                l += 1
            if s[r] not in ref:
                r -= 1
        return "".join(s)

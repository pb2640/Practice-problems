# 1844. Replace All Digits with Characters
class Solution:
    def replaceDigits(self, s: str) -> str:
        ref = list("abcdefghijklmnopqrstuvwxyz")
        i = 0
        mapping = {}
        for char in ref:
            mapping[char] = i
            i += 1
        ans = ""
        for i in range(0, len(s) - 1, 2):
            char = s[i]
            num = s[i + 1]
            ans += char + ref[mapping[char] + int(num)]
        if len(s) % 2 != 0:
            ans += s[len(s) - 1]
        return ans

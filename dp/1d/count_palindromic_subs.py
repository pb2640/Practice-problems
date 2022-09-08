class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for j in range(len(s)):
            count += 1
            if j > 0 and j < len(s) - 1:
                l = j - 1
                r = j + 1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
            if j < len(s) - 1:
                l = j
                r = j + 1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
        return count

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        ans = s[0]

        for i in range(len(s)):
            temp_s1 = ""
            if i > 0 and i < len(s) - 1 and s[i - 1] == s[i + 1]:
                temp_s1 = s[i]
                l = i - 1
                r = i + 1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        temp_s1 = s[l] + temp_s1 + s[r]
                        l -= 1
                        r += 1
                    else:
                        break

            temp_s2 = ""
            if i > 0 and s[i - 1] == s[i]:
                l = i - 1
                r = i
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        temp_s2 = s[l] + temp_s2 + s[r]
                        l -= 1
                        r += 1
                    else:
                        break
            if len(temp_s1) > len(temp_s2):
                if len(temp_s1) > len(ans):
                    ans = temp_s1
            else:
                if len(temp_s2) > len(ans):
                    ans = temp_s2

        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):

            seen = set()
            j = i
            while j < len(s) and s[j] not in seen:

                seen.add(s[j])
                j += 1
            ans = max(ans, j - i)
        return ans

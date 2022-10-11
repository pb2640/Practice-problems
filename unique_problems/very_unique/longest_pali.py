class Solution:
    def longestPalindrome(self, s: str) -> int:
        ref = set()
        ans = 0
        for alpha in s:
            if alpha in ref:
                ans += 2
                ref.remove(alpha)
            else:
                ref.add(alpha)
        if len(ref) > 0:
            ans += 1
        return ans

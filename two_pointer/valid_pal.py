class Solution:
    def isPalindrome(self, s: str) -> bool:
        # base case
        if len(s) == 1:
            return True
        l = 0
        r = len(s) - 1
        while l < r:

            # find valid left pointer
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

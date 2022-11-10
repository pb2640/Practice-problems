class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # to track first and last occurences
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]][1] = i
            else:
                hashmap[s[i]] = [i, i]
        ans = 0
        for item in hashmap:
            first = hashmap[item][0]
            last = hashmap[item][1]
            print(first, last)
            if first < last:
                ans += len(set(s[first + 1 : last]))
        return ans

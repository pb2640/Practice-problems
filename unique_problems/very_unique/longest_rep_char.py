class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        hashmap = {}
        for r in range(len(s)):

            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            char_count = r - l + 1
            if char_count - max(hashmap.values()) <= k:
                max_len = max(max_len, char_count)
            else:
                hashmap[s[l]] -= 1
                l += 1
        return max_len

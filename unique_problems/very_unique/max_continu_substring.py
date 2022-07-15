class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_len = 0
        while i < len(s):
            temp_hash = set()
            j = i
            temp_str = ""
            mp = {}
            next_idx = 0
            while j < len(s):
                if s[j] not in temp_hash:
                    temp_str += s[j]
                    temp_hash.add(s[j])
                    mp[s[j]] = j
                    j += 1
                else:
                    next_idx = mp[s[j]]
                    break
            if len(temp_str) > max_len:
                max_len = len(temp_str)
            i += 1
        return max_len

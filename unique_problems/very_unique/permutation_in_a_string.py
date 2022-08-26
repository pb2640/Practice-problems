from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_s1 = Counter(s1)
        i, j = 0, 0
        temp = ""
        while j < len(s1):
            temp += s2[j]
            j += 1
        hash_s2 = Counter(temp)
        if hash_s1 == hash_s2:
            return True
        while j < len(s2):
            if s2[j] in hash_s2:
                hash_s2[s2[j]] += 1
            else:
                hash_s2[s2[j]] = 1
            hash_s2[s2[i]] -= 1
            if hash_s2 == hash_s1:
                return True
            i += 1
            j += 1
        return False

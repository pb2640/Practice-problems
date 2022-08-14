class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        total = 0
        for char in s1:
            total += 1
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        i = 0

        while i < len(s2):
            flag = 0
            if s2[i] in hashmap:
                temp_hashmap = hashmap.copy()
                j = i
                temp_total = total
                while temp_total > 0 and j < len(s2):
                    if s2[j] not in temp_hashmap:
                        flag = 1
                        break

                    else:
                        if temp_hashmap[s2[j]] > 0:
                            temp_hashmap[s2[j]] -= 1
                            temp_total -= 1
                        else:
                            break

                    j += 1
                if temp_total == 0:
                    return True
            if flag:
                i = j + 1
            else:
                i += 1
        return False

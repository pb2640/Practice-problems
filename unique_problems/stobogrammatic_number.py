class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dict_strob = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        i = 0
        j = len(num) - 1
        while i <= j:
            if num[i] not in dict_strob or num[j] not in dict_strob:
                return False
            elif dict_strob[num[i]] == num[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ref = set(list("QWERTYUIOPASDFGHJKLZXCVBNM"))
        if len(word) == 1:
            return True
        first = word[0]
        second = word[1]
        if first not in ref:
            # rets letters should not be in if for true
            for letter in word:
                if letter in ref:
                    return False
            return True
        if first in ref and second in ref:
            for letter in word:
                if letter not in ref:
                    return False
            return True
        else:
            for i in range(2, len(word)):
                if word[i] in ref:
                    return False
            return True

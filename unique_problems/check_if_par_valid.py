class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        bal = 0
        for i in range(len(s)):
            if locked[i] == "0" or s[i] == "(":
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        bal = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0" or s[i] == ")":
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return True

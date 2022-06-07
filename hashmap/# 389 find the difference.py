# 389 find the difference
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)

        for char in t:
            if char not in counter_s or counter_s[char] == 0:
                return char
            else:
                counter_s[char] -= 1

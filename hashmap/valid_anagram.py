class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        for letter in t:
            if letter not in hashmap:
                return False
            else:
                hashmap[letter] -= 1
        for item in hashmap:
            if hashmap[item] != 0:
                return False
        return True

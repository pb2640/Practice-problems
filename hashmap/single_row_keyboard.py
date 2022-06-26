class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        for i in range(len(keyboard)):
            hashmap[keyboard[i]] = i
        index = 0
        ans = 0
        for letter in word:
            ans+=abs(hashmap[letter]-index)
            index = hashmap[letter]
        return ans
        
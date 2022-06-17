class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for char in magazine:
            if char in hashmap:
                hashmap[char]+=1
            else:
                hashmap[char]=1
        for char in ransomNote:
            if char in hashmap:
                hashmap[char]-=1
            else:
                return False
        for char in ransomNote:
            if(hashmap[char] <0):
                return False
        return True
        
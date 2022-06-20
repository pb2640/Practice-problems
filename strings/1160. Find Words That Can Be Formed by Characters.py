class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # O(len(words)*len(max_word))
        hashmap = {}
        for char in chars:
            if char in hashmap:
                hashmap[char]+=1
            else:
                hashmap[char] = 1
        ans = 0
        for word in words:
            flag = 1
            temp = hashmap.copy()
            for char in word:
                if(char in temp and temp[char]!=0):
                    temp[char]-=1
                else:
                    flag = 0
                    break
            if(flag):
                ans+=len(word)
            
        return ans
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if(len(pref)>len(word)):
                continue
            elif(pref==word[:len(pref)]):
                count+=1
        return count
        
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = [] 
        w2 = []
        for i in range(len(wordsDict)):
            if(word1==wordsDict[i]):
                w1.append(i)
            elif(word2==wordsDict[i]):
                w2.append(i)
        
        mini = float("inf")
        for i in w1:
            for j in w2:
                mini = min(mini,abs(i-j))
                
        return mini
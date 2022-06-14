# class Solution:
#     def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
#         w1 = [] 
#         w2 = []
#         for i in range(len(wordsDict)):
#             if(word1==wordsDict[i]):
#                 w1.append(i)
#             elif(word2==wordsDict[i]):
#                 w2.append(i)
        
#         mini = float("inf")
#         for i in w1:
#             for j in w2:
#                 mini = min(mini,abs(i-j))
                
#         return mini

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1,i2 = -1,-1
        mini = len(wordsDict)
        for i in range(len(wordsDict)):
            if(word1==wordsDict[i]):
                i1 = i
            elif(word2==wordsDict[i]):
                i2 = i
            if(i1!=-1 and i2!=-1):
                mini = min(mini,abs(i1-i2))
            if(mini==1):
                return 1
        return mini
                
        
        
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ref = []
        # calculate the sum of 1's in the matrix
        for i in range(len(mat)):
            ref.append([sum(mat[i]),i])
        ref.sort(key=lambda x:x[0])
        ans = []
        it = 0
        while(len(ans)<k):
            if(ref[it][0]<ref[it+1][0]):
                ans.append(ref[it][1])
            elif(ref[it][0]==ref[it+1][0] and ref[it][1]<ref[it+1][1]):
                ans.append(ref[it][1])
            it+=1
        # print(ref)
        return ans
        
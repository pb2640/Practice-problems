class Solution:
    def kWeakestRows(self, mat, k):
        """
        make a refrence array, classify a row as weak/not-weak,
        append [index,count_soldiers] if the row is weak
        sort the array by count_soldier as the key
        return first k indexes

        IMPROVEMENT: use heap
        """
        ref = []
        for i in range(len(mat)):
            ref.append([i, sum(mat[i])])
        ref.sort(key=lambda x: x[1])
        ans = []
        for i in range(k):
            ans.append(ref[i][0])
        return ans

        # i = 0
        # j = 1
        # ref = []
        # while(j<len(mat)):
        #     row_i = sum(mat[i])
        #     row_j = sum(mat[j])
        #     if(row_i<=row_j):
        #         ref.append([i,row_i])
        #     else:
        #         ref.append([j,row_j])
        #         i+=2
        #         j+=2
        #         continue
        #     i+=1
        #     j+=1
        # #sort ref by count soldiers
        # ref.sort(key = lambda x:x[1])
        # print(ref)
        # mat = []
        # for i in range(min(k,len(ref))):
        #     mat.append(ref[i][0])
        # return mat

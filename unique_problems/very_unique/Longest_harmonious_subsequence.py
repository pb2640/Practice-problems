class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        ans = 0
        unique = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]][1] = i
            else:
                hashmap[nums[i]] = [i, i]
            unique.add(nums[i])
        # print(hashmap)
        # calcaulate max
        for num in unique:
            if num + 1 in hashmap:
                ans = max(ans, (hashmap[num + 1][1] + 1 - hashmap[num][0]))
        return ans

        # brute force approach


#         ans = 0

#         for i in range(len(nums)):
#             count = 0
#             flag = False
#             for j in range(len(nums)):
#                 if(nums[j]==nums[i]):
#                     count+=1
#                 elif(nums[j]==nums[i]+1):
#                     count+=1
#                     flag = True
#             if(flag):
#                 ans = max(ans,count)

#         return ans

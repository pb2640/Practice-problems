class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        hashmap = {}
        for i in range(len(nums)):
            if(nums[i] in hashmap):
                continue
            else:
                hashmap[nums[i]] = 1
            for j in range(i+1,len(nums)-1):
                if(nums[j]==nums[i]-1):
                    hashmap[nums[i]]+=1
            if(ans<hashmap[nums[i]]):
                ans = hashmap[nums[i]]
        return ans
                
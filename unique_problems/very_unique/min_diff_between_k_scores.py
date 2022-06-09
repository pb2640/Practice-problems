class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #sort and sliding difference
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)-k+1):
            ans = min(ans,nums[k+i-1]-nums[i])
        return ans
            
        
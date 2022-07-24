class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        temp_max = nums[0]
        for i in range(1, len(nums)):

            temp_max = max(nums[i], nums[i] + temp_max)

            ans = max(ans, temp_max)

        return ans

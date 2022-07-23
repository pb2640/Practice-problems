class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this will fail because one number can be repeated more than once
        n = len(nums) - 1
        sum_without_num = n * (n + 1) // 2
        sum_with_num = 0
        for num in nums:
            sum_with_num += num

        ans = sum_with_num - sum_without_num
        if ans == 0:
            return nums[0]
        return ans

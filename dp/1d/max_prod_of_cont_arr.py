class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        min_so_far = nums[0]
        max_so_far = nums[0]

        ans = max_so_far
        for i in range(1, len(nums)):
            curr = nums[i]
            max_temp = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = max_temp
            ans = max(ans, max_so_far)
        return ans

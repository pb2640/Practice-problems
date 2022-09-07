class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        hashmap = {}
        # n below is the house number[0,len(nums)-1]
        def rob(n):
            if n > len(nums) - 1:
                return 0
            if n in hashmap:
                return hashmap[n]
            cost_n = nums[n] + max(rob(n + 2), rob(n + 3))
            hashmap[n] = cost_n
            return cost_n

        return max(rob(0), rob(1))

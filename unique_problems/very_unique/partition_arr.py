class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        res = 1
        nums.sort()
        mx, mn = nums[0], nums[0]
        for num in nums:
            mn = min(num, mn)
            mx = max(num, mx)
            if mx - mn > k:
                res += 1
                mx = mn = num
        return res

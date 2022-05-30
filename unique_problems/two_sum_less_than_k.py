class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        i = 0
        j = len(nums) - 1
        while i < j:
            ans_new = nums[i] + nums[j]

            if ans_new > ans and ans_new < k:
                ans = ans_new
                i += 1
            elif ans_new >= k:
                j -= 1
            elif ans_new < k:
                i += 1
        return ans

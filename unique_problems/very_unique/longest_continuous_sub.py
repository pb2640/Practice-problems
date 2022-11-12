class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in nums:
                continue
            temp_ans = 1
            temp_num = num + 1
            while temp_num in nums:
                temp_ans += 1
                temp_num += 1
            ans = max(ans, temp_ans)
        return ans

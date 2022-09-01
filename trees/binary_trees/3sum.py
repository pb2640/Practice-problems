class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            l, h = i + 1, len(nums) - 1
            while l < h:
                s = nums[i] + nums[l] + nums[h]
                if s == 0:
                    ans.add((nums[i], nums[l], nums[h]))
                    l += 1
                    h -= 1
                elif s > 0:
                    h -= 1
                else:
                    l += 1
        return ans

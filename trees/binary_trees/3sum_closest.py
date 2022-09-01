class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        diff = float("inf")
        ans = diff
        for i in range(len(nums)):

            l, h = i + 1, len(nums) - 1
            while l < h:
                s = nums[i] + nums[l] + nums[h]
                if abs(target - s) < abs(diff):
                    diff = target - s
                    ans = s

                if s > target:
                    h -= 1
                else:
                    l += 1
            if ans == target:
                break
        return target - diff

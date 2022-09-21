class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            # print(mid)
            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    r = mid - 2
                else:
                    l = mid + 1
            elif mid + 1 <= n - 1 and nums[mid + 1] == nums[mid]:
                if (mid + 1) % 2 == 0:
                    r = mid - 1
                else:
                    l = mid + 2
            else:
                return nums[mid]

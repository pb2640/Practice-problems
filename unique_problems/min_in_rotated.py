class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]
        pivot = 0
        while l < h:
            mid = (l + h) // 2
            if nums[mid + 1] < nums[mid]:
                pivot = mid
                break
            if nums[l] < nums[mid]:
                l = mid
            else:
                h = mid
        return nums[pivot + 1]
        # print(l,h)

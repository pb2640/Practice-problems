class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
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
        if target >= nums[0] and target <= nums[pivot]:
            l = 0
            h = pivot
        else:
            l = pivot + 1
            h = len(nums) - 1
        # print(l,h)
        while l <= h:
            mid = (l + h) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        return -1

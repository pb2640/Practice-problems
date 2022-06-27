class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        even, odd = 0, 0
        while l < r:
            if even and odd:
                # swap
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                odd, even = 0, 0
                l += 1
                r -= 1
                continue
            if nums[l] % 2 != 0:
                even = 1
            else:
                l += 1
            if nums[r] % 2 == 0:
                odd = 1
            else:
                r -= 1
        return nums

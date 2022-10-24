class Solution:
    def sortColors(self, nums: List[int]) -> None:
        fp = 0
        lp = len(nums) - 1

        while fp < lp:
            if nums[fp] != 0 and nums[lp] == 0:
                temp = nums[lp]
                nums[lp] = nums[fp]
                nums[fp] = temp
                fp += 1
                lp -= 1
            if nums[fp] == 0:
                fp += 1
            if nums[lp] != 0:
                lp -= 1
        lp = len(nums) - 1

        while fp < lp:
            if nums[fp] == 0:
                fp += 1
                continue
            if nums[fp] != 1 and nums[lp] == 1:
                temp = nums[lp]
                nums[lp] = nums[fp]
                nums[fp] = temp
                fp += 1
                lp -= 1
            if nums[fp] == 1:
                fp += 1
            if nums[lp] != 1:
                lp -= 1

        """
        Do not return anything, modify nums in-place instead.
        """

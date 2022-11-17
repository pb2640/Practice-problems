class Solution:
    def reverse(self, arr, start, end):
        i = start
        j = end
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        """
        Do not return anything, modify nums in-place instead.
        """

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        maintain a var that keeps a recordx of the mini abs(i-start), if you come across a value lower, update it
        """
        ans = float("inf")
        for i in range(len(nums)):
            if nums[i] == target and abs(i - start) < ans:
                ans = abs(i - start)
        return ans

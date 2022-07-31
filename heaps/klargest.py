class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        heap = nums
        heapq.heapify(heap)
        i = 1
        while i != k:
            ele = heap.pop(0)
            heapq.heapify(heap)
            i += 1
        return heap.pop(0) * -1

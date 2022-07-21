class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for val in stones:
            heapq.heappush(heap, -1 * val)

        while len(heap) > 1:
            # print("initial",heap)
            ele1 = heapq.heappop(heap) * -1
            ele2 = heapq.heappop(heap) * -1
            # print(ele1,ele2)
            if ele1 == ele2:
                heapq.heappush(heap, 0)
            else:
                heapq.heappush(heap, abs(ele1 - ele2) * -1)
            # print("after",heap)
        return heap[0] * -1

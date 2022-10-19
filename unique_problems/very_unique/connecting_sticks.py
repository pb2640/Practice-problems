class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        if len(sticks) == 1:
            return cost
        heapq.heapify(sticks)
        while len(sticks) != 1:
            temp_sum = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += temp_sum
            heapq.heappush(sticks, temp_sum)
        return cost

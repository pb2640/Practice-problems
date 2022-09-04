class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        e = intervals[0][1]
        heap = [e]

        heapq.heapify(heap)
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i][1])

        return len(heap)

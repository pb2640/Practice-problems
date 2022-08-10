import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc(point):
            # function to calculatre dist from origin
            dist = (point[0] ** 2) + (point[1] ** 2)
            dist = math.sqrt(dist)
            return (dist, point[0], point[1])

        for i in range(len(points)):
            points[i] = calc(points[i])

        heap = points
        heapq.heapify(heap)
        ans = []
        while k:
            ele = heapq.heappop(heap)
            ans.append([ele[1], ele[2]])
            # heapq.heapify(heap)
            k -= 1
        return ans

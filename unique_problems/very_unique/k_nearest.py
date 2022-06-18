class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        # calculate distance and record distance and index
        for i in range(len(points)):
            point = points[i]
            ans.append([(point[0] ** 2) + (point[1] ** 2), i])
        # sort ans by distance
        ans.sort(key=lambda x: x[0])
        # return first k
        final_ans = []
        for i in range(k):
            index = ans[i][1]
            final_ans.append(points[index])

        return final_ans

    ### can you do it in O(N)???

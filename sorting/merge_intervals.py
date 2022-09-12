class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # if there is an intersection, update end
            if interval[0] >= ans[-1][0] and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        return ans

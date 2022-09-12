class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []
        i = 0

        new_start, new_end = newInterval[0], newInterval[1]
        # add all intervals before new interval
        while i < len(intervals) and new_start > intervals[i][0]:
            ans.append(intervals[i])
            i += 1
        # add new Interval
        # if no overlap add the interval
        if not ans or ans[-1][1] < new_start:
            ans.append(newInterval)

        # if there is an overlap
        else:
            ans[-1][1] = max(ans[-1][1], new_end)

        while i < len(intervals):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
            i += 1
        return ans

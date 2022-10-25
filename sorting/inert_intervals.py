class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        i = 0
        flag_add_to_end = 1
        ans = []
        new_start, new_end = newInterval[0], newInterval[1]
        while i < len(intervals):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if curr_end < new_start:
                ans.append(intervals[i])
            else:
                flag_add_to_end = 0
                if new_end < curr_start:
                    ans.append(newInterval)

                else:
                    ans.append([min(curr_start, new_start), max(curr_end, new_end)])
                break
            i += 1
        if flag_add_to_end:
            ans.append(newInterval)
            return ans
        while i < len(intervals):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

            i += 1
        return ans

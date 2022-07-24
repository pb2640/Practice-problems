class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            start_time = intervals[i + 1][0]
            prev_end = intervals[i][1]
            if start_time < prev_end:
                return False
        return True

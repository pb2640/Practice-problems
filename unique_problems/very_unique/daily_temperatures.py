class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        if len(temperatures) == 1:
            return [0]
        stack = []
        stack.append([temperatures[0], 0])
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            while stack:
                if curr_temp > stack[-1][0]:
                    that_days_index = stack.pop()[1]
                    ans[that_days_index] = i - that_days_index
                else:
                    break

            stack.append([curr_temp, i])
        return ans

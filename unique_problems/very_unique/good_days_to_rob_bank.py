class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        forward = [0] * len(security)
        backward = [0] * len(security)

        days = []
        temp_c = 0

        prev = security[0] + 1
        for i in range(len(security)):

            if security[i] <= prev:
                temp_c += 1
            else:
                temp_c = 0
            prev = security[i]

            if i < time:
                continue
            else:
                if temp_c >= time:
                    forward[i] = 1
        # print(forward)
        temp_c = 0

        prev = security[-1] - 1
        for i in range(len(security) - 1, -1, -1):

            if security[i] <= prev:
                temp_c += 1
            else:
                temp_c = 0
            prev = security[i]

            if i > len(security) - time:
                continue
            else:
                if temp_c >= time:
                    backward[i] = 1
        # print(backward)
        for i in range(len(forward)):
            if forward[i] == 1 and backward[i] == 1:
                days.append(i)
        return days

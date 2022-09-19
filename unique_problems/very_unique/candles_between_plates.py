class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prev_candle = [0] * n
        next_candle = [0] * n
        pref_sum = [0] * n
        prev_val = -1
        next_val = -1
        for i in range(len(s)):
            if s[i] == "|":
                prev_val = i
            prev_candle[i] = prev_val
            if s[n - i - 1] == "|":
                next_val = n - i - 1
            next_candle[n - i - 1] = next_val

            if i == 0:
                if s[i] == "*":
                    pref_sum[i] = 1
            else:
                if s[i] == "*":
                    pref_sum[i] += pref_sum[i - 1] + 1
                else:
                    pref_sum[i] = pref_sum[i - 1]
        ans = [0] * (len(queries))
        for i in range(len(queries)):
            query = queries[i]
            ans[i] = max(
                0,
                pref_sum[max(prev_candle[query[1]], 0)]
                - pref_sum[min(next_candle[query[0]], query[1])],
            )
        return ans

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(arr, rate):
            ans = 0
            for ele in arr:
                ans += ele // rate
                if math.ceil(ele % rate):
                    ans += 1
            return ans

        lo = min(piles)
        hi = max(piles)
        ans = float("inf")
        mid = (lo + hi) // 2

        while lo < hi:
            mid = (lo + hi) // 2
            temp_ans = calculate(piles, mid)
            if temp_ans <= h:
                hi = mid
            else:
                lo = mid + 1

        return hi

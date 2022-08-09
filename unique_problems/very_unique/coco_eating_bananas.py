import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(arr, rate):
            ans = 0
            for ele in arr:
                ans += math.ceil(ele / rate)

            return ans

        lr = 1
        hr = max(piles)
        ans = float("inf")
        mid = (lr + hr) // 2

        while lr <= hr:
            if lr == h:
                return lr
            mid = (lr + hr) // 2
            temp_ans = calculate(piles, mid)
            if temp_ans <= h:
                hr = mid - 1
            else:
                lr = mid + 1

        return lr

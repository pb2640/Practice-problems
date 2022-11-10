class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        f = 0
        s = 0
        n = len(nums)
        temp_sum = nums[0]
        ans = 0
        while f < n and s < n:
            if temp_sum == k:
                ans += 1
                if f <= s:
                    s += 1
                    if s < n:
                        temp_sum += nums[s]
            elif temp_sum < k:
                s += 1
                if s < n:
                    temp_sum += nums[s]
            else:
                if f < s:
                    temp_sum -= nums[f]
                    f += 1

                else:
                    temp_sum -= nums[f]
                    f += 1
                    s += 1
                    if f < n:
                        temp_sum += nums[f]
        return ans

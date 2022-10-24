class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = set()
        for x in nums:
            if x > 0:
                ans.add(x)

        return len(ans)

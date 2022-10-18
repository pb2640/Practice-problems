class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # start with an empty set
        ans = [[]]
        # print(type([]))
        for num in nums:
            temp_ans = ans.copy()
            for item in temp_ans:
                ans += [item + [num]]
        return ans

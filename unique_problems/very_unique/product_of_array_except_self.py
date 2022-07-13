class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        r = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            l[i] = product
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            product *= nums[j]
            r[j] = product
        # print(l,r)
        ans = [0] * len(nums)
        ans[0] = r[1]
        ans[len(nums) - 1] = l[-2]
        for i in range(1, len(nums) - 1):
            ans[i] = l[i - 1] * r[i + 1]
        return ans

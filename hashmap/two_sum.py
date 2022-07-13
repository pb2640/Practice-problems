class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hashmap by iterating over the list
        hashmap = {}
        for i in range(len(nums)):
            if target - (nums[i]) in hashmap:
                hashmap[target - nums[i]].append(i)
                return hashmap[target - nums[i]]
            else:
                hashmap[nums[i]] = [i]

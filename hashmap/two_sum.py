class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hashmap by iterating over the list
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                if len(hashmap[target - nums[i]]) > 1:
                    for it in hashmap[target - nums[i]]:
                        if it != i:
                            return [i, it]
                elif hashmap[target - nums[i]][0] != i:

                    return [i, hashmap[target - nums[i]][0]]


####################### IDEAL SOLUTION ###############################

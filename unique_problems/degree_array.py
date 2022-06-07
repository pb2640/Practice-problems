class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        hashmap = {}
        max_num = nums[0]
        max_freq = 1
        ans = 1
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                freq = 1
                min_idx = i
                max_idx = i
                hashmap[nums[i]] = [freq, min_idx, max_idx]
            else:
                hashmap[nums[i]][0] += 1
                if i > hashmap[nums[i]][2]:
                    hashmap[nums[i]][2] = i
        # iterate over the hashmap to calc the max freq, incase of a tie report smallest subarray
        for it in hashmap:
            
            if hashmap[it][0] > max_freq:
                max_freq = hashmap[it][0]
                max_num = it
                ans = hashmap[it][2] - hashmap[it][1] + 1
            elif hashmap[it][0] >= max_freq:
                ans = min((hashmap[it][2] - hashmap[it][1] + 1), ans)
        return ans

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        
        #n below is the house number[0,len(nums)-1]
        def rob2(n,arr,hashmap):
            if(n>len(arr)-1):
                return 0
            if(n in hashmap):
                return hashmap[n]
            cost_n = arr[n]+max(rob2(n+2,arr,hashmap),rob2(n+3,arr,hashmap))
            hashmap[n] = cost_n
            return cost_n
        
    
        hashmap1 = {} 
        hashmap2 = {}
        return max(max(rob2(0,nums[:-1],hashmap1),rob2(1,nums[:-1],hashmap1)),max(rob2(0,nums[1:],hashmap2),rob2(1,nums[1:],hashmap2)))        
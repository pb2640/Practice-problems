from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i,val in enumerate(nums):
            while(dq and nums[dq[-1]]<val):
                dq.pop()
            dq.append(i)
            if(dq[0]==i-k):
                dq.popleft()
            if(i>=k-1):
                ans.append(nums[dq[0]])
        return ans
            
        
        
        
        
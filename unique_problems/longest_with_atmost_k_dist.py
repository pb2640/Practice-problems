class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hashmap = {}
        max_len = 0
        while(r<len(s)):
            if(s[r] in hashmap):
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]] = 1
            if(len(hashmap)<=k):
                max_len = max(max_len,r-l+1)
                r+=1
            else:
                hashmap[s[l]]-=1
                if(hashmap[s[l]]==0):
                    del hashmap[s[l]]
                l+=1
                r+=1
                
        return max_len
                
                
        
            
            
            
        
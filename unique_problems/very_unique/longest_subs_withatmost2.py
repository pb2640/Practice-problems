class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            seen = set()
            j = i
            
            while(j<len(s)):
                if(s[j] not in seen):
                    seen.add(s[j])
                if(len(seen)>2):
                    break
                j+=1
                
            ans = max(ans,j-i)
        return ans
                    
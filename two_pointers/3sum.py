class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)-1):
            k=len(nums)-1
            temp_set = {}
            for j in range(i+1,len(nums)):
                if(j>=k):
                    break
                if(nums[k] in temp_set):
                    temp_set[nums[k]]+=1
                else:
                    temp_set[nums[k]] = 1
                if(-(nums[i]+nums[j]) in temp_set and temp_set[-(nums[i]+nums[j])]>0):
                    ans.append([nums[i],nums[j],-(nums[i]+nums[j])])
                    temp_set[-(nums[i]+nums[j])]-=1
                k-=1
            print(temp_set)
            
            #check for last j
            if(-(nums[i]+nums[j]) in temp_set and temp_set[-(nums[i]+nums[j])]>0):
                ans.append([nums[i],nums[j],-(nums[i]+nums[j])])
        return ans
        
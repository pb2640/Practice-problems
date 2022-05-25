class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ##method 1
        # reference set
        #         hashmap = set(nums)
        #         for i in range(len(nums)):
        #             if i not in hashmap:
        #                 return i
        #         return i+1

        # ###method 2
        #         visited = set()
        #         to_visit = set()
        #         for i in range(len(nums)):
        #             visited.add(nums[i])
        #             # if i in visted:
        #             #dont add this i to to_visit
        #             if i not in visited:
        #                 to_visit.add(i)
        #             if nums[i] in to_visit:
        #                 #remove this element from to_visit
        #                 to_visit.remove(nums[i])
        #         if(len(to_visit)>0):
        #             return(to_visit.pop())
        #         else:
        #             return i+1

        ##method 3
        actual_sum = 0
        current_sum = 0
        for i in range(len(nums)):
            actual_sum += nums[i]
            current_sum += i
        return current_sum + i + 1 - actual_sum

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1
        while(low<high):
            tsum = numbers[low]+numbers[high]
            if(target==tsum):
                return [low+1,high+1]
            elif(target>tsum):
                low+=1
            else:
                high-=1
        # hashmap = {}
        # for i in range(len(numbers)):
        #     ele = numbers[i]
        #     if target-ele in hashmap:
        #         return sorted([i+1,hashmap[target-ele]+1])
        #     else:
        #         hashmap[ele] = i
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for num in nums:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1

        arr = []
        for key in record:
            arr.append([key, record[key]])
        arr.sort(key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
        return ans


"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for num in nums:
            if num in record:
                record[num]+=1
            else:
                record[num] = 1
                
        arr = []
        for key in record:
            arr.append((-record[key],key))
        heap = arr
        heapq.heapify(heap)
        ans = []                      
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
            heapq.heapify(heap)
        return ans
"""

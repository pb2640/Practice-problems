# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         ref = {}
#         for num in nums:
#             if num in ref:
#                 ref[num] += 1
#             else:
#                 ref[num] = 1
#         arr = []
#         for num in ref:
#             arr.append([num, ref[num]])
#         arr.sort(key=lambda x: -x[1])
#         # print(arr)
#         ans = []
#         count = 0
#         while count < k:
#             ans.append(arr[count][0])
#             count += 1

#         return ans

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

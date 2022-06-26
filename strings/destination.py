class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res = set()
        for item in paths:
            res.add(item[0])
        for item in paths:
            if item[1] not in res:
                return item[1]


# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         check = set()
#         ref = set()
#         for city in paths:
#             first = city[0]
#             second = city[1]
#             ref.add(first)
#             #if from city in check remove it from check
#             if(first in check):
#                 check.remove(first)
#             if(second not in ref):
#                 check.add(second)
#         return list(check)[0]

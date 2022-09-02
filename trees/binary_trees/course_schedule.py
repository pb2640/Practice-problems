class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref = {}
        for i in range(len(prerequisites)):
            prereq = prerequisites[i]
            if prereq[0] in ref:
                ref[prereq[0]].add(prereq[1])
            else:
                ref[prereq[0]] = set([prereq[1]])
        state = [0] * (numCourses + 1)
        for i in range(numCourses):
            if i not in ref:
                ref[i] = []

        def has_cycle(v):
            if state[v] == 1:
                return False
            if state[v] == -1:
                return True
            state[v] = -1
            for i in ref[v]:
                if has_cycle(i):
                    return True
            state[v] = 1
            return False

        for node in ref:
            if has_cycle(node):
                return False
        return True


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         ref = {}
#         for i in range(len(prerequisites)):
#             prereq = prerequisites[i]
#             if prereq[0] in ref:
#                 ref[prereq[0]].add(prereq[1])
#             else:
#                 ref[prereq[0]] = set([prereq[1]])
#         visited = set()
#         # check neighbors of every node, if there is a cycle from this node, return false or if there is a on the way return false
#         for node in ref:
#             # if(node in visited):
#             #     continue
#             q = []
#             q.append(node)

#             # start visiting the path from this node
#             visited_n = set()
#             while q:
#                 ele = q.pop(0)
#                 if ele in visited:  # already analyzed paths for this node
#                     continue
#                 visited.add(ele)  # mark as visited
#                 visited_n.add(ele)
#                 if ele not in ref:  # no prereq
#                     continue
#                 for n in ref[ele]:  # looking at neighbours
#                     if n == node or n == ele or n in visited_n:
#                         return False
#                     if n in visited:
#                         continue
#                     q.append(n)

#         return True

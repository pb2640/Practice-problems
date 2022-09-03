"""
start with a node in the list,
do a DFS with this node
if you reach an end count+=1
repeat
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ref = {}
        # to populate the neighbors of a node
        for e in edges:
            if e[0] in ref:
                ref[e[0]].append(e[1])
            else:
                ref[e[0]] = [e[1]]
            if e[1] in ref:
                ref[e[1]].append(e[0])
            else:
                ref[e[1]] = [e[0]]
        component = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            q = [i]
            while q:
                node = q.pop(0)
                visited.add(node)
                if node not in ref:
                    continue
                neighbors = ref[node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
            component += 1
        return component

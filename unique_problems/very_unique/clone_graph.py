"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node
        visited = {}
        q = []
        q.append(node)
        visited[node] = Node(node.val)
        while q:
            pnode = q.pop(0)
            for n in pnode.neighbors:
                if n not in visited:
                    temp = Node(n.val)
                    visited[n] = temp
                    q.append(n)
                visited[pnode].neighbors.append(visited[n])

        # print(visited)
        return visited[node]

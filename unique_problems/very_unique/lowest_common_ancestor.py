"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        a = []
        b = []
        node = p
        while node != None:
            a.append(node.val)
            node = node.parent
        node = q
        while node != None:
            b.append(node.val)
            node = node.parent
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    return Node(int(a[i]))

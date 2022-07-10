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


#### Better solution

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
        """
        find the depth of each node,
        get them to same depth, check if they have same val,
        if not decrease depth and check again and return val
        """
        nodep = p
        depth_p = 0
        while nodep != None:
            depth_p += 1
            nodep = nodep.parent
        nodeq = q
        depth_q = 0
        while nodeq != None:
            depth_q += 1
            nodeq = nodeq.parent
        # get depth to same level
        # print(depth_q,depth_p)
        nodep = p
        nodeq = q
        while depth_p != depth_q:
            if depth_p > depth_q:
                nodep = nodep.parent
                depth_p -= 1
            else:
                nodeq = nodeq.parent
                depth_q -= 1
        while nodep != None and nodeq != None:
            if nodep == nodeq:

                return nodep
            else:
                nodep = nodep.parent
                nodeq = nodeq.parent
        if nodeq == None:
            return nodeq
        else:
            return nodep

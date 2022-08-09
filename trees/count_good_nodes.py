# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = 0
        self.max_val = -float("inf")

    def dfs(self, node, max_v):
        self.visited.add(node)
        if node.val >= max_v:
            self.ans += 1
            max_v = max(max_v, node.val)
        if node.left and node.left not in self.visited:
            self.dfs(node.left, max_v)
        if node.right and node.right not in self.visited:
            self.dfs(node.right, max_v)

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, self.max_val)
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        self.visited = set()

    def dfs(self, node):
        ld, rd = 0, 0
        self.visited.add(node)
        if not node.left and not node.right:
            return 0
        if node.left and node.left not in self.visited:
            ld = 1 + self.dfs(node.left)

        if node.right and node.right not in self.visited:
            rd = 1 + self.dfs(node.right)
        self.ans = max(self.ans, ld + rd)
        return max(ld, rd)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans

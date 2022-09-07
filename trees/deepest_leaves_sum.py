# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level_max = 0
        self.ans = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
            if self.level_max == level:
                self.ans += node.val
            elif level > self.level_max:
                self.ans = node.val
                self.level_max = level
            return

        dfs(root, 1)
        return self.ans

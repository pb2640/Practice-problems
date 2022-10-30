# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, depth, parent, val):
            if not node:
                return None
            if node.val == val:
                return depth, parent
            else:
                left = dfs(node.left, depth + 1, node, val)
                right = dfs(node.right, depth + 1, node, val)
                if left:
                    return left
                else:
                    return right

        depth_x, parent_x = dfs(root, 0, None, x)
        depth_y, parent_y = dfs(root, 0, None, y)
        if depth_x == depth_y and (parent_x) != parent_y:
            return True
        else:
            return False

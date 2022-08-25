# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.order = 0
        self.ans = 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, k):
            if not node:
                return
            if node.left:
                inorder(node.left, k)
            self.order += 1
            if self.order == k:
                self.ans = node.val
            if (node.right, k):
                inorder(node.right, k)

        inorder(root, k)
        return self.ans

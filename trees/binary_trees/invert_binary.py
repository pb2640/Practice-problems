# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Go to root, swap left val with right val and recurse
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        elif root.left == None:
            # make roots right node left
            root.left = self.invertTree(root.right)
            root.right = None
        elif root.right == None:
            root.right = self.invertTree(root.left)
            root.left = None

            # make rootsleft node right
        if root.left != None and root.right != None:
            temp = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(temp)

        return root
        # change both values and recurse

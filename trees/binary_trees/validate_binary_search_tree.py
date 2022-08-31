# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node, low=-math.inf, high=math.inf):
            if node == None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return bst(node.left, low, node.val) and bst(node.right, node.val, high)

        return bst(root)

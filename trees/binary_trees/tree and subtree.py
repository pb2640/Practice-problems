# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, n1, n2):
        if not n1 and not n2:
            return True
        if n1 and n2:
            if n1.val == n2.val:
                return self.same(n1.left, n2.left) and self.same(n1.right, n2.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.same(root, subRoot):
            return True
        #         if(root.left and root.right):
        #             return self.same(root.left,subRoot) or self.same(root.right,subRoot)
        #         if(root.left):
        #             return self.same(root.left,subRoot)
        #         if(root.right):
        #             return self.same(root.right,subRoot)

        #         else:
        #             return False
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

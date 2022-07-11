# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        since it is a BST , we will compare p and q with root
        if oneof them is less than root and the other is greater, return root
        if both less than root recurse on left, if both greater recurse on right
        """
        if p == root or q == root:
            return root
        if p.right == q or p.left == q:
            return p
        if q.right == p or q.left == p:
            return q
        if (p.val < root.val and q.val > root.val) or (
            p.val > root.val and q.val < root.val
        ):
            return root
        elif p.val < root.val and q.val < root.val:
            ans = self.lowestCommonAncestor(root.left, p, q)
        else:
            ans = self.lowestCommonAncestor(root.right, p, q)
        return ans

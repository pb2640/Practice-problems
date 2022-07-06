# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(
        self, root: Optional[TreeNode], low=-float("inf"), high=float("inf")
    ) -> bool:
        # print(high)
        if not root.left and not root.right and root.val < high and root.val > low:
            return True
        if root.left and root.right:
            if (
                root.val > root.left.val
                and root.val < root.right.val
                and root.val < high
                and root.val > low
            ):
                return self.isValidBST(
                    root.left, low=low, high=min(high, root.val)
                ) and self.isValidBST(root.right, low=max(root.val, low), high=high)
            else:
                return False
        if root.left and not root.right:
            if root.val > root.left.val:
                return self.isValidBST(root.left, low=low, high=min(high, root.val))
            else:
                return False
        if root.right:
            if root.val < root.right.val:
                return self.isValidBST(root.right, low=max(root.val, low), high=high)

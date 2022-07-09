# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Do an inorder traversal and keep making nodes and adding them to the previous node
'''
class Solution:
    def __init__(self):
        self.head = TreeNode()
        self.node = self.head
    def increasingBST(self, root: TreeNode) -> TreeNode:
        '''
        if left and right node are absent, add the node to the linked list
        if a left node exists, recurse on that node
        add root node to the list
        if right node exist recurse on right node
        '''
        if(not root.left and not root.right):
            self.node.right = TreeNode(root.val)
            self.node = self.node.right
            return root
        if(root.left):
            self.increasingBST(root.left)
        self.node.right = TreeNode(root.val)
        self.node = self.node.right
        if(root.right):
            self.increasingBST(root.right)
        return self.head.right
        
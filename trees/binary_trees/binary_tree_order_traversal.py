# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def inorder(node,level):
            if(node==None):
                return
            
            if(len(ans)==level):
                ans.append([])
            ans[level].append(node.val)
            if(node.left):
                inorder(node.left,level+1)
            if(node.right):
                inorder(node.right,level+1)
        inorder(root,0)
        
        return ans
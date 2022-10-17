# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root.left and not root.right:
            return [[root.val]]

        def traversal(node):
            if not node:
                return None

            if not node.left and not node.right:
                ans[-1].append(node.val)
                return None
            node.left = traversal(node.left)
            node.right = traversal(node.right)

            return node

        # temp = []
        # traversal(root,temp)
        # print(root)
        # print(temp)
        ans = []
        # count = 0
        while root:
            ans.append([])
            root = traversal(root)
            # ans.append(temp)
            # count+=1
            # if(count==3):
            #     break
        # print(root)
        return ans

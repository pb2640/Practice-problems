# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        if not root.left and not root.right:
            return [[root.val]]

        hashmap = {}
        # max_level = 1
        def traverse(node, level):
            if not node:
                return
            if level in hashmap:
                hashmap[level].append(node.val)
            else:
                hashmap[level] = [node.val]
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 1)
        # print(max_level)
        print(hashmap)
        lev = 1
        rev_flag = False
        ans = []
        while lev in hashmap:
            if rev_flag:
                ans.append(hashmap[lev][::-1])
            else:
                ans.append(hashmap[lev])
            rev_flag = not rev_flag

            lev += 1
        return ans

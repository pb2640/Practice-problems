# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = []
        self.pre_target_list_left = {}
        self.pre_target_list_right = {}
        self.target_level = 0
        self.target_part = "r"

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def pre_target(node, level, sub):
            if not node:
                return
            if node == target:
                if sub == "r":
                    self.target_part = "r"
                else:
                    self.target_part = "l"

                self.target_level = level

                return

            if sub == "l" and level not in self.pre_target_list_left:
                self.pre_target_list_left[level] = []
            elif sub == "r" and level not in self.pre_target_list_right:
                self.pre_target_list_right[level] = []
            if sub == "l":
                self.pre_target_list_left[level].append(node.val)
            else:
                self.pre_target_list_right[level].append(node.val)
            pre_target(node.left, level + 1, sub)
            pre_target(node.right, level + 1, sub)

        def post_target(node, level):
            if not node:
                return
            if level == k:
                self.ans.append(node.val)
                return
            post_target(node.left, level + 1)
            post_target(node.right, level + 1)

        post_target(target, 0)
        pre_target(root.left, 1, "l")
        pre_target(root.right, 1, "r")
        if self.target_part == "l":
            # look for k-self.target dist node
            if k - self.target_level in self.pre_target_list_right:
                for node in self.pre_target_list_right[k - self.target_level]:
                    self.ans.append(node)
            if k in self.pre_target_list_left:
                for node in self.pre_target_list_left[k]:
                    self.ans.append(node)
        if self.target_part == "r":
            # look for k-self.target dist node
            if k - self.target_level in self.pre_target_list_left:
                for node in self.pre_target_list_left[k - self.target_level]:
                    self.ans.append(node)
            if k in self.pre_target_list_right:
                for node in self.pre_target_list_right[k]:
                    self.ans.append(node)
        if self.target_level == k:
            if root.val not in self.ans:
                self.ans.append(root.val)
        # if(self.target_level-k in self.pre_target_list):
        #     for node in self.pre_target_list[self.target_level-k]:
        #         self.ans.append(node)
        return list(set(self.ans))

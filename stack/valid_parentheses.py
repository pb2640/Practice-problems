class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []
        for bracket in s:
            if not stack:
                stack.append(bracket)
            else:
                if bracket in hashmap and hashmap[bracket] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(bracket)
        if stack:
            return False
        else:
            return True

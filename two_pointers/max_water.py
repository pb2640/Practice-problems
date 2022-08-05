class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = -float("inf")
        pt1 = 0
        pt2 = len(height) - 1
        while pt1 < pt2:
            l = min(height[pt1], height[pt2])
            b = pt2 - pt1
            a = max(a, l * b)
            if height[pt1] <= height[pt2]:
                pt1 += 1
            else:
                pt2 -= 1
        return a

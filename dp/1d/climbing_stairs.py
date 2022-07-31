class Solution:
    def __init__(self):
        self.hashmap = {}
        self.hashmap[1] = 1
        self.hashmap[2] = 2

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.hashmap:
            return self.hashmap[n]
        else:
            self.hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

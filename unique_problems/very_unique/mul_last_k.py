class ProductOfNumbers:
    def __init__(self):
        self.s = []
        self.zero_pos = -float("inf")

    def add(self, num: int) -> None:
        if num == 0:
            idx = len(self.s)
            if idx > self.zero_pos:
                self.zero_pos = idx
            self.s.append(num)
        else:
            if not self.s:
                self.s.append(num)
            elif self.s[-1] == 0:
                self.s.append(num)
            else:
                self.s.append(self.s[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.zero_pos >= len(self.s) - k:
            return 0
        else:
            if k == len(self.s):
                return self.s[-1]
            elif self.s[len(self.s) - k - 1] == 0:
                return self.s[-1]
            else:
                return self.s[-1] // self.s[len(self.s) - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

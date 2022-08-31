class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        power = 31
        while n:
            last_bit = n & 1
            ret += last_bit << power
            power -= 1
            n = n >> 1
        return ret

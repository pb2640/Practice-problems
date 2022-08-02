class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        length = len(digits)
        for i in range(length):
            num += digits[i] * (10 ** (length - i - 1))
        # print(num)
        num += 1
        arr = []
        while num:
            arr.append(num % 10)
            num //= 10
        return arr[::-1]

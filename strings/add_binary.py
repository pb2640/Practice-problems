class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ""
        while i >= 0 or j >= 0:
            if i < 0:
                temp = int(b[j]) + carry
                carry = temp // 2
                dig = temp % 2
            elif j < 0:
                temp = int(a[i]) + carry
                carry = temp // 2
                dig = temp % 2
            else:
                temp = int(a[i]) + int(b[j]) + carry
                carry = temp // 2
                dig = temp % 2
            ans = str(dig) + ans
            i -= 1
            j -= 1
        if carry:
            ans = str(carry) + ans
        return ans

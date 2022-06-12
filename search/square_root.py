class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            mid = (l + r) // 2
            # print(mid)
            check = mid ** 2
            if check == num:
                return True
            elif check > num:
                # look left
                r = mid - 1
            else:
                l = mid + 1
        return False

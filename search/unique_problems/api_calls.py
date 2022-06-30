class Solution:
    def firstBadVersion(self, n: int) -> int:
        # idea : implement binary search to minimize API calls
        # Time complexity : O(logN)
        l = 1
        r = n
        if n == 1:
            return 1
        while l <= r:
            mid = (l + r) // 2
            curr = isBadVersion(mid)
            nex = isBadVersion(mid + 1)
            if not curr and nex:
                return mid + 1
            elif not curr and not nex:
                l = mid + 1
            else:
                r = mid - 1
        return mid

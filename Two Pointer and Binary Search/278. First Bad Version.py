# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lst = list(range(n + 1))
        lt, rt = 1, n

        while lt <= rt:
            mid = (lt + rt) // 2
            if not isBadVersion(mid):
                lt = mid + 1
            else:
                rt = mid - 1

        return lt
class Solution:
    def mySqrt(self, x: int) -> int:
        lt, rt = 0, x
        res = 0
        while lt <= rt:
            mid = (lt+rt)//2
            if mid**2 > x:
                rt = mid - 1
            else:
                res = mid
                lt = mid + 1
        return res

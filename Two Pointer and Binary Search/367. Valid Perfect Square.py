class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lt = 0
        rt = num
        while lt <= rt:
            mid = (lt+rt)//2
            if mid**2 < num:
                lt = mid+1
            elif mid**2 > num:
                rt = mid-1
            else:
                return True
        return False

class Solution:
    def arrangeCoins(self, n: int) -> int:
        lst = []
        temp = n
        i = 1
        while True:
            if i >= temp:
                lst.append(temp)
                break
            lst.append(i)
            temp -= i
            i += 1

        lt = 0
        rt = len(lst) - 1
        res = 0

        while lt <= rt:
            mid = (lt + rt) // 2
            if lst[mid] == mid + 1:
                res = mid + 1
                lt = mid + 1
            else:
                return res
        return res
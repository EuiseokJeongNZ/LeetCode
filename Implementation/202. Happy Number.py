class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        str_n = str(n)
        while len(str_n) != 1:
            lst = [int(i) ** 2 for i in str_n]
            str_n = str(sum(lst))
            if str_n == '1':
                return True

        if str_n == '7':
            return True

        return False



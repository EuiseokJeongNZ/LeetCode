class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n < 10:
            return False
        sum_n = 0
        multi_n = 1

        temp = str(n)
        for num in temp:
            sum_n += int(num)
            multi_n *= int(num)

        if n % (sum_n + multi_n) == 0:
            return True
        return False

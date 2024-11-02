class Solution:
    def quaternary(n):
        temp = ''

        while n >= 4:
            temp += str(n % 4)
            n //= 4

        return int(str(n) + temp[::-1])

    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        if n < 0:
            return False

        q = str(Solution.quaternary(n))

        if q.count('0') == len(q) - 1 and q[0] == '1':
            return True

        return False

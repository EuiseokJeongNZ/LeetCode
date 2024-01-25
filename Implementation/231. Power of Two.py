class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        temp = bin(n)[2:]
        zero = temp.count('0')

        if 2 ** zero == n:
            return True

        return False

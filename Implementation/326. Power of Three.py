class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or n == 2:
            return False
        if n == 1:
            return True

        power = 0
        reminder = 0
        while True:
            reminder = n % 3
            if reminder != 0:
                return False
            power += 1
            n //= 3
            if n == 2:
                return False
            elif n == 1:
                return True


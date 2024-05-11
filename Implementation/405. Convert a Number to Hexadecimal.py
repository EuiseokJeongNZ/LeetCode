class Solution:
    def toHex(self, num: int) -> str:
        hexanDigits = '0123456789abcdef'
        res = ""

        if num == 0:
            return '0'

        if num < 0:
            num = (1 << 32) + num

        while num > 0:
            digit = num % 16
            hexanDigit = hexanDigits[digit]
            res = hexanDigit + res
            num //= 16

        return res

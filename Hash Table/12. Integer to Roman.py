class Solution:
    def intToRoman(self, num: int) -> str:
        rmn = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        ans = ''

        while num != 0:
            if num >= 1000:
                ans += rmn[1000] * (num // 1000)
                num %= 1000
            elif num >= 900:
                ans += rmn[900]
                num %= 900
            elif num >= 500:
                ans += rmn[500]
                num %= 500
            elif num >= 400:
                ans += rmn[400]
                num %= 400
            elif num >= 100:
                ans += rmn[100] * (num // 100)
                num %= 100
            elif num >= 90:
                ans += rmn[90]
                num %= 90
            elif num >= 50:
                ans += rmn[50]
                num %= 50
            elif num >= 40:
                ans += rmn[40]
                num %= 40
            elif num >= 10:
                ans += rmn[10] * (num // 10)
                num %= 10
            elif num >= 9:
                ans += rmn[9]
                num %= 9
            elif num >= 5:
                ans += rmn[5]
                num %= 5
            elif num >= 4:
                ans += rmn[4]
                num %= 4
            elif num >= 1:
                ans += rmn[1] * (num // 1)
                num %= 1

        return ans

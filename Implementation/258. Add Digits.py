class Solution:
    def addDigits(self, num: int) -> int:
        temp = str(num)
        while int(temp) >= 10:
            temp = str(sum([int(i) for i in temp]))
        return int(temp)

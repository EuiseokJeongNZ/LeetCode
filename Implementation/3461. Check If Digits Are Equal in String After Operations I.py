class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp = [int(n) for n in s]

        while len(temp) > 2:
            temp_sum = ''
            for i in range(len(temp) - 1):
                temp_sum += str((temp[i] + temp[i + 1]) % 10)

            temp = [int(n) for n in temp_sum]

        for t in range(len(temp) - 1):
            if temp[t] != temp[t + 1]:
                return False

        return True

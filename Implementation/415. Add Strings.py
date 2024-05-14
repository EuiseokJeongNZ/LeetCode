class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {
            '0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9
        }

        cdic = {
            0: '0', 1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9'
        }

        temp = 0
        index = 0
        res = ''

        if len(num1) >= len(num2):
            for i in range(-1, -len(num2) - 1, -1):
                temp += 10 ** abs((1 + i)) * (dic[num1[i]] + dic[num2[i]])
                index = i
            for j in range(index - 1, -len(num1) - 1, -1):
                temp += 10 ** (abs(j + 1)) * dic[num1[j]]
        else:
            for i in range(-1, -len(num1) - 1, -1):
                temp += 10 ** abs((1 + i)) * (dic[num2[i]] + dic[num1[i]])
                index = i
            for j in range(index - 1, -len(num2) - 1, -1):
                temp += 10 ** (abs(j + 1)) * dic[num2[j]]

        if temp == 0:
            return '0'

        while temp != 0:
            res = cdic[temp % 10] + res
            temp //= 10

        return res
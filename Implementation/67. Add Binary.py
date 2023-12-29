class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tempa = int(a)
        tempb = int(b)
        sum = list(str(tempa + tempb))

        for i in range(-1, -(len(sum)+1), -1):

            if sum[i] == '2' or sum[i] == '3':
                sum[i] = str(int(sum[i]) - 2)
                if i == -len(sum):
                    sum = '1' + ''.join(sum)
                else:
                    temp = int(sum[i-1]) + 1
                    sum[i-1] = str(temp)
        return ''.join(sum)
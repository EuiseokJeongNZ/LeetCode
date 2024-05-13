class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]

        cnt = 0

        if len(y) >= len(x):
            x = '0' * (len(y) - len(x)) + x
            for i in range(-1, -len(x) - 1, -1):
                if x[i] != y[i]:
                    cnt += 1
        else:
            y = '0' * (len(x) - len(y)) + y
            for i in range(-1, -len(y) - 1, -1):
                if x[i] != y[i]:
                    cnt += 1

        return cnt


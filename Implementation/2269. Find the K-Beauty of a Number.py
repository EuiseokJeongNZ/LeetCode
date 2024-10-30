class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res, n = 0, len(str(num))

        for i in range(n - k + 1):
            temp = str(num)[i:i + k]
            if int(temp) != 0 and num % int(temp) == 0:
                res += 1

        return res

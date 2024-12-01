class Solution:
    def smallestNumber(self, n: int) -> int:
        bin_n = bin(n)[2:]
        ans = 0
        cur = 0

        temp = '1' * len(bin_n)
        for i in range(len(temp)):
            ans += 2 ** cur
            cur += 1

        return ans
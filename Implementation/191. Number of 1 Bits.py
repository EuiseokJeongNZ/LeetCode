class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(n)
        n = bin(n)[2:]
        res = n.count('1')
        return res

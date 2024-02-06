class Solution:
    def countBits(self, n: int) -> List[int]:
        # Solution with Implementation
        # res = []
        # for i in range(n + 1):
        #     temp = bin(i)[2:]
        #     res.append(temp.count('1'))
        # return res

        # Solution with DP
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        def count(c):
            if c <= 26:
                return 1

            if c in memo:
                return memo[c]
            else:
                temp = count(c - 26) + count(c - 25)
                memo[c] = temp
                return temp

        alphabet = {}
        for i in range(0, 26):
            alphabet[chr(ord('a') + i)] = 1 + i

        memo = {}
        mod = 10 ** 9 + 7
        cnt = 0

        for l in s:
            cnt += count(alphabet[l] + t)

        return cnt % mod
class Solution:
    def isBalanced(self, num: str) -> bool:
        even, odd = 0, 0
        n = len(num)

        for i in range(n):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd += int(num[i])

        if even == odd:
            return True
        return False
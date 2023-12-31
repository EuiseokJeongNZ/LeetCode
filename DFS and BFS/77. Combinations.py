class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combination(start, next):
            if start == k:
                res.append(list(temp))
            else:
                for i in range(next, len(nums)):
                    temp[start] = nums[i]
                    combination(start + 1, i + 1)

        temp = [0] * k
        res = []
        nums = [i for i in range(1, n + 1)]

        combination(0, 0)

        return res
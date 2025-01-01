class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] ** 2

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        temp_gcd, temp_lcm = nums[0], nums[0]
        for num in nums[1:]:
            temp_gcd, temp_lcm = gcd(temp_gcd, num), lcm(temp_lcm, num)

        n = len(nums)
        max_factor = temp_gcd * temp_lcm

        for i in range(n):
            cur_gcd, cur_lcm = 0, 1
            for j in range(n):
                if i != j:
                    cur_gcd = gcd(cur_gcd, nums[j])
                    cur_lcm = lcm(cur_lcm, nums[j])
            max_factor = max(max_factor, cur_gcd * cur_lcm)

        return max_factor
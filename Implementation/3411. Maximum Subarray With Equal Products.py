class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        ans = 0
        left, curr, n = 0, 1, len(nums)

        for right in range(n):
            curr *= nums[right]

            current_lcm = nums[left]
            current_gcd = nums[left]
            for i in range(left + 1, right + 1):
                current_lcm = lcm(current_lcm, nums[i])
                current_gcd = gcd(current_gcd, nums[i])

            temp = current_lcm * current_gcd

            if curr == temp:
                ans = max(ans, right - left + 1)
            if curr > temp:
                curr //= nums[left]
                left += 1

        return ans

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [float('inf')] * n
        stack = []
        nums += nums

        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                stack_i, stack_num = stack.pop()
                ans[stack_i % n] = min(ans[stack_i % n], num)
            stack.append((i, num))

        while stack:
            stack_i, stack_num = stack.pop()
            if ans[stack_i % n] == float('inf'):
                ans[stack_i % n] = -1

        return ans

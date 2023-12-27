class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(-1, -(len(digits) + 1), -1):
            if digits[i] == 10:
                if (i - 1) > -(len(digits) + 1):
                    digits[i - 1] += 1
                    digits[i] = 0
            if digits[-len(digits)] == 10 and -len(digits) == i:
                digits[:] = [1] + digits
                digits[i] = 0
        return digits
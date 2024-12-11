class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1 and len(nums) >= 2:
            return True

        i, j, n = 0, k, len(nums)
        lst1, lst2 = [nums[i]], [nums[j]]

        while j + 1 < n:
            if nums[i] < nums[i + 1] and nums[j] < nums[j + 1]:
                lst1.append(nums[i + 1])
                lst2.append(nums[j + 1])
            else:
                lst1, lst2 = [nums[i + 1]], [nums[j + 1]]
            i += 1
            j += 1

            if len(lst1) == len(lst2) == k:
                return True

        return False

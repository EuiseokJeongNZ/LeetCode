class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # Solution 1
        # nums1[:] = nums1[:m]+nums2
        # nums1.sort()

        # Solution 2
        i = m - 1
        j = n - 1
        for k in reversed(range(m+n)):
            if i < 0:
                nums1[:j+1] = nums2[:j+1]
            elif j < 0:
                break
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
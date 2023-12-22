class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = []
        for i in nums:
            if i != val:
                answer.append(i)
        nums[:] = answer
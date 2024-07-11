import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq_max = [-n for n in nums]
        heapq.heapify(heapq_max)

        for _ in range(k - 1):
            heapq.heappop(heapq_max)

        return -heapq_max[0]
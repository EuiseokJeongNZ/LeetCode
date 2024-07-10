import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        max_heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(max_heap)

        ans = [''] * len(score)

        for rank in range(1, len(max_heap) + 1):
            s, i = heapq.heappop(max_heap)

            if rank == 1:
                ans[i] = 'Gold Medal'
            elif rank == 2:
                ans[i] = 'Silver Medal'
            elif rank == 3:
                ans[i] = 'Bronze Medal'
            else:
                ans[i] = str(rank)

        return ans
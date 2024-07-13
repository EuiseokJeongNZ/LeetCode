import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i] / arr[j], [arr[i], arr[j]]
                heapq.heappush(h, (a, b))

        for _ in range(k - 1):
            heapq.heappop(h)

        ans = list(heapq.heappop(h)[1])

        return ans
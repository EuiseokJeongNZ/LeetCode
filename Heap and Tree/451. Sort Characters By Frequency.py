from collections import Counter
from collections import deque
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        heap = []
        ans = ''

        for ch in s_counter:
            heapq.heappush(heap, (ch, s_counter[ch]))

        heap.sort(key=lambda x: (x[1], x[0]), reverse=True)

        for ch, count in heap:
            for _ in range(count):
                ans += ch

        return ans
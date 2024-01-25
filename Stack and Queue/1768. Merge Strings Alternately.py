from collections import deque

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = deque(list(word1)), deque(list(word2))
        print(a, b)
        res = []
        for _ in range(min(len(a), len(b))):
            res.append(a.popleft())
            res.append(b.popleft())
        if len(a) != 0:
            res += a
        else:
            res += b
        return ''.join(res)

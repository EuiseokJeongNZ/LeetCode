from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        dic = {}
        for i, letter in enumerate(s):
            if not letter in dic:
                dic[letter] = [i, 1]
            else:
                index, count = dic[letter]
                count += 1
                dic[letter] = [index, count]
        queue = deque([])
        for c in dic:
            if dic[c][1] == 1:
                queue.append(dic[c][0])
        if queue:
            res = queue.popleft()
        return res
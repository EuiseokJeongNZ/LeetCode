# My Answer
from collections import deque

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        lst = deque(list(s))
        i = 0
        answer = 0
        while lst:
            if lst[i] == 'I' and ((i + 1) < len(lst)):
                if lst[i + 1] == 'V' or lst[i + 1] == 'X':
                    tempI = dic[lst.popleft()]
                    tempVorX = dic[lst.popleft()]
                    answer += tempVorX - tempI
                else:
                    tempI = dic[lst.popleft()]
                    answer += tempI
                    continue
            elif lst[i] == 'X' and ((i + 1) < len(lst)):
                if lst[i + 1] == 'L' or lst[i + 1] == 'C':
                    tempX = dic[lst.popleft()]
                    tempLorC = dic[lst.popleft()]
                    answer += tempLorC - tempX
                else:
                    tempX = dic[lst.popleft()]
                    answer += tempX
                    continue
            elif lst[i] == 'C' and ((i + 1) < len(lst)):
                if lst[i + 1] == 'D' or lst[i + 1] == 'M':
                    tempC = dic[lst.popleft()]
                    tempDorM = dic[lst.popleft()]
                    answer += tempDorM - tempC
                else:
                    tempC = dic[lst.popleft()]
                    answer += tempC
                    continue
            else:
                answer += dic[lst.popleft()]
        return answer

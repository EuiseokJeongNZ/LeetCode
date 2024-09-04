class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        cnt = 0
        s += '!'

        temp = []
        for n in range(1, len(s)):
            if s[n - 1] == s[n]:
                temp.append(n - 1)
                print(n - 1)
            else:
                temp.append(n - 1)
                if len(temp) >= 3:
                    res.append([min(temp), max(temp)])
                temp = []

        return res




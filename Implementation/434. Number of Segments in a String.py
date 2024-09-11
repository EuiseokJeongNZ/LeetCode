class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        flag = True

        for i in s:
            if i == ' ':
                flag = True
                continue
            else:
                if flag:
                    res += 1
                    flag = False

        return res
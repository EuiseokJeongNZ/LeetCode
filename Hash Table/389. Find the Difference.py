class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(list(s)), sorted(list(t))
        sdic = {i: s.count(i) for i in s}
        tdic = {j: t.count(j) for j in t}

        for i in list(sdic.keys()):
            if sdic[i] == tdic[i]:
                del sdic[i]
                del tdic[i]
            elif sdic[i] < tdic[i]:
                tdic[i] -= sdic[i]
                del sdic[i]

        if tdic:
            answer = [i for i in tdic]
            return ','.join(answer)

        return ''
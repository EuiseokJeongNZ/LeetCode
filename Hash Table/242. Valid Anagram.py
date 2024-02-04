class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s = {i: s.count(i) for i in s}
        dic_t = {j: t.count(j) for j in t}

        for i in dic_t:
            if not i in dic_s:
                return False
            if dic_t[i] > dic_s[i]:
                return False
        return True

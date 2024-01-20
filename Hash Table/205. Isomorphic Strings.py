class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}

        for i in range(len(s)):
            if not s[i] in dic_s:
                dic_s[s[i]] = t[i]
            else:
                if dic_s[s[i]] != t[i]:
                    return False

        for i in range(len(s)):
            if not t[i] in dic_t:
                dic_t[t[i]] = s[i]
            else:
                if dic_t[t[i]] != s[i]:
                    return False

        return True
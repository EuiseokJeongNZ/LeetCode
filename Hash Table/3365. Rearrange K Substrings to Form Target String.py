class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        dic_s, dic_t = {}, {}

        for i in range(k):
            temp1 = s[i * (len(s) // k): (i + 1) * (len(s) // k)]
            temp2 = t[i * (len(t) // k): (i + 1) * (len(t) // k)]

            dic_s[temp1] = dic_s.get(temp1, 0) + 1
            dic_t[temp2] = dic_t.get(temp2, 0) + 1

        return dic_s == dic_t
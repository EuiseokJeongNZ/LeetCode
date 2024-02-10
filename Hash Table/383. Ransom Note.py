class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_r, dic_m = {}, {}
        for i in ransomNote:
            if not i in dic_r:
                dic_r[i] = 1
            else:
                dic_r[i] += 1
        for j in magazine:
            if not j in dic_m:
                dic_m[j] = 1
            else:
                dic_m[j] += 1

        for k in dic_r:
            if not k in dic_m:
                return False
            if dic_r[k] > dic_m[k]:
                return False 
        return True
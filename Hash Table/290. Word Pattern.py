class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        string = s.split(' ')
        temp = []

        if len(pattern) != len(string):
            return False

        for i in range(len(pattern)):
            dic[pattern[i]] = string[i]

        reverseDic = {v: k for k, v in dic.items()}

        for j in range(len(pattern)):
            temp.append(dic[pattern[j]])
            if dic[pattern[j]] != string[j]:
                return False

        for k in range(len(pattern)):
            if pattern[k] != reverseDic[dic[pattern[k]]]:
                return False

        return True
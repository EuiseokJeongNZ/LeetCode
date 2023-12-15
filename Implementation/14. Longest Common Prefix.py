class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        answer = ""
        min_index = min(len(i) for i in strs)

        for i in range(min_index):
            flag = True
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    flag = False
                    break
            if flag:
                answer += strs[0][i]
            else:
                break
        return answer
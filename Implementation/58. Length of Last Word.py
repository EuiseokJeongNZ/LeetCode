class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        isFind = False
        answer = 0
        for i in range(-1, -(len(s)+1), -1):
            if s[i] != ' ':
                isFind = True
                answer += 1
            elif s[i] == ' ' and isFind:
                return answer
        return answer
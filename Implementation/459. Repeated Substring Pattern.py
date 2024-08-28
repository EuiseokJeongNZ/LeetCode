class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s + s)[1:-1]
        if ss.find(s) != -1:
            return (True)
        else:
            return (False)
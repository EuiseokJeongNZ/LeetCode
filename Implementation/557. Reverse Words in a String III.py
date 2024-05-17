class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s.split(' '))
        res = ''

        for i in lst:
            res += i[::-1] + ' '

        return res[:len(res) - 1]
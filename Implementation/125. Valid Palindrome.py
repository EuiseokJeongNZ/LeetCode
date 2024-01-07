class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s.split(' ')) == 0:
            return True

        # 65 ~ 90 / 97 ~ 122 / 48 ~ 57
        temp = ''
        for i in s:
            check = ord(i)
            if 65 <= check <= 90 or 97 <= check <= 122 or 48 <= check <= 57:
                temp += i.lower()

        if temp == temp[::-1]:
            return True

        return False
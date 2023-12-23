# My Answer
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        index = 0
        point = 0
        answer = []
        i = 0
        while i < len(haystack):
            if index < len(needle):
                if haystack[i] == needle[index]:
                    answer.append(i)
                    index += 1
                else:
                    answer = []
                    index = 0
                    point += 1
                    i = point
                    continue
                i += 1
            elif index == len(needle):
                return answer[0]
        if len(answer) == len(needle):
            return answer[0]
        return -1

# Someone's Answer
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        # Check if both strings are equal
        if haystack == needle:
            return 0

        # If lengths are different, perform substring search
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
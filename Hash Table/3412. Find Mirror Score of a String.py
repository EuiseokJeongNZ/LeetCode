class Solution:
    def calculateScore(self, s: str) -> int:
        # original code
        cnt = 0
        n = len(s)
        mirror_dic = {}
        stack = {}

        for i in range(26):
            mirror_dic[chr(ord('a') + i)] = chr(ord('z') - i)

        for i, letter in enumerate(s):
            mirror_letter = mirror_dic[letter]

            if not mirror_letter in stack:
                if not letter in stack:
                    stack[letter] = [i]
                else:
                    stack[letter].append(i)
            else:
                if stack[mirror_letter]:
                    j = stack[mirror_letter].pop()
                    cnt += i - j
                else:
                    if not letter in stack:
                        stack[letter] = [i]
                    else:
                        stack[letter].append(i)

        return cnt

        # optimised code
        # cnt = 0
        # dic_mirror = {}
        # stack = {}

        # for letter in range(26):
        #     dic_mirror[chr(ord('a') + letter)] = chr(ord('z') - letter)

        # for i, curr in enumerate(s):
        #     mirror = dic_mirror[curr]

        #     if mirror in stack and stack[mirror]:
        #         j = stack[mirror].pop()
        #         cnt += i - j
        #     else:
        #         if curr not in stack:
        #             stack[curr] = []
        #         stack[curr].append(i)

        # return cnt

        # time limit execution - wrong code
        # cnt = 0
        # n = len(s)
        # dic_mirror = {}
        # visited = [False] * n

        # for letter in range(26):
        #     dic_mirror[chr(ord('a') + letter)] = chr(ord('z') - letter)

        # for i in range(n):
        #     curr = s[i]
        #     mirror = dic_mirror[curr]
        #     for j in range(i - 1, -1, -1):
        #         if mirror == s[j] and not visited[j]:
        #             cnt += i - j
        #             visited[j] = True
        #             visited[i] = True
        #             break

        # return cnt

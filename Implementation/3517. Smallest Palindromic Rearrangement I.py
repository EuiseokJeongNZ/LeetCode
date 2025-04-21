# class Solution:
#     def smallestPalindrome(self, s: str) -> str:
#         dic = {ch:s.count(ch) for ch in sorted(list(s))}
#         keys_lst = list(dic.keys())
#         ans = []
#         mid = ''

#         for ch in keys_lst:
#             if dic[ch] % 2 == 1:
#                 mid += ch
#                 dic[ch] -= 1

#             for i in range(dic[ch]//2):
#                 ans.append(ch)
#             dic[ch] -= dic[ch]//2
#             if dic[ch] == 0:
#                 del dic[ch]
#         ans.append(mid)

#         for ch in keys_lst[::-1]:
#             while ch in dic and dic[ch] > 0:
#                 ans.append(ch)
#                 dic[ch] -= 1

#         return ''.join(ans)

from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(s)
        lst = sorted(counter.keys())
        ans = []
        mid = ''

        for ch in lst:
            if counter[ch] % 2 == 1 and mid == '':
                mid = ch
            ans.extend([ch] * (counter[ch] // 2))

        return ''.join(ans + [mid] + ans[::-1])
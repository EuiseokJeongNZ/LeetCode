class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # first solution but inefficient

        strs_dic = {}

        for s in strs:
            temp = sorted(list(s))
            sort_s = ''.join(temp)
            if not sort_s in strs_dic:
                strs_dic[sort_s] = {letter: temp.count(letter) for letter in temp}

        ans_dic = {srt_dic: [] for srt_dic in strs_dic}

        for s in strs:
            sort_s = ''.join(sorted(list(s)))
            temp = {t: list(s).count(t) for t in s}

            flag = True

            if sort_s in strs_dic:
                for l in sort_s:
                    if temp[l] != strs_dic[sort_s][l]:
                        flag = False
                        break
                if flag:
                    ans_dic[sort_s].append(s)

        ans = ans_dic.values()

        return ans

#         # other solution more effective

#         anagrams = {}

#         for s in strs:
#             sorted_s = ''.join(sorted(s))
#             if sorted_s not in anagrams:
#                 anagrams[sorted_s] = []
#             anagrams[sorted_s].append(s)

#         return list(anagrams.values())
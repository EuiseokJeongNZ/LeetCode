class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def res_dic(dic1, dic2, res):
            for i in dic1:
                if i in dic2:
                    res.append(i)
            return res

        dic1, dic2 = {}, {}
        res = []
        length = 0

        for i in nums1:
            if not i in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for j in nums2:
            if not j in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1

        if len(dic1) > len(dic2):
            res_dic(dic1, dic2, res)
        else:
            res_dic(dic2, dic1, res)
        return res

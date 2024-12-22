class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        temp = [(i - k, i + k) for i in nums]
        temp.sort(key=lambda k: k[1])

        cur_i = float('-inf')
        res = set()

        for s, e in temp:
            for i in range(max(s, cur_i), e + 1):
                if not res or i not in res:
                    res.add(i)
                    cur_i = i + 1
                    break

        return len(res)

        # for i in range(len(temp)):
        #     s, e = temp[i][0], temp[i][1]
        #     for j in range(s, e+1):
        #         if not j in res and len(res)<len(temp):
        #             res.append(j)
        #             break
        # return len(res)
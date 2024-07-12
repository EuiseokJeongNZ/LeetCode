class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        h = [(n, c) for n, c in dic.items()]
        h.sort(key=lambda x: x[1], reverse=True)

        for i in range(k):
            n, c = h[i][0], h[i][1]
            ans.append(n)

        return ans

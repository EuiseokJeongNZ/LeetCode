from collections import defaultdict
import math


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0

        ans = 0
        dic_points = defaultdict(int)
        for x, y in points:
            dic_points[y] += 1

        total_comb = 0
        sum_squares = 0

        for cnt in dic_points.values():
            if cnt >= 2:
                c = math.comb(cnt, 2)
                total_comb += c
                sum_squares += c * c

        ans = (total_comb * total_comb - sum_squares) // 2
        return ans % (10 ** 9 + 7)

        # Time Limit Exceeded: Time Complexity O(N**2)
        # if len(points) < 4:
        #     return 0

        # ans = 0
        # dic_points = {}
        # for x, y in points:
        #     if not y in dic_points:
        #         dic_points[y] = [x]
        #     else:
        #         dic_points[y].append(x)

        # list_dic_points = list(dic_points.items())
        # for i in range(len(list_dic_points)):
        #     for j in range(i+1, len(list_dic_points)):
        #         first = list_dic_points[i][1]
        #         second = list_dic_points[j][1]
        #         if len(first) > 1 and len(second) > 1:
        #             ans += math.comb(len(first), 2) * math.comb(len(second), 2)

        # return ans%(10**9 + 7)
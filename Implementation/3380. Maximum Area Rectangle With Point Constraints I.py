class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        def function(lst):
            lst.sort(key=lambda x: (x[0], x[1]))

            x1, y1 = lst[0]
            x2, y2 = lst[1]
            x3, y3 = lst[2]
            x4, y4 = lst[3]

            if x1 != x2 or x3 != x3 or y1 != y3 or y2 != y4 or x3 - x1 != x4 - x2 or y2 - y1 != y4 - y3:
                return -1

            for x, y in points:
                if (x, y) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
                    continue
                else:
                    if x1 <= x <= x3 and y1 <= y <= y2:
                        return -1

            return (x3 - x1) * (y2 - y1)

        max_area = -1

        for lst in combinations(points, 4):
            max_area = max(max_area, function(list(lst)))
        return max_area
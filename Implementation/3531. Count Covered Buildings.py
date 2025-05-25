class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minIJ = [float('inf')] * (n + 1)
        maxIJ = [float('-inf')] * (n + 1)
        minJI = [float('inf')] * (n + 1)
        maxJI = [float('-inf')] * (n + 1)

        cnt = 0

        for i, j in buildings:
            minIJ[i] = min(minIJ[i], j)
            maxIJ[i] = max(maxIJ[i], j)
            minJI[j] = min(minJI[j], i)
            maxJI[j] = max(maxJI[j], i)

        for i, j in buildings:
            if minIJ[i] < j < maxIJ[i] and minJI[j] < i < maxJI[j]:
                cnt += 1

        return cnt

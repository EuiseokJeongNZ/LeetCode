class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(v):
            visited[v] = True
            for n in dic[v]:
                if not visited[n]:
                    dfs(n)

        dic = {i+1:[] for i in range(len(isConnected))}
        visited = [False]*(len(isConnected)+1)
        res = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i == j:
                    continue
                else:
                    if isConnected[i][j] == 0:
                        continue
                    else:
                        dic[i+1].append(j+1)
        
        for i in range(1, len(isConnected)+1):
            if not visited[i]:
                res += 1
                dfs(i)

        return res

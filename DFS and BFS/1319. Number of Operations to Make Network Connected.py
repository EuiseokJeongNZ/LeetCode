class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(start):
            visited[start] = True
            for i in graph_dic[start]:
                if not visited[i]:
                    dfs(i)

        graph_dic = {i: set() for i in range(n)}
        visited = [False] * n

        global com_cnt
        com_cnt = 0

        edge_cnt = len(connections)
        cnt = 0

        for connection in connections:
            f_idx, s_idx = connection[0], connection[1]
            graph_dic[f_idx].add(s_idx)
            graph_dic[s_idx].add(f_idx)

        for k, v in graph_dic.items():
            if not visited[k]:
                dfs(k)
                cnt += 1

        if n - 1 > edge_cnt:
            return -1

        return cnt - 1
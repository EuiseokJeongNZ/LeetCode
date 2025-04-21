class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(lst1, lst2, k):
            return len(set(lst1) & set(lst2)) >= k

        def dfs(start):
            visited[start] = True
            for i in graph_dic[start]:
                if not visited[i]:
                    dfs(i)

        n = len(properties)
        graph_dic = {i: set() for i in range(n)}
        visited = [False] * (n)
        cnt = 0

        for i in range(n):
            properties[i].sort()

        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j], k):
                    graph_dic[i].add(j)
                    graph_dic[j].add(i)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                cnt += 1

        return cnt
class dfs_class:
    def __init__(self):
        self.graph = [
            [1, 2],
            [4, 5],
            [3],
            [5],
            [],
            []
        ]
        self.visited = [False] * 6
        self.res = []
    def dfs(self, start : int):
        if self.visited[start]:
            return

        self.res.append(start+1)
        self.visited[start] = True

        for i in self.graph[start]:
            if not self.visited[i]:
                self.dfs(i)

class my_dfs:
    def __init__(self):
        self.graph = {
            1: [2, 3],
            2: [1, 5, 6],
            3: [1, 4],
            4: [3, 6],
            5: [2],
            6: [2, 4]
        }
        self.visited = [False]*(6+1)
        self.res = []
    def traversal(self, start: int):
        self.visited[start] = True
        self.res.append(start)

        for i in self.graph[start]:
            if not self.visited[i]:
                self.traversal(i)


if __name__ == '__main__':

    # 창중이 코드
    dfs = dfs_class()

    dfs.dfs(0)
    print(dfs.res)
    print()

    # 내코드
    euiseok_dfs = my_dfs()
    euiseok_dfs.traversal(1)
    print(euiseok_dfs.res)

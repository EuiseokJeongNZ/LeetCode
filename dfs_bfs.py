## DFS 그래프 구현
# '''
#    1 -- 2
#   / \    \
# 3    \    7
# | \   \ / |
# 4 -5   8  6
# '''

# def dfs(graph, v, visited):
#        # 현재 노드를 방문처리
#        visited[v] = True
#        print(v, end=' ')
#        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#        for i in graph[v]:
#               if not visited[i]:
#                      dfs(graph, i, visited)
#
# # 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
#        [],
#        [2, 3, 8],
#        [1, 7],
#        [1, 4, 5],
#        [3, 5],
#        [3, 4],
#        [7],
#        [2, 6, 8],
#        [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 표현(1차원 리스트)
# visited = [False] * 9
#
# # 정의된 DFS 함수 호출, 첫번쨰 노드부터 출발
# dfs(graph, 1, visited)

# # BFS 구현
# '''
#    1 -- 2
#   / \    \
# 3    \    7
# | \   \ / |
# 4 -5   8  6
# '''

# # double-ended-queue 양방향에서 추가 또는 제거 할 수 있는 자료구조
# from collections import deque
#
#
# def bfs(graph, start, visited):
#     # 큐(queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌때까지 거짓일때 까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v, end=' ')
#         # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# # 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 표현(1차원 리스트)
# visited = [False] * 9
#
# # 정의된 BFS 함수 호출, 첫번쨰 노드부터 출발
# bfs(graph, 1, visited)

## 다른방법으로 푼 dfs/bfs
# from collections import deque
#
# def dfs(start):
#     visited_dfs[start] = True
#     print(start, end=' ')
#     for i in range(1, n+1):
#         if visited_dfs[i]==False and graph[start][i]==True:
#             dfs(i)
#
# def bfs(start):
#     q = deque([start])
#     visited_bfs[start] = True
#     while q: # q가 빌때까지
#         start = q.popleft()
#         print(start, end=" ")
#         for i in range(1, n + 1):
#             if visited_bfs[i] == False and graph[start][i] == True:
#                 q.append(i)
#                 visited_bfs[i] = True
#
# n, m, v = map(int, input().split())
#
# graph = [[False] * (n+1) for _ in range(n+1)]
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x][y] = True
#     graph[y][x] = True
#
# visited_dfs = [False]*(n+1)
# visited_bfs = [False]*(n+1)
#
# dfs(v)
# print()
# bfs(v)

# 문제풀기 dfs
# n*m 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는것으로 간주됩니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 다음의 4*5 얼음 틀 예시에서는 아이스크름이 총 3개 생성됩니다.
# 00110
# 00011
# 11111
# 00000
#
# def dfs(x, y):
#     if x<0 or y<0 or x>=n or y>=m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         for i in range(4):
#             dfs(x+dx[i], y+dy[i])
#         return True
#     return False
#
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     temp = list(map(int, input()))
#     graph.append(temp)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             cnt += 1
# print(cnt)

# # 문제풀기 bfs 백준 2178
# from collections import deque
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 q.append((nx, ny))
#     return graph[n-1][m-1]
#
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     temp = list(map(int, input()))
#     graph.append(temp)
# dx = [-1, 1, 0 ,0]
# dy = [0, 0, -1, 1]
# result = bfs(0, 0)
#
# print(result)

# # 문제풀기 dfs 백준 2606
# def dfs(v):
#     visited[v] = True
#     global cnt
#     cnt += 1
#     for i in range(1, computer_num+1):
#         if visited[i] == False and graph[v][i] == True:
#             dfs(i)
#
# computer_num = int(input())
# link_num = int(input())
# graph = [[False]*(computer_num+1) for _ in range(computer_num+1)]
# visited = [False]*(computer_num+1)
# cnt = 0
# for _ in range(link_num):
#     x, y = map(int, input().split())
#     graph[x][y] = True
#     graph[y][x] = True
#
# dfs(1)
# print(cnt-1)

# # 백준 10451
# import sys
# sys.setrecursionlimit(2000)
#
# def dfs(start):
#     visited[start] = True
#     next_path = arr[start]
#     if not visited[next_path]:
#         dfs(next_path)
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     temp_arr = list(map(int, sys.stdin.readline().split()))
#     arr = [0] + temp_arr
#     visited = [False] * (n + 1)
#     cnt = 0
#
#     for i in range(1, n + 1):
#         if not visited[i]:
#             dfs(i)
#             cnt += 1
#     print(cnt)

## 10451 내코드 시간 초과
# import sys
# sys.setrecursionlimit(2000)
#
# def dfs(v):
#     if not visited[v]:
#         visited[v] = True
#         for i in range(1, n + 1):
#             if graph[v][i] and not visited[i]:
#                 dfs(i)
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     arr = list(map(int, sys.stdin.readline().split()))
#     graph = [[False] * (n + 1) for _ in range(n+1)]
#     visited = [False]*(n+1)
#     for i in range(1, n+1):
#         graph[i][arr[i-1]] = True
#         graph[arr[i-1]][i] = True
#     cnt = 0
#     for i in range(1, n+1):
#         if not visited[i]:
#             dfs(i)
#             cnt += 1
#     print(cnt)

# # 백준 11724
# import sys
# sys.setrecursionlimit(10**4)
#
# def dfs(start):
#     visited[start] = True
#     for i in range(1, n+1):
#         if graph[start][i] and not visited[i]:
#             dfs(i)
#
#
# n, m = map(int, sys.stdin.readline().split())
# graph = [[False] * (n + 1) for _ in range(n+1)]
# visited = [False] * (n + 1)
# cnt = 0
#
# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x][y] = True
#     graph[y][x] = True
#
# for i in range(1, n + 1):
#     if not visited[i]:
#         dfs(i)
#         cnt += 1
# print(cnt)

# # 백준 2667
# import sys
# sys.setrecursionlimit(10**5)
#
# def dfs(x, y):
#     global cnt
#     if x < 0 or y < 0 or x >= n or y >= n:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         for i in range(4):
#             dfs(x + dx[i], y + dy[i])
#         cnt += 1
#         return True
#     return False
#
# n = int(sys.stdin.readline())
# graph = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0
# apartment_cnt = 0
# res = []
#
# for _ in range(n):
#     graph.append(list(map(int, input())))
#
# for i in range(n):
#     for j in range(n):
#         if dfs(i, j) == True:
#             res.append(cnt)
#             cnt = 0
#             apartment_cnt += 1
#
# print(apartment_cnt)
# res.sort()
# for i in res:
#     print(i)

# # 백준 2468 X
# import sys
# from collections import deque
# sys.setrecursionlimit(10 ** 6)
#
# def bfs(x, y, height, visited):
#     global dx, dy
#
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = 1
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if graph[nx][ny] > height and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 queue.append((nx, ny))
#
# n = int(sys.stdin.readline())
# graph = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0
# res = []
#
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# m = max(map(max, graph))
#
# for h in range(m):
#     visited = [[0] * n for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] > h and visited[i][j] == 0:
#                 bfs(i, j, h, visited)
#                 cnt += 1
#     res.append(cnt)
#
# print(max(res))

# # 백준 1743
# import sys
# sys.setrecursionlimit(10 ** 5)
#
# def dfs(x, y):
#     global cnt, dx, dy
#     graph[x][y] = 0
#     cnt += 1
#
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if nx < 0 or ny < 0 or nx > n or ny > m:
#             continue
#         if graph[nx][ny] == 1:
#             dfs(nx, ny)
#
# n, m, k = map(int, sys.stdin.readline().split())
# graph = [[0] * (m + 1) for _ in range(n + 1)]
# res = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for _ in range(k):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a][b] = 1
#
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if graph[i][j] == 1:
#             cnt = 0
#             dfs(i, j)
#             res.append(cnt)
#
# print(max(res))

# # 백준 1012
# import sys
# sys.setrecursionlimit(10000)

# def dfs(x, y):
#     global dx, dy
#     graph[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 1:
#                 dfs(nx, ny)
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# t = int(sys.stdin.readline())
# for _ in range(t):
#     m, n, k = map(int, sys.stdin.readline().split())
#     graph = [[0] * m for _ in range(n)]
#
#     for _ in range(k):
#         y, x = map(int, sys.stdin.readline().split())
#         graph[x][y] = 1
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 dfs(i, j)
#                 cnt += 1
#     print(cnt)

# 백준 7562
import sys
from collections import deque

def bfs(r, c, final_r, final_c):  # row and column in graph
    global dr, dc

    # When the start coordinate and destination coordinate are same
    if r == final_r and c == final_c:
        return 0
    else:
        q = deque()
        q.append((r, c))
        graph[r][c] = 1
        while q:
            r, c = q.popleft()
            for a in range(8):
                nr = r + dr[a]
                nc = c + dc[a]
                if 0 <= nr < i and 0 <= nc < i:
                    if graph[nr][nc] == 0:
                        q.append((nr, nc))
                        graph[nr][nc] = graph[r][c] + 1
        return graph[final_r][final_c] - 1

# The direction coordinate of that the Knight moves
dr = [1, 2, 2, 1, -1, -2, -2, -1]
dc = [-2, -1, 1, 2, -2, -1, 1, 2]

t = int(sys.stdin.readline())
for _ in range(t):
    # The length of a side
    i = int(sys.stdin.readline())
    # The first start coordinate row and column
    fr, fc = map(int, sys.stdin.readline().split())
    # The last destination coordinate row and column
    lr, lc = map(int, sys.stdin.readline().split())
    # Graph list
    graph = [[0] * i for _ in range(i)]

    print(bfs(fr, fc, lr, lc))
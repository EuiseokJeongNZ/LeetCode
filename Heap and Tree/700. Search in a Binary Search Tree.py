import sys
from collections import deque

n = int(sys.stdin.readline())
#farm = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[1]*n for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if n//2==i or n//2==j or abs(n//2-i)==j or abs(n//2-j)==i or (abs(n//2-i)==abs(n//2-j)):
            visited[i][j] = 0
        if (i==0 and j==0) or (i==n-1 and j==n-1):
            visited[i][j] = 1

print(visited)




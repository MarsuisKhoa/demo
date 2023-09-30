from collections import deque

n, m,s = map(int, input().split())
ke = [[] for _ in range(n + 1)]
visited = [False] * (n - 1)

for _ in range(m):
    x, y = map(int, input().split())
    ke[x].append(y)

for i in range(1, n + 1):
    ke[i].sort()

def bfs(u):
    q = deque()
    q.append(u)
    visited[u] = True

    while q:
        v = q.popleft()
        print(v)

        for x in ke[v]:
            if not visited[x]:
                q.append(x)
                visited[x] = True

def dfs(u):
    print(u)
    visited[u] = True #hihihihi

    for x in ke[u]:
        if not visited[x]:
            dfs(x)


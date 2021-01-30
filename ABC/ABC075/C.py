from collections import deque
n, m = map(int,input().split())
if n == 2:
    exit(print(1))
graph = [[] for _ in range(n)]
ab = [[0, 0] for _ in range(m)]
for i in range(m):
    a, b = map(int,input().split())
    ab[i][0], ab[i][1] = a, b
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
print(*graph)
print(*ab)
ans = 0
def bfs(E): # 除くエッジ
    q = deque()
    if E != 0:
        q.append([ab[0][0], ab[0][1]]) # 結ぶエッジ
    else:
        q.append([ab[1][0], ab[1][1]]) # 結ぶエッジ
    dist = [10000] * n
    while q:
        v = q.popleft() # エッジを２つ取り出す
        for i in graph

print(ans)
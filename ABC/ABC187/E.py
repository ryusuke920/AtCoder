from collections import deque
n = int(input())

graph = [[] for _ in range(n)]
ab = [[0, 0] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    ab[i][0], ab[i][1] = a - 1, b - 1

cnt = [-1] * n
cnt[0] = 0

q = deque()
q.append(0)
checked = [0] * n
while q:
    v = q.popleft()
    for i in graph[v]:
        if cnt[i] == -1:
            checked[i] = checked[v] + 1
            q.append(i)
print(cnt)
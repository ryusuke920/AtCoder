from itertools import product
n = int(input())
f = [[0] * 10 for _ in range(n)]
p = [[0] * 10 for _ in range(n)]

for i in range(n):
    F = list(map(int,input().split()))
    for j in range(10):
        f[i][j] = F[j]

for i in range(n):
    P = list(map(int,input().split()))
    for j in range(10):
        p[i][j] = P[j]

ans = -10 ** 18
for i in product([0, 1], repeat = n):
    cnt = 0
    for j in range(n):
        if i[j] == 1:
            for k in range(10):

print(*f,sep = "\n")
print(*p,sep = "\n")
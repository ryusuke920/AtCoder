n = int(input())
p = list(map(int,input().split()))
ans = cnt = 0
st = [i+1 for i in range(n)]
d = [0]*n
for i in range(n):
    d[p[i] - 1] = abs(i + 1 - p[i])

if sum(d) != 2*n - 2:
    exit(print(-1))

ans = []
st = go = 0
key = 1
for i in range(n-1):
    go = p.index(key)
    for j in range(go, st, -1):
        (p[j], p[j-1]) = (p[j-1], p[j])
        if j == go: continue
        elif p[j - 1] != j:
            exit(print(-1))
        else:
            ans.append(j)
    key += go - 1
    st = go

print(ans)
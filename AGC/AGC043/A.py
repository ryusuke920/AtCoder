h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

dist1 = [[0] * w for _ in range(h)]
dist2 = [[0] * w for _ in range(h)]
if s[0][0] == '#':
    dist1[0][0] = 1
    dist2[0][0] = 0
else: # s[0][0] == '.'
    dist1[0][0] = 0
    dist2[0][0] = 1

for i in range(1, h):
    if s[i][0] == '#':
        dist1[i][0] = dist1[i - 1][0] + 1
        dist2[i][0] = dist2[i - 1][0]
    else: # s[0][0] == '.'
        dist1[i][0] = dist1[i - 1][0]
        dist2[i][0] = dist2[i - 1][0] + 1

for i in range(1, w):
    if s[0][i] == '#':
        dist1[0][i] += dist1[0][i - 1] + 1
        dist2[0][i] += dist2[0][i - 1]
    else: # s[0][0] == '.'
        dist1[0][i] = dist1[0][i - 1]
        dist2[0][i] = dist2[0][i - 1] + 1

for i in range(1, w):
    for j in range(1, h):
        if s[j][i] == '#':
            dist1[j][i] = min(dist1[j][i - 1], dist1[j - 1][i]) + 1
            dist2[j][i] = min(dist2[j][i - 1], dist2[j - 1][i])
        else:
            dist1[j][i] = min(dist1[j][i - 1], dist1[j - 1][i])
            dist2[j][i] = min(dist2[j][i - 1], dist2[j - 1][i]) + 1
print(min(dist1[-1][-1], dist2[-1][-1]))
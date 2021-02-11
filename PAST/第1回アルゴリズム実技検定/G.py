from itertools import product, combinations
n = int(input())
a = []
for i in range(n - 1):
    a.append(list(map(int,input().split())))

ans = 0

# ３つのグループに分ける場合
for i in product([0, 1, 2], repeat = n):
    score = 0
    team_1 = []
    team_2 = []
    team_3 = []
    for j in range(n):
        if i[j] == 0:
            team_1.append(j)
        elif i[j] == 1:
            team_2.append(j)
        else: # i[j] == 2:
            team_3.append(j)
    for j in range(3): # team * 3
        if j == 0 and len(team_1) >= 2:
            for k in list(combinations(team_1, 2)):
                k = list(k)
                score += a[min(k)][max(k) - 1 - min(k)]
        if j == 1 and len(team_2) >= 2:
            for k in list(combinations(team_2, 2)):
                k = list(k)
                score += a[min(k)][max(k) - 1 - min(k)]
        if j == 2 and len(team_3) >= 2:
            for k in list(combinations(team_3, 2)):
                k = list(k)
                score += a[min(k)][max(k) - 1 - min(k)]
    ans = max(ans, score)

print(ans)
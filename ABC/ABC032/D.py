n, w = map(int,input().split())
v = []
weight = []
for i in range(n):
    x, y = map(int,input().split())
    v.append(x)
    weight.append(y)

dp = [[0] * (w + 1) for j in range(n + 1)] # DPテーブルの作成
for i in range(n):
    for j in range(w + 1):
        if j < weight[i]: # 選ばない時
            dp[i + 1][j] = dp[i][j]
        else: # 選ぶ時
            dp[i + 1][j] = max(dp[i][j],dp[i][j - weight[i]] + v[i])
print(dp[n][w])
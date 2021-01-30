N,W = map(int,input().split())
w = []
v = []
for i in range(N):
    x,y = map(int,input().split())
    w.append(x)
    v.append(y)

dp = [[0]*(W+1) for j in range(N+1)] # DPテーブルの作成
for i in range(N):
    for j in range(W+1):
        if j < w[i]: # 選ばない時
            dp[i+1][j] = dp[i][j]
        else: # 選ぶ時
            dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])

print(dp[N][W])
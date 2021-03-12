n = int(input())
c = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = 1
for i in range(n):
    for j in range(i):
        if c[j] < c[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
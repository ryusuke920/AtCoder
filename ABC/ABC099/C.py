N = int(input())
lis=[]

temp = 6
while temp <= N:
    lis.append(temp)
    temp *= 6

temp = 9
while temp <= N:
    lis.append(temp)
    temp *= 9

lis.sort(reverse = True)

dp = [10 ** 9] * (N + 1)
dp[0] = 0

for item in lis:
    for i in range(N + 1):
        if i + item <= N:
            dp[i + item] = min(dp[i] + 1, dp[i + item])
print(dp)
ans = 10 ** 10
for index, item in enumerate(dp):
    ans = min(ans, item + N - index)
print(ans)
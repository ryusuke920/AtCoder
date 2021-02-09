n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
a.sort()
num = [0] * n
if n % 2 == 0:
    for i in range(n // 2 - 1):
        num[i] = a[n - 2 * (i + 1) - 1]
    num[n // 2 - 1] = a[-1]
    num[n // 2] = a[0]
    for i in range(n // 2 - 1):
        num[i + (n - 2) // 2 + 2] = a[n - (2 * i + 1) - 1]
    # 和をとる
    for i in range(n - 1):
        ans += abs(num[i + 1] - num[i])
else: # n % 2 == 1:
    cnt = [0] * 2
    for i in range(n // 2):
        cnt[0] -= 2 * a[i]
    cnt[0] += a[n // 2] + a[n // 2 + 1]
    for i in range(n // 2 - 1):
        cnt[0] += 2 * a[-1 - i]
    
    cnt[1] -= (a[n // 2 - 1] + a[n // 2])
    for i in range(n // 2):
        cnt[1] += 2 * a[-i - 1]
    for i in range(n // 2 - 1):
        cnt[1] -= 2 * a[i]
    ans = max(cnt)
print(ans)
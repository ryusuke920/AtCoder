import math
x, y = map(int,input().split())
n = int(input())
ans = 10 ** 9
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

for i in range(n - 1):
    if x[i] - x[i + 1] == 0:
        d = abs(x - x[i])
    else:
        a = (y[i] - y[i + 1]) / (x[i] - x[i + 1])
        b = (x[i] * y[i + 1] - x[i + 1] * y[i]) / (x[i] - x[i + 1])
        d = (abs(a * x[i] - y[i] + b)) / (math.sqrt(a ** 2 + 1))
    ans = min(d, ans)
print(ans)
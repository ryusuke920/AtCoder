n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
num = [0] * n
for i in range(n - 1):
    num [i + 1] += num[i] + (a[i + 1] - a[i])
print(num)
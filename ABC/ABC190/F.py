n = int(input())
a = list(map(int,input().split()))
# 転倒数
def mergecount(A):
    cnt = 0
    n = len(A)
    if n > 1:
        A1 = A[:n>>1]
        A2 = A[n>>1:]
        cnt += mergecount(A1)
        cnt += mergecount(A2)
        i1=0
        i2=0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n//2 - i1
    return cnt

num = []
for i in range(n):
    num.append(a[i])
ans = mergecount(num)
print(ans)

for i in range(n - 1):
    if n % 2 == 0:
        if a[i] >= n // 2:
            ans += -(a[i] - (n // 2)) * 2 - 1
        else:
            ans += (n // 2 - 1 - a[i]) * 2 + 1
    else:
        if a[i] >= n // 2:
            ans += -a[i] * 2 + n - 1
        else:
            ans += a[i] * 2 - n + 1
    print(ans)
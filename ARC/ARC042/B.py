import math
x,y = map(int,input().split())
n = int(input())
ans = 10**9
for i in range(n):
    a,b = map(int,input().split())
    x1 = (x-a)**2
    y1 = (y-b)**2
    ans = min(ans, math.sqrt(x1+y1))
print(ans)
from bisect import bisect_left
q = int(input())
num = []
v = 0
for i in range(q):
    t, x = map(int,input().split())
    if t == 1:
        num.append(x)
    else:
        print(i,num)
        print(num[x + v - 1])
        v += 1
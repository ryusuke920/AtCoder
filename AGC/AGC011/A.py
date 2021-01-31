n,c,k = map(int,input().split())
t = []
for i in range(n):
    t.append([0,0])
for i in range(n):
    a = int(input())
    t[i][0] = a
    t[i][1] = a+k
t.sort()
#print(t)
bus = 0
people = 0
i = 0
while i < n:
    if people == 0:
        people += 1
    if people == c:
        people = 0
        bus += 1
    if people != 0:
        print(i)
        if t[i-1][1] >= t[i][0]:
            people += 1
        else:
            people = 0
            bus += 1
    i += 1
if people == 0:
    print(bus)
else:
    print(bus-1)
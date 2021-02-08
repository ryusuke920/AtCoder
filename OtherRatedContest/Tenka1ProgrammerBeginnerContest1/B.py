n = int(input())
mi = micnt = 10**9
ma = macnt =0
for i in range(n):
    a,b = map(int,input().split())
    if mi <=a:
        mi = a
        micnt = b
    if ma >= a:
        ma = a
        macnt = b
print(macnt - (mi-1))
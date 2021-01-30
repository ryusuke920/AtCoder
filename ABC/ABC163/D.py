n,k = map(int,input().split())
ans = 0
mi = 0
ma = 0
for i in range(k,n+2):
    mi += i
    ma += k+5-i
    ans += ma - mi
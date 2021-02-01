k,t = map(int,input().split())
a = list(map(int,input().split()))
ma = max(a)
print(max(0, 2 * ma - k - 1))
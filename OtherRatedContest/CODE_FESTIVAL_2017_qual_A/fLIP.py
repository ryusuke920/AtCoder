n, m, k = map(int,input().split())
for i in range(n + 1):
    for j in range(m + 1):
        if n * j + m * i - 2 * i * j == k:
            exit(print("Yes"))
print("No")
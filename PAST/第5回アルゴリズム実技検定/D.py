n = int(input())
S = [["0", "0"] for _ in range(n)]
for i in range(n):
    s = input()
    S[i][0] = s
    t = 0
    while s[t] == "0":
        t += 1
    S[i][1] = s[t:]
S.sort(key = lambda x: x[1])
i = 0
print()
print(S[0][0])
while True:
    i += 1
    num = []
    num = [S[i][0]]
    while True:
        if S[i - 1][1] != S[i][1]:
            break
        num.append(S[i][0])
        i += 1
        if i >= n - 1:
            break
    print(*num, sep = "\n")
    if i >= n - 1:
        break
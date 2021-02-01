s = str(input())
cnt = 0
for i in range(len(s)):
    if s[i] == "C":
        cnt += 1
    if cnt >= 1 and s[i] == "F":
        print("Yes")
        exit()
print("No")
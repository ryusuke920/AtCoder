n = int(input())
num = []
if n == 0:
    exit(print(0))
while n > 0:
    n //= 36
    num.append(n % 36)
num = num[::-1]
ch = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for i in range(len(num)):
    if num[i] <= 10:
        ans += str(num[i])
    else:
        ans += str(ch[num[i]])
print(ans)
print(35 + 35*35)
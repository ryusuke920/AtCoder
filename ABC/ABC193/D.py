k = int(input()) # 9k枚
s = list(input())
t = list(input())
taka = aoki = 0
taka_num = [0] * 9
aoki_num = [0] * 9

for i in range(4):
    taka_num[int(s[i]) - 1] += 1 # 0index
    aoki_num[int(t[i]) - 1] += 1 # 0index

for i in range(9):
    if taka_num[i] == 0:
        taka += i + 1
    else:
        taka += 10 ** taka_num[i] * (i + 1)
    if aoki_num[i] == 0:
        aoki += i + 1
    else:
        aoki += 10 ** aoki_num[i] * (i + 1)

for i in range(1, 10): # takaの引くカード
    for j in range(1, 10): # aokiの引くカード
        taka = aoki = 0
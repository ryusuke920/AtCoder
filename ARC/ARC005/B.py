x, y, w = map(str,input().split())
x = int(x) - 1
y = int(y) - 1
c = [list(input()) for _ in range(9)]

grid = [[0] * 9 for _ in range(9)]
for i in range(9):
  for j in range(9):
    grid[i][j] = int(c[i][j])

if w == "R":
  d = [0, 1]
  dd = [0, -1]
elif w == "L":
  d = [0, -1]
  dd = [0, 1]
elif w == "U":
  d = [-1, 0]
  dd = [1, 0]
elif w == "D":
  d = [1, 0]
  dd = [-1, 0]
elif w == "RU":
  d = [-1, 1]
  dd = [1, -1]
elif w == "RD":
  d = [1, 1]
  dd = [-1, -1]
elif w == "LU":
  d = [-1, -1]
  dd = [1, 1]
elif w == "LD":
  d = [1, -1]
  dd = [-1, 1]

ans = [0] * 4
ans[0] = grid[y][x]
ch = 0
for i in range(3):
  if ch == 0:
    if 0 <= y + (i + 1) * d[0] <= 8 and 0 <= x + (i + 1) * d[1] <= 8:
      ans[i + 1] = grid[y + (i + 1) * d[0]][x + (i + 1) * d[1]]
    else:
      cnt = 2
      ch = 1
  if ch == 1:
    ans[i + 1] = grid[y + (i + 1) * d[0] + dd[0] * cnt][x + (i + 1) * d[1] + dd[1] * cnt]
    cnt += 1
print(*ans, sep = "")
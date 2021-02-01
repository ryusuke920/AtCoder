from collections import Counter
s = input()
x = Counter(s)
if len(x) == 1:
    print("NO")
else:
    if len(s)%2 == 0:
        
_ = input()
H = map(int, input().split())
ans = True
max_h = -1
for h in H:
    if max_h - h > 1:
        ans = False
        break
    max_h = max(max_h, h)
print("Yes" if ans else "No")

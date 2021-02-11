A, B, C = map(int, input().split())
amari = A % B
ans = False
for i in range(1, B):
    tmp = (amari * i) % B
    if tmp == 0:
        break
    if C % tmp == 0:
        ans = True
        break
print("YES" if ans else "NO")

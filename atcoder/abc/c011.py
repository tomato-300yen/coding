N = int(input())
NG = set([int(input()) for _ in range(3)])
if N in NG:
    print("NO")
    exit(0)
for _ in range(100):
    if 0 <= N <= 3:
        print("YES")
        break
    if N - 3 not in NG:
        N -= 3
    elif N - 2 not in NG:
        N -= 2
    elif N - 1 not in NG:
        N -= 1
else:
    print("NO")

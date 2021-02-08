L, H = tuple(map(int, input().split()))
N = int(input())
A = [int(input()) for _ in range(N)]
for a in A:
    if a > H:
        print(-1)
    elif a >= L:
        print(0)
    else:
        print(L - a)

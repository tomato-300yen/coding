N = int(input())
A = map(int, input().split())
ans = sorted([(i, n) for i, n in enumerate(A)], key=lambda ll: -ll[1])
for i, _ in ans:
    print(i + 1)

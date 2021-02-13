T = int(input())
C = [map(int, input().split()) for _ in range(T)]
for left, right in C:
    tmp = right - 2 * left + 1
    print(tmp * (tmp + 1) // 2 if tmp > 0 else 0)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split())) + [0]
last = -1
ans = 0
for a in A:
    ans += B[a - 1]
    if a - last == 1:
        ans += C[last - 1]
    last = a
print(ans)

N, M, A, B = map(int, input().split())
C = [int(input()) for _ in range(M)]
count = N
ans = True
for i, c in enumerate(C):
    if count <= A:
        count += B
    count -= c
    if count < 0:
        ans = False
        break
print("complete" if ans else i + 1)

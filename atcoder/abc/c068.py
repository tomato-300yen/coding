N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
ans = False
sa = set()
sb = set()
for a, b in AB:
    if a == 1:
        sb.add(b)
    if b == N:
        sa.add(a)
print("POSSIBLE" if len(sa & sb) > 0 else "IMPOSSIBLE")

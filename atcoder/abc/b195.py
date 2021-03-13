A, B, W = map(int, input().split())
W *= 1000
ans_min = 1e10
ans_max = -1
is_found = False
for i in range(W // B, W // A + 1):
    if A <= W / i <= B:
        ans_min = min(ans_min, i)
        ans_max = max(ans_max, i)
        is_found = True
print(f"{ans_min} {ans_max}" if is_found else "UNSATISFIABLE")

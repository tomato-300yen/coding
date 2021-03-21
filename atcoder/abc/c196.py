N = input()
if len(N) % 2 == 0:  # even
    pree_N = N[: len(N) // 2]
    post_N = N[len(N) // 2 :]
    if int(pree_N) > int(post_N):
        ans = int(pree_N) - 1
    else:
        ans = int(pree_N)
else:
    ans = 10 ** ((len(N) - 1) // 2) - 1
print(ans)

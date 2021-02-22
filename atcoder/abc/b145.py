N, S = int(input()), input()
print("No" if N % 2 != 0 or S[: N // 2] != S[-N // 2 :] else "Yes")

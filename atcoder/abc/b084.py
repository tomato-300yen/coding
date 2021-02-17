A, B = map(int, input().split())
S = input()
print("No" if S[A] != "-" or not S[:A].isnumeric() or not S[-B:].isnumeric() else "Yes")

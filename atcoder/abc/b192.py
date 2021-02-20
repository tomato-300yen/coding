S = input()
S_odd = S[::2]
S_even = S[1:][::2]
print("Yes" if S_odd.islower() and (S_even.isupper() or len(S) == 1) else "No")

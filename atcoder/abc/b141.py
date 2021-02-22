S = input()
print("Yes" if set(S[::2]) <= set("RUD") and set(S[1:][::2]) <= set("LUD") else "No")

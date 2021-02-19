S = input()
S1 = S[::2]
S2 = S[1:][::2]
print(
    min(len(S) - S1.count("0") - S2.count("1"), len(S) - S1.count("1") - S2.count("0"))
)

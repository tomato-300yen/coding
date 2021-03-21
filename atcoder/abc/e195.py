N = int(input())
S, X, T = input(), input(), ""

S = list(S)

for i, x in enumerate(X):
    tmp_0 = int(T + "0")
    tmp_s = int(T + S[i])
    if x == "T":
        if tmp_0 % 7 == 0:
            T = T + "0"
        else:
            T = T + S[i]
    elif x == "A":
        if tmp_0 % 7 == 0:
            T = T + S[i]
        else:
            T = T + "0"
    else:
        assert False
print("Takahashi" if int(T) % 7 == 0 else "Aoki")

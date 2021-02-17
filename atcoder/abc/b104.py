S = input()
cond = (
    (S[0] == "A")
    and (list(S[2:-1]).count("C") == 1)
    and S[1:].replace("C", "").islower()
)
print("AC" if cond else "WA")

S = input()
T = input()
replace = set(list("atcoder"))
win = True
for s, t in zip(S, T):
    if s == t:
        continue
    if s == "@":
        if t in replace:
            continue
    if t == "@":
        if s in replace:
            continue
    win = False
print("You can win" if win else "You will lose")

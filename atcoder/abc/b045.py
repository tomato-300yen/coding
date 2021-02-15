S = [input() for _ in range(3)]
table = {"a": 0, "b": 1, "c": 2}
next_ = table["a"]
while True:
    if len(S[next_]) == 0:
        break
    tmp = table[S[next_][0]]
    S[next_] = S[next_][1:]
    next_ = tmp
print(list(table.keys())[next_].upper())

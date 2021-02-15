S = input()
while True:
    S = S[:-1]
    size = len(S) // 2
    if len(S) % 2 == 0 and S[:size] == S[size:]:
        print(len(S))
        break

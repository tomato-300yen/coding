import re
S, T = input().replace("?", "."), input()
ans_list = []
flag = False
for i in range(len(S) - len(T), -1, -1):
    if re.match(S[i: i + len(T)], T):
        S = S.replace(".", "a")
        print(S[:i] + T + S[i + len(T):])
        break
else:
    print("UNRESTORABLE")

N, M = map(int, input().split())
S = [map(int, input().split()) for _ in range(M)]
string = ["x" for _ in range(N)]
ans = True
for s, c in S:
    if s == 1 and c == 0 and N != 1:
        ans = False
        break
    elif string[s - 1] == "x":
        string[s - 1] = str(c)
    elif string[s - 1] == str(c):
        continue
    else:
        ans = False
        break
if string[0] == "x":
    if N == 1:
        string[0] = "0"
    else:
        string[0] = "1"
string = str(int("".join(string).replace("x", "0")))
print(string if len(string) == N and ans else -1)

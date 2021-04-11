N = input()
while True:
    if len(N) > 20:
        print("No")
        break
    if N == N[::-1]:
        print("Yes")
        break
    else:
        N = "0" + N

S = input()
N = int(input())
tmp = 0
for s in S:
    for t in S:
        tmp += 1
        if tmp == N:
            print(s + t)
            break

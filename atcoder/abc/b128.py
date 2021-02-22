N = int(input())
SP = [input().split() + [i + 1] for i in range(N)]
SP.sort(key=lambda ll: (ll[0], -int(ll[1])))
for _, _, i in SP:
    print(i)

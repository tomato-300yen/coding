S = list(input())
L = sorted(map(int, input().split()))[::-1]
for ll in L:
    S.insert(ll, '"')
print("".join(S))

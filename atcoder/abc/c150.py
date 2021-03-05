from itertools import permutations

input()
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
for a, p in enumerate(permutations(sorted(P))):
    if p == P:
        break
for b, q in enumerate(permutations(sorted(Q))):
    if q == Q:
        break
print(abs((a + 1) - (b + 1)))

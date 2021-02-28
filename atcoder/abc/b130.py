import bisect

(N, X), L = [map(int, input().split()) for _ in range(2)]
D = [0]
for elmnt in L:
    D.append(D[-1] + elmnt)
print(bisect.bisect_right(D, X))

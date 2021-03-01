from collections import Counter

N = int(input())
V = list(map(int, input().split()))
s = Counter(V[0::2]).most_common()
t = Counter(V[1::2]).most_common()
s.append((0, 0))
t.append((0, 0))
if s[0][0] != t[0][0]:
    print(N - s[0][1] - t[0][1])
else:
    print(min(N - s[0][1] - t[1][1], N - s[1][1] - t[0][1]))

from collections import Counter
N, K = map(int, input().split())
A = Counter(list(map(int, input().split())))
print(sum(sorted(A.values(), reverse=True)[K:]))

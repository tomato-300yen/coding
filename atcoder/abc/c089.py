from collections import Counter
from functools import reduce
from itertools import combinations

N = int(input())
S = Counter([input()[0] for _ in range(N)])
ans = 0
for comb in combinations("MARCH", 3):
    ans += reduce(lambda x, y: x * y, [S[char] for char in comb])
print(ans)

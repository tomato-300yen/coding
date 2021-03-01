from collections import Counter

N = int(input())
print(Counter([input() for _ in range(N)]).most_common()[0][0])

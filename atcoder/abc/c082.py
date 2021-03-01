from collections import Counter
N = int(input())
A = Counter(list(map(int, input().split())))
print(sum(item if key > item else item - key for key, item in A.items()))

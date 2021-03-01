from collections import Counter
_ = map(int, input().split())
L = Counter(map(int, input().split()))
R = Counter(map(int, input().split()))
print(sum(min(l_num, R[l_size]) for l_size, l_num in L.items()))

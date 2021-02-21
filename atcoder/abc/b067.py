N, K = map(int, input().split())
L = sorted(map(int, input().split()))[::-1]
print(sum(L[:K]))

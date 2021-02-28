N, K = map(int, input().split())
H = map(int, input().split())
print(sum(h >= K for h in H))

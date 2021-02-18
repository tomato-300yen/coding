_ = int(input())
T, A = map(int, input().split())
H = list(map(lambda h: abs(A - (T - int(h) * 0.006)), input().split()))
print(H.index(min(H)) + 1)

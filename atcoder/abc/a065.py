X, A, B = map(int, input().split())
print("delicious" if B - A < 1 else "safe" if B - A < X + 1 else "dangerous")

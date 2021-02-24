W, x, y = map(int, input().split())
min_ = min(abs(x + W - y), abs(y + W - x))
print(0 if x <= y and y <= x + W else min_)

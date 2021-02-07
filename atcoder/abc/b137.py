K, X = tuple(map(int, input().split()))
start = X - K + 1
end = X + K
print(*range(start, end))

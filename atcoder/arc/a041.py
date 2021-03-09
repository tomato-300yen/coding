x, y = map(int, input().split())
k = int(input())
print(x + k if k <= y else y + x - (k - y))

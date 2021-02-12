N = int(input())
a, b = 2, 1
for _ in range(N - 1):
    a, b = b, a + b
print(b)

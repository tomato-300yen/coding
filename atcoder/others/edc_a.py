N = int(input())
H = list(map(int, input().split()))
b, a = 0, abs(H[0] - H[1])
for i in range(2, N):
    b, a = a, min(b + abs(H[i] - H[i - 2]), a + abs(H[i] - H[i - 1]))
print(a)

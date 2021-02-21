_ = input()
A = sorted(map(int, input().split()))[::-1]
num_a = sum(A[::2])
num_b = sum(A[1:][::2])
print(num_a - num_b)

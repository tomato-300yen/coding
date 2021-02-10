N, A, B = tuple(map(int, input().split()))
num_set = N // (A + B)
print(A * num_set + min(A, N - num_set * (A + B)))

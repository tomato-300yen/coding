A, B, C = map(int, input().split())
num_min = C // min(A, B)
num_max = (C - min(A, B) * num_min) // max(A, B)
print(num_max + num_min)

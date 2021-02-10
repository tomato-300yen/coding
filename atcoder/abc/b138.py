_ = int(input())
A = tuple(map(int, input().split()))
sum_ = 0
for a in A:
    sum_ += 1 / a
print(1 / sum_)

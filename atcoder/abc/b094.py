N, M, X = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))
left_cost = 0
right_cost = 0
for a in A:
    if a > X:
        right_cost += 1
    elif a < X:
        left_cost += 1
    else:
        assert False
print(min(left_cost, right_cost))

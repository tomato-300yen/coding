N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans_set = set([i for i in range(1, 1001)])
for a, b in zip(A, B):
    if a <= b:
        ans_set &= set([a for a in range(a, b + 1)])
print(len(ans_set))

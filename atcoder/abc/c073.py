N = int(input())
ans_set = set()
for _ in range(N):
    a = input()
    if a in ans_set:
        ans_set.remove(a)
    else:
        ans_set.add(a)
print(len(ans_set))

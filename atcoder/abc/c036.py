N = int(input())
A = [int(input()) for _ in range(N)]
num_set = sorted(list(set(A)))
count = 0
dict_num = dict()
for num in num_set:
    dict_num[num] = count
    count += 1
ans = [dict_num[a] for a in A]
print(*ans, sep="\n")

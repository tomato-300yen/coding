S = input()
k = int(input())
ans_set = set()
for i in range(0, len(S) - k + 1):
    ans_set.add(S[i : i + k])
print(len(ans_set))

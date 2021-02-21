N = int(input())
S = input()
max_ = 0
for i in range(N):
    max_ = max(max_, len(set(S[:i]) & set(S[i:])))
print(max_)

from collections import Counter
N = int(input())
S = [Counter(input()) for _ in range(N)]
ans_dict = S[0]
# count
for s in S:
    tmp_dict = dict()
    for key in ans_dict.keys() & s.keys():
        tmp_dict[key] = min(ans_dict[key], s[key])
    ans_dict = tmp_dict
# 文字列を作成
ans = ""
for s in sorted(ans_dict.keys()):
    ans = ans + s * ans_dict[s]
print(ans)

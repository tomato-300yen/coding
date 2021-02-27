def calc_score(S):
    score = 0
    for s in range(1, 10):
        s = int(s)
        c_i = S.count(str(s))
        score += s * (10 ** c_i)
    return score


K = int(input())
S, T = [input() for _ in range(2)]

# 残りのカードの枚数を調べる
rest_list = [K for _ in range(9)]
for s in set(S[:-1]):
    s = int(s)
    c_i = S.count(str(s))
    rest_list[s - 1] = rest_list[s - 1] - c_i
for t in set(T[:-1]):
    t = int(t)
    c_i = T.count(str(t))
    rest_list[t - 1] = rest_list[t - 1] - c_i

# 確率を計算する
bunbo = 0
bunshi = 0
for s in range(1, 10):
    if rest_list[s - 1] == 0:
        continue
    num_s = rest_list[s - 1]
    rest_list_tmp = [rest - 1 if s - 1 == i else rest for i, rest in enumerate(rest_list)]
    for t in range(1, 10):
        if rest_list_tmp[t - 1] == 0:
            continue
        num_t = rest_list_tmp[t - 1]
        bunbo += num_s * num_t
        score_a = calc_score(S[:-1] + str(s))
        score_b = calc_score(T[:-1] + str(t))
        if score_a > score_b:
            bunshi += num_s * num_t
print(bunshi / bunbo)

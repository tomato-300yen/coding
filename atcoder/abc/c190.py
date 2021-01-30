def main():
    # 条件を読み込む
    N, M = list(map(int, input().split()))
    cond_list = [[0, 0] for _ in range(M)]
    for i in range(M):
        a, b = list(map(int, input().split()))
        cond_list[i][0] = a
        cond_list[i][1] = b

    # 皿にボールを置く
    pallet_set = set()
    K = int(input())
    ball_list = [[0, 0] for _ in range(K)]
    for i in range(K):
        c, d = list(map(int, input().split()))
        pallet_set.add(c)
        pallet_set.add(d)
        ball_list[i][0] = c
        ball_list[i][1] = d

    # 条件を数えるがボールを置けない場所は無視する
    pallet_list = [[0, 0] for _ in range(N)]
    for a, b in cond_list:
        if a not in pallet_set or b not in pallet_set:
            continue
        pallet_list[a - 1][0] = pallet_list[a - 1][0] + 1
        pallet_list[b - 1][0] = pallet_list[b - 1][0] + 1

    # 満たしている条件を確認する
    for c, d in ball_list:
        if pallet_list[c - 1][0] >= pallet_list[d - 1][0]:  # c の方が条件が多い場合
            if pallet_list[c - 1][1] == 0:  # まだcにボールが置かれていない場合は置く
                pallet_list[c - 1][1] = 1
            else:
                pallet_list[d - 1][1] = 1
        else:
            if pallet_list[d - 1][1] == 0:
                pallet_list[d - 1][1] = 1
            else:
                pallet_list[c - 1][1] = 1

    # 満たしている条件を確認する
    ans = 0
    for a, b in cond_list:
        if pallet_list[a - 1][1] and pallet_list[b - 1][1]:
            ans = ans + 1
    print(ans)


if __name__ == "__main__":
    main()

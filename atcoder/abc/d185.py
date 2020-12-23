import math


def main():
    N, M = map(int, input().split())
    ll = list(map(int, input().split()))
    ll.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return

    # kを求める
    k = 1e10
    # print("ll ", ll)
    for i in range(len(ll) - 1):
        diff = abs(ll[i + 1] - ll[i]) - 1
        if k > diff and diff != 0:
            k = diff

    # 連続領域を求める
    ll = [0] + ll + [N + 1]  # この端を足す操作が秀逸
    ll_conti = []
    min_conti = 1e10
    for i in range(len(ll) - 1):
        conti = ll[i + 1] - ll[i] - 1
        if conti == 0:
            continue
        ll_conti.append(conti)
        if min_conti > conti:
            min_conti = conti

    # 求めたkが最小区間よりお大きい場合を考慮
    k = min([min_conti, k])
    # print("k ", k)

    # print("ll_conti ", ll_conti)
    # スタンプの回数を数える
    ans = 0
    for conti in ll_conti:
        ans += math.ceil(conti / k)

    print(ans)


if __name__ == "__main__":
    main()

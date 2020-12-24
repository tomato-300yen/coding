def main():
    N, W = list(map(int, input().split()))
    ll_s = []
    ll_t = []

    for _ in range(N):
        s, t, p = tuple(map(int, input().split()))
        ll_s.append((s, p))
        ll_t.append((t, p))

    ll_s.sort()
    ll_t.sort()

    ammt_now = 0
    idx_s = 0
    idx_t = 0
    for _ in range(2 * N):
        # print(ammt_now)
        # print("idx ", idx_s, idx_t)
        # print("time ", ll_s[idx_s][0], ll_t[idx_t][1])
        if ll_s[idx_s][0] < ll_t[idx_t][0]:
            ammt_now += ll_s[idx_s][1]
            idx_s += 1
            # print("add ", idx_s)
            if ammt_now > W:
                # print("last amount ", ammt_now)
                print("No")
                return -1
        else:
            ammt_now -= ll_t[idx_t][1]
            idx_t += 1
            # print("sub ", idx_t)

        # 終了条件
        if idx_t == N or idx_s == N:
            break

    print("Yes")


def test():
    t = tuple(map(int, input().split()))
    print(type(t))


if __name__ == "__main__":
    # test()
    main()

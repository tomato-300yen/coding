def main():
    N, W = list(map(int, input().split()))
    time_tot = int(2 * 1e5 + 1)
    T = [0] * (time_tot)

    # record
    for _ in range(N):
        s, t, p = map(int, input().split())
        T[s] = T[s] + p
        T[t] = T[t] - p

    # simulate
    simulate = [0]
    for i in range(len(T)):
        amount = simulate[-1] + T[i]
        if amount > W:
            print("No")
            return -1
        simulate.append(amount)

    # result
    print("Yes")


if __name__ == "__main__":
    # test()
    main()

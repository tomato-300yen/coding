def main():
    N, Y = list(map(int, input().split()))

    for num_man in reversed(range(0, Y // 10000 + 1)):
        rem_man = Y - 10000 * num_man
        if rem_man < 0:
            continue
        for num_gosen in range(0, rem_man // 5000 + 1):
            rem_gosen = Y - 10000 * num_man - 5000 * num_gosen
            if rem_gosen < 0:
                continue
            num_sen = rem_gosen // 1000
            rem_sen = Y - 10000 * num_man - 5000 * num_gosen - 1000 * num_sen
            if rem_sen == 0 and N == num_sen + num_gosen + num_man:
                print(f"{num_man} {num_gosen} {num_sen}")
                return
    print("-1 -1 -1")


if __name__ == "__main__":
    main()

def main() -> None:
    H, W = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(H)]

    min_a = 101
    for row in A:
        for a in row:
            min_a = min(min_a, a)

    sum = 0
    for row in A:
        for a in row:
            sum += a - min_a
    print(sum)


if __name__ == "__main__":
    main()

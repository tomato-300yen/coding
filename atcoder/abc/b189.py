def main() -> None:
    N, X = tuple(map(int, input().split()))
    alc = [tuple(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i, (v, p) in enumerate(alc):
        sum = sum + v * p
        if sum > X * 100:
            print(i + 1)
            return
    print(-1)


if __name__ == "__main__":
    main()

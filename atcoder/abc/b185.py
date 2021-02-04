def main():
    N, M, T = tuple(map(int, input().split()))
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    battery = N
    time = 0
    for a, b in AB:
        battery = battery - (a - time)
        if battery <= 0:
            print("No")
            exit(0)
        battery = min(battery + b - a, N)
        time = b
    battery = battery - (T - time)
    if battery <= 0:
        print("No")
        exit(0)
    print("Yes")


if __name__ == "__main__":
    main()

def main():
    N, S, D = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        x, y = list(map(int, input().split()))
        if x >= S:
            continue
        if y <= D:
            continue
        ans = 1
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

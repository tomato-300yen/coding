def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1, 2):
        count = 1
        for j in range(3, i + 1, 2):
            if i % j == 0:
                count += 1
        if count == 8:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()

def main() -> None:
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(len(A)):
        x = A[i]
        for j in range(i, len(A)):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)


if __name__ == "__main__":
    main()

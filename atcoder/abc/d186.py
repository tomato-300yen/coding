def main():
    N = int(input())
    ll = list(map(int, input().split()))
    ll.sort()

    ll_diff = []
    for i in range(len(ll) - 1):
        ll_diff.append(ll[i + 1] - ll[i])

    sum = 0
    for i in range(len(ll_diff)):
        sum += ll_diff[i] * (i + 1) * (N - i - 1)

    print(sum)


if __name__ == "__main__":

    main()

def main():
    _ = input()
    L = list(map(int, input().split()))
    ans = 0
    # print(L)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            for k in range(j + 1, len(L)):
                if L[i] >= L[j] + L[k]:
                    continue
                if L[j] >= L[k] + L[i]:
                    continue
                if L[k] >= L[i] + L[j]:
                    continue
                if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                    continue
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()

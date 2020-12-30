import itertools


def main():
    N, M = list(map(int, input().split()))
    mat = [[0 for i in range(N)] for j in range(N)]

    for i in range(M):
        a, b = tuple(map(int, input().split()))
        mat[a - 1][b - 1] = 1
        mat[b - 1][a - 1] = 1

    v_str = ''.join([str(i + 1) for i in range(N)])
    ans = 0
    for perm in itertools.permutations(v_str):
        if perm[0] != '1':
            break
        for i in range(len(perm) - 1):
            a = int(perm[i])
            b = int(perm[i + 1])

            if mat[a - 1][b - 1] == 0:
                break
            if i == len(perm) - 2:
                ans += 1
                break
    print(ans)


if __name__ == "__main__":
    main()

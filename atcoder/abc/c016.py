N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
friend_map = [[0 for _ in range(N)] for _ in range(N)]
for a, b in AB:
    friend_map[a - 1][b - 1] = 1
    friend_map[b - 1][a - 1] = 1
for i in range(N):
    ans = 0
    f_of_f_set = set()
    for j in range(N):
        if friend_map[i][j] == 0:
            continue
        else:
            for k in range(N):
                    continue
                if friend_map[j][k] == 0 or friend_map[i][k] == 1 or k in f_of_f_set:
                    continue
                else:
                    ans += 1
                    f_of_f_set.add(k)
    print(ans)

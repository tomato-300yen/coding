N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
road = [[0 for _ in range(N)] for _ in range(N)]
for a, b in AB:
    road[a - 1][b - 1] += 1
    road[b - 1][a - 1] += 1
for line in road:
    print(sum(line))

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
score_list = [0 for i in range(N)]
for a in A:
    score_list[a - 1] += 1
for s in score_list:
    if -(Q - s) + K <= 0:
        print("No")
    else:
        print("Yes")

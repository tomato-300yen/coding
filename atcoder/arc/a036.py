from collections import deque
N, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
ans_dq = deque([0, 0, 0])
for i, t in enumerate(T):
    ans_dq.append(t)
    ans_dq.popleft()
    if sum(ans_dq) < K and i > 1:
        print(i + 1)
        break
else:
    print(-1)

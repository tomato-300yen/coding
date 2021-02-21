N, Q = map(int, input().split())
S = input()
LR = [map(int, input().split()) for _ in range(Q)]
arr = [0 for _ in range(N)]
for i in range(1, N):
    arr[i] = arr[i - 1]
    if S[i - 1 : i + 1] == "AC":
        arr[i] += 1
for left, right in LR:
    print(arr[right - 1] - arr[left - 1])

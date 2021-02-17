S = input()
N = int(input())
LR = [map(int, input().split()) for _ in range(N)]
for left, right in LR:
    s = S[: left - 1] + S[left - 1 : right][::-1] + S[right:]
print(S)

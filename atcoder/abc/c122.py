N, Q = map(int, input().split())
S = input()
LR = [map(int, input().split()) for _ in range(Q)]
for left, right in LR:
    print(S[left - 1 : right].count("AC"))

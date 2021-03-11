N, M, A, B = map(int, input().split())
C = [int(input()) for _ in range(M)]
num_card = N
for i, c in enumerate(C):
    num_card += B if num_card <= A else 0
    num_card -= c
    if num_card < 0:
        print(i + 1)
        break
else:
    print("complete")

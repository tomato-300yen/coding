C = [list(input().split()) for _ in range(4)]
C = [[el for el in line[::-1]] for line in C[::-1]]
for line in C:
    print(*line, sep=" ")

N = int(input())
A = map(int, input().split())
ans = True
for a in A:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            ans = False
            break
print("APPROVED" if ans else "DENIED")

N = int(input())
L = sorted(map(int, input().split()))
print("Yes" if sum(L[:-1]) > L[-1] else "No")

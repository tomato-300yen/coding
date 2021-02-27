N = int(input())
ans = set()
for i in range(2, int(N ** 0.5) + 2):
    for j in range(2, int(N ** 0.5) + 2):
        if i ** j > N:
            break
        ans.add(i ** j)
print(N - len(ans))

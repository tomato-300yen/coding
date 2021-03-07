from collections import deque

n = int(input())
A = list(map(int, input().split()))
ans = deque()
for i, a in enumerate(A):
    if i % 2 == 0:
        ans.append(a)
    else:
        ans.appendleft(a)
if len(A) % 2 != 0:
    ans = list(ans)[::-1]
print(*ans)

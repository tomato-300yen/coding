from collections import deque

S = input()
num_reversed = 0
T = deque()
for s in S:
    if s == "R":
        num_reversed += 1
    else:
        if num_reversed % 2 == 0:
            T.append(s)
        else:
            T.appendleft(s)
T = "".join(list(T))
if num_reversed % 2 == 1:
    T = T[::-1]

stack = []
if len(T) > 0:
    stack.append(T[0])
    if len(T) > 1:
        for t in T[1:]:
            if len(stack) > 0 and t == stack[-1]:
                stack.pop()
            else:
                stack.append(t)
print("".join(stack))

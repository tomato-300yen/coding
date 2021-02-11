def f(x):
    return (x - 2) % 13


A, B = map(int, input().split())
if f(A) > f(B):
    print("Alice")
elif f(A) < f(B):
    print("Bob")
else:
    print("Draw")

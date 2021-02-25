N = int(input())
ans = ""
while abs(N) > 0:
    amari = N % (-2)
    ans = str(amari * -1) + ans
    N = (N - 1) // -2
print(ans if ans else 0)

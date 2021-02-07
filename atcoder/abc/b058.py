Odd = list(input())
Even = list(input()) + [""]
for o, e in zip(Odd, Even):
    print(o, e, sep="", end="")

N = int(input())
XY_list = list()
for _ in range(N):
    A = int(input())
    XY = [list(map(int, input().split())) for _ in range(A)]
    XY_list.append(XY)

# print()
ans = 0
for i in range(2 ** N):
    pattern = str(bin(i))[2:].zfill(N)
    # print("pattern", pattern)
    compatible = True
    for j, XY in enumerate(XY_list):
        if not (i & (1 << j)):  # lier
            # print(f"{j} is lier.")
            continue
        for x, y in XY:
            # print(f"{j} said {x} is {y}, the fact is {pattern[-x]}.")
            if pattern[-x] != str(y):
                compatible = False
                break
        if not compatible:
            break
    # print("result", pattern, compatible)
    ans = max(ans, str(bin(i)).count("1") if compatible else 0)
print(ans)

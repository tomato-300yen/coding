from itertools import groupby
N = int(input())
XC = [list(map(int, input().split())) for _ in range(N)]
XC = sorted(XC, key=lambda ll: (ll[1]))
last = 0
ans = 0
move_list = []
lr_list = []
for k, g in groupby(XC, key=lambda ll: ll[1]):
    g = list(map(lambda ll: ll[0], g))
    left = min(g)
    right = max(g)
    move_to_left = abs(last - left)
    move_to_right = abs(last - right)
    lr_list.append((left, right))
    move_list.append((move_to_left, move_to_right))
    if left <= last <= right:
        if move_to_left > move_to_right:
            ans += right - left + move_to_right
            last = left
        else:
            ans += right - left + move_to_left
            last = right
    else:
        if move_to_left > move_to_right:
            ans += move_to_left
            last = left
        else:
            ans += move_to_right
            last = right

# for i in range(len(lr_list)):
#     left, right = lr_list[i]
#     move_to_left, move_to_right = move_list[i]
#     if left <= last <= right:
#         if move_to_left > move_to_right:
#             ans += right - left + move_to_right
#             last = left
#         else:
#             ans += right - left + move_to_left
#             last = right
#     else:
#         if move_to_left > move_to_right:
#             ans += move_to_left
#             last = left
#         else:
#             ans += move_to_right
#             last = right
ans += last
print(ans)

L, R = tuple(map(int, input().split()))
if R - L >= 2019:
    ans = 0
else:
    left, right = L % 2019, R % 2019
    num_list = [i for i in range(left, right + 1)]
    ans = 2020
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            ans = min(ans, (num_list[i] * num_list[j]) % 2019)
print(ans)

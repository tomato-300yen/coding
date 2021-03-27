from functools import reduce
N = int(input())
A = list(map(int, input().split()))
ans = 1e10
for i in range(2 ** (N - 1)):  # 全パターンの生成
    tmp = 0
    tmp_list = [0]
    for j in range(N - 1):  # 各パターンについて検証
        tmp_list.append(A[j])
        if i & (1 << j):  # 区切る
            tmp = tmp ^ reduce(lambda x, y: x | y, tmp_list)
            tmp_list = [0]
        else:  # 区切らない
            pass
    else:
        tmp_list.append(A[-1])
        tmp = tmp ^ reduce(lambda x, y: x | y, tmp_list)

    ans = min(ans, tmp)
print(ans)

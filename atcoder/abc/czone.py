import numpy as np

N = int(input())
ABCDE = [list(map(int, input().split())) for _ in range(N)]
ans_list = ABCDE[:3]
for each in ABCDE[3:]:
    ans_list.append(each)

    print(*ans_list, sep="\n")
    print()
    arr = np.array(ans_list)
    ans_list = []
    idx_set = set()
    count = 0
    while count < 3:
        arr_max = arr.max(axis=0)
        arr_argmax = arr.argmax(axis=0)
        idx = arr_argmax[arr_max.argmin()]
        if idx not in idx_set:
            ans_list.append(list(arr[idx]))
            count += 1
            idx_set.add(idx)
        arr = np.delete(arr, idx, 0)

    # ここでうまい操作が必要
    # それぞれの最大のlistの場所を探す
    # ans_list = sorted(ans_list, reverse=True)
    print(*ans_list, sep="\n")
    print("---")
    # ans_list.pop()
    # print()

ans = [-1 for _ in range(5)]
for each in ans_list:
    for i in range(5):
        ans[i] = max(each[i], ans[i])
print(min(ans))

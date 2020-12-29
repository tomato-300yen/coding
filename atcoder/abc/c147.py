def bin_search(bit_str, N, xy_list_all, num_true):
    if len(bit_str) == N:
        for i, xy_list in enumerate(xy_list_all):
            # 人iが付箋説な人だったらcontinue
            if bit_str[i] == '0':
                continue
            # それぞれの証言についてfor
            # print(bit_str, xy_list)
            for xy in xy_list:
                if int(bit_str[xy[0] - 1]) ^ xy[1]:  # 矛盾
                    return 0
        return num_true

    else:
        return max([bin_search(bit_str + '0', N, xy_list_all, num_true), bin_search(bit_str + '1', N, xy_list_all, num_true + 1)])


def main():
    N = int(input())
    xy_list_all = []
    for i in range(N):
        A_i = int(input())
        xy_list = []
        for j in range(A_i):
            each_xy = list(map(int, input().split()))
            xy_list.append(each_xy)
        xy_list_all.append(xy_list)
    ans = bin_search('', N, xy_list_all, 0)
    print(ans)


if __name__ == "__main__":
    main()
